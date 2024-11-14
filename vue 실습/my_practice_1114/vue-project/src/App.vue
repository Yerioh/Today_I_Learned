<template>
  <header>
    <nav>
      <RouterLink :to="{ name: 'ArticleView' }">Articles</RouterLink>
      <span> | </span>
      <RouterLink :to="{ name: 'SignUpView' }">Sign Up</RouterLink>
      <span> | </span>
      <RouterLink :to="{ name: 'LogInView' }">Log In</RouterLink>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
</script>

<style scoped>
</style>
