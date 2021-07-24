<template>
  <div id="User">
    <input v-model="user" placeholder="Usuario" />
    <input v-model="password" type="password" placeholder="Contraseña" />
    <button v-if="user && password" v-on:click="login">Iniciar sesión</button>
    <br>
    <h2 v-if="logueado">
      Hola, <span>{{ userLogeado.user }}</span
      >. ¡Bienvenido! tu id es {{ userLogeado.id }}
    </h2>
    <h2 v-if="mensaje">
      <span>{{mensaje}}</span>
    </h2>
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
      logueado:false,
      mensaje:"",
      userLogeado:{}
    };
  },
  created: function () {},
  methods: {
    login: function () {
      let self = this;
self.logueado=false;
      axios
        .post(`http://localhost/graphql?`,{
			query: ` 
				query ($user:String!, $password:String!){
					userLogin(user: $user, password: $password){
						id,
						user,
            password
					}
				}
			`,
			variables: {
				user: self.user,
				password: self.password
			}
		})
       .then((res) => {
           if(res.data.data.userLogin.length>0){
             self.logueado=true;
             self.userLogeado=res.data.data.userLogin[0];
             self.mensaje="";
           }else{
             self.mensaje="Usuario o contraseña incorrecto!";
           }
         })
         .catch((error) => {
           self.mensaje="";
           self.logueado=false;
           console.error(error);
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