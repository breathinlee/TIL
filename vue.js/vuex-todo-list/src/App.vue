<template>
  <div id="app">
    <h1>Todo List</h1>
    <h2>All Todos: {{ all }}</h2>
    <h2>Completed Todo: {{ complete }}</h2>
    <h2>Uncompleted Todo: {{ uncomplete }}</h2>
    <todo-list></todo-list>
    <todo-form></todo-form>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import TodoList from '@/components/TodoList'
import TodoForm from '@/components/TodoForm'

export default {
  name: 'App',
  components: {
    TodoList,
    TodoForm,
  },
  computed: {
    ...mapGetters({
      'complete': 'completedCount',
      'uncomplete': 'uncompletedCount',
      'all': 'allTodoCount',
    })
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
