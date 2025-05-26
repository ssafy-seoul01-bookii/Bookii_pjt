<!-- LogInForm.vue -->

<template>
  <form class="login-form" @submit.prevent="handleSubmit">
    <!-- 로고 -->
    <h1 class="logo">
      <img src="@/assets/003.PNG" alt="Bookii 로고">
    </h1>
    <h2 class="title">로그인</h2>

    <!-- 아이디 / 비밀번호 입력 -->
    <input v-model="form.username" type="text" placeholder="아이디" required />
    <input v-model="form.password" type="password" placeholder="비밀번호" required />

    <!-- 로그인 버튼 -->
    <button type="submit" class="login-btn">로그인</button>

    <!-- 회원가입 링크 -->
    <p class="signup-guide">
      계정이 없으신가요? <span class="signup-link" @click="$emit('go-signup')">회원가입</span>
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

    <!-- 안내 문구 -->
    <p class="guide-text">
      <strong>Bookii</strong>는 <strong>SNS 연동 로그인</strong>도 가능합니다.<br />
      편하게 <strong>Bookii</strong>의 서비스를 즐겨보세요!
    </p>
  </form>
</template>

<script setup>
import { reactive } from 'vue'

const emit = defineEmits(['submit', 'go-signup'])

const form = reactive({
  username: '',
  password: ''
})

function handleSubmit() {
  emit('submit', { ...form })
}
</script>

<style scoped>
.login-form {
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

.login-btn {
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

.signup-guide {
  font-size: 14px;
  color: #333;
  margin-bottom: 20px;
}

.signup-link {
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
  margin-bottom: 24px;
}

.sns-icon {
  width: 48px;
  height: 48px;
  cursor: pointer;
}

.guide-text {
  background-color: #e3e8fd;
  color: #4d4d4d;
  text-align: center;
  padding: 12px;
  border-radius: 8px;
  font-size: 13px;
  line-height: 1.4;
}
</style>