import streamlit as st
import requests

# -----------------------------
# SETTINGS
# -----------------------------
USERNAME = "vishalk99vk"  # <-- change this
TITLE = "🚀 My GitHub Portfolio"
DESCRIPTION = "Hi, I'm Vishal 👋 A passionate developer and AI specialist. Explore my GitHub projects below."

# ✅ Manually map repos to Streamlit app links (deploy on Streamlit Cloud first)
STREAMLIT_APPS = {
    "📦 ZIP → JPG Converter": "https://all-image-type-to-jpeg-hgvbtewplye9h67bdq77kw.streamlit.app/",
    "Image Similarity Clustering App": "https://psldcqtszimyzo8nucxxbm.streamlit.app/",
    "File Comparison Tool": "https://match-cgc-files-ms69djbyyeaaw5g9wnnzdq.streamlit.app/",
    # Add more if needed...
}

# -----------------------------
# STREAMLIT CONFIG
# -----------------------------
st.set_page_config(page_title="GitHub Portfolio", layout="wide")
st.title(TITLE)
st.write(DESCRIPTION)
st.markdown("---")

# -----------------------------
# FETCH DATA FROM GITHUB API
# -----------------------------
url = f"https://api.github.com/users/{USERNAME}/repos?per_page=100&sort=updated"
response = requests.get(url)

if response.status_code == 200:
    repos = response.json()

    # -----------------------------
    # SEARCH, SORT & FILTER CONTROLS
    # -----------------------------
    languages = sorted({repo['language'] for repo in repos if repo['language']})
    languages = ["All"] + languages

    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        search_query = st.text_input("🔍 Search repositories", "").lower()
    with col2:
        sort_option = st.selectbox("Sort by", ["Last Updated", "Stars", "Forks", "Name (A-Z)"])
    with col3:
        lang_filter = st.selectbox("Filter by Language", languages)

    # Apply search filter
    if search_query:
        repos = [repo for repo in repos if search_query in repo['name'].lower()]

    # Apply language filter
    if lang_filter != "All":
        repos = [repo for repo in repos if repo['language'] == lang_filter]

    # Apply sort
    if sort_option == "Stars":
        repos = sorted(repos, key=lambda x: x['stargazers_count'], reverse=True)
    elif sort_option == "Forks":
        repos = sorted(repos, key=lambda x: x['forks_count'], reverse=True)
    elif sort_option == "Name (A-Z)":
        repos = sorted(repos, key=lambda x: x['name'].lower())
    else:  # Last Updated
        repos = sorted(repos, key=lambda x: x['updated_at'], reverse=True)

    # -----------------------------
    # DISPLAY REPOS IN GRID
    # -----------------------------
    if repos:
        for i in range(0, len(repos), 3):
            cols = st.columns(3)
            for col, repo in zip(cols, repos[i:i+3]):
                with col:
                    repo_name = repo['name']
                    app_link = STREAMLIT_APPS.get(repo_name, None)  # check if app link exists

                    st.markdown(
                        f"""
                        <div style="border-radius:15px; padding:20px; margin:10px; 
                                    background-color:#f8f9fa; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
                            <h3 style="margin:0;">📂 {repo_name}</h3>
                            <p style="color:#555;">{repo['description'] if repo['description'] else 'No description available'}</p>
                            <p>
                                ⭐ {repo['stargazers_count']} &nbsp;&nbsp; 
                                🍴 {repo['forks_count']} &nbsp;&nbsp; 
                                📝 {repo['language'] if repo['language'] else 'N/A'}
                            </p>
                            <a href="{repo['html_url']}" target="_blank" style="text-decoration:none;">
                                <button style="background-color:#4CAF50; color:white; border:none; 
                                               padding:10px 15px; border-radius:8px; cursor:pointer;">
                                    🔗 View Repo
                                </button>
                            </a>
                        """,
                        unsafe_allow_html=True
                    )

                    # Show "Run App" button only if mapped
                    if app_link:
                        st.markdown(
                            f"""
                            <a href="{app_link}" target="_blank" style="text-decoration:none;">
                                <button style="background-color:#2196F3; color:white; border:none; 
                                               padding:10px 15px; border-radius:8px; cursor:pointer; margin-top:8px;">
                                    🚀 Run App
                                </button>
                            </a>
                            """,
                            unsafe_allow_html=True
                        )

                    st.markdown("</div>", unsafe_allow_html=True)

    else:
        st.warning("No repositories found for the selected filters.")
else:
    st.error("❌ Failed to fetch repositories. Check username or API limit.")
