import streamlit as st


st.header('Emotion Analyzer Source Code')
st.subheader('This python code is implemented for Streamlit')
st.code(''' 
import streamlit as st
import joblib
import nltk
from nltk.corpus import names

# Download the necessary NLTK data
nltk.download('names')

# Load the classifier from the .sav file
classifier = joblib.load(r'pages/emotion_classifier.sav')  # Ensure this file exists and the path is correct

# Define function to extract features from input sentence
def word_features(words):
    return dict([(word, True) for word in words.split()])

# Streamlit app
def main():
    st.title("Emotion Analyzer :rainbow:")
    st.markdown("""
    Welcome to the Streamlit app for analyzing different emotions.
    Enter your current feeling in the text box below, and let's see what the emotion analyzer says!
    """)

    message = st.text_input("Tell me what you feel today:")

    def classify_feeling():
        if message:
            message_emotion = classifier.classify(word_features(message))
            if message_emotion == 'happy':
                st.write("You seem happy! :smile:")
            elif message_emotion == 'sad':
                st.write("You seem sad. :pensive:")
            elif message_emotion == 'angry':
                st.write("You seem angry. :rage:")
            elif message_emotion == 'excited':
                st.write("You seem excited! :star_struck:")
            elif message_emotion == 'nervous':
                st.write("You seem nervous. :grimacing:")
            elif message_emotion == 'scared':
                st.write("You seem scared. :scream:")
            else:
                st.write("Hmm, I'm not sure about that feeling. :thinking_face:")
        else:
            st.write("Please enter a feeling to analyze.")

    if st.button('Analyze Feeling'):
        classify_feeling()

if __name__ == '__main__':
    main()



''')