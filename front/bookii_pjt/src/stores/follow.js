// ✅ Follow Store
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import api from '@/lib/axios'
import { useUserStore } from './user'

export const useFollowStore = defineStore('follow', () => {
  const follows = ref([])

  const fetchFollows = async () => {
    try {
      const res = await api.get('/follows/')
      follows.value = res.data
    } catch (err) {
      console.error('팔로우 정보 불러오기 실패:', err)
    }
  }

  // 현재 로그인한 사용자가 팔로우 중인 사용자 ID 목록
  const userStore = useUserStore()
  const followings = computed(() => {
    if (!userStore.userInfo) return []
    return follows.value
      .filter(f => f.from_user === userStore.userInfo.id)
      .map(f => f.to_user)
  })

  // 팔로우 여부
  const isFollowing = (userId) => {
    return followings.value.includes(userId)
  }

  // 팔로우 토글
  const toggleFollow = (targetUserId) => {
    const fromUserId = userStore.userInfo?.id
    if (!fromUserId) return

    const index = follows.value.findIndex(f => f.from_user === fromUserId && f.to_user === targetUserId)
    if (index !== -1) {
      // 언팔로우
      follows.value.splice(index, 1)
    } else {
      // 팔로우 추가
      follows.value.push({ from_user: fromUserId, to_user: targetUserId })
    }
  }

  return {
    follows,
    fetchFollows,
    followings,
    isFollowing,
    toggleFollow
  }
})
