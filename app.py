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
        color: #8B4513;  /* Saddle Brown */
        font-size: 4rem;
        text-align: center;
        margin-bottom: 0.2rem;
        text-shadow: 2px 2px 4px rgba(139, 69, 19, 0.1);
        border-bottom: 3px solid #CD853F;  /* Peru brown */
        display: inline-block;
        padding-bottom: 10px;
    }
    
    .sub-title {
        font-family: 'Inter', sans-serif;
        color: #A0522D;  /* Sienna */
        font-size: 1.4rem;
        font-weight: 400;
        text-align: center;
        letter-spacing: 0.5px;
        margin-top: 0.5rem;
        font-style: italic;
    }
    
    /* African pattern divider */
    .african-divider {
        background: linear-gradient(90deg, 
            transparent, 
            #CD853F, 
            #8B4513, 
            #D2691E, 
            #8B4513, 
            #CD853F, 
            transparent);
        height: 4px;
        width: 100%;
        margin: 30px 0;
        border-radius: 2px;
    }
    
    /* Cards with warm African tones */
    .card {
        background: rgba(255, 248, 235, 0.9);
        backdrop-filter: blur(5px);
        padding: 25px 20px;
        border-radius: 16px;
        box-shadow: 0 8px 20px rgba(139, 69, 19, 0.15);
        text-align: center;
        height: 100%;
        border: 1px solid rgba(205, 133, 63, 0.3);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .card::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 5px;
        background: linear-gradient(90deg, #CD853F, #8B4513, #CD853F);
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(139, 69, 19, 0.25);
        border-color: #CD853F;
        background: rgba(255, 248, 235, 1);
    }
    
    /* Stats boxes with Kente cloth inspired colors */
    .stat-box {
        background: linear-gradient(135deg, #8B4513, #A0522D);
        padding: 25px 15px;
        border-radius: 12px;
        text-align: center;
        color: white;
        box-shadow: 0 8px 16px rgba(139, 69, 19, 0.3);
        border: 2px solid #CD853F;
    }
    
    .stat-number {
        font-family: 'DM Serif Display', serif;
        font-size: 3rem;
        font-weight: 700;
        color: #FFD700;  /* Gold */
        line-height: 1;
        margin-bottom: 5px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    .stat-label {
        font-family: 'Inter', sans-serif;
        font-size: 1.1rem;
        font-weight: 500;
        color: #FFF8E7;
        letter-spacing: 0.5px;
    }
    
    /* Welcome message with warm background */
    .welcome-box {
        background: linear-gradient(135deg, #FFF8E7, #FFE4C4);
        padding: 30px;
        border-radius: 20px;
        margin: 30px 0;
        border-left: 8px solid #8B4513;
        border-right: 8px solid #CD853F;
        box-shadow: 0 10px 25px rgba(139, 69, 19, 0.15);
        font-family: 'Inter', sans-serif;
        font-size: 1.2rem;
        line-height: 1.6;
        color: #2c1810;
    }
    
    /* Feature icons with African colors */
    .feature-icon {
        font-size: 4rem;
        background: linear-gradient(135deg, #8B4513, #D2691E);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 15px;
    }
    
    /* Buttons with African mud cloth pattern inspiration */
    .stButton > button {
        background: linear-gradient(135deg, #8B4513, #A0522D);
        color: white;
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        font-size: 1.1rem;
        padding: 12px 30px;
        border-radius: 40px;
        border: 2px solid #CD853F;
        transition: all 0.3s ease;
        width: 100%;
        margin-top: 15px;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 4px 10px rgba(139, 69, 19, 0.3);
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #A0522D, #8B4513);
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(139, 69, 19, 0.4);
        border-color: #FFD700;
    }
    
    /* Sidebar styling */
    .css-1d391kg, .css-12oz5g7 {
        background: linear-gradient(180deg, #FFF8E7, #FFE4C4);
    }
    
    .sidebar-content {
        background: rgba(255, 248, 235, 0.95);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #CD853F;
    }
    
    /* Region expanders */
    .streamlit-expanderHeader {
        background: linear-gradient(90deg, #FFF8E7, #FFE4C4);
        color: #8B4513;
        font-family: 'DM Serif Display', serif;
        font-size: 1.2rem;
        font-weight: 600;
        border-radius: 8px;
        border: 1px solid #CD853F;
    }
    
    /* Footer with African textile pattern */
    .footer {
        background: linear-gradient(135deg, #2c1810, #3e2a1f);
        padding: 40px 30px;
        border-radius: 30px 30px 0 0;
        text-align: center;
        color: #FFE4C4;
        margin-top: 60px;
        border-top: 8px solid #CD853F;
        position: relative;
    }
    
    .footer::before {
        content: "⦿ ⦿ ⦿";
        position: absolute;
        top: -25px;
        left: 50%;
        transform: translateX(-50%);
        background: #CD853F;
        color: #2c1810;
        padding: 5px 30px;
        border-radius: 30px;
        font-size: 1.2rem;
        letter-spacing: 10px;
    }
    
    .footer h3 {
        font-family: 'DM Serif Display', serif;
        color: #FFD700;
        font-size: 2.2rem;
        margin-bottom: 15px;
    }
    
    .footer a {
        color: #FFD700;
        text-decoration: none;
        font-weight: 500;
        transition: color 0.3s;
    }
    
    .footer a:hover {
        color: #CD853F;
        text-decoration: underline;
    }
    
    /* Custom badges */
    .badge {
        background: linear-gradient(135deg, #8B4513, #A0522D);
        color: #FFD700;
        padding: 5px 15px;
        border-radius: 25px;
        font-size: 0.9rem;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 15px;
        border: 1px solid #CD853F;
        letter-spacing: 1px;
    }
    
    /* Success message styling */
    .stAlert {
        background: linear-gradient(135deg, #FFE4C4, #FFF8E7);
        border-left-color: #8B4513;
        color: #2c1810;
    }
    
    /* Select box styling */
    .stSelectbox label {
        color: #8B4513;
        font-weight: 600;
        font-family: 'Inter', sans-serif;
    }
    
    .stSelectbox div[data-baseweb="select"] {
        background: #FFF8E7;
        border-color: #CD853F;
    }
    
    /* Divider styling */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #CD853F, #8B4513, #CD853F, transparent);
        margin: 40px 0;
    }
    </style>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────
# Header Section with African-inspired design
# ────────────────────────────────────────────────

# Create two columns for logo and title
col1, col2 = st.columns([1, 4])

with col1:
    # Try to load the existing logo
    if os.path.exists("icons/ERAS-192.jpg"):
        st.image("icons/ERAS-192.jpg", width=120)
    elif os.path.exists("ERAS-192.jpg"):
        st.image("ERAS-192.jpg", width=120)
    else:
        st.markdown("""
            <div style="background: linear-gradient(135deg, #8B4513, #CD853F); 
                        width: 120px; 
                        height: 120px; 
                        border-radius: 50%; 
                        display: flex; 
                        align-items: center; 
                        justify-content: center;
                        color: #FFD700;
                        font-size: 3rem;
                        font-weight: bold;
                        border: 3px solid #FFD700;
                        box-shadow: 0 8px 16px rgba(139,69,19,0.3);
                        margin: 10px;">
                🌍
            </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown('<p class="main-title">ERAS Africa</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Enhanced Recovery After Surgery – Empowering African Healthcare</p>', unsafe_allow_html=True)

# African pattern divider
st.markdown('<div class="african-divider"></div>', unsafe_allow_html=True)

# Welcome message with African-inspired design
st.markdown("""
    <div class="welcome-box">
        <span class="badge">🌍 Welcome to ERAS Africa</span>
        <p style="font-size: 1.2rem; margin-top: 15px;">
            a collaborative initiative to advance evidence-based perioperative care across the continent. 
            We provide tools, training, guidelines, and certified e-courses to reduce surgical complications 
            and improve patient recovery in African and low-resource settings.
        </p>
    </div>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────
# Stats Section with African colors
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
st.markdown("<h2 style='text-align: center; color: #8B4513; font-size: 2.5rem;'>Core Tools & Resources</h2>", unsafe_allow_html=True)

# Create three columns for features
feat_col1, feat_col2, feat_col3 = st.columns(3)

with feat_col1:
    st.markdown("""
        <div class="card">
            <div class="feature-icon">🩺</div>
            <h3 style="color: #8B4513; font-family: 'DM Serif Display', serif;">Risk Calculator</h3>
            <p style="color: #5c3e2e; font-family: 'Inter', sans-serif;">Predict prolonged stay and 30-day complications using validated tools adapted for African populations</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Check if page exists before creating link
    if os.path.exists("pages/1_Calculator.py"):
        st.page_link("pages/1_Calculator.py", label="Launch Calculator", icon="🩺")
    else:
        st.info("📋 Calculator coming soon")

with feat_col2:
    st.markdown("""
        <div class="card">
            <div class="feature-icon">📘</div>
            <h3 style="color: #8B4513; font-family: 'DM Serif Display', serif;">Guidelines</h3>
            <p style="color: #5c3e2e; font-family: 'Inter', sans-serif;">Evidence-based ERAS protocols specifically adapted for resource-variable African healthcare settings</p>
        </div>
    """, unsafe_allow_html=True)
    
    if os.path.exists("pages/2_Guidelines.py"):
        st.page_link("pages/2_Guidelines.py", label="View Guidelines", icon="📘")
    else:
        st.info("📚 Guidelines coming soon")

with feat_col3:
    st.markdown("""
        <div class="card">
            <div class="feature-icon">🎓</div>
            <h3 style="color: #8B4513; font-family: 'DM Serif Display', serif;">E-Course & Certification</h3>
            <p style="color: #5c3e2e; font-family: 'Inter', sans-serif;">Comprehensive training program with up to 60 CEUs – certified perioperative education</p>
        </div>
    """, unsafe_allow_html=True)
    
    if os.path.exists("pages/6_E-Course.py"):
        st.page_link("pages/6_E-Course.py", label="Get Certified", icon="🎓")
    else:
        st.info("🌟 E-Course coming soon")

st.markdown('<div class="african-divider"></div>', unsafe_allow_html=True)

# ────────────────────────────────────────────────
# Additional Resources
# ────────────────────────────────────────────────
res_col1, res_col2 = st.columns(2)

with res_col1:
    st.markdown("""
        <div class="card">
            <div class="feature-icon">📚</div>
            <h3 style="color: #8B4513; font-family: 'DM Serif Display', serif;">Resources</h3>
            <p style="color: #5c3e2e;">Educational materials, videos, and implementation toolkits for ERAS protocols</p>
        </div>
    """, unsafe_allow_html=True)
    
    if os.path.exists("pages/4_Resources.py"):
        st.page_link("pages/4_Resources.py", label="Browse Resources →")

with res_col2:
    st.markdown("""
        <div class="card">
            <div class="feature-icon">ℹ️</div>
            <h3 style="color: #8B4513; font-family: 'DM Serif Display', serif;">About Us</h3>
            <p style="color: #5c3e2e;">Learn about our mission, team, partners, and impact across the continent</p>
        </div>
    """, unsafe_allow_html=True)
    
    if os.path.exists("pages/5_About.py"):
        st.page_link("pages/5_About.py", label="Learn More →")

st.markdown('<div class="african-divider"></div>', unsafe_allow_html=True)

# ────────────────────────────────────────────────
# Sidebar with African Regions
# ────────────────────────────────────────────────
st.sidebar.markdown("""
    <h2 style="color: #8B4513; font-family: 'DM Serif Display', serif; text-align: center; border-bottom: 3px solid #CD853F; padding-bottom: 10px;">
        🌍 African Regions
    </h2>
""", unsafe_allow_html=True)

# Region data
regions = {
    "East Africa": ["Ethiopia", "Kenya", "Tanzania", "Uganda", "Rwanda", "Burundi", "South Sudan"],
    "Southern Africa": ["South Africa", "Botswana", "Namibia", "Zimbabwe", "Zambia", "Malawi", "Mozambique", "Eswatini", "Lesotho"],
    "West Africa": ["Nigeria", "Senegal", "Ghana", "Côte d'Ivoire", "Mali", "Burkina Faso", "Niger", "Guinea", "Sierra Leone"],
    "Central Africa": ["Chad", "Cameroon", "Central African Republic", "DR Congo", "Republic of Congo", "Gabon", "Equatorial Guinea"],
    "North Africa": ["Morocco", "Tunisia", "Algeria", "Egypt", "Libya", "Sudan"]
}

# Country selector with African styling
st.sidebar.markdown('<p style="color: #8B4513; font-weight: 600; margin-top: 20px;">📍 Select your country</p>', unsafe_allow_html=True)

all_countries = []
for country_list in regions.values():
    all_countries.extend(country_list)

selected_country = st.sidebar.selectbox(
    "",
    ["None selected"] + sorted(all_countries),
    label_visibility="collapsed"
)

if selected_country != "None selected":
    st.sidebar.markdown(f"""
        <div style="background: linear-gradient(135deg, #FFE4C4, #FFF8E7); 
                    padding: 10px; 
                    border-radius: 10px; 
                    border-left: 5px solid #8B4513;
                    margin: 10px 0;">
            <span style="color: #8B4513; font-weight: 600;">👋 Welcome!</span><br>
            <span style="color: #5c3e2e;">Colleague from {selected_country}</span>
        </div>
    """, unsafe_allow_html=True)

# Region expanders with African styling
for region, countries in regions.items():
    with st.sidebar.expander(f"📌 {region} ({len(countries)})"):
        for country in countries:
            if country == selected_country:
                st.markdown(f"<span style='color: #8B4513; font-weight: 600;'>🌟 {country}</span>", unsafe_allow_html=True)
            else:
                st.markdown(f"<span style='color: #5c3e2e;'>• {country}</span>", unsafe_allow_html=True)

# Sidebar contact with African motif
st.sidebar.markdown("""
    <div style="background: linear-gradient(135deg, #8B4513, #A0522D); 
                padding: 20px; 
                border-radius: 15px; 
                margin-top: 30px;
                border: 2px solid #CD853F;">
        <h4 style="color: #FFD700; font-family: 'DM Serif Display', serif; margin-top: 0;">📬 Contact Us</h4>
        <p style="color: #FFE4C4; margin: 5px 0;">📧 amaretom22@gmail.com</p>
        <p style="color: #FFE4C4; margin: 5px 0;">📱 +251 XXX XXX XXX</p>
        <div style="border-top: 2px solid #CD853F; margin: 10px 0;"></div>
        <p style="color: #FFD700; font-style: italic; margin: 0;">"Advancing perioperative care across Africa"</p>
    </div>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────
# Call to Action with African pattern
# ────────────────────────────────────────────────
cta_col1, cta_col2, cta_col3 = st.columns([1, 2, 1])

with cta_col2:
    st.markdown("""
        <div style="text-align: center; padding: 30px; background: linear-gradient(135deg, #FFF8E7, #FFE4C4); border-radius: 20px; border: 2px solid #CD853F;">
            <h2 style="color: #8B4513; font-family: 'DM Serif Display', serif; font-size: 2rem;">Ready to Transform Surgical Care?</h2>
            <p style="color: #5c3e2e; font-size: 1.2rem; margin: 20px 0;">Join hundreds of healthcare professionals across Africa</p>
            <div style="background: linear-gradient(90deg, transparent, #CD853F, #8B4513, #CD853F, transparent); height: 2px; width: 80%; margin: 20px auto;"></div>
        </div>
    """, unsafe_allow_html=True)
    
    if os.path.exists("pages/6_E-Course.py"):
        if st.button("🌟 GET CERTIFIED – START E-COURSE NOW", use_container_width=True):
            st.switch_page("pages/6_E-Course.py")
    else:
        st.info("🎓 E-Course launching soon! Check back later.")

# ────────────────────────────────────────────────
# Footer with African textile pattern
# ────────────────────────────────────────────────
st.markdown("""
    <div class="footer">
        <h3>ERAS Africa</h3>
        <p style="font-size: 1.2rem; margin: 20px 0; font-style: italic;">Advancing perioperative excellence across the continent</p>
        
        <div style="display: flex; justify-content: center; gap: 50px; margin: 30px 0; flex-wrap: wrap;">
            <div>
                <h4 style="color: #CD853F; font-family: 'DM Serif Display', serif;">Contact</h4>
                <p>📧 <a href="mailto:amaretom22@gmail.com">amaretom22@gmail.com</a></p>
                <p>📱 +251 XXX XXX XXX</p>
            </div>
            <div>
                <h4 style="color: #CD853F; font-family: 'DM Serif Display', serif;">Follow Us</h4>
                <p>🐦 Twitter</p>
                <p>💼 LinkedIn</p>
            </div>
            <div>
                <h4 style="color: #CD853F; font-family: 'DM Serif Display', serif;">Partners</h4>
                <p>🏥 WHO Africa</p>
                <p>🎓 Universities</p>
            </div>
        </div>
        
        <div style="background: rgba(205, 133, 63, 0.2); padding: 15px; border-radius: 10px; margin: 20px 0;">
            <p style="color: #FFE4C4; font-size: 1rem; letter-spacing: 2px;">⦿ ⦿ ⦿ ⦿ ⦿</p>
        </div>
        
        <p style="color: #CD853F;">© 2026 ERAS Africa – For healthcare professionals | Pilot version v1.0</p>
        <p style="color: #FFE4C4; font-size: 0.9rem; margin-top: 20px;">
            📍 Addis Ababa, Ethiopia | 🌍 Serving all 54 African nations
        </p>
    </div>
""", unsafe_allow_html=True)