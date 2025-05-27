// src/lib/axios.js

import axios from 'axios'

// axios 인스턴스 생성
const api = axios.create({
  baseURL: 'http://localhost:8000/api',  // Django API 주소
  withCredentials: true,                   // 쿠키 인증 시 필수
  headers: {
    'Content-Type': 'application/json',
  }
})
const auth = axios.create({
  baseURL: 'http://localhost:8000',  // Django API 주소
  withCredentials: true,                   // 쿠키 인증 시 필수
  headers: {
    'Content-Type': 'application/json',
  }
})

// 요청 인터셉터 (예: 토큰 자동 첨부)
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('accessToken')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
}, (error) => {
  return Promise.reject(error)
})

// 응답 인터셉터 (예: 에러 처리)
api.interceptors.response.use((response) => {
  return response
}, (error) => {
  console.error('[API ERROR]', error.response?.data || error.message)
  return Promise.reject(error)
})

export default api
