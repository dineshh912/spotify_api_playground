import requests
import config


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


print(get_audio_analysis('6y0igZArWVi6Iz0rj35c1Y'))