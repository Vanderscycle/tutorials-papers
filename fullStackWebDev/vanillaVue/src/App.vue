<template>
  <h1>Hello Vue</h1>
  <div class="container">
    <Header title="bro" />
    <!-- The app is very small so vuex is not needed, but for bigger apps you must use vuex to sync -->
    <Tasks @delete-task='deleteTask' :tasks="tasks" />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Header from "./components/Header.vue";
import Tasks from "./components/Tasks.vue";
interface TaskInterface {
  id: number;
  text: string;
  day: string;
  reminded: Boolean;
}
interface TaskInterface extends Array<TaskInterface> {}
export default defineComponent({
  name: "App",
  // don't forget to add the component
  components: {
    Header,
    Tasks
  },
  //unless you use vuex you want the data to be in the top level view
  data(): TaskInterface[] {
    return {
      tasks: [],
    };
  },
  methods: {
    deleteTask(id: TaskInterface[number]) {
      if (confirm('Are you sure?')) {
        console.log('task',id)
        //filter high order array method
        this.tasks = this.tasks.filter((task) => task.id !== id )
      }
    }
  },
  created() {
    this.tasks = [
      {
        id: 1,
        text: "Doc's app",
        day: "March 1st at 2:30pm",
        reminder: true,
      },
      {
        id: 2,
        text: "Interview",
        day: "March 3st at 2:30pm",
        reminder: true,
      },
      {
        id: 3,
        text: "play video games",
        day: "March 3st at 4:30pm",
        reminder: false,
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
