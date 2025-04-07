
import streamlit as st
import time
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Mission to Mars", layout="wide")

st.title("🚀 Journey to Mars")
st.markdown("### An Educational Walkthrough of a Mars Mission")

# Narration Text
narration = [
    "Welcome aboard! Today, we're taking a journey from Earth to the Red Planet — Mars.",
    "As our spacecraft launches, it leaves the atmosphere and enters the vastness of space.",
    "Now cruising through space, the spacecraft carefully navigates the millions of kilometers to reach Mars.",
    "And there it is — the Red Planet in sight. Our mission is almost complete. Welcome to Mars!"
]

# Display narration with timed delays
for line in narration:
    st.markdown(f"**{line}**")
    time.sleep(4)

# Set up animation parameters
fig, ax = plt.subplots(figsize=(10, 4))
earth_x, earth_y = 1, 0
mars_x, mars_y = 9, 0
spacecraft_path = np.linspace(earth_x, mars_x, 100)
spacecraft_y = np.sin(np.linspace(0, np.pi, 100)) * 0.5

# Animation simulation
space = st.empty()
for i in range(len(spacecraft_path)):
    ax.clear()
    ax.set_xlim(0, 10)
    ax.set_ylim(-1, 1)
    ax.set_facecolor("black")
    ax.plot(earth_x, earth_y, 'bo', markersize=12, label="Earth")
    ax.plot(mars_x, mars_y, 'ro', markersize=12, label="Mars")
    ax.plot(spacecraft_path[i], spacecraft_y[i], 'wo', markersize=8, label="Spacecraft")
    ax.legend(loc="upper right", facecolor='gray')
    ax.set_title("Spacecraft Journey to Mars", color="white")
    ax.tick_params(colors='white')
    for spine in ax.spines.values():
        spine.set_edgecolor('white')
    space.pyplot(fig)
    time.sleep(0.05)


# Play background music
audio_file = open("assets/background.mp3", "rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes, format="audio/mp3")
