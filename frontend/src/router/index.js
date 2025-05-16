import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/components/Home.vue'
import Login from '@/components/Login.vue'
import Roulette from '@/components/Roulette.vue'

const routes = [
  {
    path: '/',
    component: Home,
    meta: { title: 'SCIdrop - Home' }
  },
  {
    path: '/login',
    component: Login,
    meta: { title: 'Log in to SCIdrop' }
  },
  {
    path: '/chest/:id',
    component: Roulette,
    meta: { title: 'SCIdrop - open the chest' }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  document.title = to.meta.title || 'SCIdrop'
  next()
})

export default router