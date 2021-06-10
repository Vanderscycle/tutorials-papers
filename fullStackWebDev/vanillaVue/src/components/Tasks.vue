<template>
  <div v-for="task in tasks" v-bind:key="task">
  
    <h3>{{ task.text }}</h3>
  </div>
  <h5>{{tasks}}</h5>
</template>

<script>
// v-bind
export default {
  name: "Tasks",
  props: {
    tasks: Array,
  },
};
</script>
