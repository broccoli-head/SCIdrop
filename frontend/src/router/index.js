import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/components/Home.vue'
import Login from '@/components/Login.vue'

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