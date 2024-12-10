import streamlit as st
import requests

# API URL
API_URL = "https://api.adviceslip.com/advice"

def fetch_advice():
    """
    Fetch a random piece of advice from the Advice Slip API.
    
    Returns:
        str: A random piece of advice.
    """
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise HTTPError for bad responses
        advice_data = response.json()
        return advice_data["slip"]["advice"]
    except requests.exceptions.RequestException as e:
        return f"Error fetching advice: {e}"

# Streamlit App
st.title("Random Advice Generator 💡")
st.write("Click the button below to get a random piece of advice.")

if st.button("Get Advice"):
    advice = fetch_advice()
    st.subheader("Here's your advice:")
    st.write(f"💬 *{advice}*")
