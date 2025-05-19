import axios from 'axios';
import { global } from '@/store.js';

export async function refreshBalance(instance) {
    try {
        //gets balance from the backend
        const response = await axios.get('http://localhost:8000/api/userInfo/', {
            withCredentials: true
        });

        global.balance = response.data.balance + " PLN";
    } catch (err) {
        console.error('Failed to fetch user info:', err);
    }
}