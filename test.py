import streamlit as st
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.Certificate("melody-62325-56ef018aebcf.json")
firebase_admin.initialize_app(cred)
def app():
# Usernm = []
    st.title('Welcome to :violet[Melody] :')

    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''



    def f(): 
        try:
            user = auth.get_user_by_email(email)
            print(user.uid)
            st.session_state.username = user.uid
            st.session_state.useremail = user.email
            
            global Usernm
            Usernm=(user.uid)
            
            st.session_state.signedout = True
            st.session_state.signout = True    
  
            
        except: 
            st.warning('Login Failed')

    def t():
        st.session_state.signout = False
        st.session_state.signedout = False   
        st.session_state.username = ''


        
    
        
    if "signedout"  not in st.session_state:
        st.session_state["signedout"] = False
    if 'signout' not in st.session_state:
        st.session_state['signout'] = False    
        

        
    
    if  not st.session_state["signedout"]: # only show if the state is False, hence the button has never been clicked
        choice = st.selectbox('Login/Signup',['Login','Sign up'])
        email = st.text_input('Email Address')
        password = st.text_input('Password',type='password')
        

        
        if choice == 'Sign up':
            username = st.text_input("Enter  your unique username")
            
            if st.button('Create my account'):
                user = auth.create_user(email = email, password = password,uid=username)
                
                st.success('Account created successfully!')
                st.markdown('Please Login using your email and password')
                st.balloons()
                def main():
                    st.title("Your Streamlit App")
                
                
                
             
                
        else:
            # st.button('Login', on_click=f)          
            st.button('Login', on_click=f)
            
            
    if st.session_state.signout:
                st.text('Name :'+st.session_state.username)
                st.text('Email id: '+st.session_state.useremail)
                st.button('Sign out', on_click=t) 
                
                #recommender
                import pickle
                import spotipy
                from spotipy.oauth2 import SpotifyClientCredentials

                CLIENT_ID = "70a9fb89662f4dac8d07321b259eaad7"
                CLIENT_SECRET = "4d6710460d764fbbb8d8753dc094d131"

                # Initialize the Spotify client
                client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
                sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


                def get_song_album_cover_url(song_name, artist_name):
                    search_query = f"track:{song_name} artist:{artist_name}"
                    results = sp.search(q=search_query, type="track")

                    if results and results["tracks"]["items"]:
                        track = results["tracks"]["items"][0]
                        album_cover_url = track["album"]["images"][0]["url"]
                        print(album_cover_url)
                        return album_cover_url
                    else:
                        return "https://i.postimg.cc/0QNxYz4V/social.png"

                def recommend(song):
                    index = music[music['song'] == song].index[0]
                    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
                    recommended_music_names = []
                    recommended_music_posters = []
                    for i in distances[1:6]:
                        # fetch the movie poster
                        artist = music.iloc[i[0]].artist
                        print(artist)
                        print(music.iloc[i[0]].song)
                        recommended_music_posters.append(get_song_album_cover_url(music.iloc[i[0]].song, artist))
                        recommended_music_names.append(music.iloc[i[0]].song)

                    return recommended_music_names,recommended_music_posters

                st.header('Music Recommender System')
                music = pickle.load(open('df.pkl','rb'))
                similarity = pickle.load(open('similarity.pkl','rb'))

                music_list = music['song'].values
                selected_music = st.selectbox(
                    "Type or select a song from the dropdown",
                    music_list
                )

                if st.button('Show Recommendation'):
                    recommended_music_names,recommended_music_posters = recommend(selected_music)
                    col1, col2, col3, col4, col5= st.columns(5)
                    with col1:
                        st.text(recommended_music_names[0])
                        st.image(recommended_music_posters[0])
                    with col2:
                        st.text(recommended_music_names[1])
                        st.image(recommended_music_posters[1])

                    with col3:
                        st.text(recommended_music_names[2])
                        st.image(recommended_music_posters[2])
                    with col4:
                        st.text(recommended_music_names[3])
                        st.image(recommended_music_posters[3])
                    with col5:
                        st.text(recommended_music_names[4])
                        st.image(recommended_music_posters[4])



    # Audio Player for Selected Song
                if selected_music:
                    results = sp.search(q=selected_music, limit=1)
                    if results and results["tracks"]["items"]:
                        track = results["tracks"]["items"][0]
                        preview_url = track["preview_url"]
                        if preview_url:
                            st.audio(preview_url, format="audio/ogg", start_time=0)
                        else:
                            st.warning("No audio preview available for this track.")
                    else:
                        st.warning("Selected song not found on Spotify.")              
                                                
def ap():
            st.write('Posts')
