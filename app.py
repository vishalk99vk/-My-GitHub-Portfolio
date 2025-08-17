import streamlit as st

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
                            background-color:#f8f9fa; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
                    <h3 style="margin:0;">📂 {name}</h3>
                    <p style="color:#555;">{details['description']}</p>
                    <a href="{details['url']}" target="_blank" style="text-decoration:none;">
                        <button style="background-color:#2196F3; color:white; border:none; 
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
