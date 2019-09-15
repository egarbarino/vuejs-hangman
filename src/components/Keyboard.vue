<template>
  <div id="buttons">
    <div v-for="row in keys" :key="row">
      <b-button v-for="key in row" 
                :key="key" 
                size="sm" 
                pill 
                variant="dark"
                :disabled="usedLetters.includes(key)"
                v-on:click="click(key)"
                >
                {{key}}
      </b-button>
    </div>
    <div>
      <b-button variant="dark" v-on:click="$emit('restart')">Restart</b-button>
    </div>
  </div> 
</template>

<script>
export default {
  name: 'Keyboard',
  props: {
    usedLetters: String
  },
  data() { 
    return {
      keys : ["QWERTYUIOP",
              "ASDFGHJKL",
              "ZXCVBNM"
             ],
    } 
  },
  methods: {
    click(key) {
      console.log("clicked:" + key);
      this.$emit('key',key);
    }
  }
}
</script>

<style scoped>
button {
  font-family: Consolas, 'Courier New', Courier, monospace;
  margin-left: 3px;
  margin-top: 3px;
}
</style>
