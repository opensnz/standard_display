const BODY_CONTENT = `
<div id="video-player" class="home">
    <video id="video" class="myVideo">
      <source id="video-source" src="" type="video/mp4">
      Votre navigateur ne supporte pas la balise vidéo.
    </video>
</div>
`

let videos = []
let currentVideoIndex = 0;
function playlist(message)
{
    document.body.innerHTML = BODY_CONTENT
    injectCSSFile("./css/style.css")
    var video = document.getElementById('video')
    var source = document.getElementById('video-source');
    videos.push({"src":message[message.type].link})
    source.src = videos[currentVideoIndex].src;
    video.load();
    video.play()

    video.onended = function(){
        if(currentVideoIndex === videos.length - 1) {
            currentVideoIndex = 0;
        } else {
            currentVideoIndex++;
        }
        source.src = videos[currentVideoIndex].src;
        video.load();
        video.play();
    };

}


// listen for the event
document.addEventListener('playlist', function (event) {
    message = event.detail
    console.log("Playlist Event", message)
    playlist(message)
}, false);