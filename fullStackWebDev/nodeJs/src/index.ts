console.log("Hello World");
// acceptable import method
//const person = require('./person')
//console.log(person)

// better import method
//import { Person } from "./person"; //funny thing, node doesn't support import but since TS converts to JS we have no such issue
//const person = new Person("Bro", 641);
//person.greeting();

const http = require("http");
const path = require("path");
const fs = require("fs");

const server = http.createServer((req, res) => {
    console.log(req.url);
    if (req.url === "/") {
        fs.readFile(
            path.join(__dirname, "public", "index.html"),
            (err, content) => {
                //if (err) throw err;
                res.writeHead(200, { "Content-Type": "Text/HTML" });
                res.end(content);
                // old type for testing
                //res.end("<h1>Homepage Yooo</h1>");
            }
        );
    }
//current state
//https://www.youtube.com/watch?v=fBNz5xF-Kx4&t=1764s
    if (req.url === "/about") {
        fs.readFile(
            path.join(__dirname, "public", "about.html"),
            (err, content) => {
                //if (err) throw err;
                res.writeHead(200, { "Content-Type": "Text/HTML" });
                res.end(content);
                // old type for testing
                //res.end("<h1>Homepage Yooo</h1>");
            }
        );
    }
});

const PORT = process.env.PORT || 4000;
server.listen(PORT, () => console.log(`Server running on ${PORT}`));
