<!-- LogInView.vue -->

<template>
  <BaseModal modalClass="modal-narrow">
    <LogInForm @submit="handleLogin" @go-signup="goToSignup" />
  </BaseModal>
</template>

<script setup>
import LogInForm from '@/components/auth/LogInForm.vue'
import BaseModal from '@/components/modals/BaseModal.vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'

const user = useUserStore()
const router = useRouter()

const handleLogin = async (payload) => {
  await user.login(payload)
  router.back()  // 로그인 성공 시 이전 페이지로 복귀
}

const goToSignup = () => {
  router.push({ name: 'signup' })  // 회원가입 모달로 전환
}
</script>

<style lang="scss" scoped>

</style>