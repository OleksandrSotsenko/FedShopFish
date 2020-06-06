<template>
  <div id="app">
    <Myheader></Myheader>
    <h1>Fish Shop</h1>
    <router-view></router-view>
    <h2>Fish Catalog</h2>
    <Myfooter></Myfooter>
    <vMainWrapper></vMainWrapper>
  </div>
</template>

<script>
import Myheader from './components/Myheader.vue'
import Myfooter from './components/Myfooter.vue'
import vMainWrapper from './components/v-main-wrapper'

export default {
  components:
    {
      vMainWrapper,
      Myheader,
      Myfooter,
    },
  name: 'app',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  width: 100%;
  height: 100%;
  color: #2c3e50;
  position: fixed;
  top: 0;
  left: 0;
  border-bottom: 2px solid black;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}

</style>
