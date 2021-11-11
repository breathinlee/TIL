import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todos: [],
  },
  mutations: {
    CREATE_TODO: function (state, todoItem) {
      state.todos.push(todoItem)
    },
    DELETE_TODO: function (state, todoItem) {
      const idx = state.todos.indexOf(todoItem)
      state.todos.splice(idx, 1)
    },
    UPDATE_TODO: function (state, todoItem) {
      state.todos = state.todos.map((todo) => {
        if (todo === todoItem) {
          return {
            title: todoItem.title,
            isCompleted: !todoItem.isCompleted
          }
        } else {
          return todo
        }
      })
    }
  },
  actions: {
    createTodo: function ({ commit }, todoItem) {
      commit('CREATE_TODO', todoItem)
    },
    deleteTodo: function ({ commit }, todoItem) {
      commit('DELETE_TODO', todoItem)
    },
    updateTodo: function ({ commit }, todoItem) {
      commit('UPDATE_TODO', todoItem)
    }
  },
  getters: {
    allTodoCount: function (state) {
      return state.todos.length
    },
    completedCount: function (state) {
      const todos = state.todos.filter((todo) => {
        return todo.isCompleted
      })
      return todos.length
    },
    uncompletedCount: function (state) {
      const todos = state.todos.filter((todo) => {
        return !todo.isCompleted
      })
      return todos.length
    },
  },
  modules: {
  },
  plugins: [createPersistedState()],
})
