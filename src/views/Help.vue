<template>
  <div id="help">
    <b-card header="Help" border-variant="primary" bg-variant="light" header-bg-variant="primary"
        header-text-variant="white">
      <b-card-text>
        The objective of the game is to guess the name of a country.
      </b-card-text>
      <b-card-text>
        Keyboard operation:
        <ul>
          <li>A-Z: Enter letter </li>
          <li>ESC/SPACE: Restart</li>
        </ul>
      </b-card-text>
     </b-card>
  </div>
</template>

<script>
export default {
  name: 'help',
  data() { 
    return {
    }
  }
}
</script>

<style scoped>
#help {
  margin-top: 10px;
  min-width: 300px;
}
</style>
