from rest_framework import serializers
from .models import Category, Book, Thread, Comment

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "author",
            "isbn",
            "cover",
        )

class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    class ThreadDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Thread
            fields = (
                "id",
                "title",
                "content",
                "reading_date",
            )
    
    class CategoryDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Category
            fields = (
                "id",
                "name",
            )

class ThreadListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = (
            "id",
            "title",
            "book",
        )
    
    class BookDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Book
            fields = (
                "title",
            )
    
    book = BookDetailSerializer(read_only=True)

class ThreadDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = "__all__"
    
    class BookDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Book
            fields = (
                "title",
            )
    
    book = BookDetailSerializer(read_only=True)

    class CommentListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = "__all__"
    
        class ThreadDetailSerializer(serializers.ModelSerializer):
            class Meta:
                model = Thread
                fields = (
                    "title",
                )
        
        thread = ThreadDetailSerializer(read_only=True)

    comments = CommentListSerializer(read_only=True, many=True)

    num_of_comments = serializers.SerializerMethodField()

    def get_num_of_comments(self, obj):
        return obj.num_of_comments

class ThreadCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = (
            "title",
            "content",
            "reading_date",
        )

class CommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
    
    class ThreadDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Thread
            fields = (
                    "title",
                )
    
    thread = ThreadDetailSerializer(read_only =True)

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "content",
        )
