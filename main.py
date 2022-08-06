import threading, requests, time
from pprint import pprint
from refresh import Refresh

SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'

def main():
	current_track_id = None
	while True:
		response = requests.get(
			SPOTIFY_GET_CURRENT_TRACK_URL,
			headers={
			    "Authorization": f"Bearer {ACCESS_TOKEN}"
			}
		)
		json_resp = response.json()
			
if __name__ == '__main__':
	ACCESS_TOKEN = str(Refresh().refresh())
	main()