import pandas as pd
import streamlit_authenticator as stauth
import streamlit as st
import yaml
from yaml.loader import SafeLoader
# Sets page in widemode,specifically allowing header to span across page.
st.set_page_config(page_title="BrainyBytes Lab", layout="wide")
#Set background for page
page_bg_img = f"""
<style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("https://i.postimg.cc/rw2qQm9T/v935-aum-16.jpg");
    background-size: cover;
    background-position: center center;
    background-repeat: no-repeat;
    background-attachment: local];
}}
[data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
}}
</style>
"""
st.markdown(page_bg_img,unsafe_allow_html=True)
def addpoint(points): #function to add points to user
    config['credentials']['usernames'][username]['points'] += points #adds points to user
def removepoint(points): #function to remove points from user
    config['credentials']['usernames'][username]['points'] -= points
    if config['credentials']['usernames'][username]['points'] < 0: #the user cannot have a negative balance
        config['credentials']['usernames'][username]['points'] = 0
def badgeidtoimage(id): #translate badge id into the image of the badge
        if id == 0:
            image = "👨"
        if id == 1:
            image = "👩‍💻"
        if id == 2:
            image = "👨‍💻"
        if id == 3:
            image = "👨‍🎤"
        if id == 4:
            image = "👩‍🎤"
        if id == 5:
            image = "👨‍🎓"
        if id == 6:
            image = "👩‍🎓"
        if id == 7:
            image = "🧙"
        return image

