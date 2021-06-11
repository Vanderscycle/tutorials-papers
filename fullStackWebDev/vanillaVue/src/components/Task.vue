<template>
  <div :class="[fields.reminder ? 'reminder' : '', 'task']">
    <h3 class='hover:bg-green-700 items-center rounded-full'>{{ fields.text }}</h3>
      <i @click='onDelete(fields.id)' class="far fa-trash icon"></i> 
    <p class='items-center'>{{ fields.day }}</p>
  </div>
</template>

<script>
// declare the desire components "fields" in the template.
// export the available fields
export default {
  name: 'Task',
  props: {
    fields: Object,
  },
  methods: {
    onDelete(id) {
      this.$emit('delete-task', id)
    }
  }
}
</script>

<style scoped>
  .task {
    @apply p-6 max-w-sm mx-auto rounded-xl shadow-md flex items-center space-x-4 bg-gradient-to-r from-green-400 to-blue-500 
  }
  .reminder {
    @apply border-4 border-red-500
  }
  .icon {
    @apply hover:bg-red-700 rounded-full
  }
</style>
