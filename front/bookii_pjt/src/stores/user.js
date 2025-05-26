// user.js

import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

// 더미데이터
export const useUserStore = defineStore('user', () => {
  const users = ref([
    {
      id: 1,
      username: 'gimyejun',
      password: 'cs&2#4Xd$a',
      profile_img_url: 'https://via.placeholder.com/100x100?text=User1',
      gender: 'M',
      age: 18,
      is_critic: false,
      annual_reading_amount: 20,
      weekly_avg_reading_time: 3.8
    },
    {
      id: 2,
      username: 'eunju02',
      password: '+6C&Koil+R',
      profile_img_url: 'https://via.placeholder.com/100x100?text=User2',
      gender: 'M',
      age: 39,
      is_critic: true,
      annual_reading_amount: 42,
      weekly_avg_reading_time: 5.4
    },
    {
      id: 3,
      username: 'seoyeong10',
      password: 'y3YGLn0E_j',
      profile_img_url: 'https://via.placeholder.com/100x100?text=User3',
      gender: 'M',
      age: 20,
      is_critic: true,
      annual_reading_amount: 19,
      weekly_avg_reading_time: 6.0
    },
    {
      id: 4,
      username: 'seonghyeoni',
      password: 'Bi_8lHHvTf',
      profile_img_url: 'https://via.placeholder.com/100x100?text=User4',
      gender: 'M',
      age: 35,
      is_critic: true,
      annual_reading_amount: 50,
      weekly_avg_reading_time: 7.2
    },
    {
      id: 5,
      username: 'seongmin88',
      password: 'H%zP&$N9ks',
      profile_img_url: 'https://via.placeholder.com/100x100?text=User5',
      gender: 'F',
      age: 25,
      is_critic: false,
      annual_reading_amount: 42,
      weekly_avg_reading_time: 4.2
    },
    {
      id: 6,
      username: 'younghee_k',
      password: 'Q2$j8uLm!z',
      profile_img_url: 'https://via.placeholder.com/100x100?text=User6',
      gender: 'F',
      age: 31,
      is_critic: false,
      annual_reading_amount: 12,
      weekly_avg_reading_time: 2.6
    },
    {
      id: 7,
      username: 'taeyong99',
      password: '8pD@iFVm_1',
      profile_img_url: 'https://via.placeholder.com/100x100?text=User7',
      gender: 'M',
      age: 23,
      is_critic: false,
      annual_reading_amount: 29,
      weekly_avg_reading_time: 3.5
    },
    {
      id: 8,
      username: 'yoona_lee',
      password: '#dP7nT*skm',
      profile_img_url: 'https://via.placeholder.com/100x100?text=User8',
      gender: 'F',
      age: 28,
      is_critic: true,
      annual_reading_amount: 36,
      weekly_avg_reading_time: 6.8
    },
    {
      id: 9,
      username: 'minsu0214',
      password: 'tJ+eRpV4@c',
      profile_img_url: 'https://via.placeholder.com/100x100?text=User9',
      gender: 'M',
      age: 40,
      is_critic: true,
      annual_reading_amount: 44,
      weekly_avg_reading_time: 8.3
    },
    {
      id: 10,
      username: 'hayoung_b',
      password: 'Lm#4!xNeXz',
      profile_img_url: 'https://via.placeholder.com/100x100?text=User10',
      gender: 'F',
      age: 22,
      is_critic: false,
      annual_reading_amount: 17,
      weekly_avg_reading_time: 2.1
    }
  ])

  const accessToken = ref(false)
  const userInfo = ref(null)
  const isLoggedIn = computed(() => !!accessToken.value)

  const setAccessToken = (token) => {
    accessToken.value = token
  }

  const clearSession = () => {
    accessToken.value = null
    userInfo.value = null
  }

  // 👉 로그인 함수 추가
  const login = async ({ username, password }) => {
    const foundUser = users.value.find(
      (user) => user.username === username && user.password === password
    )

    if (foundUser) {
      accessToken.value = 'dummy_token_' + foundUser.id  // 임의 토큰
      userInfo.value = foundUser
    } else {
      throw new Error('아이디 또는 비밀번호가 일치하지 않습니다.')
    }
  }

  return {
    users,
    accessToken,
    isLoggedIn,
    userInfo,
    login,
    setAccessToken,
    clearSession
  }
})
