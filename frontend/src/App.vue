<template>
  <div id="app">
    <h1>Fish Shop</h1>
    <h2>Fish Catalog</h2>
    <vMainWrapper></vMainWrapper>
  </div>
</template>

<script>
import vMainWrapper from './components/v-main-wrapper'

export default {
  components:
    {
      vMainWrapper,
    },
  name: 'app',
  data () {
    return {
      fishes: [],
    }
  },
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
