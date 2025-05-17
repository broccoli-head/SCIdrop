import { createRouter, createWebHistory } from 'vue-router'

import Home from '@/components/Home.vue'
import Login from '@/components/Login.vue'
import Register from '@/components/Register.vue'
import Roulette from '@/components/Roulette.vue'

import homeBg from '@/assets/images/home_background.png'
import loginBg from '@/assets/images/login_background.png'
import rouletteBg from '@/assets/images/roulette_background.png'


const routes = [
{
	path: '/',
	component: Home,
	meta: {
		title: 'SCIdrop - Home',
		background: homeBg
	}
},
{
	path: '/login',
	component: Login,
	meta: {
		title: 'Log in to SCIdrop',
		background: loginBg
	}
},
{
	path: '/register',
	component: Register,
	meta: {
		title: 'Sign up for SCIdrop',
		background: loginBg
	}
},
{
	path: '/chest/:id',
	component: Roulette,
	meta: {
		title: 'SCIdrop - Chest opening',
		background: rouletteBg
	}
}
]

const router = createRouter({
	history: createWebHistory(),
	routes
})

router.beforeEach((to, from, next) => {
	//changes website title per page
	document.title = to.meta.title || 'SCIdrop'

	//changes body background per page
	const background = to.meta.background
	if (background) {
		document.body.style.backgroundImage = `url('${background}')`
	}

	next()
})

export default router