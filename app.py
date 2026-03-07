import streamlit as st

st.set_page_config(
    page_title="ERAS Africa – Enhanced Recovery After Surgery",
    page_icon="🏥",
    layout="wide"
)

# Header with logo (use your custom icon)
col1, col2 = st.columns([1, 5])
with col1:
    st.image("icons/ERAS-192.jpg", width=100)
with col2:
    st.title("Enhanced Recovery After Surgery – Africa")
    st.markdown("**ERAS Africa** – Advancing perioperative care in African and low-resource settings")

# Hero / Mission section (inspired by ocrahope.org & erassociety.org)
st.markdown("""
### Our Mission
ERAS Africa is dedicated to promoting **Enhanced Recovery After Surgery** principles across African hospitals and low-resource environments.  
We provide tools, training, guidelines, and evidence-based resources to reduce complications, shorten hospital stays, and improve patient outcomes.

**Certified CEUs available**: 60 total across four core programs (15 CEUs each), endorsed by ERAS Africa, Federal Ministry of Health Ethiopia, African Union, and CDC Africa.
""")

# Quick access cards (modern layout like acrnhealth.com)
st.markdown("### Quick Access to Key Resources")
cols = st.columns(3)

with cols[0]:
    st.markdown("**🩺 Postoperative Risk Calculator**")
    st.markdown("Predict prolonged stay and 30-day complications in real time.")
    st.page_link("pages/1_Calculator.py", label="Open Calculator", icon="🩺")

with cols[1]:
    st.markdown("**📘 ERAS Guidelines & Protocols**")
    st.markdown("Adapted protocols for colorectal, cesarean, emergency laparotomy and more.")
    st.page_link("pages/2_Guidelines.py", label="View Guidelines", icon="📘")

with cols[2]:
    st.markdown("**📚 Training & E-Course**")
    st.markdown("Manuals, PPTs, interactive modules – earn CEUs.")
    st.page_link("pages/6_E-Course.py", label="Start Training", icon="📚")

# Recent updates / news section (like facs.org)
st.markdown("### Latest Updates")
st.markdown("- March 2026: Full e-course modules launched with CEU certification")
st.markdown("- February 2026: Risk calculator updated with improved probability model")
st.markdown("- January 2026: Hub website launched for African surgical teams")

# Footer with contact (inspired by all example sites)
st.markdown("---")
col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    st.markdown("**ERAS Africa**")
    st.markdown("Advancing perioperative recovery in Africa and LMICs")
with col2:
    st.markdown("**Contact**")
    st.markdown("Email: amaretom22@gmail.com")
with col3:
    st.markdown("**Links**")
    st.markdown("[ERAS Society](https://erassociety.org/)")
    st.markdown("[Federal Ministry of Health Ethiopia](https://www.moh.gov.et/)")

st.caption("© 2026 ERAS Africa – All rights reserved | Pilot version for internal use")