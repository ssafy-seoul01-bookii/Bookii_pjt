from django.urls import path
from . import views
from . import creates

urlpatterns = [
    path("categories/", views.get_categories),
    path("keywords/", views.get_keywords),
    path("", views.get_books),
    path("get_high_rank_book_by_critic/", views.get_high_rank_book_by_critic),
    path("get_many_threads_book/", views.get_many_threads_book),
    path("get_high_rank_book/", views.get_high_rank_book),
    path("<int:book_pk>/", views.get_book),
    path("<int:book_pk>/threads/", views.get_threads),
    path("<int:book_pk>/threads/create_thread/", views.create_thread),
    path("<int:book_pk>/threads/<int:thread_pk>/", views.get_update_delete_thread),
    path("<int:book_pk>/threads/<int:thread_pk>/comments/", views.get_comments),
    path("<int:book_pk>/threads/<int:thread_pk>/comments/create_comment/", views.create_comment),
    path("<int:book_pk>/threads/<int:thread_pk>/comments/<int:comment_pk>/", views.delete_comment),
    # path("search/", views.search_books),

    # 더미데이터 삽입
    path("insert_books/", creates.insert_books),
    path("insert_categories/", creates.insert_categories),
    path("insert_keywords/", creates.insert_keywords),
    path("insert_threads/", creates.insert_threads),
    path("insert_book_ranks/", creates.insert_book_ranks),
    path("insert_book_background_img/", creates.insert_book_background_img),
    path("change_book_background_img_file_name/", creates.change_book_background_img_file_name),
]
