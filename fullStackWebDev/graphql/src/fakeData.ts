interface User {
    name: string
    age: number
    married: boolean
}
interface User extends Array<User> {}

let users: User= [
    {
        name: "bob McChad",
        age: 69,
        married: false
    },
    {
        name: "Stoner McChad",
        age: 420,
        married: false
    }
]
