<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png" />
    <div class="container">
      <Todos />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
//import HelloWorld from './components/HelloWorld.vue'
import Todos from "./components/Todos.vue";

export default defineComponent({
  name: "App",
  components: {
    Todos,
  },
});
</script>

<style>
body {
  font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
  line-height: 1.6;
  background: #e8f7f0;
}
.container {
  max-width: 1100px;
  margin: auto;
  overflow: auto;
  padding: 0 2rem;
}
</style>
