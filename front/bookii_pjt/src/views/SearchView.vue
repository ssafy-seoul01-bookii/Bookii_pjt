<!-- views/SearchView.vue -->
<template>
  <div class="search-view">
    <!-- 좌측: 태그 필터 -->
    <aside class="sidebar">
      <h3>태그검색</h3>
      <div class="filter-group">
        <p class="filter-title">카테고리</p>
        <div v-for="genre in genreOptions" :key="genre">
          <input type="checkbox" :value="genre" v-model="selectedTags" />
          <label>{{ genre }}</label>
        </div>
      </div>

      <hr />

      <div class="filter-group">
        <p class="filter-title">키워드</p>
        <div v-for="keyword in keywordOptions" :key="keyword">
          <input type="checkbox" :value="keyword" v-model="selectedTags" />
          <label>{{ keyword }}</label>
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
import { ref, computed, watch } from 'vue'
import { useRoute } from 'vue-router'
import { useBookStore } from '@/stores/book'

const route = useRoute()
const bookStore = useBookStore()

const query = ref(route.query.q || '')

// route.query.q가 바뀔 때마다 반영
// SearchView에서 재검색 가능하게
watch(
  () => route.query.q,
  (newQuery) => {
    query.value = newQuery || ''
  }
)

const selectedTags = ref([])

// 임시 장르/키워드 - 실제로는 백엔드에서 가져오거나 store에서 관리 가능
const genreOptions = ['genre 1', 'genre 2', 'genre 3']
const keywordOptions = [
  '삶', '문학', '산문집', '자기계발', '명상',
  '감정', '관계', '소설', '힐링'
]

// 검색어 기반 필터
const searchedBooks = computed(() =>
  bookStore.books.filter(book =>
    book.title.toLowerCase().includes(query.value.toLowerCase())
  )
)

// 태그까지 필터
const filteredBooks = computed(() => {
  if (selectedTags.value.length === 0) return searchedBooks.value

  return searchedBooks.value.filter(book =>
    selectedTags.value.every(tag => book.tags.includes(tag))
  )
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