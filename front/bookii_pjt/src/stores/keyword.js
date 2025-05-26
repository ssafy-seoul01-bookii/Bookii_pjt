// ✅ Keyword Store
import { defineStore } from 'pinia'
import { ref } from 'vue'
import api from '@/lib/axios'

export const useKeywordStore = defineStore('keyword', () => {
  const keywords = ref([])

  const fetchKeywords = async () => {
    try {
      const res = await api.get('/keywords/')
      keywords.value = res.data
    } catch (err) {
      console.error('키워드 불러오기 실패:', err)
    }
  }

  return {
    keywords,
    fetchKeywords
  }
})