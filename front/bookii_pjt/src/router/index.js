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
  { path: '/search/tag/:tag', name: 'tag-search', component: TagSearchView },
  { path: '/profile/:username', name: 'profile', component: ProfileView },

  // modal 라우트
  {
    path: '/signup',
    name: 'signup',
    component: SignUpView,
    meta: { isModal: true }
  },
  {
    path: '/login',
    name: 'login',
    component: LogInView,
    meta: { isModal: true }
  },
  {
    path: '/profile/:username/edit',
    name: 'profile-edit',
    component: ProfileView,
    meta: { isModal: true }
  },
  {
    path: '/thread/:id',
    name: 'thread-detail',
    component: ThreadDetailView,
    meta: { isModal: true }
  },
  {
    path: '/thread/create',
    name: 'thread-create',
    component: ThreadCreateView,
    meta: { isModal: true }
  },
  {
    path: '/thread/:id/edit',
    name: 'thread-edit',
    component: ThreadUpdateView,
    meta: { isModal: true, isSubModal: true }
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router

// const router = createRouter({
//   history: createWebHistory(import.meta.env.BASE_URL),
//   routes: [
//     // 1. home 라우팅
//     {
//       path: '/',
//       name: 'home',
//       component: HomeView,
//     },
//     // 2. signup 라우팅(modal)
//     {
//       path: '/signup',
//       name: 'signup',
//       component: {
//         default: HomeView,
//         modal: SignUpView,
//       },
//     },
//     // 3. login 라우팅(modal)
//     {
//       path: '/login',
//       name: 'login',
//       component: {
//         default: HomeView
//       }
//     },
//     // 4. profile 라우팅
//     {
//       path: '/profile/:username',
//       name: 'profile',
//       component: ProfileView,
//     },
//     // 5. profile 수정 라우팅(modal)
//     {
//       path: '/profile/:username/edit',
//       name: 'profile-edit',
//       component: ProfileUpdateView,
//     },
//     // 6. book-detail 라우팅
//     {
//       path: '/book/:bookId',
//       name: 'book-detail',
//       component: BookDetailView,
//     },
//     // 7. search 라우팅
//     {
//       path: '/search',
//       name: 'search',
//       component: SearchView,
//     },
//     // 8. tag-search 라우팅
//     {
//       path: '/search/tag/:tag',
//       name: 'tag-search',
//       component: TagSearchView,
//     },
//     // 9. thread-detail 라우팅(modal)
//     {
//       path: '/thread/:id',
//       name: 'thread-detail',
//       component: ThreadDetailView,
//     },
//     // 10. thread 생성 라우팅(modal)
//     {
//       path: '/thread/create',
//       name: 'thread-create',
//       component: ThreadCreateView,
//     },
//     // 11. thread 수정 라우팅(modal-modal)
//     {
//       path: '/thread/:id/edit',
//       name: 'thread-edit',
//       component: ThreadUpdateView,
//     },

//   ],
// })
