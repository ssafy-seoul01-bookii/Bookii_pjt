<template>
  <form @submit.prevent="handleSubmit" class="form-container">
    <!-- 프로필 이미지 미리보기 + 사용자명 -->
    <div class="profile-box">
      <img :src="form.profile_img_url" class="profile-img" />
      <div class="profile-meta">
        <p class="username">{{ form.username }}</p>
        <p class="label">프로필 사진 변경은 이미지 URL을 붙여넣어 주세요.</p>
      </div>
    </div>

    <!-- 이미지 URL 입력 -->
    <div class="form-group">
      <label>프로필 이미지 URL</label>
      <input v-model="form.profile_img_url" type="text" placeholder="https://..." />
    </div>

    <!-- 나이 -->
    <div class="form-group">
      <label>나이</label>
      <input v-model.number="form.age" type="number" min="0" />
    </div>

    <!-- 비평가 여부 -->
    <div class="form-group switch-group">
      <label for="is_critic">비평가 여부</label>
      <input id="is_critic" type="checkbox" v-model="form.is_critic" />
    </div>

    <!-- 연간 독서량 -->
    <div class="form-group">
      <label>연간 독서량 (권)</label>
      <input v-model.number="form.annual_reading_amount" type="number" />
    </div>

    <!-- 주간 평균 독서시간 -->
    <div class="form-group">
      <label>주간 평균 독서 시간 (시간)</label>
      <input v-model.number="form.weekly_avg_reading_time" type="number" step="0.1" />
    </div>

    <!-- 저장 버튼 -->
    <div class="form-group">
      <button type="submit" class="submit-btn">저장</button>
    </div>
  </form>
</template>

<script setup>
import { ref, watch } from 'vue'

const props = defineProps({ user: Object })
const emit = defineEmits(['submit'])

const form = ref({ ...props.user })

watch(() => props.user, (newVal) => {
  form.value = { ...newVal }
})

const handleSubmit = () => {
  emit('submit', { ...form.value })
}
</script>

<style scoped>
.form-container {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  padding: 2rem;
  max-width: 500px;
  margin: 0 auto;
  background-color: #fff;
  border-radius: 12px;
}

.profile-box {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.profile-img {
  width: 72px;
  height: 72px;
  border-radius: 50%;
  object-fit: cover;
  border: 1px solid #ccc;
}

.profile-meta .username {
  font-weight: bold;
  font-size: 1.2rem;
}

.profile-meta .label {
  font-size: 0.85rem;
  color: #888;
}

.form-group {
  display: flex;
  flex-direction: column;
}

.form-group label {
  margin-bottom: 0.5rem;
  font-weight: 500;
}

input[type='text'],
input[type='number'] {
  padding: 0.6rem;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-size: 0.95rem;
}

.switch-group {
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}

.submit-btn {
  padding: 0.8rem;
  background-color: #a2ace2;
  color: white;
  font-weight: bold;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}
</style>