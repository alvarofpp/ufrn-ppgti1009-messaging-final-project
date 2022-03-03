<script setup lang="ts">
import { ref } from 'vue'

defineProps<{ msg: string }>()

const count = ref(0)
</script>

<template>

<va-card id="main-content">
    <va-card-title>Pedidos</va-card-title>
    <va-card-content>
        <ul>
            <li>Pedido 1</li>
            <li>Pedido 2</li>
        </ul>
    </va-card-content>
</va-card>
</template>

<style scoped>
a {
  color: #42b983;
}

label {
  margin: 0 0.5em;
  font-weight: bold;
}

code {
  background-color: #eee;
  padding: 2px 4px;
  border-radius: 4px;
  color: #304455;
}

#main-content {
    width: 80vw
}
</style>
