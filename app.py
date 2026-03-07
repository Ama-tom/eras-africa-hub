import streamlit as st

# ────────────────────────────────────────────────
# Page config + vibrant African-inspired CSS
# ────────────────────────────────────────────────
st.set_page_config(
    page_title="ERAS Africa – Enhanced Recovery After Surgery",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS – no white background, rich colors, subtle animations
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@700&display=swap');

    html, body, [class*="stApp"] {
        font-family: 'Inter', sans-serif;
        background: linear-gradient(135deg, #0f766e 0%, #166534 50%, #d97706 100%);
        background-attachment: fixed;
        color: #fefce8 !important;
    }

    section[data-testid="stSidebar"] {
        background: rgba(30,58,138,0.85) !important;
        backdrop-filter: blur(8px);
    }

    h1 {
        font-family: 'Playfair Display', serif;
        color: #fbbf24;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.6);
        font-size: 3.8rem;
        text-align: center;
        margin-bottom: 0.2rem;
    }

    h2 {
        color: #fefce8;
        font-weight: 700;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.5);
    }

    .stButton > button {
        background: linear-gradient(90deg, #fbbf24, #f59e0b);
        color: #1e3a8a;
        border: none;
        border-radius: 12px;
        padding: 16px 40px;
        font-size: 1.25rem;
        font-weight: bold;
        transition: all 0.4s ease;
        box-shadow: 0 6px 15px rgba(251,191,36,0.4);
        margin: 20px auto;
        display: block;
    }

    .stButton > button:hover {
        background: linear-gradient(90deg, #f59e0b, #fbbf24);
        transform: scale(1.08);
        box-shadow: 0 12px 25px rgba(251,191,36,0.6);
    }

    .mission-card {
        background: rgba(255,255,255,0.15);
        backdrop-filter: blur(10px);
        border-radius: 16px;
        padding: 32px;
        border: 1px solid rgba(251,191,36,0.3);
        margin: 30px 0;
        transition: all 0.4s ease;
    }

    .mission-card:hover {
        background: rgba(255,255,255,0.25);
        transform: translateY(-10px);
        border: 1px solid #fbbf24;
        box-shadow: 0 15px 30px rgba(0,0,0,0.4);
    }

    .footer {
        margin-top: 80px;
        padding: 60px 0 30px;
        background: linear-gradient(135deg, #1e3a8a 0%, #0f172a 100%);
        color: #e0f2fe;
        text-align: center;
        border-radius: 20px 20px 0 0;
    }

    .footer a {
        color: #fbbf24;
        font-weight: 500;
        text-decoration: none;
    }

    .footer a:hover {
        color: #fefce8;
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────
# Hero Welcome Section – no images, only color & text
# ────────────────────────────────────────────────
st.markdown("""
    <div style="text-align: center; padding: 100px 20px 80px;">
        <h1>ERAS Africa</h1>
        <h2 style="color: #fbbf24; margin: 10px 0 40px;">Enhanced Recovery After Surgery</h2>
        <p style="font-size: 1.4rem; max-width: 900px; margin: 0 auto 40px; line-height: 1.6;">
            Empowering African healthcare teams with evidence-based perioperative care,  
            certified training, and practical tools to reduce complications and transform surgical recovery.
        </p>
    </div>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────
# Mission & Values – colorful animated cards
# ────────────────────────────────────────────────
st.markdown("### Why ERAS Africa Matters")

cols = st.columns(3)

with cols[0]:
    st.markdown("""
        <div class="mission-card">
            <h3>Patient-First Recovery</h3>
            <p>Reduce hospital stays, lower complications, and improve outcomes using proven ERAS protocols adapted for African realities.</p>
        </div>
    """, unsafe_allow_html=True)

with cols[1]:
    st.markdown("""
        <div class="mission-card">
            <h3>Certified Training</h3>
            <p>Up to 60 CEUs through e-courses and workshops – certified by ERAS Africa, FMOH Ethiopia, African Union & CDC Africa.</p>
        </div>
    """, unsafe_allow_html=True)

with cols[2]:
    st.markdown("""
        <div class="mission-card">
            <h3>Local Leadership</h3>
            <p>Tools, guidelines and collaboration designed by and for African healthcare professionals and institutions.</p>
        </div>
    """, unsafe_allow_html=True)

# ────────────────────────────────────────────────
# Big Call-to-Action Button – Get Certified
# ────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
    <div style="text-align: center; padding: 80px 20px;">
        <h2 style="color: #fbbf24; margin-bottom: 30px;">Ready to Lead Change in Surgical Care?</h2>
        <a href="/E-Course" target="_self">
            <button style="font-size: 1.5rem; padding: 20px 60px;">
                Get Certified – Start E-Course Now →
            </button>
        </a>
        <p style="margin-top: 20px; font-size: 1.1rem; color: #fefce8;">
            Earn up to 60 CEUs – join hundreds of professionals already transforming perioperative care in Africa.
        </p>
    </div>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────
# Footer
# ────────────────────────────────────────────────
st.markdown("""
    <div class="footer">
        <h3>ERAS Africa</h3>
        <p>Advancing perioperative excellence across the continent</p>
        <p>Email: <a href="mailto:amaretom22@gmail.com">amaretom22@gmail.com</a></p>
        <p>© 2026 ERAS Africa – For healthcare professionals | Pilot version</p>
    </div>
""", unsafe_allow_html=True)