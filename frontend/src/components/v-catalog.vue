<template>
  <div class="v-catalog">
    <router-link :to="{name: 'cart', params:{cart_data: CART}}">
      <div class="v-catalog__link_to_cart">Cart: {{CART.length}}</div>
    </router-link>
    <h1>Catalog</h1>
    <div class="v-catalog__list">
      <v-catalog-item
        v-for="fish in PRODUCTS"
        :key="fish.id"
        v-bind:product_data="fish"
        @addToCart="addToCart"
      />
    </div>
  </div>
</template>

<script>
  import vCatalogItem from './v-catalog-item'
  import {mapActions, mapGetters} from 'vuex'
  export default {
    name: 'v-catalog',
    components: {
      vCatalogItem,
    },
    props: {},
    computed:
      {
        ...mapGetters([
          'PRODUCTS',
          'CART'
        ])
      },
    methods:
      {
      addToCart(data)
      {
        this.ADD_TO_CART(data)
      },
        ...mapActions([
          'GET_PRODUCTS',
          'ADD_TO_CART'
        ]),
      },
    data(){
      return{}
    },
    mounted() {
      this.GET_PRODUCTS()
   },
  }

</script>

<style lang="scss">
  @import "../assets/styles/styles.scss";
  .v-catalog {
    &__list {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
    }
    &__link_to_cart{
      position: absolute;
      top:10px;
      right: 10px;
      padding: $padding*2;
      border: solid 1px #aeaeae;
    }
  }
</style>
