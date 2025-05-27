from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.core.files.base import ContentFile

import requests
from io import BytesIO
from PIL import Image, UnidentifiedImageError
import os
import re

from .models import Category, Book, Keyword, Thread
from .inserts import get_bestseller_list, get_item_new_special_list, get_new_category, get_keyword_list, get_author_info, get_book_audio_file, get_thread_cover_img, insert_book_keyword, insert_book_category
from .utils import is_valid_url

category_items = [
    "소설/시/희곡", "경제/경영", "자기계발", "인문/교양",
    "과학", "취미/실용", "어린이/청소년", "종교/철학",
]
keyword_items = [
    "성장", "감정", "사랑", "우정", "자기이해", "동기부여", "리더십", "창의성", "습관", "돈",
    "시간관리", "커리어", "심리", "철학", "역사", "문화", "여행", "요리", "건강", "과학기술",
    "AI", "환경", "미래", "교육", "감성", "창업", "자연", "가족", "명상", "스토리텔링",
]

# 더미데이터 삽입을 위한 함수
@api_view(["GET"])
def insert_books(request):
    # bestseller 50권 저장
    bestseller_list = get_bestseller_list()
    for bestseller in bestseller_list:
        print(bestseller)
        book = Book(
            title=bestseller["title"],
            description=bestseller["description"],
            isbn=bestseller["isbn"],
            publisher=bestseller["publisher"],
            pub_date=bestseller["pub_date"],
            author_name=bestseller["author"],
        )

        # author 정보
        author_data = get_author_info(book.author_name)
        book.author_info = author_data.get("summary", "")
        # author 썸네일
        author_thumb_url = author_data.get("thumbnail", "")
        if is_valid_url(author_thumb_url):
            try:
                response = requests.get(author_thumb_url, stream=True, timeout=5)
                if response.status_code == 200 and 'image' in response.headers.get("Content-Type", ""):
                    img = Image.open(response.raw)
                    buffer = BytesIO()
                    img.save(buffer, format="PNG")
                    book.author_profile_img_url.save(
                        f"{book.author_name[:10]}_thumbnail.png", 
                        ContentFile(buffer.getvalue())
                    )
            except (requests.RequestException, UnidentifiedImageError) as e:
                print(f"[author thumbnail 저장 실패] {author_thumb_url} - {e}")

        # 오디오 요약 파일
        try:
            mp3_fp = get_book_audio_file(book.author_name, book.title)
            book.audio_file.save(
                f"{book.title[:10]}_summary.mp3", 
                ContentFile(mp3_fp.read())
            )
        except Exception as e:
            print(f"[audio 저장 실패] {book.title} - {e}")

        # 책 표지 이미지
        cover_url = bestseller.get("cover", "")
        if is_valid_url(cover_url):
            try:
                response = requests.get(cover_url, stream=True, timeout=5)
                if response.status_code == 200 and 'image' in response.headers.get("Content-Type", ""):
                    img = Image.open(response.raw)
                    buffer = BytesIO()
                    img.save(buffer, format="PNG")
                    book.cover_img_url.save(
                        f"{book.title[:10]}_cover.png", 
                        ContentFile(buffer.getvalue())
                    )
            except (requests.RequestException, UnidentifiedImageError) as e:
                print(f"[cover 저장 실패] {cover_url} - {e}")

        # 최종 저장
        try:
            book.save()

            # category 저장
            insert_book_category(get_new_category(bestseller["category"]), book)
            
            # keyword_list 저장
            data = get_keyword_list(bestseller["title"])
            insert_book_keyword(data.split(","), book)
            
            print(f"[성공] '{book.title}' 저장 완료")
        except Exception as e:
            print(f"[ERROR] '{book.title}' 저장 실패: {e}")

    # 화제의 신작 50권 저장
    item_new_special_list = get_item_new_special_list()
    for item_new_special in item_new_special_list:
        print(item_new_special)
        book = Book(
            title=item_new_special["title"],
            description=item_new_special["description"],
            isbn=item_new_special["isbn"],
            publisher=item_new_special["publisher"],
            pub_date=item_new_special["pub_date"],
            author_name=item_new_special["author"],
        )

        # author 정보
        author_data = get_author_info(book.author_name)
        book.author_info = author_data.get("summary", "")
        # author 썸네일
        author_thumb_url = author_data.get("thumbnail", "")
        if is_valid_url(author_thumb_url):
            try:
                response = requests.get(author_thumb_url, stream=True, timeout=5)
                if response.status_code == 200 and 'image' in response.headers.get("Content-Type", ""):
                    img = Image.open(response.raw)
                    buffer = BytesIO()
                    img.save(buffer, format="PNG")
                    book.author_profile_img_url.save(
                        f"{book.author_name[:10]}_thumbnail.png", 
                        ContentFile(buffer.getvalue())
                    )
            except (requests.RequestException, UnidentifiedImageError) as e:
                print(f"[author thumbnail 저장 실패] {author_thumb_url} - {e}")

        # 오디오 요약 파일
        try:
            mp3_fp = get_book_audio_file(book.author_name, book.title)
            book.audio_file.save(
                f"{book.title[:10]}_summary.mp3", 
                ContentFile(mp3_fp.read())
            )
        except Exception as e:
            print(f"[audio 저장 실패] {book.title} - {e}")

        # 책 표지 이미지
        cover_url = item_new_special.get("cover", "")
        if is_valid_url(cover_url):
            try:
                response = requests.get(cover_url, stream=True, timeout=5)
                if response.status_code == 200 and 'image' in response.headers.get("Content-Type", ""):
                    img = Image.open(response.raw)
                    buffer = BytesIO()
                    img.save(buffer, format="PNG")
                    book.cover_img_url.save(
                        f"{book.title[:10]}_cover.png", 
                        ContentFile(buffer.getvalue())
                    )
            except (requests.RequestException, UnidentifiedImageError) as e:
                print(f"[cover 저장 실패] {cover_url} - {e}")

        # 최종 저장
        try:
            book.save()

            # category 저장
            insert_book_category(get_new_category(item_new_special["category"]), book)
            
            # keyword_list 저장
            data = get_keyword_list(item_new_special["title"])
            insert_book_keyword(data.split(","), book)
            
            print(f"[성공] '{book.title}' 저장 완료")
        except Exception as e:
            print(f"[ERROR] '{book.title}' 저장 실패: {e}")
        
    return Response({"message": "ok"}, status=status.HTTP_200_OK)

