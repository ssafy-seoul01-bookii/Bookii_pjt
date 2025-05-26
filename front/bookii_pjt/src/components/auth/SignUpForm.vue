<template>
  <form class="signup-form" @submit.prevent="handleSubmit">
    <!-- 로고 -->
    <h1 class="logo">
      <img src="@/assets/003.png" alt="Bookii 로고" />
    </h1>
    <h2 class="title">회원가입</h2>

    <!-- 입력 필드 -->
    <input v-model="form.name" type="text" placeholder="이름" required />
    <input v-model="form.username" type="text" placeholder="아이디" required />
    <input v-model="form.password" type="password" placeholder="비밀번호" required />

    <!-- 에러 메시지 표시 -->
    <p v-if="error" class="error-text">{{ error }}</p>

    <!-- 가입 버튼 -->
    <button type="submit" class="signup-btn">회원가입</button>

    <!-- 로그인 링크 -->
    <p class="login-guide">
      이미 가입하셨나요?
      <span class="login-link" @click="$emit('go-login')">로그인</span>
    </p>

    <!-- 구분선 -->
    <div class="divider">
      <hr />
      <span>OR</span>
      <hr />
    </div>

    <!-- SNS 로그인 -->
    <div class="sns-login">
      <img src="#" alt="카카오 로그인" class="sns-icon" />
      <img src="#" alt="구글 로그인" class="sns-icon" />
    </div>
  </form>
</template>

<script setup>
import { reactive } from 'vue'

// emits 정의
const emit = defineEmits(['submit', 'go-login'])

// error prop 수신
const props = defineProps({
  error: String
})

// form 상태
const form = reactive({
  name: '',
  username: '',
  password: ''
})

function handleSubmit() {
  emit('submit', { ...form })
}
</script>

<style scoped>
.signup-form {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 360px;
  margin: 0 auto;
  font-family: 'Pretendard', sans-serif;
}

.logo {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 8px;
}

.logo img {
  height: auto;
  max-width: 160px;
  object-fit: contain;
}

.title {
  font-size: 20px;
  margin-bottom: 24px;
}

input {
  width: 100%;
  padding: 12px;
  margin-bottom: 12px;
  border: none;
  border-radius: 8px;
  background-color: #fff7e4;
  font-size: 14px;
  color: #a2ace2;
}

.error-text {
  color: red;
  font-size: 0.85rem;
  margin-bottom: 8px;
  align-self: flex-start;
}

.signup-btn {
  width: 100%;
  padding: 12px;
  background-color: #c4d9ed;
  color: white;
  font-weight: bold;
  border: none;
  border-radius: 8px;
  margin-bottom: 20px;
  cursor: pointer;
}

.login-guide {
  font-size: 14px;
  color: #333;
  margin-bottom: 20px;
}
.login-link {
  color: #a2ace2;
  cursor: pointer;
  font-weight: bold;
}

.divider {
  display: flex;
  align-items: center;
  width: 100%;
  gap: 8px;
  margin-bottom: 20px;
}
.divider hr {
  flex: 1;
  border: none;
  height: 1px;
  background-color: #ccc;
}
.divider span {
  font-size: 12px;
  color: #666;
}

.sns-login {
  display: flex;
  gap: 16px;
  margin-bottom: 16px;
}
.sns-icon {
  width: 48px;
  height: 48px;
  cursor: pointer;
}
</style>