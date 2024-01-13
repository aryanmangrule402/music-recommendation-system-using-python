import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "70a9fb89662f4dac8d07321b259eaad7"
CLIENT_SECRET = "4d6710460d764fbbb8d8753dc094d131"

# Initialize the Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_track_preview_url(track_uri):
    track_info = sp.track(track_uri)
    if 'preview_url' in track_info and track_info['preview_url']:
        return track_info['preview_url']
    else:
        return None

# Rest of your code remains unchanged...

if st.button('Show Recommendation'):
    recommended_music_names, recommended_music_posters = recommend(selected_movie)
    recommended_track_uris = []  # List to store track URIs
    for song_name in recommended_music_names:
        search_query = f"track:{song_name}"
        results = sp.search(q=search_query, type="track")
        if results and results["tracks"]["items"]:
            track_uri = results["tracks"]["items"][0]["uri"]
            recommended_track_uris.append(track_uri)

    col1, col2, col3, col4, col5 = st.columns(5)
    for i, track_uri in enumerate(recommended_track_uris):
        preview_url = get_track_preview_url(track_uri)
        if preview_url:
            with col1 if i % 5 == 0 else col2 if i % 5 == 1 else col3 if i % 5 == 2 else col4 if i % 5 == 3 else col5:
                st.text(recommended_music_names[i])
                st.image(recommended_music_posters[i])
                st.audio(preview_url, format='audio/ogg', start_time=0)
