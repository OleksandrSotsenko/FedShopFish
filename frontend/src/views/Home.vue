<template>
  <section class="container">
    <redirectButton pathname="catalog"></redirectButton>
  </section>
</template>
<script>
  import redirectButton from './../components/redirect'
  export default {
    components: {
      redirectButton
    }
  }
</script>
<style scoped lang="sass">
  @import './../assets/styles/colors'
  @import './../assets/styles/global'
  .container
    h1
      color: black
</style>
