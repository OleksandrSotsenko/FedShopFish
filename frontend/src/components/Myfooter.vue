<template>
  <footer>
    <p>Thank you for choosing our online store.</p>
    <div id="sitemaps">
      <h5>Sitemap</h5>
      <ul>
        <router-link tag='li' :to="{ name: 'home'}">
          <a>Home</a>
        </router-link>
        <router-link tag='li' :to="{ name: 'catalog'}">
          <a>Catalog</a>
        </router-link>
      </ul>
    </div>
  </footer>
</template>
<script>
export default
{
  data () {
    return {
}
  }
}
</script>

<style scoped lang="sass">
@import './../assets/styles/colors'
footer
  position: fixed
  left: 0
  bottom: 0
  width: 100%
  background-color: #808080
  color: black
  text-align: center
  border-top: 2px solid darken(green, 20%)
  ul
    padding: 0
    display: flex
    justify-content: space-around
    list-style: none
    a
      text-decoration: none
      color: white
      vertical-align: center
</style>
