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
		<button>Login</button>
	</router-link>

	<router-link to="/register">
		<button>Sign up</button>
	</router-link>
</nav>

<main>
    <router-view />
</main>
</template>

<style>
	@import "@/assets/styles/base.css";
</style>