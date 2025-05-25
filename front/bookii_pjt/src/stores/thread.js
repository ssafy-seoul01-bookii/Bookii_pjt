// thread.js

import { defineStore } from 'pinia'
import { ref } from 'vue'

// 더미데이터
export const useThreadStore = defineStore('thread', () => {
  const threads = ref([
    {
      id: 1,
      book_id: 1,
      user_id: 101,
      title: '삶에 대해 다시 생각하게 됐다',
      content: '김영하 작가의 문장을 읽으며 내 삶을 성찰하게 되었다.',
      cover_img_url: 'https://via.placeholder.com/100x100?text=Thread1',
      created_at: '2024-05-01',
      updated_at: '2024-05-01',
      rank: 5
    },
    {
      id: 2,
      book_id: 2,
      user_id: 102,
      title: '재테크 입문서로 딱 좋아요',
      content: '부의 전략 수업은 현실적인 팁이 많아 좋았어요.',
      cover_img_url: 'https://via.placeholder.com/100x100?text=Thread2',
      created_at: '2024-05-02',
      updated_at: '2024-05-02',
      rank: 4
    },
    {
      id: 3,
      book_id: 3,
      user_id: 103,
      title: '숨에 대한 철학적 고찰',
      content: '짧은 문장에 삶의 무게가 담겨있어요.',
      cover_img_url: 'https://via.placeholder.com/100x100?text=Thread3',
      created_at: '2024-05-03',
      updated_at: '2024-05-03',
      rank: 4
    },
    {
      id: 4,
      book_id: 4,
      user_id: 104,
      title: '급류는 감정의 롤러코스터',
      content: '정대건 작가의 필력에 압도당했어요. 몰입감 최고!',
      cover_img_url: 'https://via.placeholder.com/100x100?text=Thread4',
      created_at: '2024-05-04',
      updated_at: '2024-05-04',
      rank: 5
    },
    {
      id: 5,
      book_id: 5,
      user_id: 105,
      title: '지구 끝의 온실을 읽고 나서',
      content: 'SF인데 현실보다 더 현실 같았던 이야기...',
      cover_img_url: 'https://via.placeholder.com/100x100?text=Thread5',
      created_at: '2024-05-05',
      updated_at: '2024-05-05',
      rank: 5
    },
    {
      id: 6,
      book_id: 6,
      user_id: 106,
      title: '떡볶이 에세이의 위로',
      content: '누군가 내 마음을 이렇게 정확히 쓴 줄 몰랐어요.',
      cover_img_url: 'https://via.placeholder.com/100x100?text=Thread6',
      created_at: '2024-05-06',
      updated_at: '2024-05-06',
      rank: 4
    },
    {
      id: 7,
      book_id: 1,
      user_id: 107,
      title: '문장의 힘을 느낀 책',
      content: '단어 하나하나가 마음을 건드리는 책이었어요.',
      cover_img_url: 'https://via.placeholder.com/100x100?text=Thread7',
      created_at: '2024-05-07',
      updated_at: '2024-05-07',
      rank: 5
    },
    {
      id: 8,
      book_id: 5,
      user_id: 108,
      title: '미래를 생각하게 만든 책',
      content: '기후 위기를 이토록 감성적으로 풀어낸 책은 처음이에요.',
      cover_img_url: 'https://via.placeholder.com/100x100?text=Thread8',
      created_at: '2024-05-08',
      updated_at: '2024-05-08',
      rank: 5
    }
  ])

  return {
    threads
  }
})