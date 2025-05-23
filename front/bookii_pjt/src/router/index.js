import { createRouter, createWebHistory } from 'vue-router'
// View파일 import
// Home
import HomeView from '@/views/HomeView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
// Profile
import ProfileView from '@/views/ProfileView.vue'
import ProfileUpdateView from '@/views/ProfileUpdateView.vue'
// Book
import BookDetailView from '@/views/BookDetailView.vue'
import SearchView from '@/views/SearchView.vue'
import TagSearchView from '@/views/TagSearchView.vue'
// Thread
import ThreadDetailView from '@/views/ThreadDetailView.vue'
import ThreadCreateView from '@/views/ThreadCreateView.vue'
import ThreadUpdateView from '@/views/ThreadUpdateView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // 1. home 라우팅
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    // 2. signup 라우팅
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView,
    },
    // 3. login 라우팅
    {
      path: '/login',
      name: 'login',
      component: LogInView,
    },
    // 4. profile 라우팅
    {
      path: '/profile/:username',
      name: 'profile',
      component: ProfileView,
    },
    // 5. profile 수정 라우팅
    {
      path: '/profile/:username/edit',
      name: 'profile-edit',
      component: ProfileUpdateView,
    },
    // 6. book-detail 라우팅
    {
      path: '/book/:bookId',
      name: 'book-detail',
      component: BookDetailView,
    },
    // 7. search 라우팅
    {
      path: '/search',
      name: 'search',
      component: SearchView,
    },
    // 8. tag-search 라우팅
    {
      path: '/search/tag/:tag',
      name: 'tag-search',
      component: TagSearchView,
    },
    // 9. thread-detail 라우팅
    {
      path: '/thread/:id',
      name: 'thread-detail',
      component: ThreadDetailView,
    },
    // 10. thread 생성 라우팅
    {
      path: '/thread/create',
      name: 'thread-create',
      component: ThreadCreateView,
    },
    // 11. thread 수정 라우팅
    {
      path: '/thread/:id/edit',
      name: 'thread-edit',
      component: ThreadUpdateView,
    },

  ],
})

export default router
