<template>
  <div id="app">
    <img alt="movie thief" src="./assets/movieThief200.png" class="mx-auto">
    <TorrentManager/>
  </div>
</template>

<script>
import TorrentManager from './components/TorrentManager.vue'

export default {
  name: 'app',
  components: {
    TorrentManager
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
