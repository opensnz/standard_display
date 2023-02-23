const BODY_CONTENT = `<div id="home" class="home">
                        <div id="video-container" class="video-container"></div>
                      </div>`

var videoContainer;
var allVideos = [];
var allSources = [];
var currentVideoIndex = 0;


// Launch main function
$(document).ready(() => {
    playlist();
});


function playlist()
{
    // listen for the event

    document.addEventListener('playlist', function (event) {
        message = event.detail;
        playlistStart(message[message.type]);
    }, false);
}


function playlistStart(sources)
{
    document.body.innerHTML = BODY_CONTENT;    
    videoContainer = document.getElementById("video-container");
    allSources = sources;
    sources.forEach(function(src, index) {
        var videoElement = document.createElement('video');
        videoElement.muted = true;
        videoContainer.appendChild(videoElement);
        allVideos.push(videoElement);
        // Load first and second videos
        if (index === 0 || index === 1) {
            videoElement.src = src;
            videoElement.load();
        } 
        // Set the first and video to be visible and all others to be hidden
        if (index === 0) {
            videoElement.id = "videoID";
            videoElement.classList.add('visible');
            // Launch the playlist
            videoElement.play();
        } else {
            videoElement.classList.add('hidden');
        }
    });

    // Register 'ended' event for each video
    allVideos.forEach(function(video) {
        video.addEventListener('ended', nextVideo);
    });

}


// Play the videos one by one
function nextVideo() {
    // Fade out the current video
    allVideos[currentVideoIndex].classList.remove('visible');
    allVideos[currentVideoIndex].classList.add('hidden');

    // Update the current video index
    currentVideoIndex = currentVideoIndex === allVideos.length - 1 ? 0 : currentVideoIndex + 1;

    // Fade in the next video
    allVideos[currentVideoIndex].classList.remove('hidden');
    allVideos[currentVideoIndex].classList.add('visible');

    // Play
    allVideos[currentVideoIndex].play();
    
    if(allVideos.length >= 3){
        setTimeout(function(currentVideoIndex){
            // Clear previous video
            var previousVideoIndex = currentVideoIndex - 1;
            if(previousVideoIndex === - 1){
                previousVideoIndex =  allVideos.length - 1;
            }
            // This will clear memory
            allVideos[previousVideoIndex].removeAttribute("src");
            allVideos[previousVideoIndex].load();

            // Load next video
            var nextVideoIndex = currentVideoIndex + 1;
            if(nextVideoIndex === allVideos.length){
                nextVideoIndex =  0;
            }
            allVideos[nextVideoIndex].src = allSources[nextVideoIndex];
            allVideos[nextVideoIndex].load();
        }, 100, currentVideoIndex);
    }
}


setInterval(function(){
    toLocalServer({type:"screenshot", screenshot:""});
}, 100000);




