//important to check
//https://developer.mozilla.org/en-US/docs/Web/API/Document

//window is the top most dom
console.log(window);
//single elements
console.log(document.getElementById("my-form"));
// recommended
console.log(document.querySelector(".container")); // replaces jquery (only selects the first one)

//multiple elements (recommend querySelectorAll)
// .(class)
console.log(document.querySelectorAll(".item")); //node list (works with array methods)

const items = document.querySelectorAll(".item");
items.forEach((item) => console.log(item));

//manipulating the DOM/changing the DOM
const ul = document.querySelector(".items");
//ul.remove() //removes the dom elements from sight
//ul.lastElementChild.remove()
ul.firstElementChild.textContent = "Hello";
ul.children[1].innerText = "Brad";
ul.lastElementChild.innerHTML = "<h1>Hero</h1>";

const btn = document.querySelector(".btn");
btn.style.background = "red"; //normally done through CSS but this allows for dynamic events

//add event listener
/*
btn.addEventListener('click', (e:Event) => {
    e.preventDefault()//prevents submitting the form
    //console.log(e) //really cool, shows mouse event, and alot of other propreties
    //console.log(e.target.class); // provides all the different attributes


    //https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector
    document.querySelector('#my-form').style.background = '#ccc'
    document.querySelector('body').classList.add("bg-dark")
    document.querySelector('.items').lastElementChild.innerHTML = '<h1>Herrrrrro</h1>'
    console.log('click');    
})
*/
const myForm = document.querySelector("#my-form");
const nameInput = document.querySelector("#name");
const emailInput = document.querySelector("#email");
const msg = document.querySelector(".msg");
const userList = document.querySelector("#users");

//we wait for an event
myForm.addEventListener("submit", (e: Event) => {
    e.preventDefault();
    if(nameInput.value === '' || emailInput.value === '') {
        //alert are not recommended
        //alert('please enter field')
        msg.classList.add('error')
        msg.innerHTML = 'Please enter all fields'
        setTimeout(()=> msg.remove(), 3000)
    } else {
        const li = document.createElement('li')
        li.appendChild(document.createTextNode(`${nameInput.value} : ${emailInput.value}`))
        userList.appendChild(li)
        //clear fiuels
        nameInput.value = ''
        emailInput.value = ''
        console.log('success')
        //you need a backend to save the info otherwise at reload it will disapear
    }
    //console.log(nameInput.value);
});
