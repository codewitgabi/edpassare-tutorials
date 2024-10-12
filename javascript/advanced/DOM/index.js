const button = document.getElementById("btn");
const divElement = document.getElementById("div-element");

const boxes = document.getElementsByClassName("box");
const button2 = document.getElementById("btn2");

button.addEventListener("click", () => {
  console.log("Button has been clicked");

  // Check the text content of our button

  button.textContent = "Button has been clicked";

  // Change the styles of div element

  divElement.style.color = "#0000FF";
  divElement.style.backgroundColor = "#FF0000";
});

// Illustration of how javascript interprets the dom

const dom = {
  html: {
    head: {},
    body: {},
  },
};

const boxesIllus = ["box1", "box2", "box3"];

button2.addEventListener("click", () => {
  for (let box of boxes) {
    box.style.color = "#00ff00";
  }
});

// Assignment

/**
 * Create two elements in your html file. ONe should be a button and the other should be a div or span element. THe span element should hold the value of the number of times the button is clicked. This means that once the button you created is clicked, the value of the number of span or div element should be incremented by 1.
 */

// * Solution

const countButton = document.querySelector("#count-button");
const countSpan = document.querySelector("#count");

let count = 0;

countButton.addEventListener("click", () => {
  countSpan.textContent = ++count;
});

// querySelectorAll

const firstBox = document.querySelector(".box");

console.log({ firstBox });

const allBoxes = document.querySelectorAll(".box");

console.log({ allBoxes });
