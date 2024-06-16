import streamlit as st

st.title("Description of my Application")


st.header('🔮Simple Sentiment Analyzer App')
st.image("./images/emot.png")

with st.expander("Emotion Analyzer"):
    st.markdown("""
    
    #
                 Emotion Analyzer 
Welcome to the Emotion Analyzer app! This Streamlit-based application is designed to analyze and classify your emotions based on the text you provide. Whether you're feeling happy, sad, angry, excited, nervous, or scared, our app aims to understand your emotional state through natural language processing.


                
    """, unsafe_allow_html=True)

st.header(' 🦁Image Classification')
st.image("./images/pred1.png")
st.image("./images/pred2.png")

with st.expander("Lion or Cheetah Image Classification "):
    st.markdown("""
    
    #
                Image Classification for Lions and Cheetahs
    Welcome to the Image Classification app! This application uses a machine learning model to classify images of lions and cheetahs. Simply upload an image, and the app will predict whether the image is of a lion or a cheetah.

                
    """, unsafe_allow_html=True)

st.header('🔍Prediction')
st.image("./images/pred3.png")

with st.expander("Weather Prediction"):
    st.markdown("""
    
    #
                Prediction of weather
The Weather Prediction App is a user-friendly web application designed to provide accurate weather forecasts and insights. Built using the powerful Streamlit framework, this app leverages machine learning models to predict weather conditions based on historical data and various meteorological parameters. Users can easily input data such as temperature, humidity, wind speed, and more to receive predictions on future weather conditions, including temperature ranges, precipitation, and other relevant metrics.
                
    """, unsafe_allow_html=True)