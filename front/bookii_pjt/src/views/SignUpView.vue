<!-- SignUpView.vue -->

<template>
  <BaseModal modalClass="modal-narrow">
    <SignUpForm @submit="handleSignup" @go-login="goToLogin" />
  </BaseModal>
</template>

<script setup>
import BaseModal from '@/components/modals/BaseModal.vue'
import SignUpForm from '@/components/auth/SignUpForm.vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'

const router = useRouter()
const user = useUserStore()

const handleSignup = async (payload) => {
  await user.signup(payload)
  router.back()  // 회원가입 완료 시 닫기
}

const goToLogin = () => {
  router.push({ name: 'login' })
}
</script>

<style lang="scss" scoped>

</style>