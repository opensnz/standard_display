const BACKEND_LOCAL_SERVER = "ws://localhost:8080"
let localSocket;


// Launch main function
$(document).ready(() => {
    localConnection();
});


function localConnection()
{
    localSocket = new WebSocket(BACKEND_LOCAL_SERVER);
    injectJSFile("./js/connectionHandler.js")
    //injectJSFile("./js/playlist.js");
    //injectCSSFile("./css/playlist.css");
    registerLocalEventHandlers();
}


function registerLocalEventHandlers() {
    localSocket.onopen = function() {
        console.info("Local WebSocket opened");
        localSocket.send(JSON.stringify({"type": "player", "player": "frontend"}));
        localSocket.send(JSON.stringify({"type": "telemetry"}));
    };

    localSocket.onmessage = function(event) {
        var message = JSON.parse(event.data);
        console.log("Local WebSocket message:", message);
        handleLocalConnection(message);
    };

    localSocket.onclose = function(){
        console.info("Local WebSocket closed");
        // Reconnect will be attempted in 100 miliseconds
        setTimeout(reconnectToLocalServer, 100);
    };

    localSocket.onerror = function(){
        console.info("Local WebSocket error");
        // Close the connection
        localSocket.close();
    }
}

  
function toRemoteServer(message)
{
    remoteSocket.send(JSON.stringify(message));
}


function reconnectToLocalServer() {
    if (localSocket.readyState === WebSocket.CLOSED || localSocket.readyState === WebSocket.CLOSING) {
        // Connection is lost, attempt to reconnect
        localSocket = new WebSocket(BACKEND_LOCAL_SERVER);
        registerLocalEventHandlers();
    }
}




