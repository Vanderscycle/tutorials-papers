//usefull to communicate between
import axios from "axios";

const state = {
  todos: [],
};

const getters = {
  allTodos: (state) => state.todos,
};

const actions = {
  //we don't call the mutation directly
  async fetchTodos({ commit }) {
    const response = await axios.get(
      "https://jsonplaceholder.typicode.com/todos"
    );
    commit("setTodos", response.data);
  },
  //takes an object
  async addTodo({ commit }, title: string) {
    const response = await axios.post(
      "https://jsonplaceholder.typicode.com/todos",
      { title, completed: false }
    );
    commit("newTodo", response.data);
  },
  async deleteTodo({ commit }, id) {
    await axios.delete(`https://jsonplaceholder.typicode.com/todos/${id}`);
    commit("removeTodo", id);
  },
  async filterTodos({ commit }, e: Event) {
    const limit = parseInt(
      e.target.options[e.target.options.selectedIndex].innerText
    );
    console.log(limit);
    const response = await axios.get(
      `https://jsonplaceholder.typicode.com/todos?_limit=${limit}`
    );
    commit("setTodos", response.data);
  },
  async updateTodo({ commit }, updTodo) {
    const response = await axios.put(
      `https://jsonplaceholder.typicode.com/todos/${updTodo.id}`, updTodo
    );
    commit('updaTodo',response.data)
  
  },
};

const mutations = {
  setTodos: (state, todos) => (state.todos = todos),
  newTodo: (state, todo) => state.todos.unshift(todo), //unshift puts it at the beginning of the array
  removeTodo: (state, id) =>
    (state.todos = state.todos.filter((task) => task.id !== id)),
  updaTodo: (state,updTodo) => {
    const index = state.todos.findIndex(todo => todo.id === updTodo)
    if (index !== -1 ){
      state.todos.splice(index,1,updTodo)
    }
  }

};

export default {
  state,
  getters,
  actions,
  mutations,
};
