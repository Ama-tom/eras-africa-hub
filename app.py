import streamlit as st
import os
import streamlit.components.v1 as components

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
    
    /* Navigation Header */
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
    
    /* DHIS2 Dashboard styling */
    .dhis2-header {
        background: linear-gradient(135deg, #1e3a8a, #2563eb);
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
        color: white;
        text-align: center;
        border: 2px solid #93c5fd;
    }
    
    .dhis2-header h3 {
        color: #FFD700;
        margin: 0;
    }
    
    .dashboard-card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        margin: 10px 0;
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
# SIMPLE NAVIGATION HEADER
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
            <a href="/DHIS2_Dashboard" target="_self" class="nav-item">📊 DHIS2</a>
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
# DHIS2 DASHBOARD INTEGRATION
# ────────────────────────────────────────────────
st.markdown("""
    <div style="text-align: center; margin-bottom: 20px;">
        <h2 style="color: #8B4513;">📊 DHIS2 Perioperative Dashboard</h2>
        <p style="color: #5c3e2e;">Real-time surgical outcomes data from across Africa</p>
    </div>
""", unsafe_allow_html=True)

# Create tabs for different views
tab1, tab2, tab3 = st.tabs(["📈 Live Dashboard", "ℹ️ About Integration", "📋 Data Dictionary"])

with tab1:
    st.markdown("""
        <div style="background: linear-gradient(135deg, #e6f0ff, #d4e4ff); padding: 15px; border-radius: 10px; margin-bottom: 20px; border-left: 5px solid #2563eb;">
            <p style="margin: 0; color: #1e3a8a;">
                <strong>🔐 Access Credentials:</strong> Username: <code>admin</code> | Password: <code>district</code>
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Dashboard selector
    dashboard_option = st.selectbox(
        "Select Dashboard View",
        ["Main Dashboard", "Surgical Outcomes", "ERAS Compliance", "Patient Analytics", "Hospital Performance"]
    )
    
    # Map selections to URLs (you can customize these based on actual dashboard IDs)
    dashboard_urls = {
        "Main Dashboard": "http://196.189.155.58:8090/dhis-web-dashboard/#/",
        "Surgical Outcomes": "http://196.189.155.58:8090/dhis-web-dashboard/#/surgical-outcomes",
        "ERAS Compliance": "http://196.189.155.58:8090/dhis-web-dashboard/#/eras-compliance",
        "Patient Analytics": "http://196.189.155.58:8090/dhis-web-dashboard/#/patient-analytics",
        "Hospital Performance": "http://196.189.155.58:8090/dhis-web-dashboard/#/hospital-performance"
    }
    
    # Dashboard info
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(f"""
            <div class="dashboard-card">
                <h4 style="color: #1e3a8a; margin-top: 0;">{dashboard_option}</h4>
                <p>Loading live data from DHIS2 server...</p>
                <p style="font-size: 0.9rem; color: #666;">Server: 196.189.155.58:8090</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div style="background: #f0f9ff; padding: 15px; border-radius: 10px;">
                <h5 style="color: #2563eb; margin-top: 0;">Quick Stats</h5>
                <p>📊 Active Hospitals: <strong>23</strong></p>
                <p>📈 Data Points: <strong>45.2K</strong></p>
                <p>🎯 Compliance: <strong>78%</strong></p>
                <p>🔄 Last Update: <strong>Today 08:00</strong></p>
            </div>
        """, unsafe_allow_html=True)
    
    # Embed the DHIS2 dashboard
    st.markdown("### Live Dashboard View")
    components.iframe(dashboard_urls[dashboard_option], height=700, scrolling=True)

with tab2:
    st.markdown("""
        <div style="padding: 20px; background: white; border-radius: 10px;">
            <h3 style="color: #8B4513;">🌍 ERAS Africa & DHIS2 Partnership</h3>
            
            <p>This integration brings together ERAS protocols and DHIS2's robust health information
            management system to create Africa's first real-time perioperative data network.</p>
            
            <h4 style="color: #A0522D; margin-top: 25px;">Key Benefits:</h4>
            <ul>
                <li><strong>Real-time Monitoring:</strong> Track surgical outcomes as they happen across 23+ hospitals</li>
                <li><strong>Multi-country Analytics:</strong> Compare data across 8+ African nations</li>
                <li><strong>Quality Improvement:</strong> Identify best practices and areas for improvement</li>
                <li><strong>Research Ready:</strong> Export clean, standardized data for studies</li>
                <li><strong>ERAS Compliance Tracking:</strong> Monitor protocol adherence in real-time</li>
            </ul>
            
            <h4 style="color: #A0522D; margin-top: 25px;">Current Coverage:</h4>
            <div style="display: grid; grid-template-columns: repeat(2,1fr); gap: 15px; margin: 15px 0;">
                <div style="background: #f5f5f5; padding: 15px; border-radius: 8px;">
                    <strong>23</strong> Partner Hospitals
                </div>
                <div style="background: #f5f5f5; padding: 15px; border-radius: 8px;">
                    <strong>8</strong> Countries
                </div>
                <div style="background: #f5f5f5; padding: 15px; border-radius: 8px;">
                    <strong>45,000+</strong> Surgical Records
                </div>
                <div style="background: #f5f5f5; padding: 15px; border-radius: 8px;">
                    <strong>78%</strong> ERAS Compliance
                </div>
            </div>
            
            <h4 style="color: #A0522D; margin-top: 25px;">Technical Architecture:</h4>
            <p>The integration uses DHIS2's robust API framework to securely transmit anonymized 
            perioperative data from hospital EMRs to the central dashboard. Data is encrypted, 
            validated, and processed in near real-time.</p>
            
            <div style="background: #f0f9ff; padding: 15px; border-radius: 8px; margin-top: 20px;">
                <p style="margin: 0;"><strong>🔒 Privacy & Security:</strong> All data is de-identified and complies with 
                national health data protection regulations. Patient confidentiality is maintained 
                through strict access controls and data anonymization.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

with tab3:
    st.markdown("""
        <div style="padding: 20px; background: white; border-radius: 10px;">
            <h3 style="color: #8B4513;">📋 Perioperative Data Dictionary</h3>
            
            <table style="width: 100%; border-collapse: collapse;">
                <tr style="background: #8B4513; color: white;">
                    <th style="padding: 10px; text-align: left;">Metric</th>
                    <th style="padding: 10px; text-align: left;">Description</th>
                    <th style="padding: 10px; text-align: left;">Source</th>
                    <th style="padding: 10px; text-align: left;">Update Frequency</th>
                </tr>
                <tr style="border-bottom: 1px solid #ddd;">
                    <td style="padding: 10px;"><strong>Length of Stay</strong></td>
                    <td style="padding: 10px;">Days from admission to discharge</td>
                    <td style="padding: 10px;">EMR</td>
                    <td style="padding: 10px;">Real-time</td>
                </tr>
                <tr style="border-bottom: 1px solid #ddd; background: #f9f9f9;">
                    <td style="padding: 10px;"><strong>30-day Complications</strong></td>
                    <td style="padding: 10px;">Post-op complications within 30 days</td>
                    <td style="padding: 10px;">Follow-up</td>
                    <td style="padding: 10px;">Daily</td>
                </tr>
                <tr style="border-bottom: 1px solid #ddd;">
                    <td style="padding: 10px;"><strong>ERAS Compliance</strong></td>
                    <td style="padding: 10px;">% of ERAS elements completed</td>
                    <td style="padding: 10px;">Checklist</td>
                    <td style="padding: 10px;">Per procedure</td>
                </tr>
                <tr style="border-bottom: 1px solid #ddd; background: #f9f9f9;">
                    <td style="padding: 10px;"><strong>Readmission Rate</strong></td>
                    <td style="padding: 10px;">Unplanned readmission within 30 days</td>
                    <td style="padding: 10px;">EMR</td>
                    <td style="padding: 10px;">Daily</td>
                </tr>
                <tr style="border-bottom: 1px solid #ddd;">
                    <td style="padding: 10px;"><strong>Mortality Rate</strong></td>
                    <td style="padding: 10px;">In-hospital mortality</td>
                    <td style="padding: 10px;">EMR</td>
                    <td style="padding: 10px;">Real-time</td>
                </tr>
            </table>
            
            <h4 style="color: #A0522D; margin-top: 30px;">Data Quality Indicators:</h4>
            <div style="display: grid; grid-template-columns: repeat(3,1fr); gap: 15px; margin: 15px 0;">
                <div style="background: #e8f5e9; padding: 15px; border-radius: 8px; text-align: center;">
                    <div style="font-size: 1.5rem; font-weight: bold; color: #2e7d32;">94%</div>
                    <div>Completeness</div>
                </div>
                <div style="background: #fff3e0; padding: 15px; border-radius: 8px; text-align: center;">
                    <div style="font-size: 1.5rem; font-weight: bold; color: #f57c00;">89%</div>
                    <div>Timeliness</div>
                </div>
                <div style="background: #e3f2fd; padding: 15px; border-radius: 8px; text-align: center;">
                    <div style="font-size: 1.5rem; font-weight: bold; color: #1976d2;">96%</div>
                    <div>Accuracy</div>
                </div>
            </div>
            
            <p style="font-style: italic; color: #666; margin-top: 20px;">
                * Data dictionary follows WHO and DHIS2 standards for health information systems
            </p>
        </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="african-divider"></div>', unsafe_allow_html=True)

# ────────────────────────────────────────────────
# Sidebar with African Regions
# ────────────────────────────────────────────────
st.sidebar.markdown("### 🌍 African Regions")

# Region data
regions = {
    "East Africa": ["Ethiopia", "Kenya", "Tanzania", "Uganda", "Rwanda", "Burundi", "South Sudan"],
    "Southern Africa": ["South Africa", "Botswana", "Namibia", "Zimbabwe", "Zambia", "Malawi", "Mozambique"],
    "West Africa": ["Nigeria", "Ghana", "Senegal", "Côte d'Ivoire", "Mali", "Burkina Faso"],
    "Central Africa": ["Cameroon", "DR Congo", "Gabon", "Chad", "Central African Republic"],
    "North Africa": ["Morocco", "Egypt", "Tunisia", "Algeria", "Libya", "Sudan"]
}

# Country selector
all_countries = []
for country_list in regions.values():
    all_countries.extend(country_list)

selected_country = st.sidebar.selectbox(
    "Select your country",
    ["None"] + sorted(all_countries)
)

if selected_country != "None":
    st.sidebar.success(f"Welcome, colleague from {selected_country}! 👋")

# Region expanders
for region, countries in regions.items():
    with st.sidebar.expander(region):
        for country in countries:
            if country == selected_country:
                st.markdown(f"**🌟 {country}**")
            else:
                st.markdown(f"- {country}")

# DHIS2 Quick Stats in Sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 DHIS2 Quick Stats")
st.sidebar.markdown("""
- 🏥 **Active Hospitals:** 23
- 🌍 **Countries:** 8
- 📈 **Data Points:** 45.2K
- ✅ **Compliance:** 78%
- ⏱️ **Last Sync:** Today 08:00
""")

# Contact in Sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("### 📬 Contact")
st.sidebar.markdown("📧 **Email:** amaretom22@gmail.com")
st.sidebar.markdown("📍 **Location:** Addis Ababa, Ethiopia")
st.sidebar.markdown("📱 **Phone:** +251 911 742 998")

# ────────────────────────────────────────────────
# Call to Action
# ────────────────────────────────────────────────
st.markdown("""
    <div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #FFF8E7, #FFE4C4); border-radius: 15px; margin: 20px 0;">
        <h3 style="color: #8B4513;">Ready to Transform Surgical Care?</h3>
        <p style="color: #5c3e2e;">Join hundreds of healthcare professionals across Africa</p>
    </div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if os.path.exists("pages/6_E-Course.py"):
        if st.button("🌟 START E-COURSE NOW", use_container_width=True):
            st.switch_page("pages/6_E-Course.py")
    else:
        st.info("🎓 E-Course coming soon!")

# ────────────────────────────────────────────────
# Footer
# ────────────────────────────────────────────────
st.markdown("""
    <div class="footer">
        <h3>ERAS Africa</h3>
        <p style="margin: 5px 0;">Advancing perioperative excellence across Africa</p>
        <p style="margin: 15px 0 5px 0;">📧 <a href="mailto:amaretom22@gmail.com">amaretom22@gmail.com</a></p>
        <p style="margin: 5px 0;">📱 +251 XXX XXX XXX</p>
        <p style="margin: 15px 0 5px 0;">© 2026 ERAS Africa – For healthcare professionals</p>
    </div>
""", unsafe_allow_html=True)