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

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const items = ref([])
  
onMounted(async () => {
  try {
    const response = await axios.get('http://localhost:8000/api/chest/1')
    items.value = response.data.skins
    console.log(items.value)
  } catch (error) {
    console.error('Failed to load data:', error)
  }
})

</script>

<style>
.item-list {
  width: 100%;
  max-width: 600px;
  margin: 0 auto;
}

.item {
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 16px;
  margin-bottom: 16px;
}

.item-image {
  max-width: 100%;
  height: auto;
  margin: 12px 0;
}
</style>
