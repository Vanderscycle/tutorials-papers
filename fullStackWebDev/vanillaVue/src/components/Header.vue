<template>
  <header>
    <h1>{{ title }}</h1>
    <Button text='add Task' color='green'/>
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
    }
  }
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
