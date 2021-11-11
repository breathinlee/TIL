<template>
  <div>
    <span :class="{ completed: todo.isCompleted }" @click="updateTodo(todo)">{{ todo.title }}</span>
    <button @click="deleteTodo(todo)">Delete</button>
  </div>
</template>

<script>
export default {
  name: 'TodoListItem',
  props: {
    todo: Object,
  },
  methods: {
    deleteTodo: function () {
      this.$store.dispatch('deleteTodo', this.todo)
    },
    updateTodo: function () {
      this.$store.dispatch('updateTodo', this.todo)
    }
  }
}
</script>

<style>
.completed {
  text-decoration: line-through;
}
</style>