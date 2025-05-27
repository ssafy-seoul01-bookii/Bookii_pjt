// stores/thread.js
import { defineStore } from 'pinia'
import { ref } from 'vue'
import api from '@/lib/axios'

export const useThreadStore = defineStore('thread', () => {
  const threads = ref([])
  const bookThreads = ref([]) // bookId 기준 쓰레드
  const followingThreads = ref([]) // 팔로잉 유저 쓰레드
  const sortedThreads = ref([]) // 전체 쓰레드
  const baseUrl = 'http://localhost:8000'

  // ✅ thread 이미지 경로 보정 추가
  const fetchThreads = async (bookId, followingUserIds = []) => {
    try {
      const res = await api.get(`/books/${bookId}/threads/`)
      const baseUrl = 'http://localhost:8000'

      threads.value = res.data.map(thread => ({
        ...thread,
        book_id: thread.book,
        cover_img_url: thread.cover_img_url
          ? baseUrl + thread.cover_img_url.replace('/threads/', '/books/')
          : ''
      }))

      followingThreads.value = threads.value.filter(t =>
        followingUserIds.includes(t.user_id)
      )
    } catch (err) {
      console.error('쓰레드 불러오기 실패:', err)
    }
  }

  const fetchThreadById = async (id, bookId) => {
  try {
    const res = await api.get(`/books/${bookId}/threads/${id}/`)
    const baseUrl = 'http://localhost:8000'

    const thread = {
      ...res.data,
      cover_img_url: res.data.cover_img_url
        ? baseUrl + res.data.cover_img_url.replace('/threads/', '/books/')
        : ''
    }

    const idx = threads.value.findIndex(t => t.id === id)
    if (idx !== -1) {
      threads.value[idx] = thread
    } else {
      threads.value.push(thread)
    }
  } catch (err) {
    console.error(`❌ 쓰레드 ${id} (책 ${bookId}) 불러오기 실패:`, err)
  }
}



  // 좋아요 순 쓰레드 불러오기
  const fetchSortedThreads = async () => {
    try {
      const res = await api.get('/books/get_threads_ordered_by_likes/')
      sortedThreads.value = res.data
    } catch (err) {
      console.error('정렬된 쓰레드 불러오기 실패:', err)
    }
  }

  // 쓰레드 추가
  const addThread = (thread) => {
    threads.value.push(thread)
  }

  // 쓰레드 수정
  const updateThread = (id, payload) => {
  const idx = threads.value.findIndex(t => t.id === id)
  if (idx !== -1) {
    threads.value[idx] = payload
    }
  }


  return {
    threads,
    bookThreads,
    followingThreads,
    sortedThreads,
    fetchThreads,
    addThread,
    updateThread,
    fetchSortedThreads,
    fetchThreadById,
  }
})