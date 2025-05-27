// ✅ User Store (백엔드 연동)
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import api from '@/lib/axios'
import auth from '@/lib/auth_axios'
import axios from 'axios'

export const useUserStore = defineStore('user', () => {
  const users = ref([])
  const accessToken = ref(null)
  const userInfo = ref(null)

  const isLoggedIn = computed(() => !!accessToken.value)
  const username = computed(() => userInfo.value?.username || '')
  const userId = computed(() => userInfo.value?.id || null)

  const fetchUsers = async () => {
    try {
      const res = await auth.get('/accounts/user/')
      users.value = res.data
    } catch (err) {
      console.error('유저 불러오기 실패:', err)
    }
  }

  const login = async ({ username, password }) => {
    try {
      const res = await auth.post('/accounts/login/', { username, password })
      
      console.log(accessToken.value);
      accessToken.value = res.data.key
      console.log("로그인 성공");
      console.log(accessToken.value);
      localStorage.setItem('accessToken', res.data.access_token)
    } catch (err) {
      console.error('로그인 실패:', err)
      throw err
    }
  }

  const signup = async (payload) => {
    try {
      const res = await api.post('/accounts/signup/', payload)
      return res.data
    } catch (err) {
      console.error('회원가입 실패:', err)
      throw err
    }
  }

  const logout = () => {
    accessToken.value = null
    userInfo.value = null
    localStorage.removeItem('accessToken')
  }

  const checkAuth = async () => {
    const token = localStorage.getItem('accessToken')
    if (!token) return
    try {
      const res = await api.get('/auth/me/')
      accessToken.value = token
      userInfo.value = res.data
    } catch (err) {
      logout()
    }
  }

  const updateUser = async (id, payload) => {
    try {
      await api.put(`/users/${id}/`, payload)
    } catch (err) {
      console.error('유저 정보 수정 실패:', err)
      throw err
    }
  }

  return {
    users,
    accessToken,
    userInfo,
    isLoggedIn,
    username,
    userId,
    login,
    logout,
    signup,
    fetchUsers,
    checkAuth,
    updateUser,
  }
})
