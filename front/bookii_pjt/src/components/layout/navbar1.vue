<!-- navbar1.vue -->

<template>
  <nav class="navbar1">
    <div class="left">
      <router-link :to="{ name: 'home' }" class="link">Bookii</router-link>
      <!-- 태그 임의값 -->
      <router-link :to="{ name: 'tag-search' }" class="link">태그검색</router-link>
      <a href="https://www.kyobobook.co.kr" target="_blank" class="link">책 구매</a>
    </div>
    <div class="right">
      <!-- 로그인여부 분기 -->
      <template v-if="isLoggedIn">
        <router-link :to="{ name: 'profile', params: { username: user.username } }" class="greeting">
          {{ user.username }}님, 안녕하세요!
        </router-link>
      </template>
      <template v-else>
        <span class="link" @click="goToSignUp">회원가입</span>
      </template>
    </div>
  </nav>
</template>

<script setup>
import { computed } from 'vue'
import { useUserStore } from '@/stores/user'
import { useRouter, useRoute } from 'vue-router'
import { useUIStore } from '@/stores/ui'

const user = useUserStore()
const ui = useUIStore()
const router = useRouter()
const route = useRoute()

const isLoggedIn = computed(() => !!user.accessToken)

const goToSignUp = () => {
  ui.setBackgroundRoute(route.fullPath)
  router.push('/signup')
}

</script>

<style lang="scss" scoped>
.navbar1 {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: black;
  color: white;
  padding: 0.5rem 1rem;
  font-size: 0.9rem;
}

.left,
.right {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.link {
  color: white;
  text-decoration: none;
  font-weight: 500;
}

.link:hover {
  text-decoration: underline;
}

.greeting {
  font-weight: bold;
  color: #ffd700;
}
</style>