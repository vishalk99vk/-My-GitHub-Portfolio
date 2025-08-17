import streamlit as st

# -----------------------------
# SETTINGS
# -----------------------------
TITLE = "🚀 Vishal Kumar's Portfolio"
DESCRIPTION = "Hi, I'm Vishal 👋 A passionate Developer & AI Specialist. Explore my deployed Streamlit projects below."

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
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Streamlit Portfolio", layout="wide")

# -----------------------------
# LIQUID CHROME BACKGROUND
# -----------------------------
liquid_chrome_bg = """
<canvas id="liquid-chrome"></canvas>

<style>
  body, html {
    margin: 0;
    padding: 0;
    overflow-x: hidden;
    height: 100%;
    width: 100%;
    font-family: 'Segoe UI', sans-serif;
  }

  #liquid-chrome {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: -2; /* background */
  }

  .portfolio-header {
    position: relative;
    z-index: 1;
    text-align: center;
    color: white;
    padding: 2rem;
  }

  .app-card {
    border-radius: 20px;
    padding: 20px;
    margin: 15px;
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(12px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.25);
    transition: transform 0.2s ease-in-out;
  }
  .app-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 12px 30px rgba(0,0,0,0.35);
  }

  .run-btn {
    background: linear-gradient(90deg, #007BFF, #00C6FF);
    color: white;
    border: none;
    padding: 10px 15px;
    border-radius: 8px;
    cursor: pointer;
    margin-top: 10px;
    font-weight: bold;
    text-decoration: none;
    display: inline-block;
  }
</style>

<script type="module">
import { Renderer, Program, Mesh, Triangle } from "https://cdn.skypack.dev/ogl";

const canvas = document.getElementById("liquid-chrome");
const renderer = new Renderer({ dpr: 2, canvas });
const gl = renderer.gl;

const vertex = `
  attribute vec2 position;
  varying vec2 vUv;
  void main() {
    vUv = (position + 1.0) * 0.5;
    gl_Position = vec4(position, 0, 1);
  }
`;

const fragment = `
  precision highp float;
  uniform float uTime;
  varying vec2 vUv;

  void main() {
    float wave = 0.1 * sin(10.0 * vUv.x + uTime) + 0.1 * cos(10.0 * vUv.y + uTime);
    gl_FragColor = vec4(0.2 + wave, 0.5 + wave, 0.8, 1.0);
  }
`;

const program = new Program(gl, {
  vertex,
  fragment,
  uniforms: { uTime: { value: 0 } },
});

const mesh = new Mesh(gl, { geometry: new Triangle(gl), program });

function resize() {
  renderer.setSize(window.innerWidth, window.innerHeight);
}
window.addEventListener("resize", resize);
resize();

function update(t) {
  requestAnimationFrame(update);
  program.uniforms.uTime.value = t * 0.001;
  renderer.render({ scene: mesh });
}
requestAnimationFrame(update);
</script>
"""
st.markdown(liquid_chrome_bg, unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.markdown(
    f"""
    <div class="portfolio-header">
        <h1>{TITLE}</h1>
        <p style="font-size:18px; max-width:800px; margin:auto;">{DESCRIPTION}</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# DISPLAY PROJECTS
# -----------------------------
if STREAMLIT_APPS:
    cols = st.columns(3)
    for i, (name, details) in enumerate(STREAMLIT_APPS.items()):
        col = cols[i % 3]
        with col:
            st.markdown(
                f"""
                <div class="app-card">
                    <h3 style="margin:0;">📂 {name}</h3>
                    <p style="color:#eee;">{details['description']}</p>
                    <a href="{details['url']}" target="_blank" class="run-btn">🚀 Run App</a>
                </div>
                """,
                unsafe_allow_html=True
            )
else:
    st.warning("No Streamlit apps have been added yet.")
