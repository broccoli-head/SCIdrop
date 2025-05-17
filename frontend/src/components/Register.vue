<template>
<div class="centeredBox register">
    <h1 class="boldTitle orange">SIGN UP</h1>
    <form @submit.prevent="handleRegister">
        <div id="loginForm">
            <div class="field">
                <label for="username">Username:</label>
                <input v-model="username" id="username" type="text" autocomplete="username" required/>
            </div>
            <div class="field">
                <label for="email">E-mail:</label>
                <input v-model="email" id="email" type="email" autocomplete="email" required/>
            </div>

            <div class="field">
                <label for="password">Password:</label>
                <input v-model="password" id="password" type="password" autocomplete="current-password" required/>
            </div>
        </div>
        <div class="check smallCheck">
            <input id="over18" v-model="over18" type="checkbox" name="over18">
            <label for="over18">I'm over 18 years old</label><br>
        </div>
        <div class="check smallCheck">
            <input id="rulesAgreement" v-model="rulesAgreement" type="checkbox" name="rulesAgreement">
            <label for="rulesAgreement">I agree to the Terms of Service and Privacy Policy</label><br>
        </div>
        
        <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
        
        <button type="submit" :disabled="loading || !username || !email || !password || !over18 || !rulesAgreement" >
            {{ loading ? 'Signing up...' : 'Sign up' }}
        </button>

        <p>If you have already an account, <br>you can
            <router-link to="/login">log in here</router-link>.
        </p>
    </form>
</div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'Register',
    data() {
        return {
            username: '',
            email: '',
            password: '',
            over18: false,
            rulesAgreement: false,
            loading: false,
            errorMessage: '',
        };
    },
    methods: {
        async handleRegister() {
            this.loading = true;

            if (!this.over18) {
                this.errorMessage = 'You have to be above 18 years old!';
                this.loading = false;
                return;
            }
            if (!this.rulesAgreement) {
                this.errorMessage = 'You have to agree to the rules!';
                this.loading = false;
                return;
            }
   
            try {
                const response = await axios.post('http://localhost:8000/api/register/', {
                    username: this.username,
                    email: this.email,
                    password: this.password,
                });

                localStorage.setItem('isLoggedIn', 'true');
                localStorage.setItem('username', this.username);

            } catch (error) {
                if (error.response && error.response.data) {
                    this.errorMessage = error.response.data.message || 'Sign up failed.';
                } else {
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