
const BODY_CONTENT =   `<div id="home" class="home">
                            <div id="slider-container" class="slider-container">
                                <div id="slide-number" class="slide-number"></div>
                            </div>
                            <span id="prev" class="prev"></span>
                            <span id="indicators" class="indicators"></span>
                            <span id="next" class="next"></span>  
                        </div>`

// global variables

var imageContainer;
var allImages = [];
var allImageSources = [];
var currentImageIndex = 0;
var duration = 2000;
var durationHandler = 0;
var j = 1;
// Get Slider Items | Array.form [ES6 Feature]
var sliderImages;

// Get Number Of Slides
var slidesCount;

// Set Current Slide
var currentSlide;

// Slide Number Element
var slideNumberElement;

// Previous and Next Buttons
var nextButton;
var prevButton;
// Get The New Created UL
var paginationCreatedUl  ;

// Get Pagination Items | Array.form [ES6 Feature]
var paginationsBullets ;

// Launch main function
$(document).ready(() => {
    image();
});


function image()
{
    // listen for the event
    
    document.addEventListener('image', function (event) {
        message = event.detail;
        if(durationHandler != 0)
        {
            clearInterval(durationHandler);
            console.log("clearInterval");
        }
        duration = message["duration"];
        imageStart(message[message.type]);
    }, false);

}


                
function imageStart(sources)
{
    document.body.innerHTML = BODY_CONTENT;    
    imageContainer = document.getElementById('slider-container');
    allImageSources = sources;
    sources.forEach(function(src, index) {
        var imageElement = document.createElement('img');
        imageElement.alt = "";
        imageElement.decoding = "async";
        imageElement.src = src;
        imageContainer.appendChild(imageElement);
    
    });


    // Get Slider Items | Array.form [ES6 Feature]
    sliderImages = Array.from(document.querySelectorAll('.slider-container img'));

    // Get Number Of Slides
    slidesCount = sliderImages.length;

    // Set Current Slide
    currentSlide = 1;

    // Slide Number Element
    slideNumberElement = document.getElementById('slide-number');

    // Previous and Next Buttons
    nextButton = document.getElementById('next');
    prevButton = document.getElementById('prev');

    // Handle Click on Previous and Next Buttons
    nextButton.onclick = nextSlide;
    prevButton.onclick = prevSlide;

    // Create The Main UL Element
    paginationElement = document.createElement('ul');

    // Set ID On Created Ul Element
    paginationElement.setAttribute('id', 'pagination-ul');

    // Create List Items Based On Slides Count
    for (var i = 1; i <= slidesCount; i++) {

        // Create The LI
        var paginationItem = document.createElement('li-1');

        // Set Custom Attribute
        //paginationItem.setAttribute('data-index', i);

        // Set Item Content
        //paginationItem.appendChild(document.createTextNode(i));
        
        paginationElement.appendChild(paginationItem);

    }

    // Add The Created UL Element to The Page
    document.getElementById('indicators').appendChild(paginationElement);

    // Get The New Created UL
    paginationCreatedUl = document.getElementById('pagination-ul');

    // Get Pagination Items | Array.form [ES6 Feature]
    paginationsBullets = Array.from(document.querySelectorAll('#pagination-ul li'));

    // Loop Through All Bullets Items
    for( var i = 0 ;i < paginationsBullets.length; i++ ) {

        paginationsBullets[i].onclick = function () {

            currentSlide = parseInt(this.getAttribute('data-index'));

            theChecker();

        }

    }

    // Trigger The Checker Function
    theChecker();
    durationHandler = setInterval(nextSlide, duration);


}

    




// functions



// Next Slide Function
function nextSlide() {
    //console.log("duration", duration);
    if (nextButton.classList.contains('disabled')) {
        //setInterval("nextSlide(1)", 2000);
        // Do Nothing
        return false;

    } else {

        currentSlide++;

        theChecker();

    }
}


// Previous Slide Function
function prevSlide() {

    if (prevButton.classList.contains('disabled')) {

        // Do Nothing
        return false;

    } else {

        currentSlide--;

        theChecker();

    }

}

// Create The Checker Function
function theChecker() {

    // Set The Slide Number
    ///slideNumberElement.textContent = 'Slide #' + (currentSlide) + ' of ' + (slidesCount);

    // Remove All Active Classes
    removeAllActive();

    // Set Active Class On Current Slide
    sliderImages[currentSlide - 1].classList.add('active');

    // Set Active Class on Current Pagination Item
    paginationCreatedUl.children[currentSlide - 1].classList.add('active');

    // Check if Current Slide is The First
    if (currentSlide == 1) {

        // Add Disabled Class on Previous Button
        prevButton.classList.add('disabled');

    } else {

        // Remove Disabled Class From Previous Button
        prevButton.classList.remove('disabled');

    }

    // Check if Current Slide is The Last
    if (currentSlide == slidesCount) {

        // Add Disabled Class on Next Button
        //nextButton.classList.add('disabled');
        currentSlide = 0;
    } else {

        // Remove Disabled Class From Next Button
        nextButton.classList.remove('disabled');

    }

}

// Remove All Active Classes From Images and Pagination Bullets
function removeAllActive() {

    // Loop Through Images
    sliderImages.forEach(function (img) {

        img.classList.remove('active');

    });

    // Loop Through Pagination Bullets
    //paginationsBullets.forEach(function (bullet) {

        //bullet.classList.remove('active');

    //});

}