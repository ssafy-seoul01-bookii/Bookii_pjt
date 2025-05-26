<template>
  <div class="search-view">
    <!-- 좌측: 태그 필터 -->
    <aside class="sidebar">
      <h3>태그검색</h3>
      <div class="filter-group">
        <p class="filter-title">카테고리</p>
        <div v-for="genre in categoryStore.categories" :key="genre.id">
          <input type="checkbox" :value="genre.name" v-model="selectedTags" />
          <label>{{ genre.name }}</label>
        </div>
      </div>

      <hr />

      <div class="filter-group">
        <p class="filter-title">키워드</p>
        <div v-for="keyword in keywordStore.keywords" :key="keyword.id">
          <input type="checkbox" :value="keyword.name" v-model="selectedTags" />
          <label>{{ keyword.name }}</label>
        </div>
      </div>
    </aside>

    <!-- 우측: 검색 결과 -->
    <section class="results-section">
      <h2>“{{ query }}” 검색 결과</h2>

      <div class="grid">
        <div
          v-for="book in filteredBooks"
          :key="book.id"
          class="book-card"
        >
          <router-link :to="{ name: 'book-detail', params: { bookId: book.id } }">
            <img :src="book.cover_img_url" :alt="book.title" />
            <p class="title">{{ book.title }}</p>
            <p class="author">{{ book.author_name }}</p>
          </router-link>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useBookStore } from '@/stores/book'
import { useCategoryStore } from '@/stores/category'
import { useKeywordStore } from '@/stores/keyword'

const route = useRoute()

const bookStore = useBookStore()
const categoryStore = useCategoryStore()
const keywordStore = useKeywordStore()

const query = ref(route.query.q || '')
const selectedTags = ref([])

// 검색어 반영
watch(
  () => route.query.q,
  (newQuery) => {
    query.value = newQuery || ''
  }
)

const searchedBooks = computed(() =>
  bookStore.books.filter(book =>
    book.title.toLowerCase().includes(query.value.toLowerCase())
  )
)

const filteredBooks = computed(() => {
  if (selectedTags.value.length === 0) return searchedBooks.value

  return searchedBooks.value.filter(book =>
    selectedTags.value.every(tag => (book.tags ?? []).includes(tag))
  )
})

onMounted(() => {
  bookStore.fetchBooks()
  categoryStore.fetchCategories()
  keywordStore.fetchKeywords()
})
</script>

<style lang="scss" scoped>
.search-view {
  display: flex;
  padding: 1rem;
  gap: 2rem;
}
.sidebar {
  width: 200px;
  border-right: 1px solid #ddd;
}
.filter-group {
  margin-bottom: 1rem;
}
.filter-title {
  font-weight: bold;
  margin: 0.5rem 0;
}
.results-section {
  flex: 1;
}
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
  gap: 1rem;
  margin-top: 1rem;
}
.book-card {
  text-align: center;
}
.book-card img {
  width: 100%;
  border-radius: 8px;
}
</style>