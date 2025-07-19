import { createRouter, createWebHistory } from "vue-router";
import PokedexView from "../views/Pokedex_leandro.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/pokedex",
      name: "pokedex",
      component: PokedexView,
    },
    {
      path: "/pokedex/:name",
      name: "pokedex-detail",
      component: () => import("../views/PokedexDetailView.vue"),
    },
  ],
});

export default router;
