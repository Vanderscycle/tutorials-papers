function showToDo(todo: { title: string; text: string }) {
    console.log(todo.title + ": " + todo.text);
}
let myTodo = { title: "trash", text: "take out trash" };

showToDo(myTodo);
//interface (custom data types)
//https://www.educative.io/blog/typescript-interfaces
interface Todo {
    title: string;
    text: string;
}

function interfaceToDo(todo: Todo) {
    console.log(todo.title + ": " + todo.text);
}
interfaceToDo(myTodo);
