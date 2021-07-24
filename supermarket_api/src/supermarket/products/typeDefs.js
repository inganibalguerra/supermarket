export const productTypeDef = `
  type Product {
      id: Int!
      name: String!
      description: String!
      category: category!
      unit_measurement: String!
      quantity: Int!
  }
  type category {
    id: Int!
    name: String!
    description: String!
  }  
  input ProductInput {
      name: String!
      description: String!  
      category: Int!        
      unit_measurement: String!
      quantity: Int!
  }

  `;
 
export const productQueries = `
      allProducts: [Product]!
      productById(id: Int!): Product!
  `;

export const productMutations = `
    createProduct(product: ProductInput!): Product!
    updateProduct(id: Int!, product: ProductInput!): Product!
    deleteProduct(id: Int!): Int
`;


// query {
//     allProducts {
//       name,
//       description,
//       category{id,name,description},
//       unit_measurement,
//       quantity
      
      
//     }
//   }


// mutation {
//   createProduct(product: {
//     name: "papel",
//     description: "papel dasdasdasd",
//     category:2,
//     unit_measurement:"Units"
//     quantity:10
//   }) {
//     name
    
//   }
// }
