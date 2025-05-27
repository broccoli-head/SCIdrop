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
            this.loading = true;

            try {
                const url = import.meta.env.VITE_API_BASE_URL;
                
                //gets csrf token required in login verification
                const csrfResponse = await axios.get(
					`${url}/api/getCSRF/`,
					{ withCredentials: true }
				);

                //sends login request to the server
                await axios.post(`${url}/api/login/`,
                {
                    username: this.username,
                    password: this.password,
                }, {
                    //needed for django csrf protecion
                    withCredentials: true,
                    headers: {
                        'X-CSRFToken': csrfResponse.data.CSRFToken
                    }
                });

                //gets user info (username)
                const userResponse = await axios.get(
                    `${url}/api/userInfo/`,
                    { withCredentials: true }
                );

                //if user is logged in, sets in the session their username
                if(userResponse.data.username) {
                    localStorage.setItem('isLoggedIn', 'true');
                    localStorage.setItem('username', this.username);
                    //redirects user to the home page
                    this.$router.push('/');
                }
                else {
                    this.errorMessage = "Login failed.";
                }

            }
            catch (error) {
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