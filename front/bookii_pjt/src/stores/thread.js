// stores/thread.js
import { defineStore } from 'pinia'
import { ref } from 'vue'
import api from '@/lib/axios'

export const useThreadStore = defineStore('thread', () => {
  const threads = ref([])

  // 전체 쓰레드 불러오기
  const fetchThreads = async () => {
    try {
      const res = await api.get('/threads/')
      threads.value = res.data
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
    fetchThreads,
    addThread,
    updateThread,
  }
})