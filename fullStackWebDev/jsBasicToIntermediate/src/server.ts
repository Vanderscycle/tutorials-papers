import express from "express";

// express node config
const app = express();
const PORT: string | number = process.env.PORT || 4000;

app.use(express.static(__dirname + "/../public/"));
app.use("*/dist",express.static(__dirname + "/../dist/"));

app.get("/", (req, res) => {
    res.sendFile("index.html");
});

app.listen(PORT, () => console.log());
