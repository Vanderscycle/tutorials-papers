<template>
  <button :style="{ background: color }" class='text-white font-bold py-2 px-4 rounded-full'>{{ text }}</button>
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
