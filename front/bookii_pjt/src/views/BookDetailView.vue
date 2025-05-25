<!-- BookDetailView.vue -->

<template>
  <div>
    <!-- Main -->
    <div class="book-main">
      <!-- 상단: 배경 이미지 + 책 정보 -->
      <div class="main-banner">
        <img src="@/assets/dummy-banner.jpeg" alt="배경 이미지" class="bg-image" />

        <!-- 오버레이 텍스트 -->
        <div class="text-box">
          <p class="description">{{ currentBook.description }}</p>
          <h2 class="title">{{ currentBook.title }}</h2>
          <p class="meta">{{ currentBook.author_name }} · {{ currentBook.publisher }}</p>
        </div>

        <!-- 커버 이미지 (배너+배경 걸쳐서) -->
        <img :src="currentBook.cover_img_url" :alt="currentBook.title" class="cover-image" />
      </div>

      <!-- 하단: 키워드 영역 -->
      <div class="keyword-section">
        <h3># 키워드</h3>
        <div class="tag-list">
          <span v-for="tag in currentBook.tags || defaultTags" :key="tag" class="tag">#{{ tag }}</span>
        </div>
      </div>
    </div>

    <!-- BookThread(좋아요 순 정렬) -->
    <div class="section">
      <h3>Bookii들이 적은 쓰레드</h3>
      <ThreadList :threads="bookThreads.value"/>
    </div>

    <Footer1/>

    <!-- 로그인여부 따라 분기 -->
     <!-- 로그인o-->
     <template v-if="isLoggedIn">
      <div class="section">
        <!-- followeing 필터 -->
        <h3>이웃이 남긴 쓰레드</h3>
        <ThreadList :threads="followingThreads"/>
      </div>
     </template>

     <template v-else> 
      <!-- 로그인x -->
      <div class="section">
        <h3>이웃이 남긴 한마디</h3>
        <p>로그인 후, 이웃들과 {{ currentBook.title }} 에 대한 감상을 나눠보세요!</p>
      </div>
     </template>

    <!-- 키워드추천 BookList -->
    <div class="section">
      <h3>키워드 추천</h3>
      <!-- recommend로 변경 필요 -->
      <BookList :books="recommendedBooks"/>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { useBookStore } from '@/stores/book'
import { useThreadStore } from '@/stores/thread'

import ThreadList from '@/components/thread/ThreadList.vue'

const route = useRoute()
const bookId = Number(route.params.bookId)

const user = useUserStore()
const book = useBookStore()
const thread = useThreadStore()

// 로그인 여부
const isLoggedIn = computed(() => !!user.accessToken)

// 현재 책
const currentBook = computed(() =>
  book.books.find(b => b.id === bookId)
)
// 현재 책에 해당하는 쓰레드
const bookThreads = computed(() =>
  thread.threads.filter(t => t.book_id === bookId)
)
// following 쓰레드
const followingThreads = computed(() =>
  thread.threads.filter(t => 
    t.book_id === bookId &&
    user.following.includes(t.user_id)
  )
)
// 키워드추천 책
const recommendedBooks = computed(() =>
  book.books.filter(b => b.id !== bookId)
)

// 테스트용
onMounted(() => {
  console.log('bookThreads', bookThreads.value)
})

</script>

<style lang="scss" scoped>
.section {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 0 1rem;
}

// main
.book-main {
  font-family: sans-serif;
}

// 상단 배너 영역
.main-banner {
  position: relative;
  width: 100%;
  height: 600px; // ✅ 배너 높이 축소
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

// 하단 키워드 영역
.keyword-section {
  background-color: #fff7e4;
  padding: 1.5rem 5% 2rem; // ✅ 키워드 영역 여백 확대
  margin-top: -10px;

  h3 {
    font-size: 1.4rem; // ✅ 제목 강조
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
      padding: 0.5rem 1rem; // ✅ 넉넉하게
      border-radius: 1.5rem;
      font-size: 0.95rem; // ✅ 시각 강조
      font-weight: 500;
      white-space: nowrap;
    }
  }
}
</style>