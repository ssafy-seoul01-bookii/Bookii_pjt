from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404, get_list_or_404
from django.db.models import Count, Q

from .models import Category, Book, Thread, Comment
from .serializers import CategoryListSerializer, BookListSerializer, BookDetailSerializer, ThreadListSerializer, ThreadDetailSerializer, CommentDetailSerializer, ThreadCreateSerializer, CommentCreateSerializer

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
