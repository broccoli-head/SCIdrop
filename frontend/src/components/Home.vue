<template>
    <div v-if="chests.length == 0">
        <h1>Currently, there are no chests to buy.</h1>
    </div>

    <div v-else id="chestList" class="scrollY">
        <div v-for="chest in chests" :key="chest.id">
            <router-link class="chestBox" :to="`/chest/${chest.id}`">
                <h2>{{ chest.name }}</h2>
                <img :src="chest.cover ? chest.cover : '@/assets/icons/chest.svg'" />

                <p class="rarity" :class="chest.rarity">{{ chest.rarity }}</p>
                <p class="price">{{ chest.price }} ZŁ</p> 
            </router-link>
        </div>
    </div>
</template>

<script>
import { refreshBalance } from '@/utils.js';

export default {
    data() {
        return {
            chests: []
        }
    },
    mounted() {
        this.loadChests();
		refreshBalance(this);
    },

    methods: {
        async loadChests() {
            try {
                //gets chests from the backend
                const url = import.meta.env.VITE_API_BASE_URL;
                const response = await fetch(`${url}/api/chests/`);
                const data = await response.json();
                this.chests = data;
            } catch (err) {
                console.error('Failed to fetch chests: ', err);
            }
        }
    }  
}
</script>

<style>
    @import '@/assets/styles/home.css';
</style>