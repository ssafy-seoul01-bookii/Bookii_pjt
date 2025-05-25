<!-- HomeView.vue -->

<template>
  <div>
    <!-- Main -->
    <div>

    </div>
    <Footer1/>

    <!-- 로그인여부 따라 분기 -->
     <!-- 로그인o-->
     <template v-if="isLoggedIn">
      <div>
        <h3>키워드 추천 책</h3>
        <BookList :books="book.books"/>
      </div>
      <div>
        <h3>클릭 기반 추천 책</h3>
        <BookList :books="book.books"/>
      </div>
      <div>
        <h3>좋아요 순 정렬 쓰레드</h3>
        <BookList :books="book.books"/>
      </div>
     </template>

     <template v-else> 
      <!-- 로그인x -->
      <div>
        <h3>평론가 3.0 이상 책</h3>
        <BookList :books="book.books"/>
      </div>
      <div>
        <h3>쓰레드 많은 순 정렬 책</h3>
        <BookList :books="book.books"/>
      </div>
      <div>
        <!-- <h3>평점 3.5 이상 정렬 책</h3>
        <BookList :books="book.books"/> -->
        <!-- 쓰레드 테스트용 -->
        <h3>쓰레드 테스트</h3>
        <ThreadList :threads="thread.threads"/>
      </div>
     </template>

    <Footer2/>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useUIStore } from '@/stores/ui'
import { useUserStore } from '@/stores/user'
import { useBookStore } from '@/stores/book'
import { useThreadStore } from '@/stores/thread'

import Footer1 from '@/components/layout/footer1.vue'
import Footer2 from '@/components/layout/footer2.vue'
import BookList from '@/components/book/BookList.vue'
import ThreadList from '@/components/thread/ThreadList.vue'

const router = useRouter()
const route = useRoute()
const user = useUserStore()
const ui = useUIStore()
const book = useBookStore()
const thread = useThreadStore()

// 로그인여부 판단
const isLoggedIn = computed(() => !!user.accessToken)

const goToLogin = () => {
  ui.setBackgroundRoute(route.fullPath)
  router.push('/login')
}
</script>

<style lang="scss" scoped>

</style>