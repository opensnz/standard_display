const BACKEND_REMOTE_SERVER = 'ws://localhost:8000/player/';
let UUID = '';
let remoteSocket; 


// Launch main function
$(document).ready(() => {
    remoteConnection();
});


function remoteConnection()
{
    window.addEventListener('online', reconnectToRemoteServer);

    // listen for player event
    document.addEventListener('player', function (event) {
        message = event.detail
        UUID = message.player.uuid
        if(remoteSocket === undefined)
        {
            // First connection to remote server
            remoteSocket = new WebSocket(BACKEND_REMOTE_SERVER+UUID);
            registerRemoteEventHandlers();
        } else{
            // Reconnect to remote server
            reconnectToRemoteServer()
        }
    }, false);
}


function registerRemoteEventHandlers() {
    remoteSocket.onopen = function() {
        console.info("Remote WebSocket opened");
    };
    remoteSocket.onmessage = function(event) {
        var message = JSON.parse(event.data);
        console.log("Remote WebSocket message:", message);
        handleRemoteConnection(message);
    };
    remoteSocket.onclose = function(){
        console.info("Remote WebSocket closed");
        // Reconnect will be attempted in 1 second if Player have access to internet
        if(navigator.onLine)
        {
            setTimeout(reconnectToRemoteServer, 1000);
        }
    };
    remoteSocket.onerror = function(){
        console.info("Remote WebSocket error");
        // Close the connection
        remoteSocket.close();
    };
}


function toLocalServer(message)
{
    localSocket.send(JSON.stringify(message));
}


function reconnectToRemoteServer() {
    if (remoteSocket.readyState === WebSocket.CLOSED || remoteSocket.readyState === WebSocket.CLOSING) {
        // Connection is lost, attempt to reconnect
        remoteSocket = new WebSocket(BACKEND_REMOTE_SERVER+UUID);
        registerRemoteEventHandlers();
    }
}
