<template>
<div class="centeredBox">
    <h1 class="boldTitle orange">LOGIN</h1>
    <form @submit.prevent="handleLogin">
        <div id="loginForm">
            <div class="field">
                <label for="username">Username:</label>
                <input v-model="username" type="text" autocomplete="username" required/>
            </div>

            <div class="field">
                <label for="password">Password:</label>
                <input v-model="password" type="password" autocomplete="current-password" required/>
            </div>
        </div>
        <div class="check">
            <input id="rememberMe" type="checkbox" name="rememberMe" checked>
            <label for="rememberMe">Remember me</label><br>
        </div>
        
        <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
        
        <button type="submit" :disabled="loading">
            {{ loading ? 'Logging in...' : 'Log in' }}
        </button>

        <p>Don't have an account?<br>
            <router-link to="/register">Register here</router-link>
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
                await axios.post('http://localhost:8000/api/login/', {
                    username: this.username,
                    password: this.password,
                }, {
                    withCredentials: true
                });

                const userResponse = await axios.get('http://localhost:8000/api/userInfo/', {
                    withCredentials: true
                });

                if(userResponse.data.username) {
                    localStorage.setItem('isLoggedIn', 'true');
                    localStorage.setItem('username', this.username);
                    this.$router.push('/');
                }
                else {
                    this.errorMessage = "Login failed.";
                }

            } catch (error) {
                if (error.response.data) {
                    this.errorMessage = error.response.data.message || 'Login failed.';
                }
                else {
                    this.errorMessage = 'Connection error occured.';
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