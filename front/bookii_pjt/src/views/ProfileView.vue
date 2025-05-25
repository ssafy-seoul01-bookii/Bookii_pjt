<template>
  <div class="profile-background">
    <div class="profile-view">
      <!-- 프로필 영역 -->
      <section class="profile-header">
        <img :src="user.profile_img_url" alt="프로필 이미지" class="profile-img" />
        <div class="profile-info">
          <h2>{{ user.username }}</h2>
          <div class="user-stats">
            <span><strong>{{ userThreads.length }}</strong> 게시물</span>
            <span><strong>{{ user.annual_reading_amount }}</strong> 권/년</span>
            <span><strong>{{ user.weekly_avg_reading_time }}</strong> 시간/주</span>
          </div>
          <p class="user-meta">
            성별: {{ user.gender === 'M' ? '남성' : '여성' }} | 나이: {{ user.age }}세
          </p>
  
          <div class="action-buttons">
            <button v-if="isOwnProfile" @click="goToEdit">프로필 수정</button>
            <button v-else @click="toggleFollow">
              {{ isFollowing ? '언팔로우' : '팔로우' }}
            </button>
          </div>
        </div>
      </section>
  
      <!-- 탭 메뉴 디자인 -->
      <div class="profile-tabs">
        <div class="tab active">
          <span>쓰레드 🖋️</span>
        </div>
      </div>
  
      <!-- 게시물 그리드 -->
      <section class="thread-grid">
      <div
        v-for="(thread, index) in visibleThreads"
        :key="thread.id"
        class="thread-item"
        ref="setLastItem(index)"
        @click="openThreadDetail(thread)"
      >
        <img :src="thread.cover_img_url" alt="thread 이미지" />
        <div class="overlay">
          <p class="title">{{ thread.title }}</p>
          <div class="meta-bar">
            ❤️ {{ thread.like_count }} &nbsp;&nbsp; 💬 {{ thread.comment_count }}
          </div>
        </div>
      </div>
      </section>
    </div>
  </div>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router'
import { ref, computed, watch, onMounted } from 'vue'
import { useUserStore } from '@/stores/user'
import { useThreadStore } from '@/stores/thread'
import { useUIStore } from '@/stores/ui'

const route = useRoute()
const router = useRouter()

const uiStore = useUIStore()
const userStore = useUserStore()
const threadStore = useThreadStore()

// 현재 URL의 사용자
const username = route.params.username
const user = computed(() =>
  userStore.users.find(u => u.username === username)
)

// 현재 로그인된 사용자
const currentUser = computed(() =>
  userStore.users.find(u => u.username === userStore.accessToken)
)

const isOwnProfile = computed(() =>
  currentUser.value?.username === user.value?.username
)

const isFollowing = computed(() =>
  currentUser.value?.following?.includes(user.value.id)
)

// 모든 쓰레드 → 유저 기준 필터링
const userThreads = computed(() =>
  threadStore.threads.filter(t => t.user_id === user.value?.id)
)

// 무한스크롤용
const visibleCount = ref(6)
const visibleThreads = computed(() =>
  userThreads.value.slice(0, visibleCount.value)
)

const observer = ref(null)
const lastItem = ref(null)

function setLastItem(index) {
  return (el) => {
    if (index === visibleThreads.value.length - 1) {
      lastItem.value = el
    }
  }
}

const loadMore = () => {
  if (visibleCount.value < userThreads.value.length) {
    visibleCount.value += 3
  }
}

// 무한스크롤 옵저버 연결
watch(lastItem, (el) => {
  if (observer.value) observer.value.disconnect()

  if (el) {
    observer.value = new IntersectionObserver(([entry]) => {
      if (entry.isIntersecting) loadMore()
    })
    observer.value.observe(el)
  }
})

// 라우터 이동
const goToEdit = () => {
  router.push({ name: 'profile-edit', params: { username } })
}

const goToThread = (id) => {
  router.push({ name: 'thread-detail', params: { id } })
}

// 팔로우 토글
const toggleFollow = () => {
  const targetId = user.value.id
  const list = currentUser.value.following || []

  if (list.includes(targetId)) {
    currentUser.value.following = list.filter(id => id !== targetId)
  } else {
    currentUser.value.following = [...list, targetId]
  }
}

// ThreadDetail 용
const openThreadDetail = (thread) => {
  uiStore.setBackgroundRoute(router.currentRoute.value.fullPath)
  router.push({ name: 'thread-detail', params: { id: thread.id } })
}
</script>

<style scoped>
.profile-background {
  background-color: #FFF7E4;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.profile-view {
  padding: 2rem 4rem;
  width: 60%;
  margin: 0 auto;
  margin-top: 2rem;
}

.profile-header {
  display: flex;
  justify-content: center;
  max-width: 935px; 
  margin: 0 auto;   
  display: flex;
  align-items: flex-start;
  gap: 5rem;
  margin-bottom: 2rem;
}

.profile-img {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid #ddd;
  flex-shrink: 0;
}

.profile-info h2 {
  margin: 0;
  font-size: 1.6rem;
}

.user-stats {
  display: flex;
  gap: 1.2rem;
  margin: 0.5rem 0;
  font-size: 0.95rem;
}

.user-meta {
  color: #555;
  font-size: 0.9rem;
}

.action-buttons button {
  margin-top: 0.8rem;
  padding: 0.4rem 1rem;
  border: none;
  border-radius: 4px;
  background: #a2ace2;
  color: white;
  font-size: 0.9rem;
  cursor: pointer;
}

/* 쓰레드 그리드 */
.thread-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 4px;
}

.thread-item {
  display: block;
  position: relative;
  width: 100%;
  height: 100%;
  aspect-ratio: 1 / 1;
  overflow: hidden;
}

/* 이미지 */
.thread-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

/* 호버 시 확대 */
.thread-item:hover img {
  transform: scale(1.03);
}

.overlay {
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.35);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 1rem 0.5rem;
  opacity: 0;
  transition: opacity 0.3s;
}

.thread-item:hover .overlay {
  opacity: 1;
}

/* 제목 상단 */
.overlay .title {
  color: white;
  font-size: 1rem;
  text-align: center;
  text-shadow: 0 0 2px black;
  margin: 0;
}

/* 좋아요/댓글 하단 */
.meta-bar {
  color: white;
  font-size: 0.8rem;
  text-shadow: 0 0 2px black;
  text-align: center;
}

/* 탭 디자인 */
.profile-tabs {
  display: flex;
  justify-content: center;
  border-bottom: 1px solid #333;
  margin: 3rem 0 1rem;
}

.tab {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 1rem;
  font-weight: 500;
  padding: 1rem;
  color: #888;
  border-bottom: 2px solid transparent;
}

.tab.active {
  color: black;
  border-bottom: 2px solid white;
}
</style>
