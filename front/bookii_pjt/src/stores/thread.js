// stores/thread.js
import { defineStore } from 'pinia'
import { ref } from 'vue'
import api from '@/lib/axios'

export const useThreadStore = defineStore('thread', () => {
  const bookThreads = ref([]) // bookId 기준 쓰레드
  const followingThreads = ref([]) // 팔로잉 유저 쓰레드
  const threads = ref([]) // 전체 쓰레드드

  // 전체 쓰레드 불러오기
  const fetchThreads = async (bookId, followingUserIds = []) => {
    try {
      const res = await api.get(`/books/${bookId}/threads/`)
      threads.value = res.data
      followingThreads.value = res.data.filter(t =>
        followingUserIds.includes(t.user_id)
      )
    } catch (err) {
      console.error('쓰레드 불러오기 실패:', err)
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
    fetchThreads,
    addThread,
    updateThread,
  }
})