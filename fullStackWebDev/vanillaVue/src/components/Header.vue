<template>
  <header>
    <h1>{{ title }}</h1>
    <Button @toggle-add-task="$emit('toggle-add-task')" @click='onClick()' :text="showAddTask ? 'Close' : 'Add Task'" :color="showAddTask ? 'orange' : 'green'"/>
  </header>
</template>

<script>
import Button from './Button.vue'

export default {
  name: "Header",
  components: {
    Button
  },
  props: {
    title: {
    type: String,
    default: 'Yoo2',
    },
    showAddTask: Boolean
  },
  methods: {
    onClick() {
    console.log('click')
    }
  },
  //when relaying emits between components don't forget to pass on emits
  emits: ['toggle-add-task']
};
</script>
<!-- scoped means only for this component -->
<style scoped>
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}
</style>
