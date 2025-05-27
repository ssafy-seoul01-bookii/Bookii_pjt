// ✅ Keyword Store
import { defineStore } from 'pinia'
import { ref } from 'vue'
import api from '@/lib/axios'

export const useKeywordStore = defineStore('keyword', () => {
  const keywords = ref([])
  const bookKeywords = ref([])

  const fetchKeywords = async () => {
    try {
      const res = await api.get('/books/keywords/')
      keywords.value = res.data
    } catch (err) {
      console.error('키워드 불러오기 실패:', err)
    }
  }
  
  const fetchBookKeywords = async (bookId) => {
    try {
      const res = await api.get(`/books/${bookId}/get_keywords_books/`)
      bookKeywords.value = res.data ?? []  // ❌ res.data.keywords → ✅ res.data
    } catch (err) {
      console.error('키워드 기반 추천 책 불러오기 실패:', err)
    }
  }


  return {
    keywords,
    bookKeywords,
    fetchKeywords,
    fetchBookKeywords,
  }
})