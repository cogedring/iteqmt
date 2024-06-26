import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title, hide_pages

# Adding the page title
add_page_title()

# Displaying the pages
show_pages(
    [   
        Page("home.py", "ITEQMT ENDTERM - FINAL REQUIREMENT", "👨‍💻"),
        Section("Main Page", "💻"),
        Page("pages/about.py", "ABOUT ME", "1️⃣", in_section=True),
        Page("pages/appdescription.py", "App Description", "2️⃣", in_section=True),
        Page("pages/learnings.py", " What I Have Learned", "3️⃣", in_section=True),
     
        Section("My Projects", "📂"),
        Page("pages/emotion_analyzer.py", "Emotion Analyzer", "1️⃣", in_section=True),
        Page("pages/image_classification.py", "Image Classification", "2️⃣", in_section=True),
        Page("pages/predict_weather.py", "Weather Prediction", "3️⃣", in_section=True),

        Section("Project Source Code", "💾"),
        Page("pages/analyze_src.py", "Sentiment Analyzer SRC", "1️⃣", in_section=True),
        Page("pages/classification_src.py", "Image Classification SRC", "2️⃣", in_section=True),
        Page("pages/prediction_src.py", "Weather App Prediction SRC", "3️⃣", in_section=True),
    ]
)

hide_pages(["Thank you"])

st.image("./backs.jpg")

st.info("👨‍🔧 Please take note when on streamlit.app the [Image Classification] pages are not working due to Memory Limitation of 'Free Tier' hosting of Streamlit") 
st.markdown("---")

with st.expander("Sample ""st.expander"""):
    st.markdown("""
    
    <a href=""><img src="https://user-images.githubusercontent.com/875246/185755203-17945fd1-6b64-46f2-8377-1011dcb1a444.png" height="50" /></a>

    #

        HISTORY, PURPOSE AND USAGE
        Lorem ipsum, or lipsum as it is sometimes known, is dummy text used in laying out print, graphic or web designs. 
        The passage is attributed to an unknown typesetter in the 15th century who is thought to have scrambled parts of Cicero's De Finibus Bonorum et Malorum for use in a type specimen book. It usually begins with:
        “Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.”
        The purpose of lorem ipsum is to create a natural looking block of text (sentence, paragraph, page, etc.) that doesn't distract from the layout. 
        A practice not without controversy, laying out pages with meaningless filler text can be very useful when the focus is meant to be on design, not content.
        The passage experienced a surge in popularity during the 1960s when Letraset used it on their dry-transfer sheets, and again during the 90s as desktop publishers bundled the text with their software. 
        Today it's seen all around the web; on templates, websites, and stock designs. Use our generator to get your own, or read on for the authoritative history of lorem ipsum.
        
    #""", unsafe_allow_html=True)

st.markdown("""
### 👨‍🎓 Sample Header Title

##### 👨‍👦‍👦 Subheader Title

* Bullet 1
* Bullet 2
* Bullet 3


##### 👨‍🔧 More Content

   HISTORY, PURPOSE AND USAGE
        Lorem ipsum, or lipsum as it is sometimes known, is dummy text used in laying out print, graphic or web designs. 
        The passage is attributed to an unknown typesetter in the 15th century who is thought to have scrambled parts of Cicero's De Finibus Bonorum et Malorum for use in a type specimen book. It usually begins with:
        “Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.”
        The purpose of lorem ipsum is to create a natural looking block of text (sentence, paragraph, page, etc.) that doesn't distract from the layout. 
        A practice not without controversy, laying out pages with meaningless filler text can be very useful when the focus is meant to be on design, not content.
        The passage experienced a surge in popularity during the 1960s when Letraset used it on their dry-transfer sheets, and again during the 90s as desktop publishers bundled the text with their software. 
        Today it's seen all around the web; on templates, websites, and stock designs. Use our generator to get your own, or read on for the authoritative history of lorem ipsum.

### 🔎 Overview""", unsafe_allow_html=True)


st.image("./backS.jpg")


st.markdown("""
Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Id neque aliquam vestibulum morbi blandit cursus risus. Sagittis nisl rhoncus mattis rhoncus. 
Purus viverra accumsan in nisl nisi scelerisque eu. Nunc mi ipsum faucibus vitae aliquet nec ullamcorper sit amet. 
Eleifend quam adipiscing vitae proin. Neque convallis a cras semper auctor neque. Et tortor consequat id porta nibh. 
Vitae nunc sed velit dignissim sodales ut eu. Bibendum ut tristique et egestas quis ipsum suspendisse. 
Pharetra massa massa ultricies mi. In nulla posuere sollicitudin aliquam ultrices sagittis. Et pharetra pharetra massa massa. 
Pretium viverra suspendisse potenti nullam ac. Viverra accumsan in nisl nisi scelerisque eu ultrices vitae auctor. 
Nibh mauris cursus mattis molestie a iaculis at erat. Diam sit amet nisl suscipit. 
Urna molestie at elementum eu facilisis sed odio morbi quis. Arcu non sodales neque sodales.
            
### ⭐ Star the project on Github  <iframe src="https://ghbtns.com/github-btn.html?user=koalatech&repo=streamlit_web_app&type=star&count=true"  width="150" height="20" title="GitHub"></iframe>   
""", unsafe_allow_html=True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
