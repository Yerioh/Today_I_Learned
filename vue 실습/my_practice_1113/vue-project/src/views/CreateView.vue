<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <div>
        <label for="title">제목 : </label>
        <input type="text" id="title" v-model,trim="title">
      </div>
      <div>
        <label for="content">내용 : </label>
        <textarea id="content" v-model.trim="content"></textarea>
      </div>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const store = useCounterStore()

const title = ref('')
const content = ref('')

const createArticle = function() {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/`,
    data: {
      title: title.value,
      content: content.value
    }
  })
    .then((res) => {
      console.log('게시글 작성 성공')
      router.push({name: 'ArticleView'})
      title.value = ''
      content.value = ''
    })
    .catch((err) => {
      console.error(err)
    })
}

</script>

<style>

</style>
