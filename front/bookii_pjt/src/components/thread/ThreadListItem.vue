<!-- ThreadListItem.vue -->

<template>
  <li class="thread-card" @click="openThreadDetail">
    <p class="quote-icon">“</p>
    <p class="username">From_{{ thread.user_name || 'Unknown' }}</p>
    <p class="content">{{ thread.content }}</p>
    <div class="meta">
      <span class="icon like">❤️ {{ thread.like_count }}</span>
      <span class="icon comment">💬 {{ thread.comment_count }}</span>
    </div>
  </li>
</template>

<script setup>
import { useRouter, useRoute } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { useUIStore } from '@/stores/ui'
import { computed } from 'vue'
import {nextTick } from 'vue'

const props = defineProps({
  thread: {
    type: Object,
    required: true,
  }
})

const route = useRoute()
const router = useRouter()
const userStore = useUserStore()
const ui = useUIStore()

const user = computed(() =>
  userStore.users.find(u => u.id === props.thread.user_id)
)

const openThreadDetail = async () => {
  ui.setBackgroundRoute(router.currentRoute.value.fullPath)  // ✅ 진짜 현재 경로!
  await nextTick()
  router.push({ name: 'thread-detail', params: { id: props.thread.id } })
}
</script>

<style scoped>
.thread-card {
  width: 220px;
  background: #fff;
  padding: 1rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  font-family: sans-serif;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.quote-icon {
  font-size: 1.5rem;
  color: #444;
  margin: 0;
}

.username {
  font-weight: bold;
  margin: 0;
  font-size: 0.95rem;
}

.content {
  font-size: 0.9rem;
  color: #222;
  line-height: 1.4;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
}

.meta {
  display: flex;
  justify-content: flex-start;
  gap: 1rem;
  font-size: 0.85rem;
  color: #555;
}
</style>

