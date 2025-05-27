// comment.js

import { defineStore } from 'pinia'
import { ref } from 'vue'
import api from '@/lib/axios'

export const useCommentStore = defineStore('comment', () => {
  const comments = ref([])

  const fetchComments = async (threadId, bookId) => {
    try {
      const res = await api.get(`/books/${bookId}/threads/${threadId}/comments/`)
      comments.value = res.data
    } catch (err) {
      console.error(`댓글 불러오기 실패 (책 ${bookId}, 쓰레드 ${threadId}):`, err)
    }
  }
  
  const deleteCommentById = (id) => {
    comments.value = comments.value.filter(c => c.id !== id)
  }

  const addComment = ({ thread_id, user_id, content }) => {
    const newId = comments.value.length + 1
    const now = new Date().toISOString().slice(0, 10)
    comments.value.push({
      id: newId,
      thread_id,
      user_id,
      content,
      created_at: now,
      updated_at: now
    })
  }


  return {
    comments,
    fetchComments,
    deleteCommentById,
    addComment,
  }
})