const fs = require('fs')
const path = require('path')

//create folder
// fs.mkdir(
//    path.join(__dirname, "/test"), {}, (err) => {
//        if (err) throw err;
//        console.log("folder created ..");
//    }); //default async

//Create and write to file
// fs.writeFile(
//     path.join(__dirname, "/test","hello.text"), "hello World!", (err) => {
//         if (err) throw err;
//         console.log("file written to ..");
// 
//         //append to file
//         fs.appendFile(
//             path.join(__dirname, "/test","hello.text"), " I love node JS!", (err) => {
//                 if (err) throw err;
//                 console.log("file written to ..");
//             }); //default async
//     }); //default async

//read file 
fs.readFile(
    path.join(__dirname, "/test","hello.text"), 'utf8', (err, data) => {
        if (err) throw err;
        console.log(data);
    }); //default async

//rename a file 
fs.rename(
    path.join(__dirname, "/test","hello.text"), path.join(__dirname, "/test", 'helloworld.txt'), (err) => {
        if (err) throw err;
        console.log("file renamed ..");
    }); //default async
