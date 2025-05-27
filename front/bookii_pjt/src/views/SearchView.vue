<template>
  <div class="search-view">
    <!-- 좌측: 태그 필터 -->
    <aside class="sidebar">
      <h3>태그검색</h3>
      <div class="filter-group">
        <p class="filter-title">카테고리</p>
        <div v-for="category in categoryStore.categories" :key="category.id">
          <input type="checkbox" :value="category.id" v-model="selectedCategories" />
          <label>{{ category.name }}</label>
        </div>
      </div>

      <hr />

      <div class="filter-group">
        <p class="filter-title">키워드</p>
        <div v-for="keyword in keywordStore.keywords" :key="keyword.id">
          <input type="checkbox" :value="keyword.id" v-model="selectedKeywords" />
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
const selectedCategories = ref([])
const selectedKeywords = ref([])

// 검색어 반영
watch(
  () => route.query.q,
  (newQuery) => {
    query.value = newQuery || ''
  }
)

// search로 거르기
const searchedBooks = computed(() =>
  bookStore.books.filter(book => {
    const lowerQuery = query.value.toLowerCase()
    return (
      (book.title ?? '').toLowerCase().includes(lowerQuery) ||
      (book.author_name ?? '').toLowerCase().includes(lowerQuery) ||
      (book.description ?? '').toLowerCase().includes(lowerQuery)
    )
  })
)

// 태그로 거르기
// const filteredBooks = computed(() => {
//   return searchedBooks.value.filter(book => {
//     const bookCategories = book.category ?? []
//     const bookKeywords = book.keyword ?? []

//     // 카테고리 필터
//     const categoryMatch =
//       selectedCategories.value.length === 0 ||
//       selectedCategories.value.every(catId => bookCategories.includes(catId))

//     // 키워드 필터
//     const keywordMatch =
//       selectedKeywords.value.length === 0 ||
//       selectedKeywords.value.every(keyId => bookKeywords.includes(keyId))

//     return categoryMatch && keywordMatch
//   })
// })
const filteredBooks = computed(() => {
  // 선택된 카테고리와 키워드를 숫자로 변환
  const selectedCatIds = selectedCategories.value.map(Number)
  const selectedKeyIds = selectedKeywords.value.map(Number)

  return searchedBooks.value.filter(book => {
    const bookCategories = book.category ?? []
    const bookKeywords = book.keyword ?? []

    const categoryMatch =
      selectedCatIds.length === 0 ||
      selectedCatIds.every(catId => bookCategories.includes(catId))

    const keywordMatch =
      selectedKeyIds.length === 0 ||
      selectedKeyIds.every(keyId => bookKeywords.includes(keyId))

    return categoryMatch && keywordMatch
  })
})

onMounted(() => {
  bookStore.fetchBooks()
  categoryStore.fetchCategories()
  keywordStore.fetchKeywords()
})
</script>

<style lang="scss" scoped>
/* 전체 스크롤 제거 */
:global(body) {
  overflow: hidden;
}

.search-view {
  display: flex;
  height: 100vh;
  gap: 2rem;
  background-color: #FFF7E4;
  font-family: 'Segoe UI', sans-serif;
  padding: 2rem;
  box-sizing: border-box;
}

/* 좌측 필터 */
.sidebar {
  width: 240px;
  background-color: #FFECBD; // ✅ 태그검색 배경 변경
  padding: 1.5rem;
  border-radius: 1rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);

  overflow-y: auto;
  height: 100%;

  /* 스크롤바 커스터마이징 */
  &::-webkit-scrollbar {
    width: 8px;
  }
  &::-webkit-scrollbar-thumb {
    background-color: #A2ACE2; // ✅ 잘 보이도록 강조
    border-radius: 10px;
  }
  &::-webkit-scrollbar-track {
    background-color: #FFF7E4; // ✅ 배경 대비 잘 되게
  }
}

.filter-group {
  margin-bottom: 1.5rem;
}
.filter-title {
  font-weight: bold;
  margin: 0.5rem 0;
  color: #34495e;
}
.filter-group input[type="checkbox"] {
  margin-right: 0.5rem;
}
.filter-group label {
  font-size: 0.95rem;
  color: #2f3640;
}

/* 우측 결과 */
.results-section {
  flex: 1;
  overflow-y: auto;
  height: 100%;
  padding-right: 0.5rem;

  /* 스크롤바 커스터마이징 */
  &::-webkit-scrollbar {
    width: 8px;
  }
  &::-webkit-scrollbar-thumb {
    background-color: #C4D9ED;
    border-radius: 10px;
  }
  &::-webkit-scrollbar-track {
    background-color: #A2ACE2;
  }

  h2 {
    font-size: 1.5rem;
    color: black; // ✅ 검색 결과 텍스트 색
    margin-bottom: 1.5rem;
  }
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  gap: 1.5rem;
}

.book-card {
  background-color: #FFECBD;
  padding: 1rem;
  border-radius: 12px;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);

  &:hover {
    transform: translateY(-4px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  }

  img {
    width: 100%;
    border-radius: 8px;
    margin-bottom: 0.5rem;
  }

  .title {
    font-weight: 600;
    color: #2c3e50;
    font-size: 1rem;
    margin: 0.3rem 0;
  }

  .author {
    font-size: 0.85rem;
    color: #7f8c8d;
  }
}
</style>