from openai import OpenAI

import os
import json

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Book, Thread

OPENAI_API_KEY= os.environ.get("GPT_API_KEY")
TTB_KEY = os.environ.get("ALADDIN_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

def is_valid_url(url):
    validate = URLValidator()
    try:
        validate(url)
        return True
    except ValidationError:
        return False

def get_ai_thread_kw(context):
    thread_context = """
                    당신은 사용자의 도서 리뷰를 읽고 핵심 감정 5개를 추출해내는 AI입니다.
                    추출된 감정 5개를 comma로 나눠서 반환해주세요.
                    감정 5개를 제외한 다른 정보를 응답해서는 안됩니다.
                    응답 예시: '슬픔, 기쁨, 행복, 만족감, 허무함'
                    """
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": thread_context,
            },
            {
                "role": "user",
                "content": context,
            },
        ],
    )
    summary = completion.choices[0].message.content
    return summary

def get_thread_cover_img(content):
    feelings = get_ai_thread_kw(content)
    thread_cover_context = f"""
                            당신은 감정 5개를 바탕으로 이미지를 그려주는 ai 입니다.
                            창의적이고 감성적으로 표현해 주세요.
                            아래의 콤마로 나눠진 감정 5개를 바탕으로 이미지를 생성해주세요.
                            감정 또는 상황: {feelings}
                            """
    response = client.images.generate(
        model="dall-e-3",
        prompt=thread_cover_context,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    cover_img = response.data[0].url
    return cover_img

def update_book_rank(book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    total_rank = 0.0
    cnt = 0
    threads = get_list_or_404(Thread, book=book)
    if threads:
        for thread in threads:
            total_rank += thread.rank
            cnt += 1
        book.rank = round(total_rank / cnt, 2)
        book.save()

# def get_greatest_recommendation(books, user):
#     prompt = f"books: {books}, user: {user}"
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {
#                 "role": "system",
#                 "content":
#                 """
#                 """
#             },
#             {
#                 "role": "user",
#                 "content": prompt,
#             },
#         ],
#         temperature=1,
#         max_tokens=256,
#     )
#     book_list = response.choices[0].message.content
#     return book_list
