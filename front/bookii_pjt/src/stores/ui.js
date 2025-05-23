import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useUIStore = defineStore('ui', () => {
  const backgroundRoute = ref(null)

  const setBackgroundRoute = (route) => {
    backgroundRoute.value = route
  }

  return { backgroundRoute, setBackgroundRoute }
})