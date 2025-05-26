// thread.js

import { defineStore } from 'pinia'
import { ref } from 'vue'

// 더미데이터
export const useThreadStore = defineStore('thread', () => {
  const threads = ref([
    // user_id: 1
    {
      id: 1,
      user_id: 1,
      book_id: 4,
      title: '다시 삶을 돌아보다',
      content: '삶의 무게를 다시 느낀 책입니다.',
      cover_img_url: 'https://picsum.photos/150/220?random=1',
      created_at: '2024-05-01',
      updated_at: '2024-05-01',
      rank: 4,
      like_count: 9,
      comment_count: 5
    },
    {
      id: 2,
      user_id: 1,
      book_id: 4,
      title: '짧은 글, 깊은 울림',
      content: '짧지만 마음을 흔드는 글이었어요.',
      cover_img_url: 'https://picsum.photos/150/220?random=2',
      created_at: '2024-05-02',
      updated_at: '2024-05-02',
      rank: 4,
      like_count: 4,
      comment_count: 1
    },
    {
      id: 3,
      user_id: 1,
      book_id: 3,
      title: '고요함 속의 사색',
      content: '혼자 있는 시간의 소중함을 느꼈다.',
      cover_img_url: 'https://picsum.photos/150/220?random=3',
      created_at: '2024-05-03',
      updated_at: '2024-05-03',
      rank: 5,
      like_count: 5,
      comment_count: 5
    },

    // user_id: 2
    {
      id: 4,
      user_id: 2,
      book_id: 1,
      title: '돈보다 중요한 가치',
      content: '재테크의 진짜 목적을 되돌아보게 하는 책.',
      cover_img_url: 'https://picsum.photos/150/220?random=4',
      created_at: '2024-05-04',
      updated_at: '2024-05-04',
      rank: 3,
      like_count: 12,
      comment_count: 1
    },
    {
      id: 5,
      user_id: 2,
      book_id: 6,
      title: '현실적인 재테크 전략',
      content: '실제로 실행 가능한 팁이 많았어요.',
      cover_img_url: 'https://picsum.photos/150/220?random=5',
      created_at: '2024-05-05',
      updated_at: '2024-05-05',
      rank: 5,
      like_count: 4,
      comment_count: 5
    },
    {
      id: 6,
      user_id: 2,
      book_id: 6,
      title: '가치 있는 소비란?',
      content: '내 소비 습관을 돌아보게 해준 책.',
      cover_img_url: 'https://picsum.photos/150/220?random=6',
      created_at: '2024-05-06',
      updated_at: '2024-05-06',
      rank: 4,
      like_count: 3,
      comment_count: 2
    },

    // user_id: 3
    {
      id: 7,
      user_id: 3,
      book_id: 1,
      title: '문장 하나에 담긴 세상',
      content: '짧은 문장에 큰 울림이 있었어요.',
      cover_img_url: 'https://picsum.photos/150/220?random=7',
      created_at: '2024-05-07',
      updated_at: '2024-05-07',
      rank: 4,
      like_count: 8,
      comment_count: 1
    },
    {
      id: 8,
      user_id: 3,
      book_id: 2,
      title: '숨 쉬듯 읽히는 책',
      content: '부담 없이 읽히는 명작이었어요.',
      cover_img_url: 'https://picsum.photos/150/220?random=8',
      created_at: '2024-05-08',
      updated_at: '2024-05-08',
      rank: 5,
      like_count: 6,
      comment_count: 2
    },
    {
      id: 9,
      user_id: 3,
      book_id: 3,
      title: '익숙한 풍경 속 이야기',
      content: '어디선가 본 듯한 따뜻한 이야기.',
      cover_img_url: 'https://picsum.photos/150/220?random=9',
      created_at: '2024-05-09',
      updated_at: '2024-05-09',
      rank: 5,
      like_count: 5,
      comment_count: 0
    },

    // user_id: 4
    {
      id: 10,
      user_id: 4,
      book_id: 4,
      title: '급류처럼 몰입감 넘치는 책',
      content: '하루 만에 다 읽은 책이에요.',
      cover_img_url: 'https://picsum.photos/150/220?random=10',
      created_at: '2024-05-10',
      updated_at: '2024-05-10',
      rank: 5,
      like_count: 10,
      comment_count: 5
    },
    {
      id: 11,
      user_id: 4,
      book_id: 5,
      title: '기후 위기와 인간성',
      content: '환경과 감정이 어우러진 작품.',
      cover_img_url: 'https://picsum.photos/150/220?random=11',
      created_at: '2024-05-11',
      updated_at: '2024-05-11',
      rank: 4,
      like_count: 7,
      comment_count: 1
    },
    {
      id: 12,
      user_id: 4,
      book_id: 6,
      title: '다정한 한마디의 힘',
      content: '말 한마디가 큰 위로가 되는 책.',
      cover_img_url: 'https://picsum.photos/150/220?random=12',
      created_at: '2024-05-12',
      updated_at: '2024-05-12',
      rank: 5,
      like_count: 6,
      comment_count: 2
    },

    // user_id: 5
    {
      id: 13,
      user_id: 5,
      book_id: 1,
      title: '환상의 책',
      content: '정말 환상적인 세계관이었어요.',
      cover_img_url: 'https://picsum.photos/150/220?random=13',
      created_at: '2024-05-13',
      updated_at: '2024-05-13',
      rank: 5,
      like_count: 9,
      comment_count: 1
    },
    {
      id: 14,
      user_id: 5,
      book_id: 2,
      title: '여운이 남는 작품',
      content: '다 읽고도 쉽게 잊히지 않았어요.',
      cover_img_url: 'https://picsum.photos/150/220?random=14',
      created_at: '2024-05-14',
      updated_at: '2024-05-14',
      rank: 4,
      like_count: 4,
      comment_count: 1
    },
    {
      id: 15,
      user_id: 5,
      book_id: 3,
      title: '문장이 살아있다',
      content: '단어 하나하나가 생명력을 가진 책.',
      cover_img_url: 'https://picsum.photos/150/220?random=15',
      created_at: '2024-05-15',
      updated_at: '2024-05-15',
      rank: 5,
      like_count: 8,
      comment_count: 3
    },

    // user_id: 6
    {
      id: 16,
      user_id: 6,
      book_id: 4,
      title: '시간을 잊게 한 소설',
      content: '한 번 읽기 시작하면 멈출 수 없어요.',
      cover_img_url: 'https://picsum.photos/150/220?random=16',
      created_at: '2024-05-16',
      updated_at: '2024-05-16',
      rank: 5,
      like_count: 11,
      comment_count: 4
    },
    {
      id: 17,
      user_id: 6,
      book_id: 5,
      title: '그림처럼 아름다운 이야기',
      content: '눈앞에 장면이 그려지는 듯했다.',
      cover_img_url: 'https://picsum.photos/150/220?random=17',
      created_at: '2024-05-17',
      updated_at: '2024-05-17',
      rank: 5,
      like_count: 7,
      comment_count: 0
    },
    {
      id: 18,
      user_id: 6,
      book_id: 6,
      title: '내 삶의 문장',
      content: '내 삶을 돌아보게 하는 문장들이 있었어요.',
      cover_img_url: 'https://picsum.photos/150/220?random=18',
      created_at: '2024-05-18',
      updated_at: '2024-05-18',
      rank: 5,
      like_count: 10,
      comment_count: 2
    },

    // user_id: 7
    {
      id: 19,
      user_id: 7,
      book_id: 1,
      title: '마음을 울리는 한 구절',
      content: '단 한 문장에 눈물이 났다.',
      cover_img_url: 'https://picsum.photos/150/220?random=19',
      created_at: '2024-05-19',
      updated_at: '2024-05-19',
      rank: 5,
      like_count: 13,
      comment_count: 3
    },
    {
      id: 20,
      user_id: 7,
      book_id: 2,
      title: '다 읽고도 생각나는 책',
      content: '언제 다시 꺼내 읽어도 좋은 책.',
      cover_img_url: 'https://picsum.photos/150/220?random=20',
      created_at: '2024-05-20',
      updated_at: '2024-05-20',
      rank: 4,
      like_count: 6,
      comment_count: 1
    },
    {
      id: 21,
      user_id: 7,
      book_id: 3,
      title: '책 속에 나를 비추다',
      content: '나 자신을 들여다보게 해주는 책.',
      cover_img_url: 'https://picsum.photos/150/220?random=21',
      created_at: '2024-05-21',
      updated_at: '2024-05-21',
      rank: 5,
      like_count: 10,
      comment_count: 2
    },

    // user_id: 8
    {
      id: 22,
      user_id: 8,
      book_id: 4,
      title: '매일 한 줄',
      content: '매일 한 문장씩 읽고 싶어지는 책.',
      cover_img_url: 'https://picsum.photos/150/220?random=22',
      created_at: '2024-05-22',
      updated_at: '2024-05-22',
      rank: 5,
      like_count: 9,
      comment_count: 1
    },
    {
      id: 23,
      user_id: 8,
      book_id: 5,
      title: '잊고 있던 감정',
      content: '내면의 감정을 다시 떠올리게 했다.',
      cover_img_url: 'https://picsum.photos/150/220?random=23',
      created_at: '2024-05-23',
      updated_at: '2024-05-23',
      rank: 4,
      like_count: 5,
      comment_count: 0
    },
    {
      id: 24,
      user_id: 8,
      book_id: 6,
      title: '위로가 된 책',
      content: '지친 날, 꼭 필요한 한 권이었다.',
      cover_img_url: 'https://picsum.photos/150/220?random=24',
      created_at: '2024-05-24',
      updated_at: '2024-05-24',
      rank: 5,
      like_count: 7,
      comment_count: 2
    }
  ])

  return {
    threads
  }
})