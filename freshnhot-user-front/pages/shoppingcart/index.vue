<template>
  <div>
  <h1>shopping cart</h1>
  <p>{{ cartList }}</p>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  computed: {
    ...mapGetters({
      cartList: "shoppingCart/getList"
    })
  }
}
</script>

<style scoped>

</style>
