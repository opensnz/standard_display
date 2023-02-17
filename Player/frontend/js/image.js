const BODY_CONTENT_IMAGE = `<div id="home" class="home">
                                <div id="image-container" class="image-container">
                                
                                </div>
                            </div>`
var imageContainer;
var allImages = [];
var imageSources = [];
var currentImageIndex = 0;

// Launch main function
$(document).ready(() => {
    image();
});


function image()
{
    // listen for the event
    document.addEventListener('image', function (event) {
        message = event.detail;
        imageStart(message[message.type]);
    }, false);
}


function imageStart(sources)
{
    document.body.innerHTML = BODY_CONTENT_IMAGE;
    imageContainer = document.getElementById('image-container');
    allSources = sources;

    setInterval(function(){
    
    }, 100000);
}



