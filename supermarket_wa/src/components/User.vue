<template>
  <div id="User">
    <h2>
      Hola, <span>{{ username }}</span
      >. ¡Bienvenido!
    </h2>
    <input v-model="user" placeholder="Usuario" />
    <input v-model="password" type="password" placeholder="Contraseña" />
    <button v-if="user && password" v-on:click="login">Iniciar sesión</button>
  </div>
</template>

<script>
import axios from "axios";
const apiUrl = require("./../grapql/config").apiUrl;
const queries = require("./../grapql/config").queries;

export default {
  name: "User",
  data: function () {
    return {
      username: "none",
      user: "",
      password: "",
    };
  },
  created: function () {},
  methods: {
    login: function () {
      let self = this;

      let id = "5c9beed4a34c1303f3371a39";
            let body =  { 
                query: `
                    query {
            userLogin(user: "anibal",password: "guerra") {
              user
              password
            }
          }
                `, 
                variables: {}
            }
            let options = {
                headers: {
                    'Content-Type': 'application/json'
                }
            }
            axios.post("http://localhost/graphiql",body, options)
                .then((response)=>{
                    console.log(response);
                });


      // axios({
      //   url: "http://localhost/graphiql",
      //   method: "post",
      //   data: {
      //     query: `
      //     query {
      //       userLogin(user: "anibal",password: "guerra") {
      //         user
      //         password
      //       }
      //     }
      //     `,
      //   },
      // })
      //   .then((res) => {
      //     console.log(
      //       "--------------------- Lista de Personajes --------------------------"
      //     );
      //     console.log(res.data);
      //   })
      //   .catch((error) => {
      //     console.error(error);
      //   });
    },
  },
};
</script>

<style>
#User {
  width: 100%;
  height: 100%;

  display: flex;
  justify-content: center;
  align-items: center;
}
#User h2 {
  font-size: 50px;
  color: #283747;
}
#User span {
  color: crimson;
  font-weight: bold;
}
</style>