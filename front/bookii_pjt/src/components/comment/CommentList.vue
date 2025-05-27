<!-- CommentList.vue -->

<template>
  <div class="comment-list">
    <CommentListItem
      v-for="comment in filteredComments"
      :key="comment.id"
      :comment="comment"
      :thread-user="threadUser"
    />
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useCommentStore } from '@/stores/comment'
import CommentListItem from './CommentListItem.vue'

const props = defineProps({
  threadId: {
    type: Number,
    required: true
  },
  threadUser: Object,
})

const commentStore = useCommentStore()

const filteredComments = computed(() => {
  if (!props.threadId) return []
  return commentStore.comments.filter(c => c.thread === props.threadId)
})
</script>

<style scoped>
.comment-list {
  margin-top: 1rem;
}
</style>
