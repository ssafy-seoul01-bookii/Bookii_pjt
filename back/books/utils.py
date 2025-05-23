from openai import OpenAI
import json
from pydantic import BaseModel
import requests
import os
from gtts import gTTS
import io

OPENAI_API_KEY= os.environ.get("ALADDIN_API_KEY")
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
