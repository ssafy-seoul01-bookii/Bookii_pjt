from rest_framework import serializers
from .models import Category, Book, Thread, Comment, Keyword
from accounts.models import User

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"



class KeywordListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = "__all__"



class BookListSerializer(serializers.ModelSerializer):
    thread_count = serializers.IntegerField(read_only=True)
    keywords = serializers.SerializerMethodField()
    categories = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = (
            "id", "title", "description", "isbn", "cover_img_url",
            "background_img_url", "publisher", "pub_date", "author_name",
            "author_info", "author_profile_img_url", "audio_file", "rank",
            "thread_count", "keywords", "categories",
        )

    def get_keywords(self, obj):
        return [keyword.name for keyword in obj.keyword.all()]
    def get_categories(self, obj):
        return [category.name for category in obj.category.all()]



class ThreadListSerializer(serializers.ModelSerializer):
    comment_count = serializers.IntegerField(read_only=True)
    like_count = serializers.IntegerField(read_only=True)
    username = serializers.CharField(source="user.username", read_only=True)
    
    class Meta:
        model = Thread
        fields = (
            "id",
            "book",
            "user",
            "username",
            "like_count",
            "comment_count",
            "title",
            "content",
            "cover_img_url",
            "reading_date",
            "created_at",
            "updated_at",
            "rank",
        )



class CommentListSerializer(serializers.ModelSerializer):
    like_count = serializers.IntegerField(read_only=True)
    username = serializers.CharField(source="user.username", read_only=True,)

    class Meta:
        model = Comment
        fields = (
            "id",
            "like_count",
            "thread",
            "user",
            "username",
            "content",
            "created_at",
            "updated_at",
        )



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



class UserFollowCountSerializer(serializers.ModelSerializer):
    follower_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "follower_count",
            "following_count",
        )

    def get_follower_count(self, obj):
        # 해당 유저를 follow하는 사람 수
        return obj.followers.count()
    def get_following_count(self, obj):
        # 해당 유저가 follow하는 사람 수
        return obj.followings.count()
