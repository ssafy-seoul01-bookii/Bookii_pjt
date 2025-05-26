<!-- BookListItem.vue -->

<template>
  <li class="book-item">
    <img :src="book.coverImage" :alt="book.title" class="book-cover">
    <div class="book-info">
      <p class="book-title">{{ book.title }}</p>
      <p class="thread-count">{{ book.threadCount }}</p>
    </div>
  </li>
</template>

<script setup>
defineProps({
  book: Object,
})
</script>

<style lang="scss" scoped>
.book-item {
  width: 150px;
  list-style: none;
  text-align: center;
}

.book-cover {
  width: 100%;
  height: auto;
  border-radius: 4px;
}

.book-info {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 0.5rem;
  padding: 0 0.25rem;
}

.book-title {
  font-weight: bold;
  font-size: 0.95rem;
}

.thread-count {
  font-size: 0.85rem;
  color: #6b6bff;
}
</style>