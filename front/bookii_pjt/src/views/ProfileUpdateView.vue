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

const updateProfile = async (updatedUser) => {
  try {
    await userStore.updateUser(user.value.id, updatedUser)
    await userStore.fetchUsers() // 리스트 갱신
    router.back() // 모달 닫기
  } catch (err) {
    console.error('프로필 수정 실패:', err)
    alert('프로필 수정에 실패했습니다.')
  }
}
</script>

<style lang="scss" scoped>
/* 필요시 스타일 추가 */
</style>