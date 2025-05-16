const { createApp, ref } = Vue

createApp({
    setup() {
        const message = ref('test message')
        return {
            message
        }
    }
}).mount('#app')