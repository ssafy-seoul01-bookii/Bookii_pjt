<!-- ThreadList.vue -->

<template>
  <div class="thread-list">
    <div class="scroll-wrapper">
      <button class="scroll-btn left" @click="prev" :disabled="currentIndex <= 0">〈</button>

      <ul class="thread-list-items">
        <ThreadListItem
          v-for="thread in visibleThreads"
          :key="thread.id"
          :thread="thread"
       />
      </ul>

      <button
        class="scroll-btn right"
        @click="next"
        :disabled="currentIndex + visibleCount >= (props.threads?.length || 0)"
      >〉</button>
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

const visibleCount = 3
const currentIndex = ref(0)

const visibleThreads = computed(() =>
  (props.threads || []).slice(currentIndex.value, currentIndex.value + visibleCount)
)

const next = () => {
  if (currentIndex.value + visibleCount < (props.threads?.length || 0)) {
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
  width: 100%; 
  margin: 1rem 0;
}

.thread-list-items {
  display: flex;
  flex: 1;
  flex-wrap: nowrap;
  width: 100%;
  gap: 1rem;
  overflow-x: auto;
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