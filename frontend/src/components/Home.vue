<template>
<div>
    <div v-if="chests.length == 0">
        <h1>Currently, there are no chests to buy.</h1>
    </div>

    <div v-else id="chestList">
        <div v-for="chest in chests" :key="chest.id">
            <router-link class="chestBox" :to="`/chest/${chest.id}`">
                <h2>{{ chest.name }}</h2>
                <img :src="chest.cover ? chest.cover : '@/assets/icons/chest.svg'" />

                <p class="rarity" :class="chest.rarity">{{ chest.rarity }}</p>
                <p class="price">{{ chest.price }} ZŁ</p> 
            </router-link>
        </div>
    </div>
</div>
</template>

<script>

export default {
    data() {
        return { chests: [] }
    },
    async created() {
        try {
            const response = await fetch('http://localhost:8000/api/chests/');
            const data = await response.json();
            this.chests = data;
        } catch (err) {
            console.error('Failed to fetch chests:', err);
        }
    }
}
</script>

<style>
    @import '@/assets/styles/home.css';
</style>