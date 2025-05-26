// ui.is

import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useUIStore = defineStore('ui', () => {
  const backgroundRoute = ref(null)

  const setBackgroundRoute = (route) => {
    backgroundRoute.value = route
  }

  const searchText = ref('')

  return {
    backgroundRoute,
    setBackgroundRoute,
    searchText,
  }
})