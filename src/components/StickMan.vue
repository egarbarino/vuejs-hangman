<template>
  <div style="text-align: center" class="stickMan">
    <canvas ref="mycanvas" width="100" height="190" 
            v-bind:class="{'zoom' : fails == 7}"/>
    <div id="progress">
    <b-progress :value="7-fails" :max="7" animated></b-progress>
    </div>
    <div v-if="fails >=0 && fails <7">
    Attempts left
        <b-badge v-if="fails < 3" variant="success">{{7-fails}}</b-badge>
        <b-badge v-else-if="fails < 5" variant="warning">{{7-fails}}</b-badge>
        <b-badge v-else variant="danger">{{7-fails}}</b-badge>
     </div>
    <div v-else-if="fails == 7">
    Game over! 
    </div>
    <div v-else>
    You guessed the country name!
    </div>
  </div> 
</template>

<script>
export default {
  name: 'StickMan',
  props: {
    fails: Number 
  },
  methods: {
    renderStickMan: function() {
      var ctx = this.$refs['mycanvas'].getContext('2d');
      if (this.fails == 0) {
        ctx.clearRect(0, 0, 100,190);
        ctx.beginPath();
        ctx.moveTo(50, 20);
        ctx.lineTo(50, 0);
        ctx.lineTo(10, 0);
        ctx.lineTo(10, 180);
        ctx.stroke();

        ctx.beginPath();
        ctx.moveTo(40, 180);
        ctx.lineTo(0, 180);
        ctx.stroke();

        ctx.beginPath();
        ctx.moveTo(10, 165);
        ctx.lineTo(25, 180);
        ctx.stroke();

      }
      // Head 
      if (this.fails == 1) {
        ctx.beginPath();
        ctx.arc(50, 40, 19, 0, 2 * Math.PI);
        ctx.stroke();
      }

      // Body
      if (this.fails == 2) {
        ctx.beginPath();
        ctx.moveTo(50, 60);
        ctx.lineTo(50, 120);
        ctx.stroke();
      }

      // Arm left 
      if (this.fails == 3) { 
        ctx.beginPath();
        ctx.moveTo(50, 80);
        ctx.lineTo(20, 80);
        ctx.stroke();
      }

      // Arm right 
      if (this.fails == 4) {
        ctx.beginPath();
        ctx.moveTo(50, 80);
        ctx.lineTo(80, 80);
        ctx.stroke();
      }


      // Lef left 
      if (this.fails == 5) {
        ctx.beginPath();
        ctx.moveTo(50, 120);
        ctx.lineTo(30, 169);
        ctx.stroke();
      }

      // Leg Right 
      if (this.fails == 6) {
        ctx.beginPath();
        ctx.moveTo(50, 120);
        ctx.lineTo(70, 169);
        ctx.stroke();
      }

      // Game Over 
      if (this.fails == 7) {
        // Leg right 
        ctx.beginPath();
        ctx.moveTo(50, 120);
        ctx.lineTo(70, 169);
        ctx.stroke();

        // Face 
        ctx.beginPath();
        ctx.arc(43, 35, 3, 0, 2 * Math.PI);
        ctx.stroke();

        ctx.beginPath();
        ctx.arc(57, 35, 3, 0, 2 * Math.PI);
        ctx.stroke();

        ctx.beginPath();
        ctx.moveTo(43, 50);
        ctx.lineTo(57, 50);
        ctx.stroke();
      } 

    }
  },
  mounted() {
    //this.ctx = this.$refs['mycanvas'].getContext('2d');
    this.renderStickMan();
  },
  updated() {
    this.renderStickMan();
  }
}
</script>

<style scoped>
.stickMan {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 14pt;
}
#progress {
  margin-left: 25%;
  margin-right: 25%;
}

@keyframes zoominoutsinglefeatured {
  0% {
       transform: scale(1,1) rotate(0deg);
     }
  50% {
        transform: scale(1.2,1.2) rotate(5deg);
      }
  100% {
        transform: scale(1,1) rotate(0deg);
    }
}

.zoom {
    animation: zoominoutsinglefeatured 1s infinite ;
}

</style>
