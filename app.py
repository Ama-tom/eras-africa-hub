import streamlit as st

# ────────────────────────────────────────────────
# Page config + light, high-contrast African-inspired CSS
# ────────────────────────────────────────────────
st.set_page_config(
    page_title="ERAS Africa – Enhanced Recovery After Surgery",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body, [class*="stApp"] {
        font-family: 'Inter', sans-serif;
        background: linear-gradient(135deg, #e6fffa 0%, #fefce8 50%, #fff7ed 100%);
        color: #1e293b;
    }

    h1 {
        color: #1e40af;
        font-weight: 800;
        font-size: 3.2rem;
        text-align: center;
        margin-bottom: 0.4rem;
    }

    h2 {
        color: #b45309;
        font-weight: 700;
    }

    .horizontal-card {
        background: white;
        border-radius: 16px;
        padding: 28px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 10px rgba(0,0,0,0.06);
        text-align: center;
        transition: all 0.3s ease;
    }

    .horizontal-card:hover {
        border-color: #fbbf24;
        box-shadow: 0 10px 20px rgba(251,191,36,0.15);
        transform: translateY(-6px);
    }

    .region-accordion {
        background: #f8fafc;
        border-radius: 12px;
        padding: 16px;
        border: 1px solid #e2e8f0;
        margin-bottom: 16px;
    }

    .stButton > button {
        background: #1e40af;
        color: white;
        border-radius: 10px;
        padding: 14px 32px;
        font-weight: 600;
        transition: all 0.3s;
        border: none;
    }

    .stButton > button:hover {
        background: #1e3a8a;
        transform: translateY(-2px);
    }

    .footer {
        margin-top: 80px;
        padding: 40px;
        background: #1e293b;
        color: white;
        text-align: center;
        border-radius: 16px 16px 0 0;
    }
    </style>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────
# Main Content – Light & High Contrast
# ────────────────────────────────────────────────
st.title("ERAS Africa")
st.markdown("**Enhanced Recovery After Surgery – Empowering African Healthcare**")

st.markdown("""
### Welcome to ERAS Africa
We are dedicated to improving surgical outcomes across the continent through evidence-based perioperative care, training, tools and collaboration.
""")

st.markdown("---")

# ────────────────────────────────────────────────
# Horizontal Cards: Calculator – Guidelines – E-Course
# ────────────────────────────────────────────────
st.subheader("ERAS Africa Core Tools & Resources")

cols = st.columns(3)

with cols[0]:
    st.markdown('<div class="horizontal-card">', unsafe_allow_html=True)
    st.markdown("### 🩺 Risk Calculator")
    st.markdown("Predict prolonged stay and 30-day complications")
    st.page_link("pages/1_Calculator.py", label="Launch Calculator", icon="🩺")
    st.markdown('</div>', unsafe_allow_html=True)

with cols[1]:
    st.markdown('<div class="horizontal-card">', unsafe_allow_html=True)
    st.markdown("### 📘 Guidelines")
    st.markdown("Adapted ERAS protocols for African settings")
    st.page_link("pages/2_Guidelines.py", label="View Guidelines", icon="📘")
    st.markdown('</div>', unsafe_allow_html=True)

with cols[2]:
    st.markdown('<div class="horizontal-card">', unsafe_allow_html=True)
    st.markdown("### 🎓 E-Course & Certification")
    st.markdown("Earn up to 60 CEUs – certified training")
    st.page_link("pages/6_E-Course.py", label="Get Certified → Start Now", icon="🎓")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# ────────────────────────────────────────────────
# Right-side African Regions Accordion (vertical, expandable)
# ────────────────────────────────────────────────
st.sidebar.title("African Regions")

with st.sidebar.expander("East Africa"):
    st.markdown("""
    - Ethiopia
    - Kenya
    - Tanzania
    - Uganda
    - Rwanda
    - Burundi
    - South Sudan
    """)

with st.sidebar.expander("Southern Africa"):
    st.markdown("""
    - South Africa
    - Botswana
    - Namibia
    - Zimbabwe
    - Zambia
    - Malawi
    - Mozambique
    - Eswatini
    - Lesotho
    """)

with st.sidebar.expander("West Africa"):
    st.markdown("""
    - Nigeria
    - Senegal
    - Ghana
    - Côte d'Ivoire
    - Mali
    - Burkina Faso
    - Niger
    - Guinea
    - Sierra Leone
    """)

with st.sidebar.expander("Central Africa"):
    st.markdown("""
    - Chad
    - Cameroon
    - Central African Republic
    - Democratic Republic of the Congo
    - Republic of the Congo
    - Gabon
    - Equatorial Guinea
    """)

with st.sidebar.expander("North Africa"):
    st.markdown("""
    - Morocco
    - Tunisia
    - Algeria
    - Egypt
    - Libya
    - Sudan
    """)

# ────────────────────────────────────────────────
# Footer
# ────────────────────────────────────────────────
st.markdown("""
    <div class="footer">
        <h3>ERAS Africa</h3>
        <p>Empowering surgical excellence across the continent</p>
        <p>Email: amaretom22@gmail.com</p>
        <p>© 2026 ERAS Africa – For healthcare professionals</p>
    </div>
""", unsafe_allow_html=True)