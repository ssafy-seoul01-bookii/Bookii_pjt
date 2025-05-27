<!-- BookListItem.vue -->

<template>
  <li class="book-item">
    <router-link :to="{ name: 'book-detail', params: { bookId: book.id } }">
      <img
        v-if="book.cover_img_url"
        :src="book.cover_img_url"
        :alt="book.title"
        class="book-cover"
      />
    </router-link>
    <div class="book-info">
      <p class="book-title">{{ book.title }}</p>
      <p class="thread-count">{{ book.thread_count }}</p>
    </div>
  </li>
</template>

<script setup>
const props = defineProps({
  book: Object,
})
</script>

<style lang="scss" scoped>
.book-item {
  flex: 1;
  min-width: 160px;
  max-width: 240px;
  margin-right: 2rem; // ✅ 오른쪽 간격 주기
  list-style: none;
  text-align: center;
}

.book-list-items > :last-child {
  margin-right: 0 !important; // ✅ 마지막 항목은 간격 제거
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