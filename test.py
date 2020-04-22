import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys
import pprint

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

if len(sys.argv) > 1:
    search_str = sys.argv[1]
else:
    search_str = 'Drake'

result = sp.search(q=search_str, limit =5)
#pprint.pprint(result)
 
for idx, track in enumerate(result['tracks']['items']):
	print('artists  : ' + track['album']['artists'][0]['name'])
	print('track    : ' + track['name'])
	print('cover art: ' + track['album']['images'][0]['url'])