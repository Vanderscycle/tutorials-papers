<template>
  <h3>Todos</h3>
  <div class="todos">
    <div v-for="todo in allTodos" v-bind:key="todo.id" class="todo">
      {{ todo.title }}
      <i @click='deleteTodo(todo.id)' class="fas fa-trash"></i>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  name: "Todos",
  methods: {
    ...mapActions(["fetchTodos", "deleteTodo"]),
  },
  computed: mapGetters(["allTodos"]),
  created() {
    this.fetchTodos(); 
  },
};
</script>
<style scoped>
.todos {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 1rem;
}
.todo {
  border: 1px solid #ccc;
  background: #41b883;
  padding: 1rem;
  border-radius: 20px;
  text-align: center;
  position: relative;
  cursor: pointer;
}
</style>
