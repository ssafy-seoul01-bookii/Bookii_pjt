from rest_framework import serializers
from .models import Category, Book, Thread, Comment, Keyword

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"



class KeywordListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = "__all__"



class BookListSerializer(serializers.ModelSerializer):
    thread_count = serializers.SerializerMethodField()

    def get_thread_count(self, obj):
        return obj.book_threads.count()
    
    class Meta:
        model = Book
        fields = "__all__"



class ThreadListSerializer(serializers.ModelSerializer):
    comment_count = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()

    def get_comment_count(self, obj):
        return obj.thread_comments.count()
    def get_like_count(self, obj):
        return obj.like_users.count()
    
    class Meta:
        model = Thread
        fields = "__all__"



class CommentListSerializer(serializers.ModelSerializer):        
    like_count = serializers.SerializerMethodField()

    def get_like_count(self, obj):
        return obj.comment_like_set.count()
    
    class Meta:
        model = Comment
        fields = "__all__"



class ThreadCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = (
            "title",
            "content",
            "rank",
        )



class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "content",
        )
