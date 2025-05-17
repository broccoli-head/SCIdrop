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

    <p v-if="isLoggedIn">Logged as <span class="orange">{{ username }}</span></p>
	
	<template v-if="!isLoggedIn">
		<router-link to="/login">
			<button>Log in</button>
		</router-link>

		<router-link to="/register">
			<button>Sign up</button>
		</router-link>
	</template>

	<template v-else>
		<button @click="handleLogout">Log out</button>
	</template>
	
</nav>

<main>
    <router-view />
</main>
</template>

<script>
import axios from 'axios';

export default {
    name: 'App',
	data()  {
		return {
			isLoggedIn: false,
			username: ''
		};
	},
	mounted() {
		this.checkLogin();
	},
    methods: {
		//checks login status and returns username
		checkLogin() {
			this.isLoggedIn = localStorage.getItem('isLoggedIn')  == 'true';
			this.username = localStorage.getItem('username') || '';
		},
        async handleLogout() {
            try {
				//gets csrf token required in login and register forms
				const csrfResponse = await axios.get(
					'http://localhost:8000/api/getCSRF/',
					{ withCredentials: true }
				);

				//logout request
                await axios.post(
					'http://localhost:8000/api/logout/',
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