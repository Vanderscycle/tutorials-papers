<template>
  <button @click="onClick()" :style="{ background: color }" class='text-white font-bold py-2 px-4 rounded-full'>{{ text }}</button>
</template>

<script>
//35:25 at vue js
export default {
  name: "Button",
  props: {
    text: String,
    color: String,
  },
  methods: {
    onClick() {
      console.log('click')
      this.$emit('toggle-add-task')
    }
  }
}
</script>

<style scoped>
</style>
