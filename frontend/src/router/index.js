import Vue from 'vue'
import Router from 'vue-router'
import vCart from '../components/v-cart.vue'
import vCatalog from '../components/v-catalog'

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'catalog',
      component: vCatalog
    },
    {
      path: '/cart',
      name: 'cart',
      component: vCart,
      props: true
    }
    ]
})

