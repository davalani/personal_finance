<template>
  <diV>
    <P>{{ message }}</P>
    <button @click="updateMessage">Actualizar mensaje</button>
  </diV>
</template>

<script>
import { ref } from 'vue';

export default {
  setup() {
    const message = ref('Estamos aprendiendo fundamentos de Vue!');
    () => {
      message.value = '¡ Mensaje actualizado!';
    };
    return { message, updateMessage };
  }
}


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
