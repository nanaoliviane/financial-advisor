// static/js/script.js

document.addEventListener("DOMContentLoaded", function() {
    console.log("JavaScript is loaded and working!");

    // Example function to show how JS works
    function displayMessage(message) {
        alert(message);
    }

    // Add an event listener to a button or any element (if required)
    let button = document.getElementById("myButton");
    if (button) {
        button.addEventListener("click", function() {
            displayMessage("Button was clicked!");
        });
    }
});
