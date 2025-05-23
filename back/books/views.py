from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404, get_list_or_404
from django.db.models import Count, Q
from django.core.files.base import ContentFile

from .models import Category, Book, Thread, Comment
from .serializers import CategoryListSerializer, BookListSerializer, BookDetailSerializer, ThreadListSerializer, ThreadDetailSerializer, CommentDetailSerializer, ThreadCreateSerializer, CommentCreateSerializer
from .utils import get_author_info, get_book_audio_file

@api_view(["GET"])
def get_categories(request):
    categories = get_list_or_404(Category)
    serializer = CategoryListSerializer(categories, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_books(request):
    books = get_list_or_404(Book)
    serializer = BookListSerializer(books, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_book(request, book_pk):
    book = Book.objects.annotate(num_of_threads=Count("threads")).get(pk=book_pk)
    serializer = BookDetailSerializer(book)
    return Response(serializer.data)

@api_view(["GET"])
def get_threads(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    threads = get_list_or_404(Thread, book=book)
    serializer = ThreadListSerializer(threads, many=True)
    return Response(serializer.data)

@api_view(["GET", "PUT", "DELETE"])
def get_update_delete_thread(request, book_pk, thread_pk):
    thread = Thread.objects.annotate(num_of_comments=Count("comments")).get(pk=thread_pk)
    if request.method == "GET":
        serializer = ThreadDetailSerializer(thread)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ThreadCreateSerializer(thread, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == "DELETE":
        thread.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def create_thread(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    serializer = ThreadCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(book=book)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def create_comment(request, book_pk, thread_pk):
    thread = get_object_or_404(Thread, pk=thread_pk)
    serializer = CommentCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(thread=thread)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def get_update_delete_comment(request, book_pk, thread_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == "GET":
        serializer = CommentDetailSerializer(comment)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = CommentCreateSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == "DELETE":
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET"])
def search_books(request):
    query = request.GET.get("query", "")
    if not query:
        return Response({"message": "검색어를 입력해주세요."}, status=status.HTTP_400_BAD_REQUEST)
    books = Book.objects.filter(
        Q(title__icontains=query) | Q(author__icontains=query),
    )
    serializer = BookListSerializer(books, many=True)
    return Response(serializer.data)

# 더미데이터 삽입을 위한 함수
import requests
from datetime import datetime
import os
TTB_KEY = os.environ.get("ALADDIN_API_KEY")
@api_view(["GET"])
def insert(request):
    def search_books(query, max_results=10):
        url = "https://www.aladin.co.kr/ttb/api/ItemSearch.aspx"
        params = {
            "ttbkey": TTB_KEY,
            "Query": query,
            "QueryType": "Keyword",
            "MaxResults": max_results,
            "start": 1,
            "SearchTarget": "Book",
            "output": "js",
            "Version": "20131101"
        }

        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            items = response.json().get("item", [])
            books = []

            for item in items:
                book = {
                    "title": item.get("title"),
                    "author": item.get("author", ""),
                    "description": item.get("description", ""),
                    "isbn": item.get("isbn13", item.get("isbn")),
                    "cover": item.get("cover"),
                    "publisher": item.get("publisher"),
                    "pub_date": None
                }

                pub_date_str = item.get("pubDate")
                if pub_date_str:
                    try:
                        book["pub_date"] = datetime.strptime(pub_date_str, "%Y-%m-%d").date()
                    except ValueError:
                        pass  # 날짜 형식이 잘못됐을 경우 생략

                books.append(book)

            return books
        else:
            raise Exception(f"API 호출 실패: {response.status_code}")

    books = search_books("인공지능")
    for book in books:
        print(book)
        book_for_data = Book()
        book_for_data.title = book["title"]
        book_for_data.description = book["description"]
        book_for_data.isbn = book["isbn"]
        book_for_data.author_name = book["author"]
        book_for_data.cover_img_url = book["cover"]
        book_for_data.publisher = book["publisher"]
        book_for_data.pub_date = book["pub_date"]
        book_for_data.author_info = get_author_info(book_for_data.author_name)
        mp3_fp = get_book_audio_file(book_for_data.author_name, book_for_data.title)
        book_for_data.audio_file.save(f"{book_for_data.title}_ai_summary.mp3", ContentFile(mp3_fp.read()))
        book_for_data.save()
    return Response({"message": "ok"}, status=status.HTTP_200_OK)
