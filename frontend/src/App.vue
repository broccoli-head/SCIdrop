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

	<router-link to="/login">
		<button>Log in</button>
	</router-link>

	<router-link to="/register">
		<button>Sign up</button>
	</router-link>

	<button @click="handleLogout">Log out</button>
</nav>

<main>
    <router-view />
</main>
</template>

<script>
import axios from 'axios';

export default {
    name: 'App',
    methods: {
        async handleLogout() {
            try {
                await axios.post('http://localhost:8000/api/logout/');
                this.$router.push('/login');
            } catch (error) {
                console.error('Logout failed: ', error);
            }
        }
    }
}
</script>

<style>
	@import "@/assets/styles/base.css";
</style>