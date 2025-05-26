<!-- LogInView.vue -->

<template>
  <BaseModal modalClass="modal-narrow">
    <LogInForm
      @submit="handleLogin"
      @go-signup="goToSignup"
      :error="errorMessage"
    />
  </BaseModal>
</template>

<script setup>
import LogInForm from '@/components/auth/LogInForm.vue'
import BaseModal from '@/components/modals/BaseModal.vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { ref } from 'vue'

const userStore = useUserStore()
const router = useRouter()

const errorMessage = ref('')

const handleLogin = async (payload) => {
  try {
    await userStore.login(payload)
    router.back()
  } catch (err) {
    errorMessage.value = err.response?.data?.detail || '아이디 또는 비밀번호가 일치하지 않습니다.'
    alert(errorMessage.value)
  }
}

const goToSignup = () => {
  router.push({ name: 'signup' })
}
</script>