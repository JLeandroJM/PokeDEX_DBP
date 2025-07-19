<template>
  <div>
    <header>
      <div class="wrapper">
        <nav>
          <RouterLink to="/pokedex">Pokedex</RouterLink>
          <!-- Otras rutas si es necesario -->
        </nav>
      </div>
    </header>

    <RouterView />
  </div>
</template>

<script>
import { RouterLink, RouterView } from "vue-router";

export default {
  components: {
    RouterLink,
    RouterView,
  },
};
</script>


