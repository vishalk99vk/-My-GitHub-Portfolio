import streamlit as st
import base64

# -----------------------------
# SETTINGS
# -----------------------------
TITLE = "🚀 My Streamlit Portfolio"
DESCRIPTION = "Hi, I'm Vishal 👋 A passionate developer and AI specialist. Here are my deployed Streamlit projects."

# ✅ Only Streamlit apps (manually added)
STREAMLIT_APPS = {
    "All-Image-Type-To-JPEG": {
        "url": "https://all-image-type-to-jpeg-hgvbtewplye9h67bdq77kw.streamlit.app/",
        "description": "Convert any image format into JPEG seamlessly."
    },
    "CGC-": {
        "url": "https://psldcqtszimyzo8nucxxbm.streamlit.app/",
        "description": "CGC Project - AI-powered processing."
    },
    "Match-CGC-files": {
        "url": "https://match-cgc-files-ms69djbyyeaaw5g9wnnzdq.streamlit.app/",
        "description": "Smart file matcher for CGC datasets."
    },
    # Add more here...
}

# -----------------------------
# STREAMLIT CONFIG
# -----------------------------
st.set_page_config(page_title="Streamlit Portfolio", layout="wide")

# -----------------------------
# BACKGROUND VIDEO
# -----------------------------
def get_video_base64(video_file):
    with open(video_file, "rb") as file:
        data = file.read()
    return base64.b64encode(data).decode()

VIDEO_PATH = "bg.mp4"   # make sure bg.mp4 is in the same folder
VIDEO_BASE64 = get_video_base64(VIDEO_PATH)

st.markdown(f"""
    <style>
    .video-bg {{
        position: fixed;
        right: 0;
        bottom: 0;
        min-width: 100%; 
        min-height: 100%;
        z-index: -1;
        object-fit: cover;
    }}
    </style>

    <video autoplay muted loop class="video-bg">
        <source src="data:video/mp4;base64,{VIDEO_BASE64}" type="video/mp4">
    </video>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.title(TITLE)
st.write(DESCRIPTION)
st.markdown("---")

# -----------------------------
# DISPLAY PROJECTS
# -----------------------------
if STREAMLIT_APPS:
    for i, (name, details) in enumerate(STREAMLIT_APPS.items()):
        if i % 3 == 0:
            cols = st.columns(3)

        col = cols[i % 3]
        with col:
            st.markdown(
                f"""
                <div style="border-radius:15px; padding:20px; margin:10px; 
                            background-color:rgba(248, 249, 250, 0.85); 
                            box-shadow: 0 4px 8px rgba(0,0,0,0.3);">
                    <h3 style="margin:0;">📂 {name}</h3>
                    <p style="color:#333;">{details['description']}</p>
                    <a href="{details['url']}" target="_blank" style="text-decoration:none;">
                        <button style="background: linear-gradient(90deg, #2196F3, #21CBF3); 
                                       color:white; border:none; 
                                       padding:10px 15px; border-radius:8px; cursor:pointer; margin-top:8px;">
                            🚀 Run App
                        </button>
                    </a>
                </div>
                """,
                unsafe_allow_html=True
            )
else:
    st.warning("No Streamlit apps have been added yet.")
