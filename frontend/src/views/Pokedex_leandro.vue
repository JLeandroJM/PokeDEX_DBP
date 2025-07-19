<template>
    <div>
      <form @submit.prevent="buscarPokemon">
        <label for="pokemonName">Nombre del Pokémon:</label>
        <input type="text" id="pokemonName" v-model="pokemonName" />
        <button type="submit">Buscar</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        pokemonName: "",
      };
    },
    methods: {
      buscarPokemon() {
        // Redirige al usuario a la vista "PokedexDetailView" con el nombre del Pokémon
        this.$router.push({ name: "pokedex-detail", params: { name: this.pokemonName } });
      },
    },
  };
  </script>
  