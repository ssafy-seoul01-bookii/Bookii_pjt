from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404, get_list_or_404
from django.db.models import Count, Q
from django.core.files.base import ContentFile

import requests
import random
from io import BytesIO
from PIL import Image, UnidentifiedImageError

from .models import Category, Book, Thread, Comment, Keyword
from .serializers import CategoryListSerializer, KeywordListSerializer, BookListSerializer, ThreadListSerializer, CommentListSerializer, ThreadCreateSerializer, CommentCreateSerializer
from .utils import get_thread_cover_img, update_book_rank, is_valid_url
from accounts.models import User

# 카테고리 목록 조회
@api_view(["GET"])
def get_categories(request):
    categories = get_list_or_404(Category)
    serializer = CategoryListSerializer(instance=categories, many=True)
    return Response(serializer.data)

# 키워드 목록 조회
@api_view(["GET"])
def get_keywords(request):
    keywords = get_list_or_404(Keyword)
    serializer = KeywordListSerializer(instance=keywords, many=True)
    return Response(serializer.data)

# 책 목록 조회
@api_view(["GET"])
def get_books(request):
    books = get_list_or_404(Book)
    serializer = BookListSerializer(instance=books, many=True)
    return Response(serializer.data)

# 평론가의 평점 3.0점 이상인 책
@api_view(["GET"])
def get_high_rank_book_by_critic(request):
    users = get_list_or_404(User)
    
    critics = [user for user in users if user.is_critic == "Y"]
    if critics:
        random_critic = random.choice(critics)
        print(f"선택된 평론가: {random_critic.username}")
    else:
        print("평론가가 없습니다.")

    # 해당 평론가가 작성한 Thread 중 rank ≥ 3.0인 Book의 ID 추출
    high_rank_book_ids = Thread.objects.filter(
        user=random_critic,
        rank__gte=3.0
    ).values_list("book_id", flat=True).distinct()
    
    # 해당 책 목록 조회
    books = Book.objects.filter(id__in=high_rank_book_ids)
    serializer = BookListSerializer(instance=books, many=True)
    return Response(serializer.data)

# 쓰레드가 많은 책
@api_view(["GET"])
def get_many_threads_book(request):
    books = Book.objects.annotate(thread_count=Count("book_threads")).order_by("-thread_count")
    serializer = BookListSerializer(instance=books, many=True)
    return Response(serializer.data)

# 평점이 3.5점 이상인 책
@api_view(["GET"])
def get_high_rank_book(request):
    books = Book.objects.filter(rank__gte=3.5)
    serializer = BookListSerializer(instance=books, many=True)
    return Response(serializer.data)

# 책 상세 조회
@api_view(["GET"])
def get_book(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    serializer = BookListSerializer(instance=book)
    return Response(serializer.data)

# 쓰레드 목록 조회
@api_view(["GET"])
def get_threads(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    threads = get_list_or_404(Thread, book=book)
    serializer = ThreadListSerializer(instance=threads, many=True)
    return Response(serializer.data)

# 쓰레드 상세 조회, 수정, 삭제
@api_view(["GET", "PUT", "DELETE"])
def get_update_delete_thread(request, book_pk, thread_pk):
    thread = get_object_or_404(Thread, pk=thread_pk)
    if request.method == "GET":
        serializer = ThreadListSerializer(thread)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ThreadCreateSerializer(thread, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # 책 평점 재계산
            update_book_rank(book_pk)
            return Response(serializer.data)
    elif request.method == "DELETE":
        thread.delete()
        # 책 평점 재계산
        update_book_rank(book_pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

# 쓰레드 생성
@api_view(["POST"])
def create_thread(request, book_pk):
    # 일단 저장
    book = get_object_or_404(Book, pk=book_pk)
    serializer = ThreadCreateSerializer(data=request.data)
    content = request.data.get("content")
    if serializer.is_valid(raise_exception=True):
        thread = serializer.save(book=book)
        cover_url = get_thread_cover_img(content)
        print(cover_url)
        if is_valid_url(cover_url):
            try:
                response = requests.get(cover_url, stream=True, timeout=5)
                if response.status_code == 200 and 'image' in response.headers.get("Content-Type", ""):
                    img = Image.open(response.raw)
                    buffer = BytesIO()
                    img.save(buffer, format="PNG")
                    thread.cover_img_url.save(
                        f"{thread.title[:10]}_cover.png", 
                        ContentFile(buffer.getvalue()), 
                    )
            except (requests.RequestException, UnidentifiedImageError) as e:
                print(f"[cover 저장 실패] {cover_url} - {e}")

        # 책 평점 재계산
        update_book_rank(book_pk)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 댓글 목록 조회
@api_view(["GET"])
def get_comments(request, book_pk, thread_pk):
    thread = get_object_or_404(Thread, pk=thread_pk)
    comments = Comment.objects.filter(thread=thread)
    serializer = CommentListSerializer(instance=comments, many=True)
    return Response(serializer.data)

# 댓글 생성
@api_view(["POST"])
def create_comment(request, book_pk, thread_pk):
    thread = get_object_or_404(Thread, pk=thread_pk)
    serializer = CommentCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(thread=thread)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 댓글 삭제
@api_view(["DELETE"])
def delete_comment(request, book_pk, thread_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# 검색
# @api_view(["GET"])
# def search_books(request):
#     query = request.GET.get("query", "")
#     if not query:
#         return Response({"message": "검색어를 입력해주세요."}, status=status.HTTP_400_BAD_REQUEST)
#     books = Book.objects.filter(
#         Q(title__icontains=query) | Q(author__icontains=query),
#     )
#     serializer = BookListSerializer(books, many=True)
#     return Response(serializer.data)
