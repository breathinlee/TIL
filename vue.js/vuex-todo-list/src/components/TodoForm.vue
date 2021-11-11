<template>
  <div>
    <input type="text" v-model.trim="todoTitle" @keypress.enter="createTodo">
    <button @click="createTodo">Add</button>
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
  data: function() {
    return {
      todoTitle: '',
    }
  },
  methods: {
    createTodo: function () {
      const todoItem = {
        title: this.todoTitle,
        isCompleted: false,
      }
    if (this.todoTitle) {
      this.$store.dispatch('createTodo', todoItem)
    }
    this.todoTitle = ''
    }
  }
}
</script>

<style>

</style>