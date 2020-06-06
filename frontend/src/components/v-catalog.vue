<template>
  <div class="v-catalog">
    <h1>Catalog</h1>
    <v-catalog-item v-for="product in products"
    :key="products.id"
     v-bind:product_data="product"
    />
  </div>
</template>

<script>
  import vCatalogItem from './v-catalog-item'
  export default {
    name: 'v-catalog',
    components: {
      vCatalogItem,
    },
    props: {},
    data(){
      return{
        products:
        [
          {
            image: "trr.jpg",
            name: "Fish 1",
            price: "10",
            id: "1",
          },
          {
            image: "rtrw.jpg",
            name: "Fish 2",
            price: "12",
            id: "2",
          },
          {
            image: "erq.jpg",
            name: "Fish 3",
            price: "7",
            id: "3",
          }
        ]
      }
    },

  }
</script>

<style lang="scss">
  .v-catalog {
    &__list {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
    }
  }
</style>
