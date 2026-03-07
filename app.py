import streamlit as st

# ────────────────────────────────────────────────
# SEO & meta tags (helps Google indexing)
# ────────────────────────────────────────────────
st.markdown("""
    <meta name="description" content="ERAS Africa – Enhanced Recovery After Surgery hub for African hospitals. Risk calculator, guidelines, training, e-courses and CEUs.">
    <meta name="keywords" content="ERAS Africa, Enhanced Recovery After Surgery, perioperative care, surgical recovery, CEU training, African hospitals">
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────
# Page config + vibrant, light African-inspired CSS
# ────────────────────────────────────────────────
st.set_page_config(
    page_title="ERAS Africa – Enhanced Recovery After Surgery",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@700&display=swap');

    html, body, [class*="stApp"] {
        font-family: 'Inter', sans-serif;
        background: linear-gradient(135deg, #e6fffa 0%, #fefce8 50%, #fff7ed 100%);
        color: #1e293b;
    }

    h1 {
        font-family: 'Playfair Display', serif;
        color: #1e40af;
        font-size: 3.5rem;
        text-align: center;
        text-shadow: 1px 1px 4px rgba(30,64,175,0.2);
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
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        text-align: center;
        transition: all 0.3s ease;
    }

    .horizontal-card:hover {
        border-color: #fbbf24;
        box-shadow: 0 10px 20px rgba(251,191,36,0.2);
        transform: translateY(-6px);
    }

    .stButton > button {
        background: #1e40af;
        color: white;
        border-radius: 12px;
        padding: 16px 40px;
        font-size: 1.25rem;
        font-weight: 600;
        transition: all 0.3s;
        border: none;
    }

    .stButton > button:hover {
        background: #1e3a8a;
        transform: translateY(-3px);
        box-shadow: 0 8px 16px rgba(30,64,175,0.3);
    }

    .footer {
        margin-top: 80px;
        padding: 50px 0;
        background: #1e293b;
        color: #e0f2fe;
        text-align: center;
        border-radius: 16px 16px 0 0;
    }

    .footer a {
        color: #fbbf24;
        text-decoration: none;
    }

    .footer a:hover {
        color: #fefce8;
    }
    </style>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────
# Hero Section with picture
# ────────────────────────────────────────────────
st.image(
    "https://raw.githubusercontent.com/Ama-tom/eras-africa-hub/main/icons/ERAS IMPLEMENTATION.png",
    use_column_width=True
)
st.title("ERAS Africa")
st.markdown("**Enhanced Recovery After Surgery – Empowering African Healthcare**")

st.markdown("""
Welcome to ERAS Africa – a collaborative initiative to advance evidence-based perioperative care across the continent.  
We provide tools, training, guidelines, and certified e-courses to reduce surgical complications and improve patient recovery in African and low-resource settings.
""")

st.markdown("---")

# ────────────────────────────────────────────────
# Horizontal Cards: Calculator – Guidelines – E-Course
# ────────────────────────────────────────────────
st.subheader("ERAS Africa Core Tools & Resources")

cols = st.columns(3)

with cols[0]:
    st.image("icons/photo_2026-03-08-01-38-12.jpg", use_column_width=True)
    st.markdown('<div class="horizontal-card">', unsafe_allow_html=True)
    st.markdown("### 🩺 Risk Calculator")
    st.markdown("Predict prolonged stay and 30-day complications")
    st.page_link("pages/1_Calculator.py", label="Launch Calculator", icon="🩺")
    st.markdown('</div>', unsafe_allow_html=True)

with cols[1]:
    st.image("icons/photo-2020-04-20-02-35.jpg", use_column_width=True)
    st.markdown('<div class="horizontal-card">', unsafe_allow_html=True)
    st.markdown("### 📘 Guidelines")
    st.markdown("Adapted ERAS protocols for African hospitals")
    st.page_link("pages/2_Guidelines.py", label="View Guidelines", icon="📘")
    st.markdown('</div>', unsafe_allow_html=True)

with cols[2]:
    st.image("icons/photo_2026-03-08-01-38-35.jpg", use_column_width=True)
    st.markdown('<div class="horizontal-card">', unsafe_allow_html=True)
    st.markdown("### 🎓 E-Course & Certification")
    st.markdown("Earn up to 60 CEUs – certified training")
    st.page_link("pages/6_E-Course.py", label="Get Certified → Start Now", icon="🎓")
    st.markdown('</div>', unsafe_allow_html=True)

# ────────────────────────────────────────────────
# Call-to-Action Button
# ────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
    <div style="text-align: center; padding: 60px 20px;">
        <h2 style="color: #b45309;">Ready to Transform Surgical Care?</h2>
        <a href="/E-Course" target="_self">
            <button style="font-size: 1.4rem; padding: 18px 60px;">
                Get Certified – Start E-Course Now →
            </button>
        </a>
    </div>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────
# African Regions Accordion (right sidebar)
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
        <p>Advancing perioperative excellence across the continent</p>
        <p>Email: <a href="mailto:amaretom22@gmail.com">amaretom22@gmail.com</a></p>
        <p>© 2026 ERAS Africa – For healthcare professionals | Pilot version</p>
    </div>
""", unsafe_allow_html=True)