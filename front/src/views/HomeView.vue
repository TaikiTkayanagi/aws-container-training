<script setup lang="ts">
import { useHelloStore } from '@/stores/hello';
import { createSSRApp, onMounted } from 'vue';

const hello = useHelloStore();
onMounted(async () => {
  await hello.fetchHello();
  if (!hello.isSuccess) {
    alert('Failed to fetch hello message.');
  }
})
</script>

<template>
  <div>
    <img src="/arai-uma.png" />
    <h1>{{ hello.message }}</h1>
  </div>
</template>
