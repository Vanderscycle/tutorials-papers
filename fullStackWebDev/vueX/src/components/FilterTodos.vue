<template>
  <h3>Filter Todo
    <form @submit="onFilter" action=""></form>
      <input type="text" v-model="search" placeholder="filter...">
      <input type="submit" value="Submit">
      {{ search }}
  </h3>
  Limit Search
  <select @change='filterTodos($event)' name="" id="">
    <option value="200" class="">200</option>
    <option value="100" class="">100</option>
    <option value="50" class="100">50</option>
    <option value="20" class="100">20</option>
    <option value="10" class="100">10</option>
    <option value="5" class="">5</option>
  </select>
</template>

<script>
import { mapActions } from "vuex"
export default {
  name: "FilterTodo",
  data() {
    return {
      search: '',
      value: ''
    }
  },
  methods: {
    ...mapActions(['filterTodos']),
    onchange(e){
      e.preventDefault()
      console.log(this.value)
      this.filterTodos(this.value)
    },
    onsubmit(e) {
      e.preventDefault()
      console.log(this.search)
      this.filterTodo(this.search),

      this.search = ''

    }
  }
}
</script>

<style scoped>
/* where to store the css so no repeat? */
form {
  display: flex;
}
input[type="text"] {
  flex: 10;
  padding: 10px;
  border: 1px solid #41b883;
  outline: 0;
}
input[type="submit"] {
  flex: 2;
  background: #41b883;
  color: #fff;
  border: 1px #41b883 solid;
  cursor: pointer;
}

</style>
