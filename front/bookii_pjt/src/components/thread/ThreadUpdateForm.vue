<!-- ThreadUpdateForm.vue -->

<template>
  <BaseModal modalClass="modal-wide">
    <div class="thread-modal-wrapper">
      <!-- 왼쪽: 이미지 -->
      <div class="left-pane">
        <img :src="coverImgUrl" alt="커버 이미지" />
        <div class="hover-overlay">AI가 자동으로 생성한 이미지입니다.</div>
      </div>

      <!-- 오른쪽: 수정 폼 -->
      <form class="right-pane" @submit.prevent="onSubmit">
        <div class="book-info">
          <h3 class="book-title">{{ book?.title }}</h3>
          <p class="book-author">{{ book?.author_name }}</p>
        </div>

        <textarea v-model="content" placeholder="감상을 수정해보세요" required />
        <div class="bottom-row">
          <input
            type="number"
            v-model="rank"
            min="1"
            max="5"
            required
            class="rank-input"
          />
          <button type="submit" class="submit-btn">수정 완료</button>
        </div>
      </form>
    </div>
  </BaseModal>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import BaseModal from '@/components/modals/BaseModal.vue'
import { useThreadStore } from '@/stores/thread'
import { useBookStore } from '@/stores/book'

const route = useRoute()
const router = useRouter()
const threadId = Number(route.params.id)

const threadStore = useThreadStore()
const bookStore = useBookStore()

const thread = computed(() =>
  threadStore.threads.find(t => t.id === threadId)
)

const book = computed(() =>
  bookStore.books.find(b => b.id === thread.value?.book_id)
)

const content = ref('')
const rank = ref(5)

onMounted(() => {
  content.value = thread.value?.content || ''
  rank.value = thread.value?.rank || 5
})

const coverImgUrl = computed(() =>
  thread.value?.cover_img_url || 'https://via.placeholder.com/400x600'
)

const onSubmit = () => {
  if (!thread.value) return

  const updated = {
    ...thread.value,
    content: content.value,
    rank: rank.value,
    updated_at: new Date().toISOString().slice(0, 10)
  }

  // ✅ 메서드 추출 (추후 서버 연동도 가능하게)
  threadStore.updateThread(threadId, updated)

  alert('수정이 완료되었습니다!')
  router.back()
}
</script>

<style scoped>
/* 기존 ThreadCreateForm.vue 스타일 그대로 복붙 */
.thread-modal-wrapper {
  display: flex;
  height: 100%;
}
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
