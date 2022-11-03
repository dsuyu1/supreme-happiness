window.addEventListener("load", function ()
{
    // get click element references.
    let clickCounterElement = document.getElementById("click-counter"); 
    let clickButtonElement = document.getElementById('click-button');

    

    // counter value 
    let counter = 0;

    // click button function
    let clickButtonFunction = function ()
    {
        // increment counter.
        counter++; 

        // update counter value
        clickCounterElement.innerHTML = counter;
    }; 

    // attach button function
    clickButtonElement.addEventListener('click', clickButtonFunction);
}); 