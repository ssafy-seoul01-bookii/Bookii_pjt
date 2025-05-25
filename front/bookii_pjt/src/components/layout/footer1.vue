<!-- footer1.vue -->

<template>
  <footer class="footer1" v-if="randomThread">
    <p class="quote">"{{ randomThread.title }}"</p>
    <p class="user">- @{{ randomThread.username }} -</p>
  </footer>
</template>

<script setup>
import { computed } from 'vue'
import { useThreadStore } from '@/stores/thread'
import { useUserStore } from '@/stores/user'

const threadStore = useThreadStore()
const userStore = useUserStore()

// 무작위 하나 선택
const randomThread = computed(() => {
  const threads = threadStore.threads
  const users = userStore.users

  if (!threads.length) return null

  const selected = threads[Math.floor(Math.random() * threads.length)]
  const user = users.find(user => user.id === selected.user_id)

  return {
    title: selected.title,
    username: user?.username || '익명'
  }
})
</script>

<style scoped>
.footer1 {
  text-align: center;
  padding: 0.6rem 1rem;
  background-color: #C4D9ED; 
  color: white;              
  font-style: italic;
  font-size: 0.95rem;
  border-top: 1px solid #aac4dd;
}

.quote {
  font-weight: 500;
  margin: 0.05rem 0;
}

.user {
  margin-top: 0.25rem;
  font-size: 0.85rem;
  color: white;
}
</style>

