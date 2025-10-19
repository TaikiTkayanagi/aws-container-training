import type { HelloResponse } from "@/type/Hello";
import { defineStore } from "pinia";
import { ref } from "vue";

export const useHelloStore = defineStore('hello', () => {
    const message = ref('');
    const isSuccess = ref(true);

    async function fetchHello() {
        try{
            const url = import.meta.env.VITE_API_URL;
            const path = `${url}/hello`;
            var rep: HelloResponse = await fetch(path).then(res => res.json());
            message.value = rep.message;
        } catch (e) {
            console.error(e);
            isSuccess.value = false;
        }
    }

    return { message, isSuccess, fetchHello };
})