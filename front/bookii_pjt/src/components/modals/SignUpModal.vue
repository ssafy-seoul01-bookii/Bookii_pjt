<!-- 테스트
<template>
  <div class="modal">
    <div class="modal-content">
      <h2>회원가입</h2>
      <SignUpForm @submit="close" />
      <button @click="close">닫기</button>
    </div>
  </div>
</template>

<script setup>
import SignUpForm from '@/components/auth/SignUpForm.vue'
import { useRouter } from 'vue-router'
const router = useRouter()
const close = () => router.back()
</script>

<style scoped>
.modal {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 1000;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
}
.modal-content {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  width: 400px;
}
</style> -->