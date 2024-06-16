import streamlit as st
import pickle

# Load the trained NaiveBayesClassifier from the saved file
filename = 'pages/weatherprediction.sav'
with open(filename, 'rb') as file:
    loaded_model = pickle.load(file)

st.title("🌦️ WEATHER PREDICTION 🌦️")
st.subheader("Enter weather details to predict the condition:")

# User inputs for weather details
precipitation_input = st.slider("Precipitation (in inches): ", 0.0, 100.0, 0.0)
temp_max_input = st.slider("Maximum Temperature (°C): ", 0, 100, 0)
temp_min_input = st.slider("Minimum Temperature (°C): ", 0, 100, 0)
wind_input = st.slider("Wind Speed (km/h): ", 0, 100, 0)

# Function to make a prediction
def predict_weather_condition(precipitation, temp_max, temp_min, wind):
    # Features function to convert inputs into a dictionary format expected by the model
    def features(precipitation, temp_max, temp_min, wind):
        return {
            'precipitation': precipitation,
            'temp_max': temp_max,
            'temp_min': temp_min,
            'wind': wind
        }

    # Apply features function to user inputs
    test_data = features(precipitation, temp_max, temp_min, wind)

    # Use the model to get the predicted weather condition
    prediction = loaded_model.classify(test_data)
    return prediction

# Display button and result
if st.button('Predict'):
    predicted_condition = predict_weather_condition(precipitation_input, temp_max_input, temp_min_input, wind_input)
    st.text("The predicted weather condition based on the given details is:")
    st.text_area(label="", value=str(predicted_condition), height=100)
