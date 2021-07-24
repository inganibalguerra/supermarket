export const userTypeDef = `
  type User {
      id: Int!
      user: String!
      password: String!
  }
  input UserInput {
      user: String!
      password: String!  
  }

  `;

export const userQueries = `
      allUsers: [User]!
      userLogin(user: String!,password: String!): [User]!
  `;


export const userMutations = `
    createUser(user: UserInput!): User!
    updateUser(id: Int!, user: UserInput!): User!
    deleteUser(id: Int!): Int
`;


// query {
//     allUsers {
//       user,
//       description,
//       user{id,user,description},
//       unit_measurement,
//       quantity
      
      
//     }
//   }


// mutation {
//   createUser(user: {
//     user: "papel",
//     description: "papel dasdasdasd",
//     user:2,
//     unit_measurement:"Units"
//     quantity:10
//   }) {
//     user
    
//   }
// }
