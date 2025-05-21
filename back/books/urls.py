from django.urls import path
from . import views

urlpatterns = [
    path("categories/", views.get_categories),
    path("", views.get_books),
    path("<int:book_pk>/", views.get_book),
    path("<int:book_pk>/threads/", views.get_threads),
    path("<int:book_pk>/threads/create_thread/", views.create_thread),
    path("<int:book_pk>/threads/<int:thread_pk>/", views.get_update_delete_thread),
    path("<int:book_pk>/threads/<int:thread_pk>/comments/create_comment/", views.create_comment),
    path("<int:book_pk>/threads/<int:thread_pk>/comments/<int:comment_pk>/", views.get_update_delete_comment),
    path("search/", views.search_books),
]
