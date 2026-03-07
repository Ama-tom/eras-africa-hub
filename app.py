import streamlit as st
import os

# ────────────────────────────────────────────────
# Page config
# ────────────────────────────────────────────────
st.set_page_config(
    page_title="ERAS Africa – Enhanced Recovery After Surgery",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ────────────────────────────────────────────────
# African-inspired CSS with warm earth tones
# ────────────────────────────────────────────────
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Main background with African textile pattern inspiration */
    .stApp {
        background: linear-gradient(135deg, #faf3e0 0%, #fff4e6 50%, #f5e6d3 100%);
        background-image: 
            radial-gradient(circle at 10% 20%, rgba(205, 133, 63, 0.03) 0%, transparent 20%),
            radial-gradient(circle at 90% 70%, rgba(160, 82, 45, 0.03) 0%, transparent 25%),
            radial-gradient(circle at 30% 80%, rgba(210, 105, 30, 0.02) 0%, transparent 30%),
            radial-gradient(circle at 70% 30%, rgba(139, 69, 19, 0.02) 0%, transparent 35%);
        color: #2c1810;
    }
    
    /* Typography */
    h1, h2, h3, .main-title {
        font-family: 'DM Serif Display', serif;
        letter-spacing: -0.02em;
    }
    
    .main-title {
        color: #8B4513;
        font-size: 3.5rem;
        text-align: center;
        margin-bottom: 0.2rem;
        text-shadow: 2px 2px 4px rgba(139, 69, 19, 0.1);
    }
    
    .sub-title {
        font-family: 'Inter', sans-serif;
        color: #A0522D;
        font-size: 1.3rem;
        font-weight: 400;
        text-align: center;
        font-style: italic;
        margin-top: 0;
    }
    
    /* ===== SIMPLE, CLEAN NAVIGATION HEADER ===== */
    .nav-header {
        background: linear-gradient(135deg, #8B4513, #A0522D);
        padding: 5px 15px;
        border-radius: 40px;
        margin: 10px 0 20px 0;
        border: 1px solid #CD853F;
        box-shadow: 0 4px 8px rgba(139, 69, 19, 0.2);
    }
    
    .nav-container {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-wrap: wrap;
        gap: 5px;
    }
    
    .nav-item {
        color: #FFE4C4;
        font-family: 'Inter', sans-serif;
        font-weight: 500;
        font-size: 1rem;
        padding: 8px 16px;
        border-radius: 30px;
        transition: all 0.3s ease;
        text-decoration: none;
        background: transparent;
        border: none;
        cursor: pointer;
    }
    
    .nav-item:hover {
        background: #FFD700;
        color: #8B4513;
        transform: translateY(-2px);
    }
    
    .nav-item-home {
        background: #FFD700;
        color: #8B4513;
        font-weight: 600;
    }
    
    /* Mobile responsive */
    @media (max-width: 768px) {
        .nav-item {
            padding: 6px 10px;
            font-size: 0.9rem;
        }
    }
    
    /* African pattern divider */
    .african-divider {
        background: linear-gradient(90deg, transparent, #CD853F, #8B4513, #D2691E, #8B4513, #CD853F, transparent);
        height: 3px;
        width: 100%;
        margin: 25px 0;
        border-radius: 2px;
    }
    
    /* Cards */
    .card {
        background: rgba(255, 248, 235, 0.9);
        backdrop-filter: blur(5px);
        padding: 20px 15px;
        border-radius: 16px;
        box-shadow: 0 4px 12px rgba(139, 69, 19, 0.1);
        text-align: center;
        height: 100%;
        border: 1px solid rgba(205, 133, 63, 0.3);
        transition: all 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 16px rgba(139, 69, 19, 0.2);
        border-color: #CD853F;
    }
    
    /* Stats boxes */
    .stat-box {
        background: linear-gradient(135deg, #8B4513, #A0522D);
        padding: 20px 10px;
        border-radius: 12px;
        text-align: center;
        color: white;
        box-shadow: 0 4px 8px rgba(139, 69, 19, 0.2);
        border: 1px solid #CD853F;
    }
    
    .stat-number {
        font-family: 'DM Serif Display', serif;
        font-size: 2.5rem;
        font-weight: 700;
        color: #FFD700;
        line-height: 1;
    }
    
    .stat-label {
        font-family: 'Inter', sans-serif;
        font-size: 1rem;
        color: #FFF8E7;
    }
    
    /* Welcome box */
    .welcome-box {
        background: linear-gradient(135deg, #FFF8E7, #FFE4C4);
        padding: 25px;
        border-radius: 20px;
        margin: 20px 0;
        border-left: 5px solid #8B4513;
        border-right: 5px solid #CD853F;
        box-shadow: 0 4px 12px rgba(139, 69, 19, 0.1);
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #8B4513, #A0522D);
        color: white;
        font-family: 'Inter', sans-serif;
        font-weight: 500;
        font-size: 1rem;
        padding: 10px 20px;
        border-radius: 30px;
        border: 1px solid #CD853F;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #A0522D, #8B4513);
        border-color: #FFD700;
    }
    
    /* Sidebar styling */
    .css-1d391kg, .css-12oz5g7 {
        background: linear-gradient(180deg, #FFF8E7, #FFE4C4);
    }
    
    /* Footer */
    .footer {
        background: linear-gradient(135deg, #2c1810, #3e2a1f);
        padding: 30px 20px;
        border-radius: 30px 30px 0 0;
        text-align: center;
        color: #FFE4C4;
        margin-top: 40px;
        border-top: 4px solid #CD853F;
    }
    
    .footer h3 {
        color: #FFD700;
        font-size: 2rem;
        margin: 0 0 10px 0;
    }
    
    .footer a {
        color: #FFD700;
        text-decoration: none;
    }
    
    .footer a:hover {
        color: #CD853F;
    }
    </style>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────
# SIMPLE NAVIGATION HEADER (SINGLE VERSION)
# ────────────────────────────────────────────────
st.markdown("""
    <div class="nav-header">
        <div class="nav-container">
            <a href="/" target="_self" class="nav-item nav-item-home">🏠 HOME</a>
            <a href="/Calculator" target="_self" class="nav-item">🩺 CALCULATOR</a>
            <a href="/Guidelines" target="_self" class="nav-item">📘 GUIDELINES</a>
            <a href="/Resources" target="_self" class="nav-item">📚 RESOURCES</a>
            <a href="/About" target="_self" class="nav-item">ℹ️ ABOUT</a>
            <a href="/E-Course" target="_self" class="nav-item">🎓 E-COURSE</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────
# Header Section with Logo and Title
# ────────────────────────────────────────────────
col1, col2 = st.columns([1, 4])

with col1:
    # Try to load the existing logo
    if os.path.exists("icons/ERAS-192.jpg"):
        st.image("icons/ERAS-192.jpg", width=100)
    elif os.path.exists("ERAS-192.jpg"):
        st.image("ERAS-192.jpg", width=100)
    else:
        st.markdown("""
            <div style="background: linear-gradient(135deg, #8B4513, #CD853F); 
                        width: 100px; 
                        height: 100px; 
                        border-radius: 50%; 
                        display: flex; 
                        align-items: center; 
                        justify-content: center;
                        color: #FFD700;
                        font-size: 2.5rem;
                        border: 2px solid #FFD700;
                        margin: 5px;">
                🌍
            </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown('<p class="main-title">ERAS Africa</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Enhanced Recovery After Surgery – Empowering African Healthcare</p>', unsafe_allow_html=True)

# African pattern divider
st.markdown('<div class="african-divider"></div>', unsafe_allow_html=True)

# Welcome message
st.markdown("""
    <div class="welcome-box">
        <p style="font-size: 1.1rem; margin: 0;">
            Welcome to ERAS Africa – a collaborative initiative to advance evidence-based 
            perioperative care across the continent. We provide tools, training, guidelines, 
            and certified e-courses to reduce surgical complications and improve patient 
            recovery in African and low-resource settings.
        </p>
    </div>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────
# Stats Section
# ────────────────────────────────────────────────
stats_col1, stats_col2, stats_col3 = st.columns(3)

with stats_col1:
    st.markdown("""
        <div class="stat-box">
            <div class="stat-number">45+</div>
            <div class="stat-label">Partner Hospitals</div>
        </div>
    """, unsafe_allow_html=True)

with stats_col2:
    st.markdown("""
        <div class="stat-box">
            <div class="stat-number">12</div>
            <div class="stat-label">African Countries</div>
        </div>
    """, unsafe_allow_html=True)

with stats_col3:
    st.markdown("""
        <div class="stat-box">
            <div class="stat-number">500+</div>
            <div class="stat-label">Trained Professionals</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="african-divider"></div>', unsafe_allow_html=True)

# ────────────────────────────────────────────────
# Core Features Section
# ────────────────────────────────────────────────
st.markdown("<h2 style='text-align: center; color: #8B4513; margin-bottom: 20px;'>Core Tools & Resources</h2>", unsafe_allow_html=True)

# Create three columns for features
feat_col1, feat_col2, feat_col3 = st.columns(3)

with feat_col1:
    st.markdown("""
        <div class="card">
            <h1 style="font-size: 3rem; margin: 0;">🩺</h1>
            <h3 style="color: #8B4513;">Risk Calculator</h3>
            <p style="color: #5c3e2e; font-size: 0.95rem;">Predict prolonged stay and 30-day complications</p>
        </div>
    """, unsafe_allow_html=True)
    
    if os.path.exists("pages/1_Calculator.py"):
        if st.button("Launch Calculator", key="calc_btn"):
            st.switch_page("pages/1_Calculator.py")
    else:
        st.info("Coming soon")

with feat_col2:
    st.markdown("""
        <div class="card">
            <h1 style="font-size: 3rem; margin: 0;">📘</h1>
            <h3 style="color: #8B4513;">Guidelines</h3>
            <p style="color: #5c3e2e; font-size: 0.95rem;">ERAS protocols for African hospitals</p>
        </div>
    """, unsafe_allow_html=True)
    
    if os.path.exists("pages/2_Guidelines.py"):
        if st.button("View Guidelines", key="guide_btn"):
            st.switch_page("pages/2_Guidelines.py")
    else:
        st.info("Coming soon")

with feat_col3:
    st.markdown("""
        <div class="card">
            <h1 style="font-size: 3rem; margin: 0;">🎓</h1>
            <h3 style="color: #8B4513;">E-Course</h3>
            <p style="color: #5c3e2e; font-size: 0.95rem;">Certified training with CEUs</p>
        </div>
    """, unsafe_allow_html=True)
    
    if os.path.exists("pages/6_E-Course.py"):
        if st.button("Get Certified", key="course_btn"):
            st.switch_page("pages/6_E-Course.py")
    else:
        st.info("Coming soon")

st.markdown('<div class="african-divider"></div>', unsafe_allow_html=True)

# ────────────────────────────────────────────────
# Sidebar with African Regions (SIMPLIFIED)
# ────────────────────────────────────────────────
st.sidebar.markdown("### 🌍 African Regions")

# Simplified region data
regions = {
    "East Africa": ["Ethiopia", "Kenya", "Tanzania", "Uganda", "Rwanda"],
    "Southern Africa": ["South Africa", "Botswana", "Namibia", "Zimbabwe", "Zambia"],
    "West Africa": ["Nigeria", "Ghana", "Senegal", "Côte d'Ivoire"],
    "Central Africa": ["Cameroon", "DR Congo", "Gabon"],
    "North Africa": ["Morocco", "Egypt", "Tunisia", "Algeria"]
}

# Simple country selector
all_countries = []
for country_list in regions.values():
    all_countries.extend(country_list)

selected_country = st.sidebar.selectbox(
    "Select your country",
    ["None"] + sorted(all_countries)
)

if selected_country != "None":
    st.sidebar.success(f"Welcome, {selected_country}! 👋")

# Simple expanders
for region, countries in regions.items():
    with st.sidebar.expander(region):
        for country in countries:
            st.markdown(f"- {country}")

# Simple contact
st.sidebar.markdown("---")
st.sidebar.markdown("📧 **Contact:** amaretom22@gmail.com")
st.sidebar.markdown("📍 **Addis Ababa, Ethiopia**")

# ────────────────────────────────────────────────
# Simple Call to Action
# ────────────────────────────────────────────────
st.markdown("""
    <div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #FFF8E7, #FFE4C4); border-radius: 15px; margin: 20px 0;">
        <h3 style="color: #8B4513;">Ready to Transform Surgical Care?</h3>
        <p style="color: #5c3e2e;">Join healthcare professionals across Africa</p>
    </div>
""", unsafe_allow_html=True)

if os.path.exists("pages/6_E-Course.py"):
    if st.button("🌟 START E-COURSE NOW", use_container_width=True):
        st.switch_page("pages/6_E-Course.py")

# ────────────────────────────────────────────────
# Simplified Footer
# ────────────────────────────────────────────────
st.markdown("""
    <div class="footer">
        <h3>ERAS Africa</h3>
        <p style="margin: 5px 0;">Advancing perioperative excellence across Africa</p>
        <p style="margin: 15px 0 5px 0;">📧 <a href="mailto:amaretom22@gmail.com">amaretom22@gmail.com</a></p>
        <p style="margin: 5px 0;">© 2026 ERAS Africa</p>
    </div>
""", unsafe_allow_html=True)