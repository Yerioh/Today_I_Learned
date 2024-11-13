import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const article = ref([])
  const API_URL = 'http://localhost:8000'

  const getArticles = function() {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`
    })
      .then((res) => {
        // console.log(res.data)
        article.value = res.data
      })
      .catch((err) => {
        console.error(err)
      })
  }

  return { article, API_URL, getArticles }
}, { persist: true })
