import streamlit as st
import time

# Set the page configuration
st.set_page_config(page_title="Simple Clock", page_icon="🕒", layout="centered")

# Create the clock interface
st.title("Simple Clock")
clock_placeholder = st.empty()

# Update the clock every second
while True:
    current_time = time.strftime("%H:%M:%S")
    clock_placeholder.title(current_time)
    time.sleep(1)
