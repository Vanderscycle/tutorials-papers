//usefull to communicate between
import axios from 'axios'

const state = {
  todos: []
}

const getters = {
  allTodos:(state) => state.todos
}

const actions = {
  //we don't call the mutation directly
  async fetchTodos({ commit }) {
    const response = await axios.get('https://jsonplaceholder.typicode.com/todos')
    commit('setTodos',response.data)
  },
  //takes an object
  async addTodo({ commit }, title) {
    const response = await axios.post('https://jsonplaceholder.typicode.com/todos',{title, completed: false})
    commit('newTodo', response.data)
  },
  async deleteTodo({ commit }, id) {
    await axios.delete(`https://jsonplaceholder.typicode.com/todos/${id}`)
    commit('removeTodo', id)

  }
};

const mutations = {
  setTodos: (state, todos) => (state.todos = todos),
  newTodo: (state, todo ) => ( state.todos.unshift(todo)),//unshift puts it at the beginning of the array
  removeTodo: (state, id) => (state.todos = state.todos.filter((task) => task.id !== id))

}

export default {
  state,
  getters,
  actions,
  mutations,
}
