<!-- ThreadDetailView.vue -->

<template>
  <div class="thread-detail">
    <!-- 왼쪽: 이미지 -->
    <div class="thread-left">
      <img :src="thread?.cover_img_url" :alt="thread?.title" />
    </div>

    <!-- 오른쪽: 내용 -->
    <div class="thread-right">
      <!-- 작성자 정보 -->
      <div class="header">
        <span class="username">@{{ user?.username }}</span>
        <span class="book-title"> — {{ book?.title }}</span>
      </div>

      <!-- 쓰레드 내용 -->
      <div class="content">
        <p class="thread-text">{{ thread?.content }}</p>
      </div>

      <!-- 메타 정보 -->
      <div class="meta">
        <span class="likes">❤️ {{ thread?.like_count }} 좋아요</span>
        <span class="comments">💬 {{ thread?.comment_count }} 댓글</span>
        <span class="date">📅 {{ thread?.created_at }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { useThreadStore } from '@/stores/thread'
import { useUserStore } from '@/stores/user'
import { useBookStore } from '@/stores/book'

const route = useRoute()
const threadId = Number(route.params.id)

const threadStore = useThreadStore()
const userStore = useUserStore()
const bookStore = useBookStore()

const thread = computed(() => threadStore.threads.find(t => t.id === threadId))
const user = computed(() => userStore.users.find(u => u.id === thread.value?.user_id))
const book = computed(() => bookStore.books.find(b => b.id === thread.value?.book_id))
</script>

<style scoped>
.thread-detail {
  display: flex;
  width: 100%;
  max-width: 1200px;
  height: 80vh;
  background: white;
  border-radius: 12px;
  overflow: hidden;
}

.thread-left {
  width: 60%;
  background-color: #000;
  display: flex;
  justify-content: center;
  align-items: center;
}
.thread-left img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.thread-right {
  width: 40%;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  overflow-y: auto;
}

.header {
  font-size: 1.2rem;
  font-weight: bold;
}

.content {
  font-size: 1rem;
  line-height: 1.5;
}

.meta {
  font-size: 0.9rem;
  color: #666;
  display: flex;
  flex-direction: column;
  gap: 0.3rem;
}
</style>