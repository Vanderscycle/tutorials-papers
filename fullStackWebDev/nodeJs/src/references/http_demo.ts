const http = require('http')

// Create server object
http.createServer((req, res) => {
    //write response
    res.write('hello World')
    res.end()
}).listen(4000, () => console.log("Server running .."))
