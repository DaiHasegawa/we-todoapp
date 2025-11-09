<script setup lang=ts>
import { ref } from 'vue';

const name = ref('Vue 3 with TypeScript');

type Todo = { id: number; title: string; completed: boolean };

const todos = defineModel<Todo[]>("todos");

const newTitle = ref('');
// compute next id from existing todos
const nextId = ref(Math.max(0, ...todos.value.map((t) => t.id)) + 1);

function addTodo() {
  const title = newTitle.value;
  todos.value.push({ id: nextId.value++, title, completed: false });
  newTitle.value = '';
}

</script>

<template>
<h2>New Todo</h2>
<div style="display: flex; align-items: center; gap: 0.5rem; margin: 0.25rem 0;">
    <input
        v-model="newTitle"
        placeholder="New todo title"
        aria-label="New todo title"
    />
    <button v-on:click="addTodo" :disabled="!newTitle">Add</button>
</div>
</template>