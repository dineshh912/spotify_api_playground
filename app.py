from webbrowser import get
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

def get_artist(artist_id):
    """
        Get the artist information using artist id
        input: artist_id: artist id (string)
        output: artist object
    """
    artist_res = requests.get(f'{config.BASE_URL}/artists/{artist_id}',
                              headers=headers)
    return artist_res.json()


def get_artists(artist_id):
    """
        Get multiple artist information using artist id
        output: list of artist objects
        Query Parameters: ids: integer (0-50)

    """
    artists_res = requests.get(f'{config.BASE_URL}/artists?ids={artist_id}',
                               headers=headers)
    return artists_res.json()


def get_artist_albums(artist_id):
    """
        Get the albums of the artist using artist id
        input: artist_id: artist id (string)
        output: list of album objects
        Query Parameters: limit: integer (0-50) default: 20
                            offset: integer  default: 0
                            market: Country: ISO 3166-1 alpha-2 country code.
                            include_groups: string (album, single, appears_on, compilation)
    """
    artist_albums_res = requests.get(f'{config.BASE_URL}/artists/{artist_id}/albums',
                                     headers=headers)
    return artist_albums_res.json()


def get_artist_top_tracks(artist_id):
    """
        Get the top tracks of the artist using artist id
        input: artist_id: artist id (string)
        output: list of track objects
        Query Parameters: market: Country: ISO 3166-1 alpha-2 country code.
    """
    artist_top_tracks_res = requests.get(f'{config.BASE_URL}/artists/{artist_id}/top-tracks?country=US',
                                         headers=headers)
    return artist_top_tracks_res.json()


def get_related_artists(artist_id):
    """
        Get related artists based on artist id
        input: artist_id: artist id (string)
        output: list of artist objects
    """
    related_artists_res = requests.get(f'{config.BASE_URL}/artists/{artist_id}/related-artists',
                                       headers=headers)
    return related_artists_res.json()

########## TRACK ######################################

def get_track_info(track_id):
    """
        Get the track information using track id
        input: track_id: track id (string)
    """
    track_res = requests.get(f'{config.BASE_URL}/tracks/{track_id}',
                             headers=headers)
    return track_res.json()
  
    
########## SHOWS ######################################

def get_show(show_id, market):
    """
        Get the show information using show id
        input: show_id: show id (string)
        output: show object
        Query Parameters: market: Country: ISO 3166-1 alpha-2 country code.(required)
    """
    show_res = requests.get(f'{config.BASE_URL}/shows/{show_id}?market={market}',
                            headers=headers)
    return show_res.json()


def get_shows(show_ids, market):
    """
        Get multiple show information using show id
        input: show_ids: list of show ids (string)
        output: list of show objects
        Query Parameters: market: Country: ISO 3166-1 alpha-2 country code.(required)
    """
    shows_res = requests.get(f'{config.BASE_URL}/shows?ids={show_ids}&market={market}',
                             headers=headers)
    return shows_res.json()


def get_show_episodes(show_id, market):
    """
        Get the episodes of the show using show id
        input: show_id: show id (string)
        output: list of episode objects
        Query Parameters: market: Country: ISO 3166-1 alpha-2 country code.(required)
                          limit: integer (0-50) default: 20
                            offset: integer  default: 0
    """
    show_episodes_res = requests.get(f'{config.BASE_URL}/shows/{show_id}/episodes?market={market}',
                                     headers=headers)
    return show_episodes_res.json()
