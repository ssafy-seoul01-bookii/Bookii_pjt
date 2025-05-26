<!-- ThreadList.vue -->

<template>
  <div class="thread-list">
    <!-- 슬라이딩 버튼 -->
    <div class="scroll-wrapper">
      <button class="scroll-btn left" @click="prev" :disabled="currentIndex <= 0">〈</button>

    <!-- 쓰레드 아이템(한 번에 세 개씩) -->
    <div class="thread-list-items">
      <ThreadListItem
        v-for="thread in visibleThreads"
        :key="thread.id"
        :thread="thread"
      />
    </div>

      <button class="scroll-btn right" @click="next" :disabled="currentIndex + visibleCount >= (props.threads?.length || 0)">〉</button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import ThreadListItem from './ThreadListItem.vue'


const props = defineProps({
  threads: Array,
  title: String
})

const visibleCount = computed(() =>
  Math.min(3, props.threads?.length || 0)
)

const currentIndex = ref(0)

const visibleThreads = computed(() =>
  (props.threads || []).slice(currentIndex.value, currentIndex.value + visibleCount.value)
)


const next = () => {
  if (currentIndex.value + visibleCount.value < props.threads.length) {
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
.scroll-wrapper {
  display: flex;
  align-items: center;
  position: relative;
}

.thread-list {
  margin: 1rem 0;
}

.thread-list-items {
  display: flex;
  gap: 1rem;
  overflow-x: auto;
  padding: 0;
  margin: 0;
}

.scroll-btn {
  background: none;
  border: none;
  font-size: 2rem;
  cursor: pointer;
  color: #333;

  &.left {
    margin-right: 1rem;
  }

  &.right {
    margin-left: 1rem;
  }

  &:disabled {
    color: #ccc;
    cursor: default;
  }
}
</style>
