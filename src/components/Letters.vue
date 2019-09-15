<template>
  <div>
    <b-button variant="primary" size="sm" class="letters" v-for="item in letters" v-bind:key="item.index">{{item}}</b-button>
  </div> 

</template>

<script>
export default {
  name: 'Letters',
  props: {
    letters: String 
  }
}
</script>

<style scoped>
button {
  font-family: Consolas, 'Courier New', Courier, monospace;
  margin-left: 4px; 
  pointer-events: none;
}
</style>
