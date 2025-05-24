<!-- navbar2.vue -->

<template>
  <nav>
    <button @click="goToSignUp">회원가입</button>
  </nav>
</template>

<script setup>
import { useRouter, useRoute } from 'vue-router'
import { useUIStore } from '@/stores/ui'

const router = useRouter()
const route = useRoute()
const ui = useUIStore()

const goToSignUp = () => {
  ui.setBackgroundRoute(route.fullPath)
  router.push('/signup')
}
</script>

<style scoped>
nav { padding: 1rem; background-color: #f0f0f0; }
</style>