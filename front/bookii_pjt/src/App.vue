<template>
  <div>
    <!-- 공통 네비게이션 -->
    <Navbar2 />

    <!-- 배경 뷰 (현재 모달 진입 전의 페이지) -->
    <component :is="backgroundComponent" />

    <!-- 모달 뷰 (기본) -->
    <router-view v-slot="{ Component }">
      <component :is="Component" v-if="isModalRoute" class="modal-layer" />
    </router-view>

    <!-- 이중 모달 뷰 -->
    <router-view name="submodal" v-slot="{ Component }">
      <component :is="Component" v-if="Component" class="submodal-layer" />
    </router-view>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { useUIStore } from '@/stores/ui'
import Navbar2 from '@/components/layout/navbar2.vue'

import HomeView from '@/views/HomeView.vue'
import BookDetailView from '@/views/BookDetailView.vue'
import SearchView from '@/views/SearchView.vue'
import TagSearchView from '@/views/TagSearchView.vue'
import ProfileView from '@/views/ProfileView.vue'

const route = useRoute()
const ui = useUIStore()

const isModalRoute = computed(() =>
  [
    '/signup',
    '/login',
    '/profile/',
    '/thread/create',
    '/thread/',
    '/thread/:id/edit'
  ].some(path => route.path.startsWith(path.replace(':id', '')))
)

const backgroundComponent = computed(() => {
  const path = ui.backgroundRoute

  if (!isModalRoute.value || !path) return HomeView
  if (path.startsWith('/book/')) return BookDetailView
  if (path.startsWith('/search/tag')) return TagSearchView
  if (path.startsWith('/search')) return SearchView
  if (path.startsWith('/profile')) return ProfileView
  return HomeView
})
</script>

<style lang="scss" scoped>
.modal-layer {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 1000;
  width: 100%;
  height: 100%;
  background-color: rgba(255, 255, 255, 0.95);
}

.submodal-layer {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 1100;
  width: 100%;
  height: 100%;
  background-color: rgba(255, 255, 255, 1);
}
</style>