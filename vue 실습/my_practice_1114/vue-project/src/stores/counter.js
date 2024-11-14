import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  const router = useRouter()
  // state
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)


  // getters
  const isLogin = computed(() => {
    if(token.value === null) {
      return false
    } else {
      return true
    }
  })

  // actions

  // DRF로 전체 게시글 요청을 보내고 응답을 받아 articles에 저장하는 함수
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) => {
        // console.log(res.data)
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }
  // 회원가입 요청 액션
  const signUp = function(payload) {
    const { username, password1, password2 } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2
      }
    }).then((res) => {
      const password = password1
      logIn({ username, password })
    }).catch((err) => {
      console.log(err)
    })
  }
  // 로그인 요청 액션
  const logIn = function(payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    }).then((res) => {
      // console.log(res)
      token.value = res.data.key
      router.push({ name: 'ArticleView'})
    }).catch((err) => {
      console.log(err)
    })
  }

  return { articles, API_URL, getArticles, signUp, logIn, token, isLogin }
}, { persist: true })
