import streamlit as st

# Page layout: wide
st.set_page_config(page_title="BrainyBytes Lab", layout="wide")

# Set background for page
page_bg_img = f"""
<style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("https://i.postimg.cc/Dzk9yB0c/3175102.jpg");
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
st.markdown(page_bg_img, unsafe_allow_html=True)
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
        margin-left: 20px;
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
st.markdown(
    '<div class="title-container">BrainyBytes Lab<div class="image-container"><img src="https://static.vecteezy.com/system/resources/previews/023/092/211/non_2x/cartoon-cute-smart-human-brain-character-waving-vector.jpg" width="100"></div></div>',
    unsafe_allow_html=True
)
# Coding Interface
st.markdown(page_bg_img, unsafe_allow_html=True)


def run_code(code):
    # function to execute the provided code
    if code.strip():  # Check if code is not empty
        # Redirect to print output
        import sys
        from io import StringIO

        old_stdout = sys.stdout
        redirected_output = sys.stdout = StringIO()
        try:
            exec(code)
            output = redirected_output.getvalue()
            st.code(output, language='python')  # Display the output
        finally:
            sys.stdout = old_stdout
    else:
        st.warning("Please enter some code.")


def main():
    # Dropdown for selecting programming language
    language = st.selectbox("Select programming language:", ["Python", "Java"])

    # User will implement their code here
    default_code = "print('Hello, World!')"  # Default code
    code = st.text_area("", value=default_code, height=1000)

    # Button to run the code
    if st.button("Run"):
        run_code(code)


if __name__ == "__main__":
    main()