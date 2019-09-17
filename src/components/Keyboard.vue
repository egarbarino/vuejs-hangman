<template>
  <div id="buttons">
    <div v-for="row in keys" :key="row">
      <b-button v-for="key in row" 
                :key="key" 
                size="sm" 
                pill 
                variant="dark"
                :disabled="usedLetters.includes(key)"
                v-on:click="click(key, $event)"
                >
                {{key}}
      </b-button>
    </div>
    <div id="restart">
      <b-button variant="dark" v-on:click="restart">Restart</b-button>
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
    click(key,e) {
      this.$emit('key',key);
      e.target.blur();
    },
    restart(e) { 
      this.$emit('restart');
      e.target.blur();
    }
  }
}
</script>

<style scoped>
button {
  font-family: Consolas, 'Courier New', Courier, monospace;
  font-weight: bold;
  margin-left: 2px;
  margin-top: 3px;
}
#restart {
  margin-top: 5px;
}
</style>
