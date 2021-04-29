<template>
  <div>
    <h1 v-if="error.statusCode">Page not found</h1>
    <div v-else><h1>Error {{error.statusCode}}</h1><h2>{{error.message}}</h2></div>
    <NuxtLink to="/">Go back</NuxtLink>
  </div>
</template>

<script>
export default {
  name: "error",
  props: ['error'],
  layout: 'error'
}
</script>

<style scoped>

</style>
