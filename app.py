
import streamlit as st
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

st.set_page_config(page_title="Mission to Mars", layout="wide")

st.title("🚀 Journey to Mars - Interactive Mission")
st.markdown("### Experience a realistic animated mission with visuals and controls.")

# Mission speed control
speed = st.slider("Control Spacecraft Speed", min_value=0.01, max_value=0.2, value=0.05, step=0.01)

# Play background music
audio_file = open("assets/background.mp3", "rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes, format="audio/mp3", start_time=0)

# Load images
earth_img = mpimg.imread("assets/earth.png")
mars_img = mpimg.imread("assets/mars.png")
rocket_img = mpimg.imread("assets/rocket.png")

# Narration text
narration = [
    "Welcome aboard! Today, we're taking a journey from Earth to the Red Planet — Mars.",
    "As our spacecraft launches, it leaves the atmosphere and enters the vastness of space.",
    "Now cruising through space, the spacecraft carefully navigates the millions of kilometers to reach Mars.",
    "And there it is — the Red Planet in sight. Our mission is almost complete. Welcome to Mars!"
]

# Display narration
for line in narration:
    st.markdown(f"**{line}**")
    time.sleep(3)

# Prepare for animation
fig, ax = plt.subplots(figsize=(10, 4))
earth_x, mars_x = 1, 9
spacecraft_path = np.linspace(earth_x, mars_x, 100)
spacecraft_y = np.sin(np.linspace(0, np.pi, 100)) * 0.5

space = st.empty()
for i in range(len(spacecraft_path)):
    ax.clear()
    ax.set_xlim(0, 10)
    ax.set_ylim(-1, 1)
    ax.set_facecolor("black")
    ax.imshow(earth_img, extent=[earth_x-0.5, earth_x+0.5, -0.5, 0.5])
    ax.imshow(mars_img, extent=[mars_x-0.5, mars_x+0.5, -0.5, 0.5])
    ax.imshow(rocket_img, extent=[spacecraft_path[i]-0.2, spacecraft_path[i]+0.2,
                                  spacecraft_y[i]-0.4, spacecraft_y[i]+0.4])
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
    space.pyplot(fig)
    time.sleep(speed)
