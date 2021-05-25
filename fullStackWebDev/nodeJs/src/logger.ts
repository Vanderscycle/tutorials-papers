const EvenEmitter = require("events");
const uuid = require("uuid"); //creates random id format

console.log(uuid.v4());
class Logger extends EvenEmitter {
    log(msg) {
        //call event
        this.emit("message", { id: uuid.v4(), msg }); //we are extending the .emit that is found in event_demo
    }
}
// to export
//module.exports = Logger


// import  Logger from "./logger";
//instantiate the class
const logger = new Logger()
logger.on('message',(data) => console.log("Called Listener"  data))
logger.log('Hello World')
logger.log('Hi')
logger.log('Another One')

