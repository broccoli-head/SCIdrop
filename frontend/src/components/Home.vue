<template>
<div id="chestList">
    <div v-for="chest in chests" :key="chest.id">
    <a class="chestBox" href="chest/{{ chest.id }}">
        <h2>{{ chest.name }}</h2>
        <img :src="chest.cover ? chest.cover : '@/assets/icons/chest.svg'" />

        <p class="rarity {{ chest.rarity }}">{{ chest.rarity }}</p>
        <p class="price">{{ chest.price }} ZŁ</p> 
    </a>
    </div>
</div>
</template>

<script>
export default {
    data() {
        return {
            chests: []
        }
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
    @import "@/assets/styles/home.css";
</style>