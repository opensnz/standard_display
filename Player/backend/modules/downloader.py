import os, json, requests

def download_playlist(data : dict) -> dict:
    medias = data[data["type"]]
    playlist = []
    for media in medias :
        filename = media["uuid"]
        extension = media["extension"]
        path = os.getenv('FRONTEND_DIR') + "media/" + filename + extension
        # Download only if media not exists
        if not os.path.exists(path):
            response = requests.get(media["link"], allow_redirects=True)
            open(path, 'wb').write(response.content)
            print("Downloading")
        playlist.append(path)
    data.clear()
    data["type"] = "playlist"
    data["playlist"] = playlist
    return data