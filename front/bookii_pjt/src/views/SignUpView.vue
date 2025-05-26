<!-- SignUpView.vue -->

<template>
  <BaseModal modalClass="modal-narrow">
    <SignUpForm @submit="handleSignup" @go-login="goToLogin" :error="errorMessage" />
  </BaseModal>
</template>

<script setup>
import BaseModal from '@/components/modals/BaseModal.vue'
import SignUpForm from '@/components/auth/SignUpForm.vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { ref } from 'vue'

const router = useRouter()
const userStore = useUserStore()

const errorMessage = ref('')

const handleSignup = async (payload) => {
  try {
    await userStore.signup(payload)
    router.back()
  } catch (err) {
    errorMessage.value = err.response?.data?.detail || '회원가입에 실패했습니다.'
    alert(errorMessage.value)
  }
}

const goToLogin = () => {
  router.push({ name: 'login' })
}
</script>
