<template>
  <button :style="{ background: color }">{{ text }}</button>
</template>

<script>
//35:25 at vue js
export default {
  name: "Button",
  props: {
    text: String,
    color: String,
  },
}
</script>

<style scoped>
</style>
