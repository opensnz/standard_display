

function injectJSFile(filePath)
{
    if (!document.querySelector("script[src='"+filePath+"']")) {
        var script = document.createElement('script');
        script.setAttribute("type", "text/javascript");
        script.setAttribute("src", filePath);
        document.head.appendChild(script);
    }
}

function injectCSSFile(filePath)
{
    if(!document.querySelector("link[rel='stylesheet'][href='"+filePath+"']")){
        var link = document.createElement("link");
        link.setAttribute("rel", "stylesheet");
        link.setAttribute("href", filePath);
        document.head.appendChild(link);
    }

}


function removeJSFile(filePath)
{

}

function removeCSSFile(filePath)
{


}


