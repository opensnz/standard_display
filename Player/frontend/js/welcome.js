

// Launch main function
$(document).ready(() => {
    welcome();
});


function welcome()
{
    showOnlineStatusToClient(navigator.onLine)

    window.addEventListener('online', () => {
        showOnlineStatusToClient(true);
    });
     
    window.addEventListener('offline', () => {
        showOnlineStatusToClient(false);
    });

    document.addEventListener('passcode', (event) => {
        message = event.detail;
        showPasscodeToClient(message.player.passcode);
    });

    
}


function connectingToServer()
{
    injectJSFile("./js/localConnection.js");
    injectJSFile("./js/remoteConnection.js");
}
 

function showOnlineStatusToClient(status)
{
    var msg1Div = document.getElementById('message-1');
    var msg2Div = document.getElementById('message-2');
    msg1Div.style.fontWeight = "bold";
    msg2Div.style.fontWeight = "bold";
    if(status)
    {
        msg1Div.innerHTML = Config.ONLINE.MSG;
        msg1Div.style.color = Config.ONLINE.COLOR;
        msg2Div.innerHTML = Config.SERVER.ONLINE;
        connectingToServer();
    }else{
        msg1Div.innerHTML = Config.OFFLINE.MSG;
        msg1Div.style.color = Config.OFFLINE.COLOR;
        msg2Div.innerHTML = Config.SERVER.OFFLINE;
    }
}

function showActivatedStatusToClient()
{
    var msg1Div = document.getElementById('message-1');
    var msg2Div = document.getElementById('message-2');
    msg1Div.style.color = "";
    msg1Div.style.fontWeight = "";
    msg1Div.innerHTML = Config.PLAYER.ACTIVATED;
    msg2Div.style.fontWeight = "bold";
    msg2Div.innerHTML = Config.PLAYER.SYNC;
}

function showPasscodeToClient(passcode)
{
    var msg1Div = document.getElementById('message-1');
    var msg2Div = document.getElementById('message-2');
    msg1Div.style.color = "";
    msg1Div.style.fontWeight = "";
    msg1Div.innerHTML = "Allez sur <b>la plateforme</b> et utilisez le code ci-dessous pour ajouter cet écran"
    msg2Div.style.fontWeight = "bold";
    msg2Div.innerText = passcode;
}


const Config = {
    ONLINE : {
        MSG : "Réseau connecté",
        COLOR : "green",
    },
    OFFLINE : {
        MSG : "Réseau non connecté",
        COLOR : "red",
    },
    SERVER :
    {
        ONLINE : "Chargement<br><div class=\"loader\"></div>",
        OFFLINE : "Veuillez-vous connecter à Internet",
    },
    PLAYER :
    {
        ACTIVATED : "Cet écran a été bien ajouté <br> Téléchargement des contenus en cours",
        SYNC : "Synchronisation<br><div class=\"loader\"></div>",
    }
}

