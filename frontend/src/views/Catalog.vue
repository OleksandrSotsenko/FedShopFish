<template>
  <section class="container">
    <h1> Catalog. FishShop </h1>
    <p>Welcome on an another page.</p>
<!--    <img src="https://i.imgur.com/gdWIxn2.jpg" alt="shop"/>-->
      <div class="wrap">
        <h1 class="site-title">Fshop</h1>
      </div>
      <div class="main">
        <div class="wrap">
          <div class=".good-min-cart">
            <h3>{{name-goods}}}</h3>
<!--            <img src="{{img_path}}" alt="">-->
            <p>Price: {{price_goods}}</p>
          </div>
        </div>
      </div>
  </section>
</template>
<script>
  export default {
    data () {
      return {}
    }
  }
</script>
<style scoped lang="sass">
  @import './../assets/styles/colors'
  @import './../assets/styles/global'
  @import './../assets/styles/catalog.css'
  .container
    h1
      color: green
    p
      margin: 0
      color: lighten(green, 10%)
    img
      width: 100px
      height: 100px
  .catalog-panel
    h1
      color: black

</style>
