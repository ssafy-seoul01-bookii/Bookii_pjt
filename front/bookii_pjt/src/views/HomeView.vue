<!-- HomeView.vue -->

<template>
  <div>
    <!-- Main -->
    <div class="main-banner">
      <!-- 메인 타이틀 이미지 -->
      <img src="@/assets/003.png" alt="Bookii 로고" class="main-title" />
      
      <!-- 본문 -->
      <div class="banner-content">
        <!-- 좌측: 쓰레드 내용 -->
        <div class="left-quote">
          <p class="quote-mark">“</p>
          <p class="quote-text">{{ currentThread?.content || '내용 없음' }}</p>
          <p class="quote-author">@{{ currentThread?.user_name || '익명' }}</p>
        </div>
        
        <!-- 중앙: 책 커버 -->
        <div class="book-image">
          <router-link :to="{ name: 'book-detail', params: { bookId: currentBook.id } }">
            <img :src="currentBook.cover_img_url" :alt="currentBook.title" />
          </router-link>
        </div>

        <!-- 우측: 책 정보 -->
        <div class="book-info">
          <p class="book-title">{{ currentBook.title }}</p>
          <p class="book-author">- {{ currentBook.author_name }}</p>
        </div>
      </div>

      <!-- 슬라이드 버튼 -->
      <div class="pagination">
        <button @click="prevSlide" :disabled="index === 0">〈</button>
        <span>{{ index + 1 }} / {{ books.length }}</span>
        <button @click="nextSlide" :disabled="index === books.length - 1">〉</button>
      </div>
    </div>

    <Footer1/>

    <!-- 로그인여부 따라 분기 -->
     <!-- 로그인o-->
     <template v-if="isLoggedIn">
      <div class="section">
        <h3>키워드 추천 책</h3>
        <BookList :books="book.books"/>
      </div>
      <div class="section">
        <h3>클릭 기반 추천 책</h3>
        <BookList :books="book.books"/>
      </div>
      <div class="section">
        <h3>좋아요 순 정렬 쓰레드</h3>
        <BookList :books="book.books"/>
      </div>
     </template>

     <template v-else> 
      <!-- 로그인x -->
      <div class="section">
        <h3>평론가 3.0 이상 책</h3>
        <BookList :books="book.books"/>
      </div>
      <div class="section">
        <h3>쓰레드 많은 순 정렬 책</h3>
        <BookList :books="book.books"/>
      </div>
      <div class="section">
        <!-- <h3>평점 3.5 이상 정렬 책</h3>
        <BookList :books="book.books"/> -->
        <!-- 쓰레드 테스트용 -->
        <h3>쓰레드 테스트</h3>
        <ThreadList :threads="thread.threads"/>
      </div>
     </template>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useUIStore } from '@/stores/ui'
import { useUserStore } from '@/stores/user'
import { useBookStore } from '@/stores/book'
import { useThreadStore } from '@/stores/thread'
import { onMounted, onBeforeUnmount } from 'vue'

import Footer1 from '@/components/layout/footer1.vue'
import BookList from '@/components/book/BookList.vue'
import ThreadList from '@/components/thread/ThreadList.vue'

const router = useRouter()
const route = useRoute()
const user = useUserStore()
const ui = useUIStore()
const book = useBookStore()
const thread = useThreadStore()

// 로그인여부 판단
const isLoggedIn = computed(() => !!user.accessToken)

const goToLogin = () => {
  ui.setBackgroundRoute(route.fullPath)
  router.push('/login')
}

// main 배너용
const allBooks = book.books
const books = allBooks.sort(() => 0.5 - Math.random()).slice(0, 4)
const index = ref(0)

const currentBook = computed(() => books[index.value])
const currentThread = computed(() => {
  return thread.threads
    .filter(t => t.book_id === currentBook.value.id)
    .sort((a, b) => b.like_count - a.like_count)[0]
})

const nextSlide = () => {
  if (index.value < books.length - 1) index.value++
}
const prevSlide = () => {
  if (index.value > 0) index.value--
}

// 자동 pagination
let intervalId = null

onMounted(() => {
  intervalId = setInterval(() => {
    if (index.value < books.length - 1) {
      nextSlide()
    } else {
      index.value = 0 // 끝나면 다시 처음으로
    }
  }, 5000) // 5초마다 슬라이드
})

onBeforeUnmount(() => {
  clearInterval(intervalId)
})
</script>

<style lang="scss" scoped>
.section {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 0 1rem;
}

// main용
.main-banner {
  background-color: #fdeacb;
  padding: 2rem 1rem;
  text-align: center;
}
.main-title {
  height: 80px;
  font-size: 2rem;
  margin-bottom: 1rem;
}
.banner-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  max-width: 1200px;
  margin: 0 auto 1rem auto;
  padding: 0 2rem;
}
.left-quote {
  width: 200px;
  font-style: italic;
  text-align: left;

  p {
    margin: 0.25rem 0;
  }
}
.quote-mark {
  font-size: 2rem;
}
.quote-author {
  font-weight: bold;
  margin-top: 0.5rem;
}
.book-image img {
  max-width: 250px;
  border-radius: 8px;
}
.book-info {
  width: 200px;
  text-align: right;
}
.book-title {
  font-weight: bold;
  font-size: 1.2rem;
}
.book-author {
  margin-top: 0.5rem;
}
.pagination {
  display: flex;
  justify-content: flex-end;
  align-items: center;
  margin: 0 2rem;
  font-weight: bold;
}
.pagination button {
  background: none;
  border: none;
  font-size: 1.5rem;
  margin: 0 1rem;
  cursor: pointer;
}
.pagination button:disabled {
  color: #ccc;
  cursor: not-allowed;
}

</style>