const http = require("http");
const path = require("path");
const fs = require("fs");

//Creating a server (that get a request and response)
const server = http.createServer((req, res) => {
    // Build file path
    // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator
    let filePath = path.join(
        __dirname,
        "public",
        req.url === "/" ? "index.html" : req.url
    );
    // extension of file
    let extname = path.extname(filePath);

    // Initial content type
    let contentType = "text/html";

    //check ext and set content type
    switch (extname) {
        case ".js":
            contentType = "text/javascript";
            break;
        case ".css":
            contentType = "text/css";
            break;
        case ".json":
            contentType = "application/json";
            break;
        case ".png":
            contentType = "image/png";
            break;
        case ".jpg":
            contentType = "image/jpg";
            break;
    }
    // Check if contentType is text/html but no .html file extension
    if (contentType == "text/html" && extname == "") filePath += ".html";

    // log the filePath
    //read File
    fs.readFile(filePath, (err, content) => {
        if (err) {
            if (err.code == "ENOENT") {
                //page not found
                fs.readFile(
                    path.join(__dirname, "public", "404.html"),
                    (err, content) => {
                        res.writeHead(200, { contentType: "text/html" });
                        res.end(content, "utf8");
                    }
                );
                //different error
            } else {
                //some server error
                res.writeHead(500);
                res.end(`Server Error ${err.code}`);
            }
        } else {
            // success response
            res.writeHead(200, { contentType: contentType });
            res.end(content, "utf8");
        }
    });
});
const PORT = process.env.PORT || 4000;
server.listen(PORT, () => console.log(`Server running on ${PORT}`));
