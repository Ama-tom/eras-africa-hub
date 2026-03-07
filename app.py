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
# Simple CSS
# ────────────────────────────────────────────────
st.markdown("""
    <style>
    .main-title {
        color: #1e40af;
        font-size: 3.5rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 0;
    }
    .sub-title {
        color: #b45309;
        font-size: 1.3rem;
        text-align: center;
        margin-top: 0;
    }
    .card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        text-align: center;
        height: 100%;
    }
    .footer {
        background: #1e293b;
        color: white;
        padding: 30px;
        border-radius: 10px;
        text-align: center;
        margin-top: 50px;
    }
    </style>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────
# Header Section
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
            <div style="background: linear-gradient(135deg, #1e40af, #b45309); 
                        width: 100px; 
                        height: 100px; 
                        border-radius: 50%; 
                        display: flex; 
                        align-items: center; 
                        justify-content: center;
                        color: white;
                        font-size: 2rem;
                        margin: 10px;">
                EA
            </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown('<p class="main-title">ERAS Africa</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Enhanced Recovery After Surgery – Empowering African Healthcare</p>', unsafe_allow_html=True)

# Welcome message
st.markdown("""
    <div style="background: #f0f9ff; padding: 20px; border-radius: 10px; margin: 20px 0;">
        <p style="font-size: 1.2rem; margin: 0;">
            Welcome to ERAS Africa – a collaborative initiative to advance evidence-based 
            perioperative care across the continent. We provide tools, training, guidelines, 
            and certified e-courses to reduce surgical complications and improve patient 
            recovery in African and low-resource settings.
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# ────────────────────────────────────────────────
# Stats Section
# ────────────────────────────────────────────────
stats_col1, stats_col2, stats_col3 = st.columns(3)

with stats_col1:
    st.markdown("""
        <div class="card">
            <h2 style="color: #1e40af; font-size: 2.5rem; margin: 0;">45+</h2>
            <p>Partner Hospitals</p>
        </div>
    """, unsafe_allow_html=True)

with stats_col2:
    st.markdown("""
        <div class="card">
            <h2 style="color: #1e40af; font-size: 2.5rem; margin: 0;">12</h2>
            <p>African Countries</p>
        </div>
    """, unsafe_allow_html=True)

with stats_col3:
    st.markdown("""
        <div class="card">
            <h2 style="color: #1e40af; font-size: 2.5rem; margin: 0;">500+</h2>
            <p>Trained Professionals</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ────────────────────────────────────────────────
# Core Features Section
# ────────────────────────────────────────────────
st.markdown("<h2 style='text-align: center;'>Core Tools & Resources</h2>", unsafe_allow_html=True)

# Create three columns for features
feat_col1, feat_col2, feat_col3 = st.columns(3)

with feat_col1:
    st.markdown("""
        <div class="card">
            <h1 style="font-size: 3rem;">🩺</h1>
            <h3>Risk Calculator</h3>
            <p>Predict prolonged stay and 30-day complications</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Check if page exists before creating link
    if os.path.exists("pages/1_Calculator.py"):
        st.page_link("pages/1_Calculator.py", label="Launch Calculator", icon="🩺")
    else:
        st.info("Calculator coming soon")

with feat_col2:
    st.markdown("""
        <div class="card">
            <h1 style="font-size: 3rem;">📘</h1>
            <h3>Guidelines</h3>
            <p>Adapted ERAS protocols for African hospitals</p>
        </div>
    """, unsafe_allow_html=True)
    
    if os.path.exists("pages/2_Guidelines.py"):
        st.page_link("pages/2_Guidelines.py", label="View Guidelines", icon="📘")
    else:
        st.info("Guidelines coming soon")

with feat_col3:
    st.markdown("""
        <div class="card">
            <h1 style="font-size: 3rem;">🎓</h1>
            <h3>E-Course & Certification</h3>
            <p>Earn up to 60 CEUs – certified training</p>
        </div>
    """, unsafe_allow_html=True)
    
    if os.path.exists("pages/6_E-Course.py"):
        st.page_link("pages/6_E-Course.py", label="Get Certified", icon="🎓")
    else:
        st.info("E-Course coming soon")

st.markdown("---")

# ────────────────────────────────────────────────
# Additional Resources
# ────────────────────────────────────────────────
res_col1, res_col2 = st.columns(2)

with res_col1:
    st.markdown("""
        <div class="card">
            <h3>📚 Resources</h3>
            <p>Educational materials, videos, and implementation toolkits</p>
        </div>
    """, unsafe_allow_html=True)
    
    if os.path.exists("pages/4_Resources.py"):
        st.page_link("pages/4_Resources.py", label="Browse Resources →")

with res_col2:
    st.markdown("""
        <div class="card">
            <h3>ℹ️ About Us</h3>
            <p>Learn about our mission, team, and impact across Africa</p>
        </div>
    """, unsafe_allow_html=True)
    
    if os.path.exists("pages/5_About.py"):
        st.page_link("pages/5_About.py", label="Learn More →")

st.markdown("---")

# ────────────────────────────────────────────────
# Sidebar with African Regions
# ────────────────────────────────────────────────
st.sidebar.title("🌍 African Regions")

# Region data
regions = {
    "East Africa": ["Ethiopia", "Kenya", "Tanzania", "Uganda", "Rwanda", "Burundi", "South Sudan"],
    "Southern Africa": ["South Africa", "Botswana", "Namibia", "Zimbabwe", "Zambia", "Malawi", "Mozambique", "Eswatini", "Lesotho"],
    "West Africa": ["Nigeria", "Senegal", "Ghana", "Côte d'Ivoire", "Mali", "Burkina Faso", "Niger", "Guinea", "Sierra Leone"],
    "Central Africa": ["Chad", "Cameroon", "Central African Republic", "DR Congo", "Republic of Congo", "Gabon", "Equatorial Guinea"],
    "North Africa": ["Morocco", "Tunisia", "Algeria", "Egypt", "Libya", "Sudan"]
}

# Country selector
all_countries = []
for country_list in regions.values():
    all_countries.extend(country_list)

selected_country = st.sidebar.selectbox(
    "Select your country",
    ["None selected"] + sorted(all_countries)
)

if selected_country != "None selected":
    st.sidebar.success(f"Welcome, colleague from {selected_country}! 👋")

# Region expanders
for region, countries in regions.items():
    with st.sidebar.expander(f"📌 {region} ({len(countries)})"):
        for country in countries:
            if country == selected_country:
                st.markdown(f"**✓ {country}** 🌟")
            else:
                st.markdown(f"• {country}")

# Sidebar contact
st.sidebar.markdown("---")
st.sidebar.markdown("### 📬 Contact")
st.sidebar.markdown("Email: amaretom22@gmail.com")

# ────────────────────────────────────────────────
# Call to Action
# ────────────────────────────────────────────────
cta_col1, cta_col2, cta_col3 = st.columns([1, 2, 1])

with cta_col2:
    st.markdown("""
        <div style="text-align: center; padding: 20px;">
            <h2 style="color: #b45309;">Ready to Transform Surgical Care?</h2>
            <p style="font-size: 1.2rem;">Join hundreds of healthcare professionals across Africa</p>
        </div>
    """, unsafe_allow_html=True)
    
    if os.path.exists("pages/6_E-Course.py"):
        if st.button("🚀 Get Certified – Start E-Course Now", use_container_width=True):
            st.switch_page("pages/6_E-Course.py")
    else:
        st.info("🌟 E-Course launching soon! Check back later.")

# ────────────────────────────────────────────────
# Footer
# ────────────────────────────────────────────────
st.markdown("""
    <div class="footer">
        <h3 style="color: #fbbf24;">ERAS Africa</h3>
        <p>Advancing perioperative excellence across the continent</p>
        <p>📧 <a href="mailto:amaretom22@gmail.com" style="color: #fbbf24;">amaretom22@gmail.com</a></p>
        <p>© 2026 ERAS Africa – For healthcare professionals | Pilot version</p>
        <p style="font-size: 0.9rem; color: #94a3b8;">📍 Addis Ababa, Ethiopia</p>
    </div>
""", unsafe_allow_html=True)