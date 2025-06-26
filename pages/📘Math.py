import streamlit_authenticator as stauth
import streamlit as st
import yaml
from yaml.loader import SafeLoader
import json
import streamlit.components.v1 as components
#Title of the website and makes site in widemode and sets the page font to Lilita One
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
    config['credentials']['usernames'][username]['points'] += points
def removepoint(points): #function to remove points from user
    config['credentials']['usernames'][username]['points'] -= points
    if config['credentials']['usernames'][username]['points'] < 0:
        config['credentials']['usernames'][username]['points'] = 0
def badgeidtoimage(id): #function to translate badge id to badge image
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

def multichoicegame(unit,questionfile): #function to create a math multi choice game
    gamequestion = open(questionfile) #opens a json file with questions
    questions = json.load(gamequestion)
    score = 0 #intial score is set to zero
    feedback = [] #array used to give feed back to user whether they got question right or wrong
    st.title("Math Questionnaire") #title
    for i, question in enumerate(questions, 1): #iterate through each question
        st.markdown(f"<span style='font-weight:bold'> Question {i}:  {question['question']}</span>", unsafe_allow_html=True) #display the question
        if len(question['correct_answers']) > 1:
            user_answers = [] #user inputs answer via a checkbox
            for option in question['options']:
                if st.checkbox(option, key=f'{unit}{i}{option}'):
                    user_answers.append(option)  #The answer the user selects are stored in user_answers list
        else:
            user_answer = st.radio("", question['options'], key=f'{unit}Unit1{i}') #if non-multiselect question uses a radio button
        if len(question['correct_answers']) > 1: #if more then one correct answer
            if set(user_answers) == set(question['correct_answers']):
                score += 1 #if answer is correct score is incremented
                feedback.append("That is Correct✅") #feedback is stored as correct
            else:
                feedback.append("That is Wrong ❌") #feedback is stored as incorrect
        else:
            if user_answer == question['correct_answers'][0]: #if only one correct answer
                score += 1
                feedback.append("That is Correct✅") #feedback is appened
            else:
                feedback.append("That is Wrong ❌")
    if st.button("SUBMIT",key=unit): #button to submit answers
        st.write("Game Results :")
        for i, fb in enumerate(feedback, 1):
            st.write(f"Question {i}: {fb}") #display feedback

        st.write(f"Score final : {score}/{len(questions)}") #display final score
        pointsgained = round(score) #the user gains point equal to they're score
        st.write(f"You gained :red[ {pointsgained}] points") #display amount of points earned
        addpoint(pointsgained) #add points to users point balance
        config['credentials']['usernames'][username][
            'MathGamesplayed'] += 1 # track number math games played


with open('config.yaml') as file: #opening data file with user information
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate( #setting up cookies
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

#code for login
authenticator.login()
if st.session_state["authentication_status"]: #if the user is authenticated currently
    with st.sidebar:
        authenticator.logout()  # logout button
elif st.session_state["authentication_status"] is False: # if incorrect password/username inputed when clicking login
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None: #if fields login fields are empty
    st.warning('Please enter your username and password')

username = st.session_state["username"] #intilizes value of username to the current user's name

if st.session_state["authentication_status"]:
    # creating a 'points' category if currently empty
    if 'points' not in config['credentials']['usernames'][username]:
        config['credentials']['usernames'][username]['points'] = 1 #set users point balance to 1

if st.session_state["authentication_status"]: #if the user is authenticated currently
    # Creating container for header
    st.markdown(
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
        
        div.stButton > Button:first-child {
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
    # Display header with colored container and image
    st.markdown(
        '<div class="title-container">BrainyBytes Lab<div class="image-container"><img src="https://static.vecteezy.com/system/resources/previews/023/092/211/non_2x/cartoon-cute-smart-human-brain-character-waving-vector.jpg" width="100"></div></div>',
        unsafe_allow_html=True
    )
     # Creating container for the Math subheader with image
    st.markdown("""
        <style>
        .subheader-container {
            display: flex;
            align-items: center;
            padding: 10px;
            background-color: #D8EFB0;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            margin-top: 10px;
            margin-bottom: 10px;
            font-size: 24px;
              font-weight: bold;
                font-family: 'Lilita One', cursive; 
                color: #98d42c;
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
        '<div class="subheader-container"><img src="https://cdn-icons-png.freepik.com/512/4720/4720458.png" width="50" height="50"> Welcome To The Number Nook ' + username + '</div>',
        unsafe_allow_html=True)
    mathgamesplayed = config['credentials']['usernames'][username]['MathGamesplayed'] #config for tracking math games
    colm1 , colm2 = st.columns(2) #creating two column structure for selecting games to play
    with colm1:
        st.image("images/Ratiogame.jpg", caption="Ratio Game", width = 300) #display thumbnail for ratio game
        with st.popover("play"): #create a popover
            multichoicegame('unit1','math_unit1_questions.json') #multi choice ratio game is playable within popover

        st.image("images/AlgebraGame.jpg", caption="Algebra Game", width = 300) #display thumbnail for algebra game
        with st.popover("play"):
            multichoicegame('unit3','math_unit3_questions.json') #play game within popover

        st.image("images/2048.jpg", caption="2048 Game", width = 300) #display thumbnail for 2048 game
        with st.popover("play"): #create a popover
            content_url=("https://play2048.co/") #embedded html game is playable in popover
            #Embed the content using an iframe
            components.iframe(content_url, width=700, height=1000)

    with colm2:
        st.image("images/NegativeNumbers.jpg", caption="Negative Numbers Game", width = 300) #display thumbnail for negative numbers game
        with st.popover("play"): #playable negative numbers in popover
            multichoicegame('unit2','math_unit2_questions.json')

        st.image("images/puppypuzzle200.webp", caption="Puppy Puzzle", width = 300)
        with st.popover("play"): #embedded html game called puppy puzzle
            content_url2=("https://cdn.htmlgames.com/PuppyPuzzle/")
            components.iframe(content_url2, width=700, height=1000)

        st.image("images/sumjong200.webp", caption="sumjong200" , width = 300)
        with st.popover("play"): #embedded html game called Sumjong
            content_url3 = ("https://cdn.htmlgames.com/Sumjong/")
            components.iframe(content_url3, width=700, height=1000)

    #sidebar code
    pointbalance = config['credentials']['usernames'][username]['points']  # amount of points a user currently has
    badge = badgeidtoimage(
        config['credentials']['usernames'][username]['selectbadgeid'])  # badge user currently has selected

    st.sidebar.write(badge + username)
    st.sidebar.write('you currently have: ' + str(pointbalance) + ' points')

#code for login
else: #registration for the website
    try:
        email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user()
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
