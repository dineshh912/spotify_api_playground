from webbrowser import get
import requests
import config
import sample_ids
from pprint import pprint

"""
note: To access user related api endpoints, 
    (the endpoints start with me/ and post, put, delete)
    need to use different auth method than client_credentials
    so, it's not covered in this code base
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

def get_track(track_id):
    """
        Get the track information using track id
        input: track_id: track id (string)
    """
    track_res = requests.get(f'{config.BASE_URL}/tracks/{track_id}',
                             headers=headers)
    return track_res.json()


def get_tracks(track_ids):
    """
        Get the track information using track id
        input: track_ids: list of track ids (string)
    """
    tracks_res = requests.get(f'{config.BASE_URL}/tracks?ids={track_ids}',
                              headers=headers)
    return tracks_res.json()


def get_track_audio_feature(track_id):
    """
        Get audio features of the track using track id
        input: track_id: track id (string)
    """
    track_audio_feature_res = requests.get(f'{config.BASE_URL}/audio-features/{track_id}',
                                           headers=headers)
    return track_audio_feature_res.json()


def get_track_audio_features(track_ids):
    """
        Get audio features for a track
        input: track_ids: list of track ids (string)
        output: list of track objects
    """
    track_audio_features_res = requests.get(f'{config.BASE_URL}/audio-features?ids={track_ids}',
                                            headers=headers)
    return track_audio_features_res.json()


def get_audio_analysis(track_id):
    """
        Get audio analysis of the track using track id
        input: track_id: track id (string)
    """
    audio_analysis_res = requests.get(f'{config.BASE_URL}/audio-analysis/{track_id}',
                                      headers=headers)
    return audio_analysis_res.json()


def get_track_recommendations(**kwargs):
    """
        Get recommendations for a track
        output: list of track objects
        Query Parameters: seed_artist: list of artist ids (string) (0-5)
                         seed_genres: list of genre (string) (0-5)
                         seed_tracks: list of track ids (string) (0-5)
                         limit: integer (0-100) default: 20
                         market: Country: ISO 3166-1 alpha-2 country code.
                         max_acousticness: float (0.0-1.0)
                         max_danceability: float (0.0-1.0)
                         max_duration_ms: integer
                         max_energy: float (0.0-1.0)
                         max_instrumentalness: float (0.0-1.0)
                         max_key: integer (0-11)
                         max_liveness: float (0.0-1.0)
                         max_loudness: float (-60.0-0.0)
                         max_mode: integer (0-11)
                         max_popularity: integer (0-100)
                         max_speechiness: float (0.0-1.0)
                         max_tempo: integer (0-500)
                         max_time_signature: integer (0-11)
                         max_valence: float (0.0-1.0)
                         min_acousticness: float (0.0-1.0)
                         min_danceability: float (0.0-1.0)
                         min_duration_ms: integer
                         min_energy: float (0.0-1.0)
                         min_instrumentalness: float (0.0-1.0)
                         min_key: integer (0-11)
                         min_liveness: float (0.0-1.0)
                         min_loudness: float (-60.0-0.0)
                         min_mode: integer (0-11)
                         min_popularity: integer (0-100)
                         min_speechiness: float (0.0-1.0)
                         min_tempo: integer (0-500)
                         min_time_signature: integer (0-11)
                         min_valence: float (0.0-1.0)
                         target_acousticness: float (0.0-1.0)
                         target_danceability: float (0.0-1.0)
                         target_duration_ms: integer
                         target_energy: float (0.0-1.0)
                         target_instrumentalness: float (0.0-1.0)
                         target_key: integer (0-11)
                         target_liveness: float (0.0-1.0)
                         target_loudness: float (-60.0-0.0)
                         target_mode: integer (0-11)
                         target_popularity: integer (0-100)
                         target_speechiness: float (0.0-1.0)
                         target_tempo: integer (0-500)
                         target_time_signature: integer (0-11)
                         target_valence: float (0.0-1.0)
    """
    track_recommendations_res = requests.get(f'{config.BASE_URL}/recommendations',
                                             headers=headers, params=kwargs)
    return track_recommendations_res.json()
    
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


########## Episodes ######################################

def get_episode(episode_id, market):
    """
        Get the episode information using episode id
        input: episode_id: episode id (string)
        output: episode object
        Query Parameters: market: Country: ISO 3166-1 alpha-2 country code.(required)
    """
    episode_res = requests.get(f'{config.BASE_URL}/episodes/{episode_id}?market={market}',
                               headers=headers)
    return episode_res.json()


def get_episodes(episode_ids, market):
    """
        Get multiple episode information using episode id
        input: episode_ids: list of episode ids (string)
        output: list of episode objects
        Query Parameters: market: Country: ISO 3166-1 alpha-2 country code.(required)
    """
    episodes_res = requests.get(f'{config.BASE_URL}/episodes?ids={episode_ids}&market={market}',
                                headers=headers)
    return episodes_res.json()


########## Search ######################################

def search(**kwargs):
    """
        Search for an item
        input: q: search query (string) required
               type: type of search (string)
               include_external: include external search results (boolean)
               market: Country: ISO 3166-1 alpha-2 country code.(required)
               limit: integer (0-50) default: 20
               offset: integer  default: 0
        output: list of search results
    """
    search_res = requests.get(f'{config.BASE_URL}/search',params=kwargs,
                              headers=headers)
    return search_res.json()

########## Users ######################################

def get_user_profile(user_id):
    """
        Get the user profile information using user id
        input: user_id: user id (string)
        output: user object
    """
    user_profile_res = requests.get(f'{config.BASE_URL}/users/{user_id}',
                                    headers=headers)
    return user_profile_res.json()


########## Playlist ######################################

def get_playlist(playlist_id, **kwargs):
    """
        Get the playlist information using playlist id
        input: playlist_id: playlist id (string)
        output: playlist object
        Query Parameters: market: Country: ISO 3166-1 alpha-2 country code.
                                  additional_types
                                  fields
    """
    playlist_res = requests.get(f'{config.BASE_URL}/playlists/{playlist_id}',
                                params=kwargs, headers=headers)
    return playlist_res.json()


def get_playlist_items(playlist_id, **kwargs):
    """
        Get the playlist items using playlist id
        input: playlist_id: playlist id (string)
        output: list of playlist item objects
        Query Parameters: market: Country: ISO 3166-1 alpha-2 country code.
                                  additional_types
                                  fields
                                  limit: integer (0-50) default: 20
                                  offset: integer  default: 0
    """
    playlist_items_res = requests.get(f'{config.BASE_URL}/playlists/{playlist_id}/tracks',
                                      params=kwargs, headers=headers)
    return playlist_items_res.json()


def get_user_playlist(user_id, **kwargs):
    """
        Get the user playlists using user id
        input: user_id: user id (string)
        output: list of playlist objects
        Query Parameters:   limit: integer (0-50) default: 20
                            offset: integer  default: 0
    """
    user_playlist_res = requests.get(f'{config.BASE_URL}/users/{user_id}/playlists',
                                     params=kwargs, headers=headers)
    return user_playlist_res.json()


def get_featured_playlists(**kwargs):
    """
        Get the featured playlists
        input: None
        output: list of playlist objects
        Query Parameters: country: Country: ISO 3166-1 alpha-2 country code.
                                  locale
                                  timestamp
                                  limit: integer (0-50) default: 20
                                  offset: integer  default: 0
    """
    featured_playlists_res = requests.get(f'{config.BASE_URL}/browse/featured-playlists',
                                          params=kwargs, headers=headers)
    return featured_playlists_res.json()


def get_category_playlists(category_id, **kwargs):
    """
        Get the category playlists using category id
        input: category_id: category id (string)
        output: list of playlist objects
        Query Parameters: country: Country: ISO 3166-1 alpha-2 country code.
                                  limit: integer (0-50) default: 20
                                  offset: integer  default: 0
    """
    category_playlists_res = requests.get(f'{config.BASE_URL}/browse/categories/{category_id}/playlists',
                                          params=kwargs, headers=headers)
    return category_playlists_res.json()


def get_playlist_cover_image(playlist_id):
    """
        Get the playlist cover image using playlist id
        input: playlist_id: playlist id (string)
        output: image url
    """
    playlist_cover_image_res = requests.get(f'{config.BASE_URL}/playlists/{playlist_id}/images',
                                            headers=headers)
    return playlist_cover_image_res.json()


########## Categories ######################################

def get_categories(**kwargs):
    """
        Get the categories
        input: None
        output: list of category objects
        Query Parameters: country: Country: ISO 3166-1 alpha-2 country code.
                                  locale
                                  limit: integer (0-50) default: 20
                                  offset: integer  default: 0
    """
    categories_res = requests.get(f'{config.BASE_URL}/browse/categories',
                                  params=kwargs, headers=headers)
    return categories_res.json()


def get_single_category(category_id):
    """
        Get the category using category id
        input: category_id: category id (string)
        output: category object
    """
    single_category_res = requests.get(f'{config.BASE_URL}/browse/categories/{category_id}',
                                       headers=headers)
    return single_category_res.json()


########## Genres ######################################

def get_available_genre_seeds(**kwargs):
    """
        Get the available genre seeds
        input: None
        output: list of genre objects
        Query Parameters: country: Country: ISO 3166-1 alpha-2 country code.
                                  locale
    """
    available_genre_seeds_res = requests.get(f'{config.BASE_URL}/recommendations/available-genre-seeds',
                                             params=kwargs, headers=headers)
    return available_genre_seeds_res.json()