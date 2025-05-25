<!-- BaseModal.vue -->

<template>
  <div class="modal-wrapper" @click.self="close">
    <div class="modal-content" :class="modalClass">
      <button class="close-btn" @click="close">x</button>
      <slot></slot>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { onMounted, onBeforeUnmount } from 'vue'

const router = useRouter()
const close = () => router.back() // 모달 창 닫기

// ESC 처리
const handleEsc = (event) => {
  if ( event.key === 'Escape') close()
}

onMounted(() => {
  window.addEventListener('keydown', handleEsc)
})
onBeforeUnmount(() => {
  window.removeEventListener('keydown', handleEsc)
})

// Modal 크기 유동성 추가
defineProps({
  modalClass: {
    type: String,
    default: ''
  }
})
</script>

<style lang="scss" scoped>
.modal-wrapper {
  position: fixed;
  inset: 0;
  z-index: 1000;
  background-color: rgba(0, 0, 0, 0.4);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  /* 기본 스타일 (예: 좁은 폼용) */
  width: 90%;
  max-width: 420px;
  padding: 2rem;
  border-radius: 12px;
  background: white;
}

.modal-narrow {
  max-width: 420px;
}

.modal-wide {
  width: 90vw;
  max-width: 960px;
  height: 80vh;
  overflow-y: auto;
}

.close-btn {
  position: absolute;
  top: 1rem;
  right: 1rem;
  font-size: 1.5rem;
  border: none;
  background: transparent;
  cursor: pointer;
}
</style>