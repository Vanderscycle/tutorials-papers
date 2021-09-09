const EventEmitter = require('events')
//https://nodejs.org/api/events.html


// Create class
class myEmitter extends EventEmitter { }

//init object
const myEmiter = new myEmitter()

//Event listener
myEmiter.on('event', () => {
    console.log('Event Fired!')
})

// init event
myEmiter.emit('event')
myEmiter.emit('event')
myEmiter.emit('event')
myEmiter.emit('event')
myEmiter.emit('event')
