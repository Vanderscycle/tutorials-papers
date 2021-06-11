<template>
  <!-- v-bind required otherwise vetur gives you an error-->
  <div v-for="task in tasks" :key="task.id">
    <Task @delete-task="$emit('delete-task', task.id)" :fields="task" /> 
  </div>
</template>

<script>
//1. import the desired component
//2. add it to the components field
//3 declare them in the template and pass values to it.
import Task from "./Task.vue"
// v-bind
export default {
  name: "Tasks",
  props: {
    tasks: Array,
  },
  components: {
    Task
  },
  emits: ['delete-task']
};
</script>
