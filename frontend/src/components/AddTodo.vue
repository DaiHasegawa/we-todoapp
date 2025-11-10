<script setup lang=ts>
import { ref } from 'vue';
import { useTodosStore } from '../store/todos';

const todoStore = useTodosStore();

// component内での双方向バインディングなのでrefを使う
// defineModel()はv-modelをコンポーネント外に公開するためのもの
const newTitle = ref<string>(''); 

function addTodo() {
  const title = newTitle.value;
  todoStore.addTodo(title);
  newTitle.value = '';
}

</script>

<template>
<h2>New Todo</h2>
<div style="display: flex; align-items: center; gap: 0.5rem; margin: 0.25rem 0;">
    <input
        v-model="newTitle"
        placeholder="New todo title"
    />
    <button v-on:click="addTodo" :disabled="!newTitle">Add</button>
</div>
</template>