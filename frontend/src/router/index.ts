import { createRouter, createWebHistory } from 'vue-router'
import TodoListView from '../views/TodoList.vue'
import TodoDetail from '../views/TodoDetail.vue'
import About from '../views/About.vue'

const routes = [
  { path: '/', name: 'TodoList', component: TodoListView },
  { path: '/todo/:id', name: 'TodoDetail', component: TodoDetail },
  { path: '/about', name: 'About', component: About }
]

export const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router