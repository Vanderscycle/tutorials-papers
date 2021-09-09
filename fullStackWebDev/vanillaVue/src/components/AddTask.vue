<template>
  <form @submit="onSubmit" class="add-form">
    <div class="form-control">
      <label>Task</label>
      <input class='form-fields' type="text" v-model="text" name="text" placeholder="Add Task" />
    </div>
    <div class="form-control">
      <label>Day & Time</label>
      <input
        class='form-fields'
        type="date"
        v-model="day"
        name="day"
        placeholder="Add Day & Time"
      />
    </div>
    <div class="form-control form-control-check">
      <label>Set Reminder</label>
      <input class='form-fields' type="checkbox" v-model="reminder" name="reminder" />
    </div>

    <input type="submit" value="Save Task" class="form-fields" />
  </form>
</template>

<script>
export default {
  name: 'AddTask',
  data () {
    return {
      text: '',
      day: '',
      reminder: false
    }
  },
  methods: {
    onSubmit(e) {
      e.preventDefault()
      if(!this.text) {
        alert('please add a task')
        return
      }

      const newTask = {
        //you want a backend
        id: Math.floor(Math.random() * 100000 ),
        text: this.text,
        day: this.day,
        reminder: this.reminder
      }
      console.log(newTask)
      this.$emit('add-task', newTask)
      this.text = '';
      this.day =  '';
      this.reminder= false

    }
  }
}
</script>
<style>
.form-control {
  @apply self-center px-4 py-3 rounded-full 
}
.form-fields {
  @apply rounded-xl
}
  
</style>
