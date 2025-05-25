// index.js

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

const routes = [
  // 일반 page 라우트
  { path: '/', name: 'home', component: HomeView },
  { path: '/book/:bookId', name: 'book-detail', component: BookDetailView },
  { path: '/search', name: 'search', component: SearchView },
  // tag필수 해제
  { path: '/search/tag/:tag?', name: 'tag-search', component: TagSearchView },
  { path: '/profile/:username', name: 'profile', component: ProfileView },

  // modal 라우트
  {
    path: '/signup',
    name: 'signup',
    component: SignUpView,
    meta: { 
      isModal: true,
      modalClass: 'modal-narrow'
    }
  },
  {
    path: '/login',
    name: 'login',
    component: LogInView,
    meta: { 
      isModal: true,
      modalClass: 'modal-narrow'
    }
  },
  {
    path: '/profile/:username/edit',
    name: 'profile-edit',
    component: ProfileUpdateView,
    meta: {
      isModal: true,
      background: 'profile',
      modalClass: 'modal-medium'
    }
  },
  {
    path: '/thread/:id',
    name: 'thread-detail',
    component: ThreadDetailView,
    meta: {
      isModal: true,
      modalClass: 'modal-wide'
    }
  },
  {
    path: '/thread/create',
    name: 'thread-create',
    component: ThreadCreateView,
    meta: {
      isModal: true,
      modalClass: 'modal-medium'
    }
  },
  {
    path: '/thread/:id/edit',
    name: 'thread-edit',
    component: ThreadUpdateView,
    meta: {
      isModal: true,
      isSubModal: true,
      background: 'thread-detail',
      modalClass: 'modal-medium'
    }
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router