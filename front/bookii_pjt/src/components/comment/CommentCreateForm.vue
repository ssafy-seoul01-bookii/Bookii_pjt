<!-- CommentCreateForm.vue -->

<template>
  <form class="comment-form" @submit.prevent="submitComment">
    <input
      v-model="newComment"
      placeholder="댓글을 입력하세요..."
      class="input"
    />
    <button class="submit-btn">게시</button>
  </form>
</template>

<script setup>
import { ref } from 'vue'
import { useCommentStore } from '@/stores/comment'
import { useUserStore } from '@/stores/user'

const props = defineProps({
  threadId: {
    type: Number,
    required: true
  }
})

const commentStore = useCommentStore()
const userStore = useUserStore()

const newComment = ref('')

const submitComment = () => {
  if (!newComment.value.trim()) return
  commentStore.addComment({
    thread_id: props.threadId,
    user_id: userStore.accessToken,
    content: newComment.value
  })
  newComment.value = ''
}
</script>

<style scoped>
.comment-form {
  display: flex;
  gap: 0.5rem;
  margin-top: 1rem;
}
.input {
  flex: 1;
  padding: 0.5rem;
  border-radius: 20px;
  border: 1px solid #ccc;
}
.submit-btn {
  padding: 0 1rem;
  border: none;
  background-color: #a2ace2;
  color: white;
  border-radius: 20px;
  cursor: pointer;
}
</style>
