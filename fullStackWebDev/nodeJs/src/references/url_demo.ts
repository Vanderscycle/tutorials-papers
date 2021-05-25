const url = require("url");
//https://nodejs.org/api/url.html // reference
const myUrl = new URL("http://mywebsite.com/hello.html?id=100&status=active");

//serialized URL
console.log(myUrl.href);

//Host (root Domain)
console.log(myUrl.host);

//Hostname ( does not get port)
console.log(myUrl.hostname);

// Pathname
console.log(myUrl.pathname);

//serialized query
console.log(myUrl.search);

//Params object
console.log(myUrl.searchParams);

//add Param
myUrl.searchParams.append("abs", "123");
console.log(myUrl.searchParams);

//loop throught params
myUrl.searchParams.forEach((value,name) => console.log(`${name}: ${value}`))
