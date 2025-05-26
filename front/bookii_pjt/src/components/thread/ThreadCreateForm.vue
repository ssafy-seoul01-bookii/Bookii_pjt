<!-- ThreadCreateForm.vue -->

<template>
  <BaseModal modalClass="modal-wide">
    <div class="thread-modal-wrapper">
      <!-- 왼쪽: 이미지 -->
      <div class="left-pane">
        <img :src="coverImgUrl" alt="커버 이미지" />
        <div class="hover-overlay">AI가 자동으로 생성한 이미지입니다.</div>
      </div>

      <!-- 오른쪽: 폼 -->
      <form class="right-pane" @submit.prevent="onSubmit">
        <!-- 책 정보 -->
        <div class="book-info">
          <h3 class="book-title">{{ currentBook?.title }}</h3>
          <p class="book-author">{{ currentBook?.author_name }}</p>
        </div>

        <!-- 입력 영역 -->
        <textarea v-model="content" placeholder="감상을 남겨보세요!" required />
        <div class="bottom-row">
          <input
            type="number"
            v-model="rank"
            min="1"
            max="5"
            required
            class="rank-input"
          />
          <button type="submit" class="submit-btn">공유하기</button>
        </div>
      </form>
    </div>
  </BaseModal>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import BaseModal from '@/components/modals/BaseModal.vue'
import { useThreadStore } from '@/stores/thread'
import { useBookStore } from '@/stores/book'
import { useUserStore } from '@/stores/user'

const route = useRoute()
const router = useRouter()
const bookId = Number(route.query.bookId)

const threadStore = useThreadStore()
const bookStore = useBookStore()
const userStore = useUserStore()

const content = ref('')
const rank = ref(5)

const currentBook = computed(() =>
  bookStore.books.find(b => b.id === bookId)
)

const coverImgUrl = computed(() =>
  currentBook.value?.cover_img_url ??
  'https://via.placeholder.com/400x600'
)

const onSubmit = () => {
  const newThread = {
    id: threadStore.threads.length + 1, // 실제 구현에선 서버에서 받아와야 안전
    user_id: userStore.userInfo?.id ?? 1,
    book_id: bookId,
    title: content.value.slice(0, 20),
    content: content.value,
    rank: rank.value,
    cover_img_url: coverImgUrl.value,
    created_at: new Date().toISOString().slice(0, 10),
    updated_at: new Date().toISOString().slice(0, 10),
    like_count: 0,
    comment_count: 0
  }

  threadStore.addThread(newThread) // ✅ 메서드로 추출한 것 사용

  router.replace({ name: 'thread-detail', params: { id: newThread.id } })
}
</script>

<style scoped>
.thread-modal-wrapper {
  display: flex;
  height: 100%;
}

/* 왼쪽 이미지 영역 */
.left-pane {
  width: 50%;
  position: relative;
  background: black;
  display: flex;
  align-items: center;
  justify-content: center;
}
.left-pane img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.hover-overlay {
  position: absolute;
  bottom: 1rem;
  left: 1rem;
  background-color: rgba(0, 0, 0, 0.6);
  color: #fff;
  font-size: 0.8rem;
  padding: 0.4rem 0.8rem;
  border-radius: 6px;
  opacity: 0;
  transition: 0.3s;
}
.left-pane:hover .hover-overlay {
  opacity: 1;
}

/* 오른쪽 폼 */
.right-pane {
  width: 50%;
  background-color: #fff7e4;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  justify-content: space-between;
}
.book-info {
  text-align: left;
}
.book-title {
  font-size: 1.25rem;
  font-weight: bold;
  margin: 0;
}
.book-author {
  font-size: 1rem;
  color: #555;
  margin-top: 0.3rem;
}

textarea {
  flex: 1;
  height: 200px;
  padding: 1rem;
  resize: none;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 8px;
  background-color: #fff;
}

.bottom-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.rank-input {
  width: 80px;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-size: 1rem;
}

.submit-btn {
  padding: 0.6rem 1.4rem;
  background-color: #333;
  color: white;
  font-weight: bold;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}
</style>
