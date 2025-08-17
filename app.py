import streamlit as st

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Vishal Kumar | Portfolio", layout="wide")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
    <style>
    /* Background animation */
    body {
        background: linear-gradient(-45deg, #1e1e2f, #232946, #16161a, #0f0f0f);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        color: white;
    }
    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    /* Center Title */
    .main-title {
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        margin-bottom: -10px;
    }

    /* Typing animation */
    .typing {
        width: 25ch;
        white-space: nowrap;
        overflow: hidden;
        border-right: 3px solid orange;
        font-size: 20px;
        animation: typing 4s steps(30, end), blink .75s step-end infinite;
        margin: auto;
        text-align: center;
    }
    @keyframes typing {
        from { width: 0 }
        to { width: 25ch }
    }
    @keyframes blink {
        from, to { border-color: transparent }
        50% { border-color: orange; }
    }

    /* Card Style */
    .card {
        background: rgba(255,255,255,0.05);
        border-radius: 15px;
        padding: 25px;
        margin: 10px;
        transition: 0.3s;
        box-shadow: 0 4px 15px rgba(0,0,0,0.4);
    }
    .card:hover {
        transform: scale(1.05);
        box-shadow: 0 0 25px #00ffe5;
    }

    /* Run Button */
    .run-btn {
        display: inline-block;
        padding: 10px 20px;
        border-radius: 8px;
        font-weight: bold;
        text-decoration: none;
        color: white;
        background: linear-gradient(45deg, #00c6ff, #0072ff);
        transition: 0.4s;
    }
    .run-btn:hover {
        background: linear-gradient(45deg, #ff6ec4, #7873f5);
        box-shadow: 0 0 15px #ff6ec4;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- PORTFOLIO HEADER ----------------
st.markdown("<h1 class='main-title'>🚀 Vishal Kumar's Portfolio</h1>", unsafe_allow_html=True)
st.markdown("<p class='typing'>Hi, I'm Vishal 👋 Passionate AI Specialist!</p>", unsafe_allow_html=True)
st.write("")

# ---------------- PROJECTS ----------------
STREAMLIT_APPS = {
    "All-Image-Type-To-JPEG": {
        "description": "Convert any image format into JPEG seamlessly.",
        "url": "https://your-app-link-1.streamlit.app"
    },
    "CGC-Project": {
        "description": "CGC Project - AI-powered processing.",
        "url": "https://your-app-link-2.streamlit.app"
    },
    "Match-CGC-files": {
        "description": "Smart file matcher for CGC datasets.",
        "url": "https://your-app-link-3.streamlit.app"
    }
}

cols = st.columns(len(STREAMLIT_APPS))
for i, (name, app) in enumerate(STREAMLIT_APPS.items()):
    with cols[i]:
        st.markdown(f"""
            <div class="card">
                <h3>📁 {name}</h3>
                <p>{app['description']}</p>
                <a class="run-btn" href="{app['url']}" target="_blank">🚀 Run App</a>
            </div>
        """, unsafe_allow_html=True)
