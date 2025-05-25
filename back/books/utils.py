from openai import OpenAI
from pydantic import BaseModel
from gtts import gTTS
from datetime import datetime

import requests
import os
import io
import json

OPENAI_API_KEY= os.environ.get("ALADDIN_API_KEY")
TTB_KEY = os.environ.get("ALADDIN_API_KEY")
client = OpenAI(api_key=os.environ.get("GPT_API_KEY"))

class Author_info(BaseModel):
    books: list[str]
    summary: str
    thumbnail: str

def get_author_info(author_name):
    wiki_api_url = f"https://ko.wikipedia.org/api/rest_v1/page/summary/{author_name}"
    wiki_response = requests.get(wiki_api_url)
    wiki_parsed_data = wiki_response.json()
    
    persona = """
                당신은 wikipedia 데이터를 바탕으로 작가 정보를 구조화하는 AI입니다.
                JSON 형식으로 아래와 같이 출력하세요.
                {
                    "summary": "작가에 대한 한 문장 설명",
                    "books": ["대표작1", "대표작2", "대표작3", "대표작4", "대표작5"],
                    "thumbnail": "작가 사진의 링크"
                }
                """
    user_prompt = f"""
                    아래는 위키백과에서 가져온 {author_name}의 설명입니다:
                    {wiki_parsed_data.get("extract", "")}
                    작가에 대한 한 문장 설명, 대표작 5개, 작가 사진 링크를 JSON 형식으로 정리해 주세요.
                    작가에 대한 한 문장 설명은 위키백과에서 가져온 문장 중 첫 문장을 수정하지 않고 제공해주세요.
                    """
    response = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages = [
            {
                "role": "system",
                "content": persona,
            },
            {
                "role": "user",
                "content": user_prompt
            },
        ],
        response_format = Author_info,
    )
    parsed_data = json.loads(response.choices[0].message.content)
    return parsed_data

def get_book_audio_file(author_name, book_title):
    prompt = f"작가이름: {author_name}, 책 이름: {book_title}"
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system", "content": """당신을 작가와 도서에 대한 정보를 제공하는 AI입니다.
                "작가와 작가의 도서명을 입력받은 후 작가와 도서 정보에 대한 요약본을 텍스트 형식으로 출력하시오."
                "*을 사용하지 말고, 영어로 이름 제공해주지 않아도 됨."""
            },
            {
                "role": "user", "content": prompt
            },
        ],
        temperature=1,
        max_tokens=256,
    )
    ai_text = response.choices[0].message.content
    
    # gTTS로 텍스트를 음성으로 변환
    tts = gTTS(text=ai_text, lang='ko')
    
    # BytesIO 객체에 저장
    mp3_fp = io.BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    
    return mp3_fp

def get_bestseller_list():
    url = "http://www.aladin.co.kr/ttb/api/ItemList.aspx"
    params = {
        "ttbkey": TTB_KEY,
        "QueryType": "Bestseller",
        "MaxResults": 50,
        "start": 1,
        "SearchTarget": "Book",
        "output": "js",
        "Version": "20131101"
    }

    response = requests.get(url=url, params=params,)
    
    if response.status_code == 200:
        items = response.json().get("item", [])
        books = []

        for item in items:
            book = {
                "title": item.get("title", ""),
                "author": item.get("author", ""),
                "description": item.get("description", ""),
                "isbn": item.get("isbn13", item.get("isbn")),
                "cover": item.get("cover", ""),
                "publisher": item.get("publisher", ""),
                "pub_date": None,
                "category": item.get("categoryName", ""),
            }

            pub_date_str = item.get("pubDate")
            if pub_date_str:
                try:
                    book["pub_date"] = datetime.strptime(pub_date_str, "%Y-%m-%d").date()
                except ValueError:
                    pass  # 날짜 형식이 잘못됐을 경우 생략

            books.append(book)

        return books
    else:
        raise Exception(f"API 호출 실패: {response.status_code}")

def get_item_new_special_list():
    url = "http://www.aladin.co.kr/ttb/api/ItemList.aspx"
    params = {
        "ttbkey": TTB_KEY,
        "QueryType": "ItemNewSpecial",
        "MaxResults": 50,
        "start": 1,
        "SearchTarget": "Book",
        "output": "js",
        "Version": "20131101"
    }

    response = requests.get(url=url, params=params,)
    
    if response.status_code == 200:
        items = response.json().get("item", [])
        books = []

        for item in items:
            book = {
                "title": item.get("title", ""),
                "author": item.get("author", ""),
                "description": item.get("description", ""),
                "isbn": item.get("isbn13", item.get("isbn")),
                "cover": item.get("cover", ""),
                "publisher": item.get("publisher", ""),
                "pub_date": None,
                "category": item.get("categoryName", ""),
            }

            pub_date_str = item.get("pubDate")
            if pub_date_str:
                try:
                    book["pub_date"] = datetime.strptime(pub_date_str, "%Y-%m-%d").date()
                except ValueError:
                    pass  # 날짜 형식이 잘못됐을 경우 생략

            books.append(book)

        return books
    else:
        raise Exception(f"API 호출 실패: {response.status_code}")

def get_new_category(old_category):
    prompt = f"old_category: {old_category}"
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content":
                """
                당신은 도서의 카테고리를 분류하는 AI입니다.
                카테고리인 old_category를 입력 받은 후, 소설/시/회곡, 경제/경영, 자기계발, 인문/교양, 과학, 취미/실용, 어린이/청소년, 종교/철학
                이 8가지 카테고리 중 입력 받은 카테고리와 가장 유사한 한 가지를 선택해서 텍스트 형식으로 출력하시오.
                """
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        temperature=1,
        max_tokens=256,
    )
    new_category = response.choices[0].message.content
    return new_category

def get_keyword_list(book_title):
    prompt = f"book_title: {book_title}"
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content":
                """
                당신은 도서의 키워드를 정하는 AI입니다.
                book_title을 입력 받으면, 해당 도서에 관련된 2개 ~ 5개 사이의 키워드를 해시태그 형식으로 뽑아주세요.
                그리고 키워드에 소설, 희곡, 에세이와 같은 도서 카테고리는 제외해서 선정해주세요.
                인스타그램의 해시태그를 활용하면 좋을 것 같습니다.
                키워드를 #을 제거한 문자열 리스트 형식의 파이썬 데이터 타입으로 출력하시오.
                """
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        temperature=1,
        max_tokens=256,
    )
    keywords = response.choices[0].message.content
    return keywords

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
                            감정 또는 상황 : {feelings}
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
