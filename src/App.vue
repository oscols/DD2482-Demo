<script>
export default {
  data() {
    return {
      msg: 'Hello World!'
      
    }
  }
}
</script>

<template>
  <h2>{{ msg }}</h2>
  <input v-model="msg">
</template>