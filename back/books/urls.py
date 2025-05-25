from django.urls import path
from . import views
from . import creates

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

    # 더미데이터 삽입
    path("insert_books/", creates.insert_books),
    path("insert_categories/", creates.insert_categories),
    path("insert_keywords/", creates.insert_keywords),
    path("insert_threads/", creates.insert_threads),
    path("insert_books_rank/", creates.insert_books_rank),
]
