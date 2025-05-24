<!-- HomeView.vue -->

<template>
  <div>
    <h1>home</h1>
  </div>
</template>

<script setup>
import { useUIStore } from '@/stores/ui'
import { useRoute, useRouter } from 'vue-router'

const router = useRouter()
const route = useRoute()
const ui = useUIStore()

const goToLogin = () => {
  ui.setBackgroundRoute(route.fullPath)
  router.push('/login')
}
</script>

<style lang="scss" scoped>

</style>