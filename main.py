import requests, time
import lyricsgenius as lg
from pprint import pprint
from refresh import Refresh
from json import JSONDecodeError
from secrets import genius_access_token

SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'

def get_current_track():
    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        }
    )
    json_resp = response.json()

    track_id = json_resp['item']['id']
    track_name = json_resp['item']['name']
    artists = [artist for artist in json_resp['item']['artists']]

    link = json_resp['item']['external_urls']['spotify']

    artist_names = ', '.join([artist['name'] for artist in artists])

    current_track_info = {
    	"id": track_id,
    	"track_name": track_name,
    	"artists": artist_names,
    	"link": link
    }

    return current_track_info

def lyrics(song, artist):
    genius = lg.Genius(genius_access_token)
    song = genius.search_song(title=song, artist=artist)
    try:
    	lyrics = song.lyrics
    	print(lyrics)
    	print('\n')
    except AttributeError:
    	print("There are no lyrics for this song on Genius")
    	print('\n')

def main():
	current_track_id = None
	while True:
		try:
			current_track_info = get_current_track()
	
			if current_track_info['id'] != current_track_id:
				pprint(
					current_track_info,
					indent=4,
				)
				current_track_id = current_track_info['id']
				print('\n')
				lyrics(current_track_info['track_name'], current_track_info['artists'])

			time.sleep(1)
		except (JSONDecodeError, TypeError):
			time.sleep(1)
			
if __name__ == '__main__':
	ACCESS_TOKEN = str(Refresh().refresh())
	main()