<!-- 테스트
<template>
  <form @submit.prevent="submit">
    <input v-model="email" type="email" placeholder="이메일" />
    <input v-model="username" type="text" placeholder="사용자명" />
    <input v-model="password" type="password" placeholder="비밀번호" />
    <button type="submit">가입하기</button>
  </form>
</template>

<script setup>
import { ref, defineEmits } from 'vue'
// const emit = defineEmits(['submit'])
const email = ref('')
const username = ref('')
const password = ref('')

// const submit = () => {
//   console.log('회원가입 정보:', { email: email.value, username: username.value, password: password.value })
//   emit('submit')
// }
</script>

<style scoped>
input, button {
  display: block;
  margin: 0.5rem 0;
  width: 100%;
  padding: 0.5rem;
}
</style> -->