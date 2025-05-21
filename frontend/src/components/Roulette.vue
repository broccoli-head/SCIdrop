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

    <button v-if="isLoggedIn" id="spin" ref="spinButton" @click="buyChest">SPIN - {{ chestPrice }} ZŁ</button>
    <router-link v-else to="/login">
        <button id="spin" ref="spinButton">Log in to spin</button>
    </router-link>
    <p class="error">{{ message }}</p>

    <div class="window" ref="window">
        <h1>You won:</h1>
        <h2>{{ wonSkin.name }}</h2>
        <img :src="wonSkin.cover" />
        <p class="rarity" :class="wonSkin.rarity">{{ wonSkin.rarity }}</p>
        <p class="price">{{ wonSkin.price }} ZŁ</p>
        <router-link to="/">
            <button>CLAIM</button>
        </router-link>
    </div>
</template>

<script>
import { refreshBalance } from '@/utils.js';
import axios from 'axios';

export default {
    name: 'Roulette',
    data() {
        return {
            isLoggedIn: false,
            skins: [],
            chestPrice: 0,
            wonSkin: '',
            message: ''
        }
    },
    mounted() {
        this.loadSkins();
        this.checkLogin();
        refreshBalance(this);
    },

    methods: {
        async loadSkins() {
            const chestID = this.$route.params.id;

            try {
                const chestResponse = await fetch('http://localhost:8000/api/chests');
                const chestData = await chestResponse.json();

                for(const chest of chestData) {
                    if(chest.id == chestID) {
                        this.chestPrice = chest.price;
                        break;
                    }
                }             

                const skinsResponse = await fetch(`http://localhost:8000/api/skins/${chestID}/`);
                const skinsData = await skinsResponse.json();
                const shuffled = this.shuffleArray(skinsData);
                
                //fills the list with ca. 400 items
                while (this.skins.length < 400) {
                    this.skins.push(...shuffled);
                }
                this.skins.length = 400;    //cuts to 400 elements

            } catch (err) {
                console.error('Failed to fetch skins:', err);
            }
        },

        //checks login status
		checkLogin() {
			this.isLoggedIn = localStorage.getItem('isLoggedIn')  == 'true';
		},

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
        
        async buyChest() {
            try {
                //gets csrf token required to buy chest
                const csrfResponse = await axios.get(
                    'http://localhost:8000/api/getCSRF/',
                    { withCredentials: true }
                );

                const response = await axios.post('http://localhost:8000/api/buyChest/', {
                    chestID: this.$route.params.id
                }, {
                    //needed for django csrf protecion
                    withCredentials: true,
                    headers: {
                        'X-CSRFToken': csrfResponse.data.CSRFToken
                    }
                })
                
                refreshBalance(this);

                if(response.data.message) {
                    this.message = response.data.message;
                }
                else {
                    this.wonSkin = response.data.wonSkin;
                    this.spin();
                }
                
            }
            catch(error) {
                console.log(error);
                if(error.response && error.response.data) {
                    this.message = error.response.data.message || 'Spin failed. User balance has been secured.';
                }
                else {
                    this.message = 'Connection error occured.';
                }
            }            
        },

        spin() {
            const skinCount = this.skins.length;
            const skinList = this.$refs.skinList;
            const container = this.$refs.skinList;
            const window = this.$refs.window;

            const boxWidth = 140;   //width of the skin box

            const button = this.$refs.spinButton;
            button.disabled = true;

            //gets the element positioned in the 90% of the list
            //e.g. index for 400 items: 0.9 * 400 = 360
            const skinIndex = skinCount - Math.floor(skinCount / 10);

            //sets drawn skin on the specific index 
            this.skins[skinIndex] = this.wonSkin;

            //spins list from right to left
            let scrollTarget = 0;
            scrollTarget = skinIndex * boxWidth + (container.clientWidth * 2) + (boxWidth * 4.75);
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