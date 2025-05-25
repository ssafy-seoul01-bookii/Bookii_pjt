// book.js

// stores/book.js
import { defineStore } from 'pinia'
import { ref } from 'vue'

// 더미데이터 삽입
export const useBookStore = defineStore('book', () => {
  const books = ref([
    {
      id: 1,
      title: '단 한 번의 삶',
      description: '김영하 작가의 인생과 삶에 대한 통찰이 담긴 산문집.',
      isbn: '9788932901929',
      cover_img_url: 'https://picsum.photos/150/220?random=1',
      publisher: '문학동네',
      pub_date: '2024-03-15',
      author_name: '김영하',
      author_info: '소설가이자 방송인. 다양한 매체에서 활약 중.',
      author_profile_img_url: 'https://via.placeholder.com/100x100?text=김영하',
      rank: 5,
      threadCount: 10,
      tags: ['삶', '문학', '산문집', '김영하', '자기계발']
    },
    {
      id: 2,
      title: '부의 전략 수업',
      description: '돈에 휘둘리지 않고 살아남는 시스템을 제시하는 재테크 필독서.',
      isbn: '9788997924905',
      cover_img_url: 'https://picsum.photos/150/220?random=2',
      publisher: '경제출판사',
      pub_date: '2023-11-21',
      author_name: '폴 포조스키',
      author_info: '국제 금융 컨설턴트이자 베스트셀러 작가.',
      author_profile_img_url: 'https://via.placeholder.com/100x100?text=Author2',
      rank: 4,
      threadCount: 5,
      tags: ['자기계발', '재테크', '경제전략', '삶', '성장']
    },
    {
      id: 3,
      title: '숨',
      description: '숨이라는 행위에 담긴 철학과 삶의 본질에 대한 성찰.',
      isbn: '9788997929999',
      cover_img_url: 'https://picsum.photos/150/220?random=3',
      publisher: '철학사',
      pub_date: '2022-09-10',
      author_name: '류시화',
      author_info: '시인, 에세이스트, 명상가.',
      author_profile_img_url: 'https://via.placeholder.com/100x100?text=류시화',
      rank: 4,
      threadCount: 2,
      tags: ['삶', '명상', '내면탐구', '철학', '감정']
    },
    {
      id: 4,
      title: '급류',
      description: '관계와 감정의 소용돌이를 담은 정대건 작가의 소설.',
      isbn: '9788997928888',
      cover_img_url: 'https://picsum.photos/150/220?random=4',
      publisher: '민음사',
      pub_date: '2023-01-25',
      author_name: '정대건',
      author_info: '소설가. 인간 내면을 섬세하게 묘사함.',
      author_profile_img_url: 'https://via.placeholder.com/100x100?text=정대건',
      rank: 3,
      threadCount: 3,
      tags: ['감정', '관계', '문학', '소설', '심리']
    },
    {
      id: 5,
      title: '지구 끝의 온실',
      description: '기후 재앙 이후 남은 사람들의 생존과 윤리에 대한 SF 소설.',
      isbn: '9788937473217',
      cover_img_url: 'https://picsum.photos/150/220?random=5',
      publisher: '자음과모음',
      pub_date: '2021-09-01',
      author_name: '김초엽',
      author_info: 'SF와 페미니즘을 아우르는 젊은 작가.',
      author_profile_img_url: 'https://via.placeholder.com/100x100?text=김초엽',
      rank: 5,
      threadCount: 8,
      tags: ['SF소설', '페미니즘', '미래', '문학', '생존']
    },
    {
      id: 6,
      title: '죽고 싶지만 떡볶이는 먹고 싶어',
      description: '삶의 우울을 담담하게 풀어낸 심리 에세이.',
      isbn: '9788968331862',
      cover_img_url: 'https://picsum.photos/150/220?random=6',
      publisher: '흔',
      pub_date: '2018-06-20',
      author_name: '백세희',
      author_info: '자신의 경험을 바탕으로 우울증과 삶을 풀어낸 작가.',
      author_profile_img_url: 'https://via.placeholder.com/100x100?text=백세희',
      rank: 4,
      threadCount: 6,
      tags: ['우울', '감정', '삶', '에세이', '힐링']
    }
  ])

  return {
    books
  }
})