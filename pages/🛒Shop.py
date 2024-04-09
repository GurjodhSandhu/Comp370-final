import streamlit_authenticator as stauth
import streamlit as st
import yaml
from yaml.loader import SafeLoader
st.set_page_config(page_title="BrainyBytes Lab", layout="wide") #page setup
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
    background-image: url("https://i.postimg.cc/ZRnWGtkq/fun-colorful-line-doodle-seamless-pattern-background-for-children-simple-childish-scribble-backdrop.jpg");
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
    config['credentials']['usernames'][username]['points'] += points
def removepoint(points): #function to remove points from user
    config['credentials']['usernames'][username]['points'] -= points
    if config['credentials']['usernames'][username]['points'] < 0:
        config['credentials']['usernames'][username]['points'] = 0
def badgeidtoimage(id):
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
#code for login
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

#---------------------------------------page code start---------------------------------------------------------------------------------
if st.session_state["authentication_status"]: #if logged in
    pointbalance = str(config['credentials']['usernames'][username]['points']) #store users point balance in variable
    st.markdown( #front-end html code
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
        .image-container {
            margin-left: 20px; /* Adjust the margin to create space between title and image */
        }
        div.stButton > button:first-child {
            background-color: #FFE2E0;
            color: black;
            font-size: 20px;
            height: 2em;
            width: 12em;
            border-radius: 10px 10px 10px 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown('<div class="title-container">BrainyBytes Lab<div class="image-container"><img src="https://static.vecteezy.com/system/resources/previews/023/092/211/non_2x/cartoon-cute-smart-human-brain-character-waving-vector.jpg" width="100"></div></div>',
        unsafe_allow_html=True)# display Header
    # sidebar code
    badge = badgeidtoimage(
        config['credentials']['usernames'][username]['selectbadgeid']) #translate badge id to image
    st.sidebar.write(badge + username)                                       #front-end side bar to display badge
    st.sidebar.write('you currently have: ' + str(pointbalance) + ' points') #front-end display the current points
    # Creating container for the Shop subheader with image

    st.markdown(#html code for frontend
               """
            <style>
            .subheader-container {
                display: flex;
                align-items: center;
                padding: 10px;
                background-color: #C5E9E3;
                border-radius: 10px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                margin-top: 20px;
                font-size: 24px;
                font-weight: bold;
                font-family: 'Lilita One', cursive; 
                color: #65C5B4;
            }
            .subheader-container img {
                margin-right: 10px;
            }
            </style>
            """,
                unsafe_allow_html = True
                                         )
      # Display subheader with colored background and image
    st.markdown(
        '<div class="subheader-container"><img src="https://cdn.icon-icons.com/icons2/943/PNG/512/shoppaymentorderbuy-60_icon-icons.com_73867.png" width="50" height="50"> Welcome To The Shop ' + username + '</div>',
        unsafe_allow_html=True)
    #--------------------------------------------------Main page code start---------------------------------------------
    st.header('you currently have: :green['+ pointbalance + '] points') #front end displaying point balance (main page)
    colm1, colm2 = st.columns(2) #create to columns to place elements
    with colm1: #with column 1
        st.header("👩‍💻 costs :green[20] points") #front end to display the badge information and cost
        if st.button(label="Buy 👩‍💻", key="item1"): #front end buy button with label buy and badge
            cost = 20 #price of badge
            id = 1 #badge id used to select/display badges
            if (config['credentials']['usernames'][username]['points'] - cost < 0): #if user does not have enough funds to buy badge
                st.write("insufficient funds") #front end - display a message if user cant afford badge
                id = -1
            if id in config['credentials']['usernames'][username]['ownedbadges']: #if user already owns the badge
                st.write("you already own this badge") #front end - display a message if user already owns this badge
            elif(id != -1):
                removepoint(cost) #removes the amount the badge costs from users point balance
            st.write("bought") #front end display a confirmation message
            config['credentials']['usernames'][username]['ownedbadges'].append(id) #adds badge id to the list of badges the user owns

#repeat for each badge
    with colm2:
        st.header("👨‍💻 costs :green[20] points")
        if st.button(label="Buy 👨‍💻", key="item2"):
            cost = 20
            id = 2
            if (config['credentials']['usernames'][username]['points'] - cost < 0):
                st.write("insufficient funds")
                id = -1
            if id in config['credentials']['usernames'][username]['ownedbadges']:
                st.write("you already own this badge")
            elif (id != -1):
                removepoint(cost)
                st.write("bought")
                config['credentials']['usernames'][username]['ownedbadges'].append(id)
    with colm1:
        st.header("👨‍🎤 costs :green[20] points")
        if st.button(label="Buy 👨‍🎤", key="item3"):
            cost = 20
            id = 3
            if (config['credentials']['usernames'][username]['points'] - cost < 0):
                st.write("insufficient funds")
                id = -1
            if id in config['credentials']['usernames'][username]['ownedbadges']:
                st.write("you already own this badge")
            elif (id != -1):
                removepoint(cost)
                st.write("bought")
                config['credentials']['usernames'][username]['ownedbadges'].append(id)
    with colm1:
        st.header("👩‍🎤 costs :green[20] points")
        if st.button(label="Buy 👩‍🎤", key="item4"):
            cost = 20
            id = 4
            if (config['credentials']['usernames'][username]['points'] - cost < 0):
                st.write("insufficient funds")
                id = -1
            if id in config['credentials']['usernames'][username]['ownedbadges']:
                st.write("you already own this badge")
            elif (id != -1):
                removepoint(cost)
                st.write("bought")
                config['credentials']['usernames'][username]['ownedbadges'].append(id)
    with colm2:
        st.header("👨‍🎓 costs :green[20] points")
        if st.button(label="Buy 👨‍🎓", key="item5"):
            cost = 20
            id = 5
            if (config['credentials']['usernames'][username]['points'] - cost < 0):
                st.write("insufficient funds")
                id = -1
            if id in config['credentials']['usernames'][username]['ownedbadges']:
                st.write("you already own this badge")
            elif (id != -1):
                removepoint(cost)
                st.write("bought")
                config['credentials']['usernames'][username]['ownedbadges'].append(id)
    with colm1:
        st.header("👩‍🎓 costs :green[20] points")
        if st.button(label="Buy 👩‍🎓", key="item6"):
            cost = 20
            id = 6
            if (config['credentials']['usernames'][username]['points'] - cost < 0):
                st.write("insufficient funds")
                id = -1
            if id in config['credentials']['usernames'][username]['ownedbadges']:
                st.write("you already own this badge")
            elif (id != -1):
                removepoint(cost)
                st.write("bought")
                config['credentials']['usernames'][username]['ownedbadges'].append(id)
    with colm2:
        st.header("🧙 costs :green[20] points")
        if st.button(label="Buy 🧙", key="item7"):
            cost = 20
            id = 7
            if (config['credentials']['usernames'][username]['points'] - cost < 0):
                st.write("insufficient funds")
                id = -1
            if id in config['credentials']['usernames'][username]['ownedbadges']:
                st.write("you already own this badge")
            elif (id != -1):
                removepoint(cost)
                st.write("bought")
                config['credentials']['usernames'][username]['ownedbadges'].append(id)

#---------------------------------------Main Page code End---------------------------------------------------------------------------------

#code for login
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