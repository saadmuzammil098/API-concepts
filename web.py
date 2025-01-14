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
        return None, f"Error fetching advice: {e}"

# Streamlit App
st.title("Random Advice Generator 💡")
st.write("Click the button below to get a random piece of advice.")

# State to hold the current advice
if "advice" not in st.session_state:
    st.session_state.advice = ""

# Fetch advice button
if st.button("Get Advice"):
    with st.spinner("Fetching advice..."):
        advice, error = fetch_advice()
        if error:
            st.error("Failed to fetch advice. Please try again later.")
        else:
            st.session_state.advice = advice

# Clear advice button
if st.button("Clear Advice"):
    st.session_state.advice = ""

# Display the advice
if st.session_state.advice:
    st.subheader("Here's your advice:")
    st.write(f"💬 *{st.session_state.advice}*")
