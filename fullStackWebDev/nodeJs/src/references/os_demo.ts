const os = require("os");
// https://nodejs.org/api/os.html // reference
// Platform
console.log(os.platform());

//CPU Arch
console.log(os.arch());

//CPU Core Info
console.log(os.cpus())

// Free memory
console.log(os.freemem())

// Total memory
console.log(os.totalmem())

//uptime
//console.log(os.uptime)
