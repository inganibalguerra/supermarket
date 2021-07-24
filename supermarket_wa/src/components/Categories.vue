<template>
  <div id="Categories">
    <h2>
      Usuario autenticado: <span>{{ username }}</span>
    </h2>

    <input v-model="product.category" />
    <input v-model="product.name" />
    <input v-model="product.description" />
    <button
      v-if="product.category && product.name && product.description"
      v-on:click="createCategory"
    >
      Crear categoria
    </button>

    <button v-on:click="getCategory">Obtener categoría</button>
    <input v-model="category_id_rest" />
    <h2>
      La categoría con id = <span>{{ category_id }}</span
      >, tiene el nombre <span>{{ name }}</span> y su descripción es «<span>{{
        description
      }}</span
      >».
    </h2>
  </div>
</template>

<script >
import axios from "axios";

export default {
  name: "Categories",

  data: function () {
    return {
      category_id_rest: "",
      category_id: "",
      name: "",
      description: "",

      product: {},
    };
  },

  created: function () {
    this.username = this.$route.params.username;
    let self = this;
  },

  methods: {
    getCategory: function () {
      this.username = this.$route.params.username;
      let self = this;

      axios
        .get("http://localhost:4000/categories/" + self.category_id_rest)
        .then((result) => {
          self.category_id = result.data.id;
          self.name = result.data.name;
          self.description = result.data.description;
        })
        .catch((error) => {
          self.category_id = null;
          self.name = null;
          self.description = null;
          alert("ERROR de Servidor");
        });
    },
    createCategory: function () {
      this.username = this.$route.params.username;
      let self = this;

      axios
        .post("http://localhost:4000/categories/", self.product)
        .then((result) => {
          (self.category_id_rest = result.data.id),
            (self.category_id = result.data.id),
            (self.name = result.data.name),
            (self.description = result.data.description);
        })
        .catch((error) => {
          alert("ERROR de Servidor");
        });
    },
  },
};
</script>

<style>
#Categories {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
#Categories h2 {
  font-size: 25 px;
  color: #283747;
}
#Categories span {
  color: crimson;
  font-weight: bold;
}
</style>