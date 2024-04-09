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
    background-image: url("https://i.postimg.cc/6pBCXcf1/7525967.jpg");
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
        config['credentials']['usernames'][username]['selectbadgeid'])  # badge user currently has selected
    # Create container for header
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
    # Display title with colored background and image
    st.markdown(
        '<div class="title-container">BrainyBytes Lab<div class="image-container"><img src="https://static.vecteezy.com/system/resources/previews/023/092/211/non_2x/cartoon-cute-smart-human-brain-character-waving-vector.jpg" width="100"></div></div>',
        unsafe_allow_html=True
    )
    # Display title with colored background and image
    st.markdown(
        '<div class="title-container">BrainyBytes Lab<div class="image-container"><img src="https://static.vecteezy.com/system/resources/previews/023/092/211/non_2x/cartoon-cute-smart-human-brain-character-waving-vector.jpg" width="100"></div></div>',
        unsafe_allow_html=True
    )
    #questions for math unit 1 stored in array
    m1cardquestion = ["What is 1 + (-1)", "What is 1 - (-1)", "What is 1 * -1", "What is -1 * -1"]
    #answers for math unit 1 stored in array
    m1cardanswer = [
        "Answer: :red[0] adding a negative value (-1) to another value is the same as substracting the its positive inverse",
        "Answer: :red[2] Subtracting a negative value is the same as adding its positive inverse.",
        "Answer: :red[-1] multiplying a positive value by a negative results in negative number.",
        "Answer: :red[1] Multiplying a negative number with a negative number results in a positive number"]
    #questions for math unit 2 stored in array
    m2cardquestion = ["How would you represent 5 spoonfuls of salsa for every 2 eggs as a fraction?","If we earn 200 reward points for spending 200 dollars how many dollar would I need to spend to earn 400 points?","If it takes you 20 bites to eat 2 sandwichs how many sandwichs can you eat in 50 bites?"]
    #answers for math unit 2 stored in array
    m2cardanswer = ["Answer:  since there is 5 spoonfulls of salsa need for 2 eggs the fraction can be represented as 5 spoonfulls/2 eggs i.e 5/2 ", "Answers: since we earn 200 points per 200 dollar spent the ration of points to dollars is 200/200 which is reduced down to 1/1 i.e 1 point = 1 dollar. so to earn 400 points we need to spend 400 dollars", "First get the ratio of sandwichs to bites i.e 2 sandwichs/20 bites = 1 sandwich/10 bites next multiple the ratio calculated by 50 i.e 50*(1/10) = 5 so you can eat 5 sandwichs in 50 bites"]
    #questions for math unit 3 stored in array
    m3cardquestion = ["Solve for x when 4x + 1 = 5",
                      "Solve for x when 3x + 2x = 10",
                      "solve for x when 20x + 10 = 10x + 20"
                      ]
    #answers for math unit 3 stored in array
    m3cardanswer = ["Answer: 1) remove the 1 for the left hand side by subtracting 1 on both sides 4x + 1 - 1 = 5 - 1\n 2)remove the lead 4 by dividing both sides by 4 (1/4)4x = 4(1/4) we find that x = 1",
                    "Answer: 1) combine like terms I.E 3x and 2x this leaves 5x = 10 \n 2) Divide both sides by 5 this leave x = 2 ",
                    "Answer: 1)Substract 10x from both sides 20x - 10x + 10 = 10x - 10x + 20 \n 2) subtract 10 from both sides 10x + 10 - 10 = 20 - 10 \n 3) divide both sides by 10 (1/10)(10x) = 20/10 \n x = 2 code data types"
                    ]
    #questions for coding unit 1 stored in array
    c1cardquestion = ["What is a String?",
                      "What is a integer?",
                      "What is a float?",
                      "What is a list?",
                      "What is a boolean"
                      ]
    #answer for coding unit 1 stored in array
    c1cardanswer = ["Answer: A string is a list of character in python strings are surrounded by quotations marks for example 'Hello worlds'",
                    "Answer: A integer is a whole number for example 3 and -3"
                    ,"Answer: A float is a floating point number such as a decimal and fraction, for example 1.3",
                    "Answer: A list is a group of elements stored in a single variable for example a list of numbers is [1,2,3,4,5]",
                    "Answer: A boolean is a variable with only two values True or False"
                    ]
    st.markdown("""<hr>""",unsafe_allow_html=True) #create a horizontal line to separate units
    st.title("Math") #title of section
    st.header("Negative - addition/subtraction/multiplication/division") #display title of unit
    i = 0
    colm1, colm2 = st.columns(2) #create a two column structure
    with colm1: #in first column
        while i < len(m1cardquestion): #iterate through all the questions in the array
            st.write(m1cardquestion[i])  # display questions
            with st.popover("Answer"): #create a popover
                st.write(m1cardanswer[i])  # display answers to corresponding question in popover
            i += 1

    with colm2:
        #embedded youtube corresponding to current unit
        st.markdown("""<iframe width="560" height="315" src="https://www.youtube.com/embed/NQSN00zL5gg?si=NLr9wwoi6aZ9Wv4v" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""", unsafe_allow_html=True)
    st.markdown("""<hr>""",unsafe_allow_html=True)
    st.header("Ratios ") #display unit title
    colmn1 ,colmn2 = st.columns(2)
    with colmn1:
        i = 0
        while i < len(m2cardquestion):
            st.write(m2cardquestion[i])  # display unit question
            with st.popover("Answer"):
                st.write(m2cardanswer[i])  # display unit answer in popover
            i += 1
    with colmn2:
        #embedded corresponding unit video
        st.markdown("""<iframe width="560" height="315" src="https://www.youtube.com/embed/HpdMJaKaXXc?si=92b2IsGRti4W5eRG" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""", unsafe_allow_html=True)

    st.markdown("""<hr>""",unsafe_allow_html=True)
    st.header("Algebra ") #display unit title
    i = 0
    colm21, colm22 = st.columns(2)
    with colm21:
        while i < len(m3cardquestion): #iterate through unit questions
            st.write(m3cardquestion[i])  # display unit questions
            with st.popover("Answer"):
                st.write(m3cardanswer[i])  # display unit answer
            i += 1
    with colm22:
        st.markdown(
            #embedded unit video
            """<iframe width="560" height="315" src="https://www.youtube.com/embed/grnP3mduZkM?si=m6BIEw3B1n_qAvAq" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""",
            unsafe_allow_html=True)

    st.markdown("""<hr>""",unsafe_allow_html=True)
    st.title("Coding") #display section title
    st.header("Data types ") #display unit title
    i = 0
    colm31, colm32 = st.columns(2)
    with colm31:
        while i < len(c1cardquestion): #iterate through unit questions array
            st.write(c1cardquestion[i])  # display the questions
            with st.popover("Answer"):
                st.write(c1cardanswer[i])  # display the answers
            i += 1

    with colm32:
        st.markdown(
            #embedded unit video
"""<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/ppsCxnNm-JI?si=j7JBwF5PgAkIv5Gu" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""",            unsafe_allow_html=True)
        # components.iframe("https://www.youtube.com/embed/NQSN00zL5gg?si=NLr9wwoi6aZ9Wv4v", width=700, height=400)
    st.markdown("""<hr>""", unsafe_allow_html=True)
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
