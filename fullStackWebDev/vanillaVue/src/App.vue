<template>
  <h1>Hello Vue</h1>
  <div class="container">
    <Header @toggle-add-task="toggleAddTask" title="Task Tracker" :showAddTask="showAddTask"/>
    <div v-if='showAddTask'>
      <AddTask @add-task="addTask"/>
    </div>
    <!-- The app is very small so vuex is not needed, but for bigger apps you must use vuex to sync -->
    <Tasks @toggle-reminder='toggleReminder' @delete-task='deleteTask' :tasks="tasks" />
    <router-view></router-view>
    <Footer/>
  </div>
</template>

<script lang="ts">

import Header from "./components/Header.vue";
import Tasks from "./components/Tasks.vue";
import AddTask from "./components/AddTask.vue";
import Footer from "./components/Footer.vue"
interface TaskInterface {
  id: number;
  text: string;
  day: string;
  reminded: Boolean;
}
interface TaskInterface extends Array<TaskInterface> {}
export default {
  name: "App",
  // don't forget to add the component
  components: {
    Header,
    Footer,
    Tasks,
    AddTask
  },
  //unless you use vuex you want the data to be in the top level view
  data(): TaskInterface[] {
    return {
      tasks: [],
      showAddTask: false
    };
  },
  methods: {
    toggleAddTask () {
      this.showAddTask = !this.showAddTask
    },
    //post
    async addTask(task: TaskInterface) {
      const res = await fetch('api/tasks', {
        method: "POST",
        headers: {
        'content-type': 'application/json',
        },
        body: JSON.stringify(task)

      })

      console.log(res)
      let data = await res.json()//.filter(() => { })
      console.log(data)


      
      this.tasks = [...this.tasks,data]
    },
    async deleteTask(id: TaskInterface[number]) {
      if (confirm('Are you sure?')) {
        const res = await fetch(`api/tasks/{id}`,{
          method: ' DELETE'
        })
        res.status == 200 ? (this.tasks = this.tasks.filter((task) => task.id !== id )) : alert('Error deleting task')
      }
    },
    toggleReminder(id:number) {
      console.log('reminder task', id)
      //map allows us to maniupulate the array and return what we want
      this.tasks = this.tasks.map((task) => task.id === id ? {...task, reminder: !task.reminder} : task)
    },
    // get
    async fetchTasks (): TaskInterface[] {
      const res = await fetch('api/tasks')
      const data = await res.json()
      return data
    },
    async fetchTask (id: number): TaskInterface {
      const res = await fetch(`api/tasks/${id}`)
      const data = await res.json()
      return data
    }

    
  },
  async created() {
    this.tasks = this.fetchTasks()
    //this.tasks = [
    //  {
    //    id: 1,
    //    text: "Doc's app",
    //    day: "March 1st at 2:30pm",
    //    reminder: true,
    //  },
    //  {
    //    id: 2,
    //    text: "Interview",
    //    day: "March 3st at 2:30pm",
    //    reminder: true,
    //  },
    //  {
    //    id: 3,
    //    text: "play video games",
    //    day: "March 3st at 4:30pm",
    //    reminder: false,
    //  },

    //];
  },
};
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
