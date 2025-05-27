from django.urls import path
from . import views
from . import creates

urlpatterns = [
    path("get_user_follow_count/<int:user_pk>/", views.get_user_follow_counts),
    path("get_user_threads/<int:user_pk>/", views.get_user_threads),
    
    # 로그인 안 한 상태일 때
    path("get_many_threads_book/", views.get_many_threads_books),
    path("get_high_rank_book/", views.get_high_rank_books),
    path("get_high_rank_book_by_critic/", views.get_high_rank_books_by_critic),

    # 로그인 상태일 때
    path("get_threads_ordered_by_likes/", views.get_threads_ordered_by_likes),
    path("get_keywords_recommend_books_by_last_thread/", views.get_keywords_recommend_books_by_last_thread),
    # path("get_greatest_recommendation/", views.get_greatest_recommendation),

    # 책 상세 페이지
    path("<int:book_pk>/get_keywords_books/", views.get_keywords_books),
    path("get_followings_threads/", views.get_followings_threads),

    path("categories/", views.get_categories),
    path("keywords/", views.get_keywords),
    path("", views.get_books),
    path("<int:book_pk>/", views.get_book),
    path("<int:book_pk>/threads/", views.get_threads),
    path("<int:book_pk>/threads/create_thread/", views.create_thread),
    path("<int:book_pk>/threads/<int:thread_pk>/", views.get_update_delete_thread),
    path("<int:book_pk>/threads/<int:thread_pk>/comments/", views.get_comments),
    path("<int:book_pk>/threads/<int:thread_pk>/comments/create_comment/", views.create_comment),
    path("<int:book_pk>/threads/<int:thread_pk>/comments/<int:comment_pk>/", views.delete_comment),

    # 더미데이터 삽입
    path("insert_books/", creates.insert_books),
    path("insert_categories/", creates.insert_categories),
    path("insert_keywords/", creates.insert_keywords),
    path("insert_threads/", creates.insert_threads),
    path("insert_book_ranks/", creates.insert_book_ranks),
    path("insert_book_background_img/", creates.insert_book_background_img),
    path("change_book_background_img_file_name/", creates.change_book_background_img_file_name),
    path("change_book_background_img_file_name_again/", creates.change_book_background_img_file_name_again),
]
