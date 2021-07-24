module.exports = {
    apiUrl: 'http://localhost/graphiql',
    queries: {
        getLogin: `
        query getuserLogin($user: string!,$password: string!) {
            userLogin (user: $user,password: $password) {
            id
            name
            actor
          }
        }`
    },
    mutations: {
        
    }
}