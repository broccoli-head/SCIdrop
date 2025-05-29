<script setup>
	import { global } from '@/store.js'
</script>

<template>
	<nav>
		<div class="logo">
			<img src="@/assets/icons/gift.svg">
			<h1 class="boldTitle">
				<router-link to="/">
					<span class="orange">sci</span><span class="white">drop</span>
				</router-link>        
			</h1>
		</div>
		
		<template v-if="!isLoggedIn">
			<router-link to="/login">
				<button>Log in</button>
			</router-link>

			<router-link to="/register">
				<button>Sign up</button>
			</router-link>
		</template>

		<template v-else>
			<p>Logged as <span class="orange">{{ username }}</span></p>
			<p>Your balance: <span class="orange">{{ global.balance }}</span></p>
			
			<router-link to="/inventory">
				<button>Inventory</button>
			</router-link>

			<button @click="handleLogout">Log out</button>
		</template>
		
	</nav>

	<main>
		<transition name="fade" mode="out-in">
			<router-view />
		</transition>
	</main>
</template>

<script>
import axios from 'axios';
import { refreshBalance } from '@/utils.js';

export default {
    name: 'App',
	data()  {
		return {
			isLoggedIn: false,
			username: '',
			balance: '0.00 PLN'
		};
	},
	mounted() {
		this.checkLogin();
		refreshBalance(this);
	},

    methods: {
		//checks login status and returns username
		checkLogin() {
			this.isLoggedIn = localStorage.getItem('isLoggedIn')  == 'true';
			this.username = localStorage.getItem('username') || '';
		},

        async handleLogout() {
            try {
				const url = import.meta.env.VITE_API_BASE_URL;

				//gets csrf token required to logout
				const csrfResponse = await axios.get(
					`${url}/api/getCSRF/`,
					{ withCredentials: true }
				);

				//logout request
                await axios.post(
					`${url}/api/logout/`,
					{ },
					{
						withCredentials: true,
						headers: {
							'X-CSRFToken': csrfResponse.data.CSRFToken
						}
					}
				);
				
				//delete user from session
				localStorage.removeItem('isLoggedIn');
				localStorage.removeItem('username');
				this.isLoggedIn = false;
				this.username = '';
				//redirects user to login page
                this.$router.push('/login');	
            }
			catch (error) {
                console.error('Logout failed: ', error);
            }
        }
    },
	watch: {
		//checks if user is still logged in even while changing pages
		'$route'() {
			this.checkLogin();
		}
	}
}
</script>

<style>
	@import "@/assets/styles/base.css";
</style>