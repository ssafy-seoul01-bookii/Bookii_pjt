<!-- App.vue -->

<template>
  <div class="app-wrapper">
    <!-- 공통 네비게이션 -->
    <Navbar1 />
    <Navbar2 />

    <!-- 배경 뷰 (현재 모달 진입 전의 페이지) -->
    <div class="main-content">
      <component :is="backgroundComponent" />
    </div>

    <!-- 모달 뷰 (기본) -->
    <router-view v-slot="{ Component }">
      <BaseModal class="modal-layer" v-if="isModalRoute">
        <component :is="Component"/>
      </BaseModal>
    </router-view>

    <!-- 이중 모달 뷰 -->
    <router-view name="submodal" v-slot="{ Component }">
      <BaseModal class="submodal-layer" v-if="Component">
        <component :is="Component"/>
      </BaseModal>
    </router-view>

    <!-- 공통 푸터 -->
    <Footer2/>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { useUIStore } from '@/stores/ui'

import BaseModal from '@/components/modals/BaseModal.vue'
import Navbar1 from '@/components/layout/navbar1.vue'
import Navbar2 from '@/components/layout/navbar2.vue'
import Footer2 from '@/components/layout/footer2.vue'

import HomeView from '@/views/HomeView.vue'
import BookDetailView from '@/views/BookDetailView.vue'
import SearchView from '@/views/SearchView.vue'
import TagSearchView from '@/views/TagSearchView.vue'
import ProfileView from '@/views/ProfileView.vue'
import ThreadDetailView from '@/views/ThreadDetailView.vue'

const route = useRoute()
const ui = useUIStore()

// 1단계 모달 조건 (router meta 기반)
const isModalRoute = computed(() => route.meta.isModal === true)

// backgroundmap 지정(기본 백)
const backgroundMap = {
    'home': HomeView,
    'book-detail': BookDetailView,
    'search': SearchView,
    'tag-search': TagSearchView,
    'profile': ProfileView,
    'thread-detail': ThreadDetailView,
}

const backgroundComponent = computed(() => {
  // 1️⃣ 일반 페이지 라우팅: route.name 기반 렌더링
  if (!isModalRoute.value) {
    return backgroundMap[route.name] || HomeView
  }
  // 2️⃣ route.meta.background가 명시되어 있으면 우선 적용
  if (route.meta.background && backgroundMap[route.meta.background]) {
    return backgroundMap[route.meta.background]
  }

  // 3️⃣ fallback: backgroundRoute(Pinia)에 따라 유추
  const path = ui.backgroundRoute
  if (!path) return HomeView
  if (path.startsWith('/book/')) return BookDetailView
  if (path.startsWith('/search/tag')) return TagSearchView
  if (path.startsWith('/search')) return SearchView
  if (path.startsWith('/profile')) return ProfileView
  // 4️⃣ 최종 fallback
  return HomeView
})

</script>

<!-- 전역 스타일로 추가 -->
<style lang="scss">
html, body {
  margin: 0;
  padding: 0;
  height: 100%;
  overflow-y: auto;
}

.app-wrapper {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.main-content {
  flex: 1;
}

.modal-layer {
  z-index: 1000;
}

.submodal-layer {
  z-index: 1100;
}
</style>