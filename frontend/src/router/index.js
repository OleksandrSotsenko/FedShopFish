import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home'
import Catalog from '../views/Catalog'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/catalog',
      name: 'catalog',
      component: Catalog
    }
  ]
})
