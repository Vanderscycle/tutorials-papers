<template>
  <h1>Hello Vue</h1>
  <div class="container">
    <Header title="bro" />
    <Tasks :tasks="tasks" />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Header from "./components/Header.vue";
import Tasks from "./components/Tasks.vue";
interface Task {
  id: number;
  text: string;
  day: string;
  reminded: Boolean;
}
interface Task extends Array<Task> {}
export default defineComponent({
  name: "App",
  // don't forget to add the component
  components: {
    Header,
    Tasks
  },
  //unless you use vuex you want the data to be in the top level view
  data(): Task[] {
    return {
      tasks: [],
    };
  },
  created() {
    this.tasks = [
      {
        id: 1,
        text: "Doc's app",
        day: "March 1st at 2:30pm",
        reminder: true,
      },
    ];
  },
});
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
