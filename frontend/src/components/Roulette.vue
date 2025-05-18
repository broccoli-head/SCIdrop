<template>
    <img class="triangle" src="@/assets/icons/triangle.svg" />
    <div id="listOverlay" ref="listOverlay">
        <div id="skinList" ref="skinList">
            <div v-for="(skin, index) in skins" :key="index" class="skinBox">
                <h2>{{ skin.name }}</h2>
                <img :src="skin.cover" />
                <p class="rarity" :class="skin.rarity">{{ skin.rarity }}</p>
                <p class="price">{{ skin.price }} ZŁ</p>
                <p class="index" ref="skinIndex">{{ index }}</p>
            </div>
        </div>
    </div>
    <button id="spin" ref="spinButton" @click="spin">Spin</button>

    <div class="window" ref="window">
        <h1>You won:</h1>
        <h2>{{ selected.name }}</h2>
        <img :src="selected.cover" />
        <p class="rarity" :class="selected.rarity">{{ selected.rarity }}</p>
        <p class="price">{{ selected.price }} ZŁ</p>
        <router-link to="/">
            <button>CLAIM</button>
        </router-link>
    </div>
</template>

<script>
export default {
    data() {
        return {
            skins: [],
            selected: []
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
            const chestID = this.$route.params.id;
            const skinCount = this.skins.length;
            const skinList = this.$refs.skinList;
            const container = this.$refs.skinList;
            const window = this.$refs.window;

            const boxWidth = 140;   //width of the skin box

            const button = this.$refs.spinButton;
            button.disabled = true;

            //gets the middle element
            const skinIndex = Math.floor(skinCount / 2);
            this.selected = this.skins[skinIndex];

            //spins list from right to left
            //checking chest id is temporary until i will find issue of finding middle element
            let scrollTarget = 0;
            if (chestID == 1) {
                scrollTarget = skinIndex * boxWidth + container.clientWidth;
            }
            else {
                scrollTarget = skinIndex * boxWidth + (container.clientWidth / 2) + (boxWidth / 2);
            }
        
            skinList.style.transform = `translateX(-${scrollTarget}px)`;
            
            //after 8s shows the window with won skin
            setTimeout(() => {
                window.style.display = 'flex';
            }, 8000);
        }
    }
}
</script>

<style>
    @import '@/assets/styles/roulette.css';
</style>