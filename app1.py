import streamlit as st
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from firebase_admin import auth
from streamlit_option_menu import option_menu


import home,  test, your, about
st.set_page_config(
        page_title="Melody",
)



class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='Melody ',
                options=['Home','Account','Your Lists','About'],
                icons=['house-fill','person-circle','trophy-fill','chat-fill','info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": ""},
        "nav-link-selected": {"background-color": "#ED1E79"},}
                
                )

        
        if app == "Home":
            home.app()
        if app == "Account":
            test.app()    
             
        if app == 'Your Lists':
            your.app()
        if app == 'About':
            about.app()    
             
          
             
    run()            
         
