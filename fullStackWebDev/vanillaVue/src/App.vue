<template>
  <h1>Hello Vue </h1>
  <div class="container">
    <Header title='bro'/>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import Header from './components/Header.vue' 

export default defineComponent({
  name: 'App',
  // don't forget to add the component
  components: {
    Header,
  }
})
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
