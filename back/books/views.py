from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404, get_list_or_404
from django.db.models import Count, Q
from django.core.files.base import ContentFile

from .models import Category, Book, Thread, Comment
from .serializers import CategoryListSerializer, BookListSerializer, BookDetailSerializer, ThreadListSerializer, ThreadDetailSerializer, CommentDetailSerializer, ThreadCreateSerializer, CommentCreateSerializer
from .utils import get_author_info, get_book_audio_file, get_bestseller_list, get_item_new_special_list, get_new_category, get_keyword_list, get_thread_cover_img

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
@api_view(["GET"])
def insert(request):
    bestseller_list = get_bestseller_list()
    item_new_special_list = get_item_new_special_list()

    for bestseller in bestseller_list:
        book_for_data = Book()
        book_for_data.title = bestseller["title"]
        book_for_data.description = bestseller["description"]
        book_for_data.isbn = bestseller["isbn"]
        book_for_data.cover_img_url = bestseller["cover"]
        book_for_data.publisher = bestseller["publisher"]
        book_for_data.pub_date = bestseller["pub_date"]

        # category 정보
        print(f"category: {get_new_category(bestseller['category'])}")
        print(f"keywords: {get_keyword_list(bestseller['title'])}")
        content = """
                    인류의 3분의 1이 하루도 안 돼서 사라졌다.
                    진격의 거인은 3 세력 간의 싸움을 그려낸 명작이다.
                    땅울림을 겪은 인류는 얼마나 두려웠을까?
                    아니면 괴롭힘을 당하고, 오랜 시간 핍박을 받은 에르디아인들은 어떤 마음이었을까?
                    누가 잘못한 것일까?
                    나는 잘 모르겠다.
                    """
        print(f"cover_img: {get_thread_cover_img(content)}")

        # # audio 파일
        # mp3_fp = get_book_audio_file(book_for_data.author_name, book_for_data.title)
        # book_for_data.audio_file.save(f"{book_for_data.title}_ai_summary.mp3", ContentFile(mp3_fp.read()))

        # # author 정보
        # book_for_data.author_name = bestseller["author"]
        # book_for_data.author_info = get_author_info(book_for_data.author_name)
        
        # book_for_data.save()

    # for item_new_special in item_new_special_list:
    #     print(item_new_special)
        
    return Response({"message": "ok"}, status=status.HTTP_200_OK)
