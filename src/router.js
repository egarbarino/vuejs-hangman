import Vue from 'vue'
import Router from 'vue-router'
import Game from './views/Game.vue'
import HighScore from './views/Help.vue'

Vue.use(Router)

export default new Router({
  mode: 'hash',
  base: process.env.BASE_URL,
  linkExactActiveClass: 'active',
  routes: [
    {
      path: '/',
      name: 'game',
      component: Game 
    },
    {
      path: '/help',
      name: 'help',
      component: HighScore 
    },
   ]
})