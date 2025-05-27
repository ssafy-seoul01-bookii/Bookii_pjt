// ✅ Category Store
import { defineStore } from 'pinia'
import { ref } from 'vue'
import api from '@/lib/axios'

export const useCategoryStore = defineStore('category', () => {
  const categories = ref([])

  const fetchCategories = async () => {
    try {
      const res = await api.get('/books/categories/')
      categories.value = res.data
    } catch (err) {
      console.error('카테고리 불러오기 실패:', err)
    }
  }

  return {
    categories,
    fetchCategories
  }
})