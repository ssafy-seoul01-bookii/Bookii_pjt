<!-- BookDetailView.vue -->
<template>
  <div>
    <!-- Main -->
    <div class="book-main">
      <div class="main-banner">
        <img
          :src="`${currentBook.background_img_url}`"
          alt="배경 이미지"
          class="bg-image"
          @error="e => console.log('배경 이미지 로드 실패', e.target.src)"
        />
        <!-- 쓰레드 작성 버튼 -->
        <button
          v-if="isLoggedIn"
          class="write-thread-btn"
          @click="goToCreateThread"
        >
          ✍️ 쓰레드 작성
        </button>

        <div class="text-box">
          <p class="description">{{ currentBook.description }}</p>
          <h2 class="title">{{ currentBook.title }}</h2>
          <p class="meta">{{ currentBook.author_name }} · {{ currentBook.publisher }}</p>
        </div>

        <img :src="currentBook.cover_img_url" :alt="currentBook.title" class="cover-image" />
      </div>

      <!-- 키워드 -->
      <div class="keyword-section">
        <h3># 키워드</h3>
        <div class="tag-list">
          <span
            v-for="tag in bookKeywordTags"
            :key="tag"
            class="tag"
          >#{{ tag }}</span>
        </div>
      </div>
    </div>

    <!-- Book Threads -->
    <div class="section">
      <h3>Bookii들이 적은 쓰레드</h3>
      <ThreadList :threads="bookThreads" />
    </div>

    <Footer1 />

    <!-- 로그인 여부 분기 -->
    <div class="section" v-if="isLoggedIn">
      <h3>이웃이 남긴 쓰레드</h3>
      <ThreadList :threads="followingThreads" />
    </div>

    <div class="section" v-else>
      <h3>이웃이 남긴 한마디</h3>
      <p>로그인 후, 이웃들과 {{ currentBook.title }} 에 대한 감상을 나눠보세요!</p>
    </div>

    <!-- 추천 도서 -->
    <div class="section">
      <h3>키워드 추천</h3>
      <BookList :books="recommendedBooks" />
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { useBookStore } from '@/stores/book'
import { useThreadStore } from '@/stores/thread'
import { useKeywordStore } from '@/stores/keyword'

import ThreadList from '@/components/thread/ThreadList.vue'
import BookList from '@/components/book/BookList.vue'
import Footer1 from '@/components/layout/footer1.vue'

const router = useRouter()
const route = useRoute()
const bookId = Number(route.params.bookId)

const userStore = useUserStore()
const bookStore = useBookStore()
const threadStore = useThreadStore()
const keywordStore = useKeywordStore()


// 현재 책
const currentBook = computed(() =>
  bookStore.books.find(b => b.id === bookId)
)

// 현재 책에 해당하는 쓰레드
const bookThreads = computed(() =>
  threadStore.threads.filter(t => t.book_id === bookId)
)

// 이웃이 남긴 쓰레드
const followingThreads = computed(() =>
  threadStore.threads.filter(
    t => t.book_id === bookId && userStore.userInfo?.following?.includes(t.user_id)
  )
)

// 추천 도서
const recommendedBooks = computed(() =>
  bookStore.books.filter(b => b.id !== bookId)
)

// 로그인 여부
const isLoggedIn = computed(() => userStore.isLoggedIn)

// 쓰레드 생성 -> ThreadCreateView 연결
const goToCreateThread = () => {
  router.push({ name: 'thread-create', query: { bookId } })
}

onMounted(async () => {
  await keywordStore.fetchBookKeywords(bookId)
})

// 진짜 키워드 뽑아내기
const bookKeywordTags = computed(() => {
  const allTags = keywordStore.bookKeywords.flatMap(book => book.keywords || [])
  return [...new Set(allTags)]  // 중복 제거
})
</script>

<style lang="scss" scoped>
.section {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 0 1rem;
}

.book-main {
  font-family: sans-serif;
}

.main-banner {
  position: relative;
  width: 100%;
  height: 600px;
  overflow: hidden;
  background-color: #fff7e4;

  .bg-image {
    width: 100%;
    height: 70%;
    object-fit: cover;
    display: block;
  }

  .text-box {
    position: absolute;
    top: 10%;
    left: 5%;
    color: white;
    max-width: 60%;
    text-shadow: 0 0 4px rgba(0, 0, 0, 0.6);

    .description {
      font-size: 1rem;
      margin-bottom: 1rem;
      white-space: pre-line;
    }

    .title {
      font-size: 2rem;
      font-weight: bold;
      margin-bottom: 0.5rem;
    }

    .meta {
      font-size: 1rem;
      opacity: 0.9;
    }
  }

  .cover-image {
    position: absolute;
    top: 72%;
    transform: translateY(-50%);
    right: 5%;
    width: 440px;
    height: auto;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    border-radius: 8px;
  }
}

.write-thread-btn {
  position: absolute;
  bottom: 5%;
  left: 5%;
  z-index: 2;
  padding: 0.6rem 1.2rem;
  background-color: #ffecbd;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: bold;
  cursor: pointer;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
  transition: background 0.2s;

  &:hover {
    background-color: #ffe2a8;
  }
}

.keyword-section {
  background-color: #fff7e4;
  padding: 1.5rem 5% 2rem;
  margin-top: -10px;

  h3 {
    font-size: 1.4rem;
    font-weight: bold;
    margin-bottom: 1rem;
  }

  .tag-list {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;

    .tag {
      background-color: #c4d9ed;
      color: black;
      padding: 0.5rem 1rem;
      border-radius: 1.5rem;
      font-size: 0.95rem;
      font-weight: 500;
      white-space: nowrap;
    }
  }
}
</style>
