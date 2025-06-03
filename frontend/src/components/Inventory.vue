<template>
    <div v-if="items.length == 0">
        <h1>You don't have any items yet. Gamble to earn some!</h1>
    </div>

    <div v-else class="scrollY">
        <h1 id="ownedTitle">Owned skins:</h1>
        <div id="itemList">
            <div v-for="item in items" :key="item.id" class="itemBox">
                <h2>{{ item.name }}</h2>
                <img :src="item.cover ? item.cover : '@/assets/icons/person.svg'" />

                <p class="rarity" :class="item.rarity">{{ item.rarity }}</p>
                <div class="info">
                    <p>{{ item.price }} ZŁ</p>
                    <p class="count">Count: {{ item.count }}</p>
                </div> 
                
            </div>
        </div>
    </div>
</template>

<script>
import { refreshBalance } from '@/utils.js';
import axios from 'axios';

export default {
    data() {
        return {
            items: []
        }
    },
    mounted() {
        this.loadItems();
		refreshBalance(this);
    },

    methods: {
        async loadItems() {
            try {      
                const url = import.meta.env.VITE_API_BASE_URL;

                //gets user's items
                const userResponse = await axios.get(
                    `${url}/api/userInfo/`,
                    { withCredentials: true }
                );

                //gets all existing skins
                const skinsResponse = await axios.get(`${url}/api/skins/`)

                for(const skin of skinsResponse.data) {
                    for(const item of userResponse.data.items) {
                        if (skin.id == item.skinID) {
                            const skinInfo = { ...skin, count: item.count };
                            this.items.push(skinInfo);
                            break;
                        }
                    }
                }
                
            } catch (err) {
                console.error('Failed to fetch inventory: ', err);
            }
        }
    }  
}
</script>

<style>
    @import '@/assets/styles/inventory.css';
</style>