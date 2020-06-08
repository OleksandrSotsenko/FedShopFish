import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './assets/styles/styles.scss'
import store from './vuex/store'

Vue.config.productionTip = false;

new Vue({
  el: '#app',
  template: '<App/>',
  components:
    {
      'app': App
    },
  render: h => h(App),
  store,
  router
});

