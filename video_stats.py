import requests
import json 
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path='./.env')

api_key=os.getenv("api_key")
channel_handle= "MrBeast"


def get_playlist_id():
    
    try:
        url=f'https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={channel_handle}&key={api_key}'

        response=requests.get(url)
        print(response) 

        data = response.json()
        #print(json.dumps(data,indent=4))

        channel_items=data['items'][0]
        channel_playlistID= channel_items['contentDetails']['relatedPlaylists']['uploads']
        print(channel_playlistID)
        return channel_playlistID
    
    except requests.exceptions.RequestException as e:
        raise e
    
if __name__=="__main__":
    get_playlist_id()
