<template>
<div class="item-list">
    <div v-for="item in items" :key="item.id" class="item">
        <h2>{{ item.name }}</h2>
        <img :src="item.cover" alt="item image" class="item-image" />
        <p>{{ item.rarity }}</p>
        <p>{{ item.price }}</p>
    </div>
</div>
</template>

<script>
export default {
    data() {
        return {
            skins: []
        }
    },
    async created() {
        const chestID = this.$route.params.id;
        try {
            const response = await fetch('http://localhost:8000/api/skins/${chestID}/');
            const data = await response.json();
            this.skins = data;
        } catch (err) {
            console.error('Failed to fetch skins:', err);
        }
    }
}
</script>

<style>
    @import '@/assets/styles/roulette.css';
</style>