@api_view(["GET"])
def insert_threads(request):
    threads = Thread.objects.all()
    for thread in threads:
        cover_url = get_thread_cover_img(thread.content)
        print(cover_url)
        if is_valid_url(cover_url):
            try:
                response = requests.get(cover_url, stream=True, timeout=5)
                if response.status_code == 200 and 'image' in response.headers.get("Content-Type", ""):
                    img = Image.open(response.raw)
                    buffer = BytesIO()
                    img.save(buffer, format="PNG")
                    thread.cover_img_url.save(
                        f"{thread.title[:10]}_cover.png", 
                        ContentFile(buffer.getvalue()),
                    )
            except (requests.RequestException, UnidentifiedImageError) as e:
                print(f"[cover 저장 실패] {cover_url} - {e}")
    return Response({"message": "ok"}, status=status.HTTP_200_OK)

@api_view(["GET"])
def insert_categories(request):
    for item in category_items:
        Category.objects.get_or_create(name=item)
    return Response({"message": "ok"}, status=status.HTTP_200_OK)

@api_view(["GET"])
def insert_keywords(request):
    for item in keyword_items:
        Keyword.objects.get_or_create(name=item)
    return Response({"message": "ok"}, status=status.HTTP_200_OK)

@api_view(["GET"])
def insert_book_ranks(request):
    books = Book.objects.all()
    for book in books:
        total_rank = 0.0
        cnt = 0
        threads = Thread.objects.filter(book=book)
        if threads:
            for thread in threads:
                total_rank += thread.rank
                cnt += 1
            book.rank = round(total_rank / cnt, 2)
            book.save()
    return Response({"message": "ok"}, status=status.HTTP_200_OK)

@api_view(["GET"])
def insert_book_background_img(request):
    books = Book.objects.all()
    cnt = 1
    for book in books:
        new_title  = re.sub(r'[\\/*?:"<>|]', '', book.title[:10])
        book.background_img_url = f"{new_title}_background_img_{cnt}.png"
        book.save()
        cnt += 1
    return Response({"message": "ok"}, status=status.HTTP_200_OK)

@api_view(["GET"])
def change_book_background_img_file_name(request):
    books = Book.objects.all()
    cnt = 1
    for book in books:
        new_title  = re.sub(r'[\\/*?:"<>|]', '', book.title[:10])
        
        # 원본 파일 경로
        old_path = rf"C:\Users\SSAFY\Desktop\title\{cnt}.png"

        # 새 파일 경로 (이름 변경)
        new_path = rf"C:\Users\SSAFY\Desktop\title\{new_title}_background_img_{cnt}.png"

        # 이름 변경
        os.rename(old_path, new_path)

        cnt += 1
    
    return Response({"message": "ok"}, status=status.HTTP_200_OK)

@api_view(["GET"])
def change_book_background_img_file_name_again(request):
    books = Book.objects.all()
    for book in books:
        book.background_img_url = f"books/background_imgs/{book.background_img_url}"
        book.save()
    return Response({"message": "ok"}, status=status.HTTP_200_OK)
