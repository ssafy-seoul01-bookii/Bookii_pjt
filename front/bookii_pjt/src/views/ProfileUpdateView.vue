<!-- ProfileUpdateView.vue -->

<template>
  <div class="profile-update-view">
    <ProfileUpdateForm :user="user" @submit="updateProfile" />
  </div>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router'
import { computed } from 'vue'
import { useUserStore } from '@/stores/user'
import ProfileUpdateForm from '@/components/auth/ProfileUpdateForm.vue'

const route = useRoute()
const router = useRouter()
const userStore = useUserStore()

const username = route.params.username
const user = computed(() =>
  userStore.users.find(u => u.username === username)
)

const updateProfile = (updatedUser) => {
  const idx = userStore.users.findIndex(u => u.username === username)
  if (idx !== -1) {
    userStore.users[idx] = updatedUser
    router.back() // 모달 닫기
  }
}
</script>

<style lang="scss" scoped>

</style>