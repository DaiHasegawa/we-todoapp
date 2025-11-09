<script setup lang=ts>
import { ref, computed } from 'vue';
import AddTodo from './components/AddTodo.vue';

const name = ref('Vue 3 with TypeScript');

type Todo = { id: number; title: string; completed: boolean };

// Hardcoded (pseudo) todo data
const todos = ref<Todo[]>([
  { id: 1, title: 'Buy groceries', completed: false },
  { id: 2, title: 'Write report', completed: true },
  { id: 3, title: 'Call Alice', completed: false },
]);

</script>

<template>
  <div id="app">

    <section class="todo-app">
      <h2>Todos</h2>

      <ul>
        <li
          v-for="todo in todos"
          :key="todo.id"
          style="display:flex; align-items:center; gap:0.5rem; margin:0.25rem 0;"
        >
          <input type="checkbox" v-model="todo.completed" />
          <span :style="{ textDecoration: todo.completed ? 'line-through' : 'none' }">
            {{ todo.title }}
          </span>
        </li>
      </ul>
    </section>
    <section>
      <AddTodo v-model:todos="todos"/>
    </section>
  </div>
</template>