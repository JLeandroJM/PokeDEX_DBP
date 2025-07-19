import { defineStore, acceptHMRUpdate } from "pinia";

export const useUserStore = defineStore({
  id: "user",
  state: () => ({
    name: "",
    email: "",
    favorites: [],
  }),

  actions: {
    logout() {
      this.name = "";
      this.email = "";
      // we could do other stuff like redirecting the user
    },
    /**
     * Attempt to login a user
     * @param {string} user
     */
    async login(user) {
      this.name = user;
      this.email = this.name + "@utec.edu.pe";
      this.favorites = JSON.parse(localStorage.getItem(user)) || [];
    },
    isAuthenticated() {
      return this.name !== "";
    },
    addFavorite(favorite) {
      this.favorites.push(favorite);
      localStorage.setItem(this.name, JSON.stringify(this.favorites));
    },
    removeFavorite(favorite) {
      this.favorites = this.favorites.filter((item) => item !== favorite);
      localStorage.setItem(this.name, JSON.stringify(this.favorites));
    },
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useUserStore, import.meta.hot));
}

//export default useUserStore;
