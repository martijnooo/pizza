import streamlit as st
from datetime import datetime
import time
import random
import os # We'll use this if we need to check paths

# --- Configuration ---
NEW_YEARS_DAY = datetime(datetime.now().year + 1, 1, 1)

EMOJIS = ['🍕', '🤯', '🥳', '🚀', '🔥', '🤪', '😵‍💫', '👽', '💥', '✨', '🌪️', '🧠', '🦩', '👾']

# YOUR THREE LOCAL CRAZY IMAGE FILE PATHS
# NOTE: These paths are relative to where you run 'streamlit run wild_countdown.py'
IMAGE_PATHS = [
    "images/image1.png",
    "images/image2.png", # Assuming you have image2.png and image3.png as well
    "images/pizza3.jpg"
]

# CSS for the bananas interface - INTENSIFIED
CRAZY_CSS = f"""
<style>
/* ... (Existing global styles omitted for brevity) ... */

h1 {{
    font-size: 90px !important;
    font-family: 'Impact', 'Arial Black', sans-serif;
    text-shadow: 6px 6px #000000;
    animation: color-flash 0.3s infinite alternate, aggressive-bounce 0.2s infinite;
    text-align: center;
    border-bottom: 10px double red;
    padding-bottom: 10px;
}}

/* Image Container Styling - Applying rotation to the ST element */
.crazy-image-container {{
    /* This targets the Streamlit element containing the image */
    border: 10px groove #FF00FF; /* Funky border */
    box-shadow: 0 0 20px black;
    margin: 10px;
    animation: random-rotation 5s infinite alternate; /* New rotation effect */
}}

/* Animation Keyframes */
@keyframes aggressive-gradient {{
    0% {{ background-position: 0% 0%; }}
    100% {{ background-position: 100% 100%; }}
}}

@keyframes aggressive-bounce {{
    from {{ transform: translateY(0px); }}
    to {{ transform: translateY(-20px); }}
}}

@keyframes color-flash {{
    0% {{ color: #FF0000; }}
    33% {{ color: #FFFF00; }}
    66% {{ color: #00FF00; }}
    100% {{ color: #FF00FF; }}
}}

@keyframes random-rotation {{
    0% {{ transform: rotate(0deg); }}
    25% {{ transform: rotate(5deg); }}
    75% {{ transform: rotate(-8deg); }}
    100% {{ transform: rotate(0deg); }}
}}

/* Ensure Streamlit container also has some chaos */
.main {{
    background-color: rgba(255, 255, 255, 0.2);
    padding: 30px;
}}

</style>
"""

# --- Functions ---
def calculate_countdown():
    """Calculates the time difference to New Year's Day."""
    now = datetime.now()
    return NEW_YEARS_DAY - now

def display_countdown(delta):
    """Displays the countdown with crazy metrics in a jumbled layout."""
    total_seconds = int(delta.total_seconds())
    if total_seconds <= 0:
        st.balloons()
        st.toast(f"🎉 NEW YEAR, NEW PIZZA! {random.choice(EMOJIS)} {random.choice(EMOJIS)}")
        return

    days = total_seconds // (60 * 60 * 24)
    hours = (total_seconds % (60 * 60 * 24)) // (60 * 60)
    minutes = (total_seconds % (60 * 60)) // 60
    seconds = total_seconds % 60

    col_order = random.sample(range(4), 4)
    cols = st.columns(4)

    metrics_data = [
        (f"DAYS {random.choice(EMOJIS)}", days),
        (f"HOURS {random.choice(EMOJIS)}", hours),
        (f"MINUTES {random.choice(EMOJIS)}", minutes),
        (f"SECONDS {random.choice(EMOJIS)}", seconds)
    ]

    for i, col_index in enumerate(col_order):
        title, value = metrics_data[i]
        cols[col_index].metric(title, value, delta=random.choice(EMOJIS))


def display_crazy_message():
    """Displays the personalized message with max energy."""
    st.markdown(f"""
        # 🚨 DANGER: PIZZA INCOMING AT WARP SPEED\! {random.choice(EMOJIS)}
        ## TIME IS MELTING. THE PIZZA IS WAITING. WE ARE UNHINGED. {random.choice(EMOJIS)} {random.choice(EMOJIS)}
    """)

def display_chaotic_image_area():
    """
    Displays the three local images using st.image() and applies custom CSS class for rotation.
    """

    img_cols = st.columns(3)

    for i, path in enumerate(IMAGE_PATHS):
        # 1. Start a custom container with the chaotic CSS class
        # This custom div wraps the image and gets the rotation/border
        img_cols[i].markdown(f"<div class='crazy-image-container'>", unsafe_allow_html=True)

        # 2. Use st.image to load the local file path reliably
        # We must set width to 100% to fill the container correctly
        try:
            img_cols[i].image(path, use_container_width='always')
        except FileNotFoundError:
            # Display a warning if the file isn't found
            img_cols[i].warning(f"File not found: {path}. Check folder structure!")

        # 3. Close the custom container
        img_cols[i].markdown("</div>", unsafe_allow_html=True)


# --- Streamlit App Layout ---

st.set_page_config(
    page_title="WILD PIZZA COUNTDOWN",
    page_icon="🤯",
    layout="wide"
)

# Inject the Crazy CSS
st.markdown(CRAZY_CSS, unsafe_allow_html=True)

display_crazy_message()

st.markdown("---")


# Create placeholder for the dynamic countdown metrics
countdown_placeholder = st.empty()

st.markdown("---")

# Display the images immediately
display_chaotic_image_area()



st.sidebar.markdown(f"**{random.choice(EMOJIS)} SYSTEM STATUS: EXTREMELY BANANAS {random.choice(EMOJIS)}**")

# The main loop to update the countdown every second
while True:
    delta = calculate_countdown()

    with countdown_placeholder.container():
        display_countdown(delta)
        # Randomly change the background color of a sidebar element for extra flash
        st.sidebar.markdown(f"<div style='background-color: {random.choice(['red', 'yellow', 'lime', 'magenta'])}; padding: 5px; margin-top: 10px;'>PIZZA HYPE LEVEL: 1000%</div>", unsafe_allow_html=True)

    if delta.total_seconds() <= 0:
        break

    time.sleep(1)