with open('config.yaml') as file: #opening data file with user information
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate( #setting up cookies
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
authenticator.login()

if st.session_state["authentication_status"]: #if the user is authenticated currently
    with st.sidebar:
        authenticator.logout() #logout button
elif st.session_state["authentication_status"] is False: # if incorrect password/username inputed when clicking login
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None: #if fields login fields are empty
    st.warning('Please enter your username and password')

username = st.session_state["username"] #intilizes value of username to the current user's name

if st.session_state["authentication_status"]:
    # creating a 'points' category if currently empty
    if 'points' not in config['credentials']['usernames'][username]:
        config['credentials']['usernames'][username]['points'] = 1 #set users point balance to 1

#----------------------page code start---------------------------------
if st.session_state["authentication_status"]: #if the user is authenticated currently
    pointbalance = config['credentials']['usernames'][username]['points']  # amount of points a user currently has
    badge = badgeidtoimage(
        config['credentials']['usernames'][username]['selectbadgeid'])  # badge user currently has selected is displayed
    # Create container for header
    st.markdown( #html code for frontend button and header
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Lilita+One&display=swap');
        .title-container {
            display: flex;
            align-items: center;
            padding: 10px;
            background-color: #fcc4d4;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            font-size: 50px; 
            margin-top: -105px; 
            font-family: 'Lilita One', cursive; 
            color: #d33f73;

        }
         div.stButton > Button:first-child {
            background-color: #FFE2E0;
            color: black;
            font-size: 20px;
            height: 2em;
            width: 12em;
            border-radius: 10px 10px 10px 10px;
        }
        .image-container {
            margin-left: 20px; /* Adjust the margin to create space between title and image */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    # Display title with colored background and image
    st.markdown(
        '<div class="title-container">BrainyBytes Lab<div class="image-container"><img src="https://static.vecteezy.com/system/resources/previews/023/092/211/non_2x/cartoon-cute-smart-human-brain-character-waving-vector.jpg" width="100"></div></div>',
        unsafe_allow_html=True
    )

    challenges = pd.read_csv('challenges.csv') #csv file holding challenges
    #Main page code
    st.write(f'Welcome *{st.session_state["name"]}*')
    mathgamesplayed = config['credentials']['usernames'][username]['MathGamesplayed']
    codegamesplayed = config['credentials']['usernames'][username]['CodeGamesplayed']

    Completedchallengesid = config['credentials']['usernames'][username]['challengesCompletedid']
    #displaying three challenges to the user

    st.write(f'Challenge #1: :red[*{challenges["Challenge"][0]}*] worth :green[ *{challenges["pointsworth"][0]}*] points status: :red[*{mathgamesplayed}*]/:red[*{challenges["tracker2"][0]}*]')
    if challenges["tracker2"][0] <= mathgamesplayed and (1 in Completedchallengesid) == False: #if the user has completed challenge and has not redeemed points
        if st.button("Redeem points",key="challenge1"):
            config['credentials']['usernames'][username]['challengesCompletedid'].append(1)
            addpoint(int(challenges["pointsworth"][0]))

    st.write(f'Challenge #2: :red[*{challenges["Challenge"][1]}*] worth :green[ *{challenges["pointsworth"][1]}*] points status: :red[*{mathgamesplayed}*]/:red[*{challenges["tracker2"][1]}*]')
    if challenges["tracker2"][1] <= mathgamesplayed and (2 in Completedchallengesid) == False:
        if st.button("Redeem points",key="challenge2"):
            config['credentials']['usernames'][username]['challengesCompletedid'].append(2)
            addpoint(int(challenges["pointsworth"][2]))

    st.write(f'Challenge #3: :red[*{challenges["Challenge"][2]}*] worth :green[ *{challenges["pointsworth"][2]}*] points status: :red[*{mathgamesplayed}*]/:red[*{challenges["tracker2"][2]}*]')
    if challenges["tracker2"][2] <= mathgamesplayed and (3 in Completedchallengesid) == False:
        if st.button("Redeem points",key="challenge3"):
            config['credentials']['usernames'][username]['challengesCompletedid'].append(3)
            addpoint(int(challenges["pointsworth"][2]))

    st.write(
        f'Challenge #4: :red[*{challenges["Challenge"][6]}*] worth :green[ *{challenges["pointsworth"][6]}*] points status: :red[*{codegamesplayed}*]/:red[*{challenges["tracker2"][6]}*]')
    if challenges["tracker2"][6] <= codegamesplayed and (7 in Completedchallengesid) == False:
        if st.button("Redeem points", key="challenge4"):
            config['credentials']['usernames'][username]['challengesCompletedid'].append(7)
            addpoint(int(challenges["pointsworth"][6]))

    st.write(
        f'Challenge #5: :red[*{challenges["Challenge"][7]}*] worth :green[ *{challenges["pointsworth"][7]}*] points status: :red[*{codegamesplayed}*]/:red[*{challenges["tracker2"][7]}*]')
    if challenges["tracker2"][7] <= codegamesplayed and (8 in Completedchallengesid) == False:
        if st.button("Redeem points", key="challenge5"):
            config['credentials']['usernames'][username]['challengesCompletedid'].append(8)
            addpoint(int(challenges["pointsworth"][7]))

    st.write(
        f'Challenge #6: :red[*{challenges["Challenge"][8]}*] worth :green[ *{challenges["pointsworth"][8]}*] points status: :red[*{codegamesplayed}*]/:red[*{challenges["tracker2"][8]}*]')
    if challenges["tracker2"][8] <= codegamesplayed and (9 in Completedchallengesid) == False:
        if st.button("Redeem points", key="challenge6"):
            config['credentials']['usernames'][username]['challengesCompletedid'].append(9)
            addpoint(int(challenges["pointsworth"][8]))
    st.markdown("""<hr>""",unsafe_allow_html=True)
    st.markdown("""<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/yJmK_BOUc2Y?si=f5tqUBnngcTtHFRG" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""",unsafe_allow_html=True)
    #sidebar code
    st.sidebar.write(badge + username) #display badge and point balance on sidebar
    st.sidebar.write('you currently have: ' + str(pointbalance) + ' points')

#----------------------page code end---------------------------------

else: #registration for the website
    try:
        email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user(preauthorization=False)
        if email_of_registered_user:
            st.success('User registered successfully')
            config['credentials']['usernames'][username_of_registered_user]['points'] = 20
            config['credentials']['usernames'][username_of_registered_user]['ownedbadges'] = [0]
            config['credentials']['usernames'][username_of_registered_user]['selectbadgeid'] = 0
            config['credentials']['usernames'][username_of_registered_user]['MathGamesplayed'] = 0
            config['credentials']['usernames'][username_of_registered_user]['CodeGamesplayed'] = 0
            config['credentials']['usernames'][username_of_registered_user]['challengesCompletedid'] = [0]

    except Exception as e:
        st.error(e)

with open('config.yaml', 'w') as file:
    yaml.dump(config, file, default_flow_style=False)
