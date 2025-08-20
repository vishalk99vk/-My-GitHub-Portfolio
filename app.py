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
    "Take-all-images-from-different-folder-to-a-folder":{
        "url": "https://take-all-images-from-different-folder-to-a-folder-3vmpmkvlj2tf.streamlit.app/",
        "description": "Take-all-images-from-different-folder-to-a-folder."
        },
    "take-all-images-from-different-folder-to-a-folder": {
        "url": "https://match-cgc-files-ms69djbyyeaaw5g9wnnzdq.streamlit.app/",
        "description": "take-all-images-from-different-folder-to-a-folder."
    # Add more here...
}

# -----------------------------
# STREAMLIT CONFIG
# -----------------------------
st.set_page_config(page_title="Streamlit Portfolio", layout="wide")

# -----------------------------
# CUSTOM CSS (Background + Glass Banner + Cards)
# -----------------------------
st.markdown("""
    <style>
    /* Gradient background */
    body {
        background: linear-gradient(135deg, #1e1e2f, #2c3e50, #34495e, #1c1c1c);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        color: white;
    }
    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    /* Hero Banner (Glassmorphism) */
    .hero {
        width: 100%;
        text-align: center;
        padding: 100px 20px;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        margin-bottom: 40px;
        box-shadow: 0 8px 30px rgba(0,0,0,0.6);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
    }
    .hero h1 {
        font-size: 3.5em;
        margin: 0;
        background: linear-gradient(45deg, #00c6ff, #0072ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: fadeIn 2s ease-in-out;
    }
    .hero p {
        font-size: 1.3em;
        color: #eee;
        margin-top: 15px;
        animation: fadeIn 3s ease-in-out;
    }
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }

    /* Card Style */
    .card {
        border-radius: 15px; 
        padding: 20px; 
        margin: 10px; 
        background: rgba(255,255,255,0.07); 
        box-shadow: 0 4px 15px rgba(0,0,0,0.4);
        transition: all 0.3s ease;
    }
    .card:hover {
        transform: scale(1.05);
        box-shadow: 0 0 20px #00ffe5;
    }

    /* Run button */
    .run-btn {
        background: linear-gradient(45deg, #00c6ff, #0072ff);
        color: white; 
        border: none; 
        padding: 10px 15px; 
        border-radius: 8px; 
        cursor: pointer; 
        text-decoration: none;
        font-weight: bold;
    }
    .run-btn:hover {
        background: linear-gradient(45deg, #ff6ec4, #7873f5);
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# HERO SECTION
# -----------------------------
st.markdown(f"""
    <div class="hero">
        <h1>Hi, I'm Vishal 🚀</h1>
        <p>AI Specialist • Developer • Streamlit Enthusiast</p>
    </div>
""", unsafe_allow_html=True)

# -----------------------------
# PROJECTS SECTION
# -----------------------------
st.markdown(f"<h2 style='text-align:center;'>{TITLE}</h2>", unsafe_allow_html=True)
st.write(DESCRIPTION)
st.markdown("---")

if STREAMLIT_APPS:
    for i, (name, details) in enumerate(STREAMLIT_APPS.items()):
        if i % 3 == 0:
            cols = st.columns(3)

        col = cols[i % 3]
        with col:
            st.markdown(
                f"""
                <div class="card">
                    <h3 style="margin:0;">📂 {name}</h3>
                    <p style="color:#ddd;">{details['description']}</p>
                    <a href="{details['url']}" target="_blank" class="run-btn">🚀 Run App</a>
                </div>
                """,
                unsafe_allow_html=True
            )
else:
    st.warning("No Streamlit apps have been added yet.")
