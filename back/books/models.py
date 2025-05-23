from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

PATH = {
    "Book": {
        "cover_img": "books/book_covers/",
        "author_img": "books/author_imgs/",
        "audio_file": "books/audios/",
    },
    "Thread": {
        "cover_img": "threads/thread_covers/",
    }
}

class Category(models.Model):
    name = models.CharField(max_length=20,)

class Book(models.Model):
    category = models.ManyToManyField(to="books.Category", through="Book_category", related_name="book_categories",)
    title = models.CharField(max_length=30,)
    description = models.TextField()
    isbn = models.CharField(max_length=15,)
    cover_img_url = models.ImageField(upload_to=PATH["Book"]["cover_img"], default="default_img.png",)
    publisher = models.CharField(max_length=15,)
    pub_date = models.DateField()
    author_name = models.CharField(max_length=15,)
    author_info = models.TextField()
    author_profile_img_url = models.ImageField(upload_to=PATH["Book"]["author_img"], default="default_img.png",)
    audio_file = models.FileField(upload_to=PATH["Book"]["audio_file"], blank=True,)
    rank = models.PositiveIntegerField(
        blank=True,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0),
        ],
        default=0,
    )
    keywords = models.JSONField(blank=True, default=list)

class Thread(models.Model):
    book = models.ForeignKey(to="books.Book", on_delete=models.CASCADE, related_name="book_threads",)
    user = models.ForeignKey(to="accounts.User", on_delete=models.CASCADE, related_name="user_threads",)
    title = models.CharField(max_length=30,)
    content = models.TextField()
    cover_img_url = models.ImageField(upload_to=PATH["Thread"]["cover_img"], default="default_img.png",)
    reading_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True,)
    like_users = models.ManyToManyField(
        to="accounts.User",
        through="books.Thread_like",
        related_name="like_threads",
    )

class Comment(models.Model):
    thread = models.ForeignKey(to="books.Thread", on_delete=models.CASCADE, related_name="thread_comments",)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True,)

class Book_category(models.Model):
    book = models.ForeignKey(to="books.Book", on_delete=models.CASCADE,)
    category = models.ForeignKey(to="books.Category", on_delete=models.CASCADE,)

class Preferred_category(models.Model):
    user = models.ForeignKey(to="accounts.User", on_delete=models.CASCADE,)
    category = models.ForeignKey(to="books.Category", on_delete=models.CASCADE,)

class Thread_like(models.Model):
    thread = models.ForeignKey(to="books.Thread", on_delete=models.CASCADE,)
    user = models.ForeignKey(to="accounts.User", on_delete=models.CASCADE,)

class Comment_like(models.Model):
    user = models.ForeignKey(to="accounts.User", on_delete=models.CASCADE,)
    comment = models.ForeignKey(to="books.Comment", on_delete=models.CASCADE,)
