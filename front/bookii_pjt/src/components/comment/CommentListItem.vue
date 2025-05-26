<!-- CommentListItem -->

<template>
  <div class="comment-item">
    <!-- 좌측 : 프로필 + 내용 -->
    <img :src="user?.profile_img_url" alt="프로필 이미지" class="avatar" />
    <div class="comment-body">
      <p class="username">@{{ user?.username }}</p>
      <p class="content">{{ comment.content }}</p>
      <p class="date">{{ comment.created_at }}</p>
    </div>

    <!-- 우측: 좋아요 + 삭제 -->
    <div class="actions">
      <button class="like-btn" @click="toggleLike">❤️ {{ likeCount }}</button>
      <a href="#" class="delete" @click.prevent="deleteComment">삭제</a>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useUserStore } from '@/stores/user'
import  { useCommentStore } from '@/stores/comment'

const props = defineProps({
  comment: Object
})

const userStore = useUserStore()
const commentStore = useCommentStore()
const user = computed(() => userStore.users.find(u => u.id === props.comment.user_id))

const isLiked = ref(false)
const likeCount = ref(Math.floor(Math.random() * 10) + 1) // 💡 더미용 랜덤

const toggleLike = () => {
  isLiked.value = !isLiked.value
  likeCount.value += isLiked.value ? 1 : -1
}

const deleteComment = () => {
  commentStore.comments = commentStore.comments.filter(c => c.id !== props.comment.id)
}

</script>

<style scoped>
.comment-item {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 1rem;
  margin-bottom: 1rem;
}
.avatar {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  object-fit: cover;
  flex-shrink: 0;
}
.comment-body {
  flex: 1;
  min-width: 0;
}

.username {
  font-weight: bold;
  font-size: 0.9rem;
  margin-bottom: 0.2rem;
}

.content {
  font-size: 0.9rem;
  word-wrap: break-word;
}

.date {
  font-size: 0.75rem;
  color: #999;
}

.actions {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 0.3rem;
  margin-left: 0.5rem;
}

.like-btn {
  background: none;
  border: none;
  color: #666;
  font-size: 0.85rem;
  cursor: pointer;
  padding: 0;
}

.like-btn:hover {
  color: red;
}

.delete {
  font-size: 0.75rem;
  color: #888;
  cursor: pointer;
  text-decoration: underline;
}
</style>
