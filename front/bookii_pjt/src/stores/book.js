// stores/Book.js
import { defineStore } from 'pinia'
import { ref } from 'vue'
import api from '@/lib/axios'

export const useBookStore = defineStore('book', () => {
  const books = ref([])
  const criticBooks = ref([])
  const manyThreadBooks = ref([])

  const criticUsername = ref('')

  const baseUrl = 'http://localhost:8000'

  const fetchBooks = async () => {
    try {
      const res = await api.get('/books/')
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

  // 평론가 점수 높은 책
  const fetchCriticBooks = async () => {
    try {
      const res = await api.get('/books/get_high_rank_book_by_critic/')
      const data = res.data.books || res.data.data || res.data
      criticUsername.value = res.data.critic_username
      criticBooks.value = data.map(book => ({
        ...book,
        cover_img_url: book.cover_img_url ? baseUrl + book.cover_img_url : '',
        background_img_url: book.background_img_url ? baseUrl + book.background_img_url : '',
        author_profile_img_url: book.author_profile_img_url ? baseUrl + book.author_profile_img_url : '',
      }))
    } catch (err) {
      console.error('평론가 추천 책 불러오기 실패:', err)
    }
  }

  // 쓰레드 많은 책
  const fetchManyThreadBooks = async () => {
    try {
      const res = await api.get('/books/get_many_threads_book/')
      manyThreadBooks.value = res.data.map(book => ({
        ...book,
        cover_img_url: book.cover_img_url ? baseUrl + book.cover_img_url : '',
        background_img_url: book.background_img_url ? baseUrl + book.background_img_url : '',
        author_profile_img_url: book.author_profile_img_url ? baseUrl + book.author_profile_img_url : '',
      }))
    } catch (err) {
      console.error('쓰레드 많은 책 불러오기 실패:', err)
    }
  }

  return {
    books,
    criticBooks,
    manyThreadBooks,
    criticUsername,
    fetchBooks,
    fetchCriticBooks,
    fetchManyThreadBooks,
  }
})