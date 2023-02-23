
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
        case 'playlist':
            handleMessagePlaylist(message);
            break;
        case 'screenshot':
            toLocalServer(message);
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

    if(message.player.activated === false){
        // dispatch 'passcode' event to show passcode to client
        document.dispatchEvent(new CustomEvent('passcode', {detail:message}));
    }else{
        // localSocket.send(JSON.stringify({"type":"playlist", "playlist":
        // [
        //     {
        //         "uuid": "aea79b0e-952a-4951-8d25-f40b7ee5282a",
        //         "extension": ".mp4",
        //         "link": "http://192.168.1.88:8000/media/download/aea79b0e-952a-4951-8d25-f40b7ee5282a",
        //     },
        //     {
        //         "uuid": "61cebcee-70da-4897-bb01-44497201f0dc",
        //         "extension": ".mp4",
        //         "link": "http://192.168.1.88:8000/media/download/61cebcee-70da-4897-bb01-44497201f0dc",
        //     },
        //     {
        //         "uuid": "ef2a3840-86bf-4632-bff7-49ff46004bb8",
        //         "extension": ".mp4",
        //         "link": "http://192.168.1.88:8000/media/download/ef2a3840-86bf-4632-bff7-49ff46004bb8",
        //     }
        // ]
        // }));
        localSocket.send(JSON.stringify({"type":"image", "image":

        [
            "C:/Users/Dev1/Desktop/Repository/standard_display/Player/frontend/image1.jpg",
            "C:/Users/Dev1/Desktop/Repository/standard_display/Player/frontend/image2.jpg",
            "C:/Users/Dev1/Desktop/Repository/standard_display/Player/frontend/image3.jpg",
        ]

        }));
    }
}


function handleMessagePlaylist(message)
{
    // dispatch 'player' event to launch the playlist
    document.dispatchEvent(new CustomEvent('playlist', {detail:message}));
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
    document.dispatchEvent(new CustomEvent('image', {detail:message}));
}