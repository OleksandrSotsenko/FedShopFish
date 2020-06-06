<template>
  <header>
    <div id="logo">FISH SHOP</div>
    <nav>
      <ul>
        <router-link tag='li' :to="{ name: 'home'}">
          <a>Home</a>
        </router-link>
        <router-link tag='li' :to="{ name: 'catalog'}">
          <a>Catalog</a>
        </router-link>
      </ul>
    </nav>
  </header>
</template>

<script>
export default{
  data () {
    return {
    }
  }
}
</script>
<style scoped lang="sass">
@import './../assets/styles/colors'
header
    display: flex
    width: 100%
    justify-content: space-around
    align-items: center
    background-color: rgba(0, 99, 230, 0.8)
    border-bottom: 2px solid darken(green, 30%)
    color: white
    div#logo
      font-size: 200%
      width: 33%
    nav
      flex-grow: 2
      ul
        padding: 0
        display: flex
        justify-content: space-around
        list-style: none
        a
          text-decoration: none
          color: white
</style>
