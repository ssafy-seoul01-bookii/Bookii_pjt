from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20,)

class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category",)
    title = models.CharField(max_length=30,)
    description = models.TextField()
    isbn = models.CharField(max_length=20,)
    cover = models.ImageField(upload_to="",)
    publisher = models.CharField(max_length=20,)
    pub_date = models.DateField()
    author = models.CharField(max_length=20,)
    customer_review_rank = models.IntegerField()

class Thread(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="threads",)
    title = models.CharField(max_length=30,)
    content = models.TextField()
    reading_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True,)

class Comment(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name="comments",)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True,)
