<script setup lang=ts>
import { useTodosStore } from '../store/todos';
import { computed } from 'vue';
import { useRoute } from 'vue-router';

const $route = useRoute();
const todosStore = useTodosStore();
const todo = computed(() => todosStore.getTodoById(Number($route.params.id)));
</script>

<template>
    <h2>Todo Detail</h2>
    <div v-if="todo">
        <h3>{{ todo.title }}</h3>
        <p>Status: {{ todo.completed ? 'Completed' : 'Pending' }}</p>  
    </div>
</template>