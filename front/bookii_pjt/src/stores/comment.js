// comment.js

import { defineStore } from 'pinia'
import { ref } from 'vue'

// 더미데이터
export const useCommentStore = defineStore('comment', () => {
  const comments = ref([
    {
      id: 1,
      thread_id: 5,
      user_id: 7,
      content: '내용이 흥미롭고 생각할 거리가 많았어요.',
      created_at: '2024-05-20',
      updated_at: '2024-05-20'
    },
    {
      id: 2,
      thread_id: 3,
      user_id: 5,
      content: '이 책 덕분에 마음이 따뜻해졌어요.',
      created_at: '2024-05-14',
      updated_at: '2024-05-14'
    },
    {
      id: 3,
      thread_id: 8,
      user_id: 10,
      content: '이런 주제 너무 좋아요. 공감돼요!',
      created_at: '2024-05-08',
      updated_at: '2024-05-08'
    },
    {
      id: 4,
      thread_id: 1,
      user_id: 4,
      content: '읽고 나서 깊은 여운이 남네요.',
      created_at: '2024-05-01',
      updated_at: '2024-05-01'
    },
    {
      id: 5,
      thread_id: 7,
      user_id: 9,
      content: '추천 감사합니다. 꼭 읽어볼게요.',
      created_at: '2024-05-07',
      updated_at: '2024-05-07'
    },
    {
      id: 6,
      thread_id: 6,
      user_id: 1,
      content: '리뷰가 정말 정성스럽네요.',
      created_at: '2024-05-06',
      updated_at: '2024-05-06'
    },
    {
      id: 7,
      thread_id: 2,
      user_id: 8,
      content: '이 책에서 제일 인상깊었던 부분은...',
      created_at: '2024-05-02',
      updated_at: '2024-05-02'
    },
    {
      id: 8,
      thread_id: 4,
      user_id: 3,
      content: '감정선이 섬세하게 표현된 것 같아요.',
      created_at: '2024-05-04',
      updated_at: '2024-05-04'
    },
    {
      id: 9,
      thread_id: 1,
      user_id: 2,
      content: '읽는 내내 울컥했어요.',
      created_at: '2024-05-01',
      updated_at: '2024-05-01'
    },
    {
      id: 10,
      thread_id: 5,
      user_id: 6,
      content: '책의 분위기랑 잘 어울리는 리뷰네요.',
      created_at: '2024-05-05',
      updated_at: '2024-05-05'
    },
    {
      id: 11,
      thread_id: 2,
      user_id: 10,
      content: '나도 읽고 싶은 책이에요!',
      created_at: '2024-05-02',
      updated_at: '2024-05-02'
    },
    {
      id: 12,
      thread_id: 6,
      user_id: 2,
      content: '다음 책도 기대돼요.',
      created_at: '2024-05-06',
      updated_at: '2024-05-06'
    },
    {
      id: 13,
      thread_id: 3,
      user_id: 1,
      content: '내가 느꼈던 감정이랑 비슷해서 놀랐어요.',
      created_at: '2024-05-03',
      updated_at: '2024-05-03'
    },
    {
      id: 14,
      thread_id: 4,
      user_id: 7,
      content: '몰입도가 상당했어요.',
      created_at: '2024-05-04',
      updated_at: '2024-05-04'
    },
    {
      id: 15,
      thread_id: 8,
      user_id: 4,
      content: '정말 중요한 이야기예요.',
      created_at: '2024-05-08',
      updated_at: '2024-05-08'
    },
    {
      id: 16,
      thread_id: 7,
      user_id: 6,
      content: '비슷한 책이 있다면 추천해주세요!',
      created_at: '2024-05-07',
      updated_at: '2024-05-07'
    },
    {
      id: 17,
      thread_id: 5,
      user_id: 8,
      content: '표현력이 좋네요.',
      created_at: '2024-05-05',
      updated_at: '2024-05-05'
    },
    {
      id: 18,
      thread_id: 6,
      user_id: 3,
      content: '저도 이런 책 정말 좋아해요!',
      created_at: '2024-05-06',
      updated_at: '2024-05-06'
    },
    {
      id: 19,
      thread_id: 2,
      user_id: 5,
      content: '내용이 참 알찼어요.',
      created_at: '2024-05-02',
      updated_at: '2024-05-02'
    },
    {
      id: 20,
      thread_id: 3,
      user_id: 9,
      content: '책 추천 감사해요!',
      created_at: '2024-05-03',
      updated_at: '2024-05-03'
    }
  ])

  return { comments }
})