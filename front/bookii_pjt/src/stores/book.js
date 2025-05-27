// stores/Book.js
import { defineStore } from 'pinia'
import { ref } from 'vue'
import api from '@/lib/axios'

export const useBookStore = defineStore('book', () => {
  const books = ref([])

  const fetchBooks = async () => {
    try {
      const res = await api.get('/books/')
      const baseUrl = 'http://localhost:8000'  // ✅ 서버 주소

      // ✅ 이미지 경로 보정
      books.value = res.data.map(book => ({
        ...book,
        cover_img_url: book.cover_img_url ? baseUrl + book.cover_img_url : '',
        background_img_url: book.background_img_url ? baseUrl + book.background_img_url : '',
        author_profile_img_url: book.author_profile_img_url ? baseUrl + book.author_profile_img_url : '',
      }))
    } catch (err) {
      console.error('책 불러오기 실패:', err)
    }
  }

  return {
    books,
    fetchBooks
  }
})