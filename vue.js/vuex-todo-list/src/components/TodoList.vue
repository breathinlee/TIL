<template>
  <div>
    <todo-list-item
      v-for="(todo, index) in todos" 
      :key="index"
      :todo="todo"
    ></todo-list-item>
  </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem'
export default {
  name: 'TodoList',
  components: {
    TodoListItem,
  },
  computed: {
    todos: function() {
      return this.$store.state.todos
    }
  }
}
</script>

<style>

</style>