<!-- CommentList.vue -->

<template>
  <div class="comment-list">
    <CommentListItem
      v-for="comment in filteredComments"
      :key="comment.id"
      :comment="comment"
    />
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useCommentStore } from '@/stores/comment'
import CommentListItem from './CommentListItem.vue'

const props = defineProps({
  threadId: Number
})

const commentStore = useCommentStore()
const filteredComments = computed(() =>
  commentStore.comments.filter(c => c.thread_id === props.threadId)
)
</script>

<style scoped>
.comment-list {
  margin-top: 1rem;
}
</style>
