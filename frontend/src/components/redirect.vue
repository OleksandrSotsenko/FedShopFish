<template>
  <button type="button" @click="goTo">to Shop</button>
</template>
<script>
export default {
  props:{
    pathname: {
      type: String,
      required: true
    }
  },
  methods: {
    goTo() {
      this.$router.push({name: this.pathname})
    }
  }
}
</script>
<style scoped lang="sass">
  @import './../assets/styles/colors.css'
  button
    background-color: transparent
    color: green
    padding: 18px 48px
    border: 2px solid green
    border-radius: 5px
    text-transform: uppercase
    &:hover
      background-color: green
      color: white
      border-color: white
</style>
