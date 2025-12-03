import { defineStore } from 'pinia'
import { ref } from 'vue'

interface Todo {
  id: number
  title: string
  completed: boolean
}

export const useTodosStore = defineStore('todos', () => {
    const todos = ref<Todo[]>([])
    const loading = ref(false)
    const error = ref<string | null>(null)

    // TODO一覧をバックエンドから取得する
    const fetchTodos = async () => {

        const response = await fetch('http://127.0.0.1:8001/todos')
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`)
        }
        todos.value = await response.json()
    }

    // TODOを取得する
    const getTodoById = (id: number) => {
        return todos.value.find(todo => todo.id === id);
    }

    // TODOを追加する
    const addTodo = async (title: string) => {

        const response = await fetch('http://127.0.0.1:8001/todos', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ title })
        })
        const newTodo: Todo = await response.json()
        todos.value.push(newTodo)
    }

    // TODOを削除する
    const removeTodo = async (id: number) => {
        const response = await fetch(`http://localhost:8001/todos/${id}`, {
            method: 'DELETE'
        })
        if (response.ok) {
            todos.value = todos.value.filter(todo => todo.id !== id)
        }
    }

    return {
        todos,
        fetchTodos,
        addTodo,
        removeTodo,
        getTodoById
    }

})