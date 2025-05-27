<!-- ThreadListItem.vue -->

<template>
  <li class="thread-card" @click="openThreadDetail">
    <p class="quote-icon">"</p>
    <p class="username">From_{{ thread.username || 'Unknown' }}</p>
    <p class="content">{{ thread.content }}</p>
    <div class="meta">
      <span class="icon like">❤️ {{ thread.like_count }}</span>
      <span class="icon comment">💬 {{ thread.comment_count }}</span>
    </div>
  </li>
</template>

<script setup>
import { useRouter, useRoute } from 'vue-router'
import { useUIStore } from '@/stores/ui'
import { nextTick } from 'vue'

const props = defineProps({
  thread: {
    type: Object,
    required: true,
  }
})

const router = useRouter()
const ui = useUIStore()

const openThreadDetail = async () => {
  console.log(props.thread.id);
  
  ui.setBackgroundRoute(router.currentRoute.value.fullPath)
  await nextTick()
  // router.push({ name: 'thread-detail', params: { id: props.thread.id } })
  // router.push({ name: 'thread-detail', params: { id: thread.id }, query: { bookId: thread.book } })
  router.push({ 
  name: 'thread-detail', 
  params: { id: props.thread.id }, 
  query: { bookId: props.thread.book }  // ✅ 올바르게 props에서 꺼냄
})

}
</script>

<style scoped>
.thread-card {
  list-style-type: none;
  flex: 1;
  min-width: 220px;
  max-width: 320px;
  margin-right: 2rem; 
}

.thread-list-items > :last-child {
  margin-right: 0 !important; 
}

.thread-card:hover {
  transform: translateY(-4px);
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