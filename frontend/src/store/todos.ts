import { defineStore } from 'pinia'
import { ref } from 'vue'

interface Todo {
  id: number
  title: string
  completed: boolean
}

export const useTodosStore = defineStore('todos', () => {
    let serialId = 4 // next id

    // データ定義 (reactive)
    const todos = ref<Todo[]>([
        { id: 1, title: 'Buy groceries', completed: false },
        { id: 2, title: 'Write report', completed: true },
        { id: 3, title: 'Call Alice', completed: false },
    ])

    // TODOを追加する
    const addTodo = (title: string) => {
        const newTodo: Todo = {
            id: serialId++,
            title: title,
            completed: false,
        }
        todos.value.push(newTodo)
    }

    return {
        todos,
        addTodo,
    }

})