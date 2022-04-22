import requests
import config
import sample_ids
from pprint import pprint

"""
note: To access user related api endpoints,
      need to use different auth method than client_credentials
"""

# Authentication
auth_res = requests.post(config.AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': config.CLIENT_ID,
    'client_secret': config.CLIENT_SECRET
})

# Get the access token
access_token = auth_res.json()['access_token']

# Create headers for the request with access token
headers = {
    'Authorization': 'Bearer ' + access_token
}

########## MARKET ####################################

def get_available_market():
    """
        Get the available markets
        input: none
        output: list of market objects(country_code)

    """
    available_market_res = requests.get(f'{config.BASE_URL}/markets',
                                        headers=headers)
    return available_market_res.json()  

pprint(get_available_market())


########## ALBUM ######################################

def get_album(album_id):
    """
        Get catalog information for a single album
        input: album_is: album id (string)
        output: album object
        Query Parameters: market: Country: ISO 3166-1 alpha-2 country code.
    """
    album_res = requests.get(f'{config.BASE_URL}/albums/{album_id}',
                             headers=headers)
    return album_res.json()


def get_albums(album_ids):
    """
        Get catalog information for multiple albums
        input: album_ids: list of album ids (string)
        output: list of album objects
        Query Parameters: market: Country: ISO 3166-1 alpha-2 country code.
        limit: 20 albums per request
    """
    albums_res = requests.get(f'{config.BASE_URL}/albums?ids={album_ids}', 
                              headers=headers)
    return albums_res.json()


def get_album_tracks(album_id):
    """
        Get catalog information for album tracks
        input: album_id: album id (string)
        output: list of track objects
        Query Parameters: market: Country: ISO 3166-1 alpha-2 country code.
                          limit: integer (0-50) default: 20
    """
    album_track_res = requests.get(f'{config.BASE_URL}/albums/{album_id}/tracks',
                                   headers=headers)
    return album_track_res.json()


def get_new_releases():
    """
        Get the new releases
        input: none
        output: list of album objects
        Query Parameters: limit: integer (0-50) default: 20
                          country: Country: ISO 3166-1 alpha-2 country code.
                          offset: integer  default: 0
    """
    new_releases_res = requests.get(f'{config.BASE_URL}/browse/new-releases',
                                    headers=headers)
    return new_releases_res.json()


########## ARTIST ######################################






























def get_track_info(track_id):
    """
    Get the track information using track id
    """
    track_res = requests.get(config.BASE_URL + 'tracks/' + track_id, headers=headers)
    return track_res.json()


def get_audio_features(track_id):
    """
    Get the audio features of the track using track id
    """
    audio_features_res = requests.get(config.BASE_URL + 'audio-features/' + track_id, headers=headers)
    return audio_features_res.json()


def get_audio_analysis(track_id):
    """
    Get the audio analysis of the track using track id
    """
    audio_analysis_res = requests.get(config.BASE_URL + 'audio-analysis/' + track_id, headers=headers)
    return audio_analysis_res.json()