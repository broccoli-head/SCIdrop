<template>
<div class="centeredBox">
    <h1 class="boldTitle orange">LOGIN</h1>
    <form class="login" @submit.prevent="handleLogin">
        <div class="field">
            <label for="username">Username:</label>
            <input v-model="username" type="text" autocomplete="username" required/>
        </div>

        <div class="field">
            <label for="password">Password:</label>
            <input v-model="password" type="password" autocomplete="current-password" required/>
        </div>

        <div class="rememberMe">
            <input type="checkbox" name="rememberMe" checked>
            <label>Remember me</label><br>
        </div>
        
        <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
        
        <button type="submit" :disabled="loading">
            {{ loading ? 'Logging in...' : 'Log in' }}
        </button>

        <p>Don't have an account?<br>
            <router-link :to="/register/">Register here</router-link>
        </p>
    </form>
</div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'Login',
    data() {
        return {
            username: '',
            password: '',
            loading: false,
            errorMessage: '',
        };
    },
    methods: {
        async handleLogin() {
            this.errorMessage = '';
            this.loading = true;

            try {
                const response = await axios.post('http://localhost:8000/api/login/', {
                    username: this.username,
                    password: this.password,
                });

                const token = response.data.token;
                localStorage.setItem('authToken', token);
                this.$router.push('/');

            } catch (error) {
                if (error.response && error.response.data) {
                    this.errorMessage = error.response.data.detail || 'Login failed.';
                } else {
                    this.errorMessage = 'Network or server error.';
                }
            } finally {
                this.loading = false;
            }
        },
    },
};
</script>

<style>
    @import '@/assets/styles/form.css';
</style>