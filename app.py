import streamlit as st

# ────────────────────────────────────────────────
# Basic SEO & meta tags for better Google indexing
# ────────────────────────────────────────────────
st.markdown("""
    <meta name="description" content="ERAS Africa – Enhanced Recovery After Surgery hub for African hospitals. Risk calculator, guidelines, training, e-courses and CEUs.">
    <meta name="keywords" content="ERAS Africa, Enhanced Recovery After Surgery, perioperative care, surgical recovery, CEU training, African hospitals, risk calculator">
    <meta name="author" content="ERAS Africa">
    <meta property="og:title" content="ERAS Africa – Enhanced Recovery After Surgery">
    <meta property="og:description" content="Tools, guidelines and certified training for better surgical outcomes in Africa and LMICs.">
    <meta property="og:image" content="https://raw.githubusercontent.com/Ama-tom/eras-africa-hub/main/icons/ERAS-192.jpg">
    <meta property="og:url" content="https://eras-africa-eth-lumc.streamlit.app/">
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────
# Page config & custom CSS for attractive design
# ────────────────────────────────────────────────
st.set_page_config(
    page_title="ERAS Africa – Enhanced Recovery After Surgery",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Modern CSS (blue theme, smooth animations, card style)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body, [class*="stApp"] {
        font-family: 'Inter', sans-serif;
        background-color: #f8fafc;
    }

    .stApp {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
    }

    h1, h2, h3 {
        color: #1e40af;
        font-weight: 700;
    }

    .stButton>button {
        background-color: #1e40af;
        color: white;
        border-radius: 8px;
        padding: 12px 24px;
        font-weight: 600;
        transition: all 0.3s ease;
        border: none;
    }

    .stButton>button:hover {
        background-color: #1e3a8a;
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(30,64,175,0.3);
    }

    .card {
        background: white;
        border-radius: 12px;
        padding: 24px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -1px rgba(0,0,0,0.06);
        margin-bottom: 24px;
        transition: transform 0.3s ease;
    }

    .card:hover {
        transform: translateY(-4px);
    }

    .footer {
        margin-top: 60px;
        padding: 40px 0;
        background: #0f172a;
        color: white;
        text-align: center;
        border-radius: 12px 12px 0 0;
    }
    </style>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────
# Hero / Welcome Section
# ────────────────────────────────────────────────
col_logo, col_title = st.columns([1, 6])
with col_logo:
    st.image("icons/ERAS-192.jpg", width=120)
with col_title:
    st.title("Enhanced Recovery After Surgery – Africa")
    st.markdown("**Improving surgical outcomes in African and low-resource settings**")

st.markdown("""
**ERAS Africa** is a collaborative initiative to bring **evidence-based perioperative care** to hospitals across Africa.  
We offer risk prediction tools, adapted guidelines, professional training, and certified e-courses — helping reduce complications, shorten hospital stays, and enhance patient recovery.
""")

st.markdown("---")

# ────────────────────────────────────────────────
# Quick Access Cards (attractive, clickable)
# ────────────────────────────────────────────────
st.subheader("Explore ERAS Africa Resources")

cols = st.columns(3)

with cols[0]:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 🩺 Risk Calculator")
        st.markdown("Predict prolonged stay and complications in real time.")
        st.page_link("pages/1_Calculator.py", label="Open Calculator", icon="🩺")
        st.markdown('</div>', unsafe_allow_html=True)

with cols[1]:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 📘 Guidelines & Protocols")
        st.markdown("Adapted ERAS protocols for African hospitals.")
        st.page_link("pages/2_Guidelines.py", label="View Guidelines", icon="📘")
        st.markdown('</div>', unsafe_allow_html=True)

with cols[2]:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 🎓 Training & E-Course")
        st.markdown("Earn up to **60 CEUs** (15 per program) – certified.")
        st.page_link("pages/6_E-Course.py", label="Get Certified → Start E-Course", icon="🎓")
        st.markdown('</div>', unsafe_allow_html=True)

# ────────────────────────────────────────────────
# Call-to-Action Banner
# ────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div style="background: #1e40af; color: white; padding: 32px; border-radius: 12px; text-align: center;">
    <h2 style="margin: 0;">Ready to Improve Surgical Recovery?</h2>
    <p>Join thousands of professionals using ERAS tools in Africa.</p>
    <a href="#pages/6_E-Course.py" target="_self">
        <button style="background: white; color: #1e40af; border: none; padding: 16px 32px; font-size: 18px; font-weight: bold; border-radius: 8px; cursor: pointer;">
            Get Certified – Start E-Course Now
        </button>
    </a>
</div>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────
# Footer with contact
# ────────────────────────────────────────────────
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("**ERAS Africa**")
    st.markdown("Advancing perioperative care in Africa")
with col2:
    st.markdown("**Contact**")
    st.markdown("Email: amaretom22@gmail.com")
    st.markdown("Organization: ERAS Africa")
with col3:
    st.markdown("**Important Links**")
    st.markdown("[ERAS Society](https://erassociety.org/)")
    st.markdown("[Federal Ministry of Health Ethiopia](https://www.moh.gov.et/)")

st.caption("© 2026 ERAS Africa – All rights reserved | For healthcare professionals | Pilot version")