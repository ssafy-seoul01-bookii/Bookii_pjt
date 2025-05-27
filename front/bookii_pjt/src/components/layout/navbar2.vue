<!-- navbar2.vue -->

<template>
  <nav class="navbar2">
    <!-- 좌측: 햄버거 + 로고 -->
    <div class="left">
      <!-- <button class="hamburger" @click="toggleMenu">☰</button> -->
      <router-link :to="{ name: 'home' }">
        <img src="@/assets/004.png" alt="Bookii" class="logo" />
      </router-link>
    </div>

    <!-- 우측: 검색창 + 로그인/로그아웃 버튼 -->
    <div class="right">
      <div class="search-group">
        <input
          v-model="searchText"
          type="text"
          placeholder="책 제목 검색"
          @keydown.enter="goToSearch"
        />
        <button @click="goToSearch">🔍</button>
      </div>
      <template v-if="isLoggedIn">
        <button class="auth-btn" @click="logout">로그아웃</button>
      </template>
      <template v-else>
        <button class="auth-btn" @click="goToLogin">로그인</button>
      </template>
    </div>
  </nav>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { useUIStore } from '@/stores/ui'

const router = useRouter()
const user = useUserStore()
const uiStore = useUIStore()

const isLoggedIn = computed(() => user.isLoggedIn)

// searchText → Pinia 전역 관리
const searchText = computed({
  get: () => uiStore.searchText,
  set: val => (uiStore.searchText = val)
})

// 메뉴 버튼 클릭 이벤트 (필요 시 drawer 기능 등 추가 가능)
const toggleMenu = () => {
  console.log('햄버거 버튼 클릭됨')
}

const goToSearch = () => {
  router.push({ name: 'search', query: { q: searchText.value } })
}

const goToLogin = () => {
  uiStore.setBackgroundRoute(router.currentRoute.value.fullPath)
  router.push({ name: 'login' })
}

const logout = () => {
  user.logout()
  router.push({ name: 'home' }) // ✅ 홈으로 강제 이동
}
</script>

<style scoped>
.navbar2 {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.5rem;
  background-color: #FFECBD;
  border-bottom: 1px solid #ccc;
}

.left {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.hamburger {
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
}

.logo {
  height: 48px;
  cursor: pointer;
}

.right {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.search-group {
  display: flex;
  align-items: center;
  border: 1px solid #ccc;
  border-radius: 4px;
  overflow: hidden;
}

.search-group input {
  border: none;
  padding: 0.3rem 0.5rem;
  outline: none;
  width: 150px;
}

.search-group button {
  background: #eee;
  border: none;
  padding: 0.3rem 0.7rem;
  cursor: pointer;
}

.auth-btn {
  background-color: #333;
  color: white;
  border: none;
  padding: 0.4rem 0.8rem;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.85rem;
}
</style>