
function handleLocalConnection(message)
{
    switch (message.type) {
        case 'player':
            handleMessagePlayer(message);
            break;
        case 'playlist':
            handleMessagePlaylist(message);
            break;
        case 'screenshot':
            toRemoteServer(message);
            break;
        case 'image':
            handleMessageImage(message);
            break;
        default:
            break;
    }
}

function handleRemoteConnection(message)
{
    switch (message.type) {
        case 'activation':
            handleMessageActivation(message);
            break;
        default:
            // Send data to Local Server
            toLocalServer(message);
            break;
    }
}


function handleMessagePlayer(message)
{
    // dispatch 'player' event to connect to remote server
    document.dispatchEvent(new CustomEvent('player', {detail:message}));
    console.log(message);
    if(message.player.activated === false){
        // dispatch 'passcode' event to show passcode to client
        document.dispatchEvent(new CustomEvent('passcode', {detail:message}));
    }
}


function handleMessagePlaylist(message)
{
    injectJSFile("./js/playlist.js");
    injectCSSFile("./css/playlist.css");
    // dispatch 'player' event to launch the playlist
    setTimeout(
        function(){
            document.dispatchEvent(new CustomEvent('playlist', {detail:message}));
        }, 100
    )
}

function handleMessageActivation(message)
{
    showActivatedStatusToClient();
    // Send data to Local Server
    toLocalServer(message);
}

function handleMessageImage(message)
{

    injectJSFile("./js/image.js");
    injectCSSFile("./css/image.css");
    // dispatch 'image' event to launch the slider
    setTimeout(
        function(){
            document.dispatchEvent(new CustomEvent('image', {detail:message}));
        }, 100
    )
}