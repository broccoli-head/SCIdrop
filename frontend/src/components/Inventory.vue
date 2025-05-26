<template>
<div>
    <div v-if="items.length == 0">
        <h1>You don't have any items yet. Gamble to earn some!</h1>
    </div>

    <div v-else id="itemList">
        <div v-for="item in items" :key="item.id">
            <div>
                <h2>{{ item.name }}</h2>
                <img :src="item.cover ? item.cover : '@/assets/icons/person.svg'" />

                <p class="rarity" :class="item.rarity">{{ item.rarity }}</p>
                <p class="price">{{ item.price }} ZŁ</p> 
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
                //gets user's items
                const userResponse = await axios.get(
                    'http://localhost:8000/api/userInfo',
                    { withCredentials: true }
                );

                const skinsResponse = await axios.get(
                    'http://localhost:8000/api/skins'
                )

                for(const skin of skinsResponse.data) {
                    for(const item of userResponse.data.items) {
                        if (skin.id == item.skinID) { 
                            this.items.push(skin);
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