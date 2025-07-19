<script>
import { pokemon } from "../datasets/pokemon.json";
import PokemonRow from "../components/PokemonRow.vue";

export default {
  name: "PokedexView",
  components: {
    PokemonRow,
  },
  data() {
    return {
      pokemon: pokemon,
      img: "",
      name: "",
      stats: [],
      types: [],
      abilities: [],
      id: Number,
      height: Number,
      weight: Number,
    };
  },
  created() {
    const namePkm = this.$route.params.name;  
    fetch("https://pokeapi.co/api/v2/pokemon/" + namePkm)
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      // Asigna los valores a las propiedades que desees
      this.id = data.id;
      this.name = data.name;
      this.img = data.sprites.front_default;
      
      // Pequeña funcion para cambiar la imagen a shiny
      const randomNumber = Math.floor(Math.random() * 4096);
      if (randomNumber == 1) {
        this.img = data.sprites.front_shiny;
      }
      
      this.stats = data.stats;
      this.height = (data.height / 10).toFixed(1);
      this.weight = (data.weight / 10).toFixed(1);
      this.types = data.types;
      this.abilities = data.abilities;
    })
    .catch((err) => {
      console.log(err);
    });
  },
  methods: {
    typeToIcon(type) {
      return "../src/assets/icons/" + type.toLowerCase() + ".svg";
    },
    upFirstLetter(word) {
      return word.charAt(0).toUpperCase() + word.slice(1);
    },
    getGeneration(id) {
      if (id < 152)
        return "1st Gen";
      else if (id < 252)
        return "2nd Gen";
      else if (id < 387)
        return "3rd Gen";
      else if (id < 495)
        return "4th Gen";
      else if (id < 650)
        return "5th Gen";
      else if (id < 722)
        return "6th Gen";
      else if (id < 810)
        return "7th Gen";
      else if (id < 906)
        return "8th Gen";
      else if (id < 10001)
        return "9th Gen";
      else
        return "It's another form of an existing pokemon."
    },
  },
};
</script>

<template>
  <div class="data">
    <div class="nameImg">
      <p class="bold">{{ upFirstLetter(this.name) }}</p>
      <img :src="img" alt="Imagen del Pokémon" :width="300">
    </div>
    
    <div class="stats">
      <table class="custom-table">
        <tr>
          <td>HP</td>
          <td>{{stats[0].base_stat }}</td>
        </tr>
        <tr>
          <td>Attack</td>
          <td>{{stats[1].base_stat }}</td>
        </tr>
        <tr>
          <td>Defense</td>
          <td>{{stats[2].base_stat }}</td>
        </tr>
        <tr>
          <td>Sp. Att.</td>
          <td>{{stats[3].base_stat }}</td>
        </tr>
        <tr>
          <td>Sp. Def.</td>
          <td>{{stats[4].base_stat }}</td>
        </tr>
        <tr>
          <td>Speed</td>
          <td>{{stats[5].base_stat }}</td>
        </tr>
      </table>
    </div>
    
    <div class="genData">
      <table class="custom-table">
        <tr>
          <td>N.º Pokedex:</td>
          <td class="thin">{{ this.id }}</td>
        </tr>
        
        <tr>
          <td>Name:</td>
          <td class="thin">{{ upFirstLetter(this.name) }}</td>
        </tr>
        <tr>
          <td>Type:</td>
          <td>
            <div class="typeData" v-for="item of types" :key="item">
              <img :src="typeToIcon(item.type.name)" :height="40"/>
            </div>
          </td>
        </tr>
      </table>
    </div>

    <div class="abilities">
      <div v-for="item of abilities" :key="item">
        <div v-if="item.is_hidden">
          {{ upFirstLetter(item.ability.name) }} (Hidden)
        </div>
        <div v-if="item.is_hidden == false">
          {{ upFirstLetter(item.ability.name) }}
        </div>
      </div>
    </div>
    <div class="sign1">
      Characteristics
    </div>
    <div class="sign2">
      Main Data
    </div>
    <div class="sign3">
      Abilities
    </div>
  </div>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Pixelify+Sans:wght@400;500;600;700&display=swap');
@media (min-width: 1024px) {
  .data {
    margin-left: -5%;
    overflow: auto;
    align-items: center;
    background-color: white;
    width: 900px;
    height: 95vh;
    font-family: 'Pixelify Sans', sans-serif;
    color: black;

    /* Borde al fondo expandido */
    border: 7px solid #e74c3c; /* Definición del borde (ancho, estilo y color) */
    padding: 5px; /* Espaciado para separar el texto del borde interior */
  }
  .nameImg {
    margin: 20px;
    align-items: center;
    text-align: center;
    position: absolute;
    right: 0;
    top: 0;
    width: 400px;
    height: 400px;
    font-size: 40pt;
  }
  .thin {
    font-weight: 400;
  }
  .bold {
    font-weight: 600;
  }
  .genData {
    margin: 20px;
    gap: 10px;
    position: absolute;
    display: flex;
    flex-direction: column;
    justify-content: center;
    left: 0;
    top: 0;
    font-size: 25pt;
    width: 450px;
    height: 250px;
  }
  .typeData {
    display: inline-block;
  }
  .custom-table {
    border-collapse: separate;
    border-spacing: 10px;
  }

  .custom-table th, .custom-table td {
    padding: 5px;
  }
  .stats {
    margin: 20px;
    position: absolute;
    display: flex;
    flex-direction: column;
    justify-content: center;
    left: 0;
    bottom: 0;
    width: 450px;
    height: 300px;
    font-size: 15pt;
  }
  .abilities {
    margin: 20px;
    align-items: center;
    text-align: center;
    position: absolute;
    right: 0;
    bottom: 0;
    width: 400px;
    height: 150px;
    font-size: 20pt;
  }
  .sign1 {
    margin: 20px;
    align-items: center;
    text-align: left;
    padding-left: 10px;
    background-color: red;
    box-shadow: inset 0 0 15px rgba(0, 0, 0, 0.5);
    position: absolute;
    left: 0;
    bottom: 300px;
    width: 400px;
    height: 40px;
    font-size: 20pt;
    clip-path: polygon(0% 0%, 100% 0%, 80% 100%, 0% 100%);
    color: white;
  }
  .sign2 {
    margin: 20px;
    align-items: center;
    text-align: left;
    padding-left: 10px;
    background-color: red;
    box-shadow: inset 0 0 15px rgba(0, 0, 0, 0.5);
    position: absolute;
    left: 0;
    top: -10px;
    width: 400px;
    height: 40px;
    font-size: 20pt;
    clip-path: polygon(0% 0%, 100% 0%, 80% 100%, 0% 100%);
    color: white;
  }
  .sign3 {
    margin: 20px;
    align-items: center;
    text-align: left;
    padding-left: 10px;
    background-color: red;
    box-shadow: inset 0 0 15px rgba(0, 0, 0, 0.5);
    position: absolute;
    right: 0;
    bottom: 150px;
    width: 350px;
    height: 40px;
    font-size: 20pt;
    clip-path: polygon(0% 0%, 100% 0%, 80% 100%, 0% 100%);
    color: white;
  }
}
</style>
