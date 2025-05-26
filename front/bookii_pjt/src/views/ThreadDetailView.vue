<!-- ThreadDetailView.vue -->

<template>
  <div v-if="thread" class="thread-detail">
    <!-- 왼쪽: 이미지 -->
    <!-- 책 제목 + 저자 추가 -> BookDetail 이동 -->
    <div class="thread-left">
      <img :src="thread?.cover_img_url" :alt="thread?.title" />

      <!-- 책 정보 오버레이 -->
      <div class="book-overlay">
        <router-link
          v-if="book"
          :to="{ name: 'book-detail', params: { bookId: book.id } }"
          class="book-info"
        >
          <p class="book-title">{{ book.title }}</p>
          <p class="book-author">{{ book.author_name }}</p>
        </router-link>
      
        <!-- 좋아요 버튼 -->
        <div class="like-overlay">
          <button class="heart" :class="{ active: isLiked }" @click="toggleLike">❤️</button>
          <span class="count">{{ likeCount }}</span>
        </div>
      </div>
    </div>

    <!-- 오른쪽: 내용 -->
    <div class="thread-right">
      <div class="scroll-area">
        <!-- 작성자 정보 -->
        <div class="header">
          <span class="username">@{{ user?.username }}</span>
          <h3 class="title">{{ thread?.title }}</h3>
          
          <!-- 쓰레드 수정 버튼 -->
          <button
            v-if="isMine"
            class="edit-btn"
            @click="goToEditThread"
          >
            ✏️ 수정
          </button>
        </div>
  
        <!-- 쓰레드 내용 -->
        <div class="content">
          <p>{{ thread?.content }}</p>
        </div>
  
        <!-- 댓글 리스트 -->
        <CommentList v-if="thread" :thread-id="thread.id"></CommentList>
      </div>

      <!-- 댓글작성 -->
      <div class="comment-fixed">
        <CommentCreate v-if="thread" :thread-id="thread.id" ></CommentCreate>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useThreadStore } from '@/stores/thread'
import { useUserStore } from '@/stores/user'
import { useBookStore } from '@/stores/book'
import { useFollowStore } from '@/stores/follow'

import CommentList from '@/components/comment/CommentList.vue'
import CommentCreate from '@/components/comment/CommentCreateForm.vue'

const route = useRoute()
const router = useRouter()
const threadId = Number(route.params.id)

const threadStore = useThreadStore()
const userStore = useUserStore()
const bookStore = useBookStore()
const followStore = useFollowStore()

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

// 쓰레드 작성자가 본인인지 확인
const isMine = computed(() =>
  userStore.currentUserId === thread.value.user_id
)

// 쓰레드 수정폼 이동
const goToEditThread = () => {
  router.push({ name: 'thread-edit', params: { id: threadId } })
}
</script>

<style scoped>
/* 그대로 유지 */
.thread-detail {
  display: flex;
  width: 100%;
  max-width: 1200px;
  height: 80vh;
  background: #FFF7E4;
  border-radius: 12px;
  overflow: hidden;
}
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
.book-overlay {
  position: absolute;
  bottom: 1rem;
  left: 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  opacity: 0;
  transform: translateY(10px);
  transition: all 0.3s ease;
}
.thread-left:hover .book-overlay {
  opacity: 1;
  transform: translateY(0);
}
.book-info {
  background-color: rgba(0, 0, 0, 0.5);
  padding: 0.75rem 1rem;
  border-radius: 6px;
  color: white;
  text-decoration: none;
  display: block;
}
.book-title {
  font-weight: bold;
  font-size: 1rem;
  margin: 0;
}
.book-author {
  font-size: 0.85rem;
  opacity: 0.9;
  margin: 0;
}
.like-overlay {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  margin-top: 0.5rem;
}
.heart {
  font-size: 1.4rem;
  background: none;
  border: none;
  cursor: pointer;
  color: #ddd;
  transition: color 0.2s;
}
.heart.active {
  color: #FF6B6B;
}
.count {
  font-size: 0.9rem;
  color: #f0f0f0;
}
.thread-right {
  width: 40%;
  display: flex;
  flex-direction: column;
  height: 100%;
  padding-left: 0;
  background-color: #FFF7E4;
}
.scroll-area {
  flex: 1;
  overflow-y: auto;
  padding: 2.5rem 1.5rem 1rem 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
}
.comment-fixed {
  padding: 1rem 1rem 1rem 0;
  background-color: #FFF7E4;
  display: flex;
  justify-content: center;
}
.comment-fixed form {
  width: 100%;
  max-width: 90%;
  margin-top: -3px;
}
.header {
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
  font-size: 1rem;
  font-weight: bold;
}
.content {
  font-size: 1rem;
  line-height: 1.5;
}
.edit-btn {
  margin-top: 0.5rem;
  padding: 0.4rem 0.8rem;
  background-color: #a2ace2;
  border: none;
  color: white;
  font-weight: bold;
  border-radius: 6px;
  cursor: pointer;
  align-self: flex-start;
}
</style>