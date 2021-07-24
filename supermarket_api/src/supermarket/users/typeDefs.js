export const userTypeDef = `
  type User {
      id: Int!
      name: String!
      email: String!
  }
  type user {
    id: Int!
    name: String!
    email: String!
  }  
  input UserInput {
      name: String!
      email: String!  
  }

  `;
 
export const userQueries = `
      allUsers: [User]!
      userById(id: Int!): User!
  `;

export const userMutations = `
    createUser(user: UserInput!): User!
    updateUser(id: Int!, user: UserInput!): User!
    deleteUser(id: Int!): Int
`;


// query {
//     allUsers {
//       name,
//       description,
//       user{id,name,description},
//       unit_measurement,
//       quantity
      
      
//     }
//   }


// mutation {
//   createUser(user: {
//     name: "papel",
//     description: "papel dasdasdasd",
//     user:2,
//     unit_measurement:"Units"
//     quantity:10
//   }) {
//     name
    
//   }
// }
