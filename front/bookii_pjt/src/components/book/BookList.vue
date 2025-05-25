<!-- BookList.vue -->

<template>
  <div class="book-list">
    <!-- 슬라이딩 버튼 -->
    <div class="scroll-wrapper">
      <button class="scroll-btn left" @click="prev" :disabled="currentIndex === 0">〈</button>

      <ul class="book-list-items">
        <BookListItem
          v-for="book in visibleBooks"
          :key="book.id"
          :book="book"
        />
      </ul>

      <button class="scroll-btn right" @click="next" :disabled="currentIndex + visibleCount >= (books?.length || 0)">〉</button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

import BookListItem from './BookListItem.vue'

const props = defineProps({
  books: Array,
  title: String
})

const visibleCount = 4
const currentIndex = ref(0)

const visibleBooks = computed(() => {
  const all = props.books || []
  return all.slice(currentIndex.value, currentIndex.value + visibleCount)
})


const next = () => {
  const length = props.books ? props.books.length : 0
  if (currentIndex.value + visibleCount < length) {
    currentIndex.value++
  }
}

const prev = () => {
  if (currentIndex.value > 0) {
    currentIndex.value--
  }
}
</script>

<style lang="scss" scoped>
.scroll-wrapper {
  display: flex;
  align-items: center;
  position: relative;
}

.book-list-items {
  display: flex;
  gap: 1.5rem;
  list-style: none;
  padding: 0;
  margin: 0;
  overflow: hidden;
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