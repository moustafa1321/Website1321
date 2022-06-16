from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


#Find more emojis here:https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage",page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("Style/Style.css")




#---- load assets -----

lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_w51pcehl.json")
# img_contact_form = Image.open("images/images.jpg")
img_lottie_animation = Image.open("Images/images.jpg")
#https://assets10.lottiefiles.com/packages/lf20_w51pcehl.json
#lottie_coding = "https://assets10.lottiefiles.com/packages/lf20_4kx2q32n.jsonpi"
#https://assets10.lottiefiles.com/packages/lf20_4kx2q32n.json
## ---------- HEADER SECTION ------ ##
st.subheader("Hi,I am Musatafa :wave:")
st.title("A Data Analyst From Germany")
st.write("I am passionate about finding ways to use Python,Lua to be more efficient and effective in programming.")

#--- what i do ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write("I Program sometimes some stupid stuff for fun.")
        st.write("i've always liked coding.")
        st.write("my future plans are to make a application, game")
        with right_column:
            st_lottie(lottie_coding, height=300, key="Coding")

#--- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My future projects")
    st.write("##")
    st.write("")




#--- not used rn----

#   image_column, text_column = st.columns((1, 2))
# with image_column:
#    st.image(img_lottie_animation)
# with text_column:
#    st.subheader("Rickroll")
#    st.write("Get rickrolled noob")

# st.markdown("[Watch Video ...](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

#--- Contact ---
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
     <form action="https://formsubmit.co/Streamingwithmarco@gmail.com"method="POST">
     <input type="hidden"name="_captcha"value="false">
     <input type="text"name="name"placeholder="Your name"required>
     <input type="email"name="email"placeholder="Your email"required>
     <textarea name="message"placeholder="Your message here"required></textarea>
     <button type="submit">Send</button>
 </form>
 """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()















