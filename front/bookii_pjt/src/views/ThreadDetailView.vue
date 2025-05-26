<!-- ThreadDetailView.vue -->

<template>
  <div v-if="thread" class="thread-detail">
    <!-- 왼쪽: 이미지 -->
    <!-- 책 제목 + 저자 추가 -> BookDetail 이동 -->
    <div class="thread-left">
      <img :src="thread?.cover_img_url" :alt="thread?.title" />

      <!-- 책 정보 오버레이 -->
      <router-link
        v-if="book"
        :to="{ name: 'book-detail', params: { bookId: book.id } }"
        class="book-overlay"
      >
        <p class="book-title">{{ book.title }}</p>
        <p class="book-author">{{ book.author_name }}</p>
      </router-link>
    </div>

    <!-- 오른쪽: 내용 -->
    <div class="thread-right">
      <!-- 작성자 정보 -->
      <div class="header">
        <span class="username">@{{ user?.username }}</span>
        <h3 class="title">{{ thread?.title }}</h3>
        <!-- <span class="book-title"> — {{ book?.title }}</span> -->
      </div>

      <!-- 쓰레드 내용 -->
      <div class="content">
        <p>{{ thread?.content }}</p>
      </div>

      <!-- 댓글 리스트 -->
      <CommentList v-if="thread" :thread-id="thread.id"></CommentList>

      <!-- 좋아요 -->
      <div class="like-section">
        <button class="heart" :class="{ active: isLiked }" @click="toggleLike">❤️</button>
        <span class="count">{{ likeCount }}</span>
      </div>

      <!-- 댓글작성 -->
      <div>
        <CommentCreate v-if="thread" :thread-id="thread.id" ></CommentCreate>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { useRoute } from 'vue-router'
import { useThreadStore } from '@/stores/thread'
import { useUserStore } from '@/stores/user'
import { useBookStore } from '@/stores/book'

import CommentList from '@/components/comment/CommentList.vue'
import CommentCreate from '@/components/comment/CommentCreateForm.vue'

const route = useRoute()
const threadId = Number(route.params.id)

const threadStore = useThreadStore()
const userStore = useUserStore()
const bookStore = useBookStore()

const thread = computed(() => threadStore.threads.find(t => t.id === threadId))
const user = computed(() => userStore.users.find(u => u.id === thread.value?.user_id))
const book = computed(() => bookStore.books.find(b => b.id === thread.value?.book_id))

// 좋아요 갯수 증가
const isLiked = ref(false)
const likeCount = ref(0)

const toggleLike = () => {
  isLiked.value = !isLiked.value
  likeCount.value += isLiked.value ? 1 : -1
}


watch(thread, (newThread) => {
  if (newThread) {
  likeCount.value = newThread.like_count
  // 현재 로그인 유저가 이미 좋아요한 경우 (가정)
  isLiked.value = newThread.liked_user_ids?.includes(userStore.currentUserId)
  }
}, { immediate: true })
</script>

<style scoped>
.thread-detail {
  display: flex;
  width: 100%;
  max-width: 1200px;
  height: 80vh;
  background: #fff;
  border-radius: 12px;
  overflow: hidden;
}

/* ===== 왼쪽 영역 ===== */
.thread-left {
  width: 60%;
  position: relative;
  background-color: #000;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

.thread-left img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* hover 효과로 오버레이 표시 */
.thread-left:hover ::v-deep(.book-overlay) {
  opacity: 1;
  transform: translateY(0);
}

.book-overlay {
  position: absolute;
  bottom: 1rem;
  left: 1rem;
  background-color: rgba(0, 0, 0, 0.5);
  padding: 0.75rem 1rem;
  border-radius: 6px;
  color: white;
  text-decoration: none;
  z-index: 10;
  opacity: 0;
  transform: translateY(10px);
  transition: all 0.3s ease;

  p {
    margin: 0;
    line-height: 1.4;
  }

  .book-title {
    font-weight: bold;
    font-size: 1rem;
  }

  .book-author {
    font-size: 0.85rem;
    opacity: 0.9;
  }
}

/* ===== 오른쪽 영역 ===== */
.thread-right {
  width: 40%;
  padding: 2rem 1rem 2rem 2rem;
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
  overflow-y: auto;
}

.header {
  font-size: 1rem;
  font-weight: bold;
}

.content {
  font-size: 1rem;
  line-height: 1.5;
}

/* ===== 좋아요 버튼 ===== */
.like-section {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.heart {
  font-size: 1.5rem;
  background: none;
  border: none;
  cursor: pointer;
  color: #999;
  transition: color 0.2s;
}

.heart.active {
  color: red;
}

.count {
  font-size: 0.95rem;
  color: #444;
}
</style>
