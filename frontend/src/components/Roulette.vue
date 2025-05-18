<template>
    <img class="triangle" src="@/assets/icons/triangle.svg" />
    <div id="skinsOverlay">
        <div id="skinList" ref="skinList">
            <div v-for="skin in skins" :key="skin.id"class="skinBox">
                <h2>{{ skin.name }}</h2>
                <img :src="skin.cover" />
                <p class="rarity" :class="skin.rarity">{{ skin.rarity }}</p>
                <p class="price">{{ skin.price }} ZŁ</p>
            </div>
        </div>
    </div>
    <button id="spin" @click="spin">Spin</button>
</template>

<script>
export default {
    data() {
        return {
            skins: [],
            isSpinning: false
        }
    },
    async created() {
        const chestID = this.$route.params.id;
        try {
            const response = await fetch(`http://localhost:8000/api/skins/${chestID}/`);
            const data = await response.json();
            
            const shuffled = this.shuffleArray(data);
            //fills list with 20x current array
            this.skins = Array(20).fill(shuffled).flat();

        } catch (err) {
            console.error('Failed to fetch skins:', err);
        }
    },

    methods: {
        shuffleArray(array) {
            for(let i = array.length - 1; i > 0; i--) {
                //randomize order of the array items
                let j = Math.floor(Math.random() * (i + 1));
                let temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
            return array;
        },
        spin() {
            const skinList = this.$refs.skinList;
            //spins list from right to left
            skinList.style.transform = "translateX(-2000%)";
        }
    }
}
</script>

<style>
    @import '@/assets/styles/roulette.css';
</style>