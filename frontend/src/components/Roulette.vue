<template>
<div id="skinList">
    <div v-for="skin in skins" :key="skin.id" class="skinBox">
        <h2>{{ skin.name }}</h2>
        <img :src="skin.cover" />
        <p class="rarity" :class="skin.rarity">{{ skin.rarity }}</p>
        <p class="price">{{ skin.price }} ZŁ</p>
    </div>
</div>
<button id="spin">Spin</button>
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
            const response = await fetch(`http://localhost:8000/api/skins/${chestID}/`);
            const data = await response.json();
            this.skins = this.shuffleArray(data);
        } catch (err) {
            console.error('Failed to fetch skins:', err);
        }
    },
    methods: {
        shuffleArray(array) {
            for(let i = array.length - 1; i > 0; i--) {
                let j = Math.floor(Math.random() * (i + 1));
                let temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
            return array;
        }
    }
}
</script>

<style>
    @import '@/assets/styles/roulette.css';
</style>