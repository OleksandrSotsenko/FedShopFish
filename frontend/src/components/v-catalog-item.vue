<template>
  <div class="v-catalog-item">
    <img src="" alt="img">
    <p class="v-catalog-item_name">{{product_data.name}}</p>
    <p class="v-catalog-item_price">Price: {{product_data.price}}</p>
    <button class="v-catalog-item_add_to_cart_btn btn">Add to cart</button>
  </div>
</template>


<script>
  export default {
    name: 'v-catalog-item',
    props: {
      product_data:{
        type: Object,
        default()
        {
          return{}
        }
      }
    },
    data(){
      return{
      }
    },
    computed: {},
  }
</script>

<style lang="scss">
  @import "../assets/styles/styles.scss";
  .v-catalog-item{
    flex-basis: 25%;
    box-shadow: 0 0 8px 0 #e0e0e0;
    padding: $padding*2;
    margin-bottom: $margin*2;
  }
</style>
