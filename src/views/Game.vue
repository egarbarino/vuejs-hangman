<template>
  <div id="game">
    <b-card header="Game" border-variant="primary" bg-variant="light" header-bg-variant="primary"
        header-text-variant="white">

      <div id="gameComponent">
      <StickMan :fails="fails"/>
      </div>

      <div id="gameComponent">
      <Letters :letters="guessedWord"/>
      </div>
      
      <div id="gameComponent">
      <Keyboard v-on:key="processLetter" v-on:restart="restart" :usedLetters="usedLetters"/>
      </div>

    </b-card>


    <br/>
 </div>
</template>

<script>
import StickMan from '@/components/StickMan.vue'
import Letters from '@/components/Letters.vue'
import Keyboard from '@/components/Keyboard.vue'
import json from '@/words.json'

export default {
  name: 'game',
  components: {
    StickMan,
    Letters,
    Keyboard
  },
  data() { 
    return {
      fails: 0,
      guessedWord: "",
      secretWord: "",
      foundLetters: "",
      usedLetters: "", 
      words : json.words
    } 
  },
  mounted: function() {
    window.addEventListener('keyup', this.keyPressed);
    this.restart();
  },
  methods: {
    restart: function() {
      var min = 0;
      var max = this.words.length-1;
      var index = parseInt(Math.random() * (max - min) + min);
      this.secretWord = this.words[index].toUpperCase();
      this.guessedWord = "";
      this.foundLetters = "";
      this.usedLetters = "";
      this.fails = 0;  
      this.guessedWord = this.secretWord.split('').map(() => '_').join("");
     },
    keyPressed(e) {
      var key = e.key.toUpperCase();
      this.processLetter(key);
    },
    processLetter(letter) {
      if (this.fails >= 0 && this.fails < 7 && !this.usedLetters.includes(letter)) {
        if (this.secretWord.includes(letter) 
            && !this.foundLetters.includes(letter)) {
          this.foundLetters += letter;
          this.guessedWord = 
            this.secretWord.split('')
              .map(l => this.foundLetters.includes(l) ? l : '_').join("");
          if (this.guessedWord == this.secretWord) {
            this.fails = -1;
          }
        } else {
          this.fails++;
          if (this.fails == 7) {
            this.guessedWord = this.secretWord;
          }
        } 
        this.usedLetters += letter;
      } 
      if (letter == "ESCAPE" || letter == " ") {
        this.restart();
      } 
    }
  }
}
</script>

<style>
#game {
  text-align: center;
  margin-top: 10px;
  min-width: 300px;
}
#gameComponent {
  margin-top: 7px;
}
</style>
