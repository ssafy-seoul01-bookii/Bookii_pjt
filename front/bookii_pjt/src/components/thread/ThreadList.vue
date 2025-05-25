<!-- ThreadList.vue -->

<template>
  <div class="thread-list">
    <!-- 슬라이딩 버튼 -->
    <div class="controls">
      <button @click="prev" :disabled="currentIndex === 0"><</button>
      <button @click="next" :disabled="currentIndex + visibleCount >= threads.length">></button>
    </div>

    <!-- 쓰레드 아이템(한 번에 세 개씩) -->
    <ul class="thread-list-items">
      <ThreadListItem
        v-for="thread in visibleThreads"
        :key="thread.id"
        :thread="thread"
      />
    </ul>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import ThreadListItem from './ThreadListItem.vue'

const props = defineProps({
  threads: Array,
  title: String
})

const visibleCount = 3
const currentIndex = ref(0)

const visibleThreads = computed(() =>
  (props.threads || []).slice(currentIndex.value, currentIndex.value + visibleCount)
)

const next = () => {
  if (currentIndex.value + visibleCount < props.threads.length) {
    currentIndex.value++
  }
}
const prev = () => {
  if (currentIndex.value > 0) {
    currentIndex.value--
  }
}
</script>

<style scoped>
.thread-list {
  margin: 1rem 0;
}

.controls {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 0.5rem;
}

.thread-list-items {
  display: flex;
  gap: 1rem;
  overflow-x: auto;
  padding: 0;
}
</style>
