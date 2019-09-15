<template>
  <div id="app">
   <b-nav tabs align="center">
      <b-nav-item to="/">Game</b-nav-item>
      <b-nav-item to="/help">Help</b-nav-item>
    </b-nav>
   <b-container class="bv-example-row" fluid>
      <b-row>
        <b-col><router-view/></b-col>
      </b-row>
    </b-container>
  </div>

</template>

<script>

</script>


<style scoped>
#app {
  margin-top: 4px;
}
</style>