<template>
  <div id="Products">
    <h2>
      Usuario autenticado: <span>{{ username }}</span>
    </h2>
    <button v-on:click="getProducts">Obtener productos</button>
    <table v-if="products">
      <tr>
        <th>Id</th>
        <th>Name</th>
        <th>Description</th>
        <th>Unit Measurement</th>
        <th>Quantity</th>
      </tr>
      <tr v-bind:key="product.id" v-for="product in products">
        <td>{{product.id}}</td>
        <td>{{product.name}}</td>
        <td>{{product.description}}</td>
        <td>{{product.unit_measurement}}</td>
        <td>{{product.quantity}}</td>
      </tr>
    </table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Products",

  data: function () {
    return {
      products: [],
    };
  },

  created: function () {
    this.username = this.$route.params.username;
    let self = this;
  },

  methods: {
    getProducts: function () {
      this.username = this.$route.params.username;
      let self = this;

      axios
        .get("http://localhost:4000/products")
        .then((result) => {
          self.products = result.data;
        })
        .catch((error) => {
          alert("ERROR de Servidor");
        });
    },
  },
};
</script>

<style>
#Products {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
#Products h2 {
  font-size: 25 px;
  color: #283747;
}
#Products span {
  color: crimson;
  font-weight: bold;
}
</style>