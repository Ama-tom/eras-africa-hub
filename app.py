import streamlit as st

import streamlit as st

# Simple password protection (change "eras2026eth" to your real secret)
password = st.text_input("Enter password to access ERAS Africa Hub", type="password", key="hub_password")

if password != "eras2026eth":  # ← replace with your chosen password
    st.warning("Access restricted. Contact admin for password.")
    st.stop()
st.set_page_configcol1, col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://raw.githubusercontent.com/Ama-tom/eras-africa-hub/main/icons/eras-192.jpg", width=100)
with col2:
    st.title("Enhanced Recovery After Surgery – Africa")

st.title("Enhanced Recovery After Surgery – Africa")
st.markdown("""
Welcome to the ERAS Africa hub — supporting enhanced recovery after surgery in African and low-resource settings.

**Key features:**
- Postoperative risk calculator (predict prolonged stay >8 days and 30-day complications)
- Guidelines & protocols adapted for LMIC contexts
- Resources, training materials, and publications
- About the initiative and contact
""")

st.markdown("### Quick Links")
st.markdown("- **Postoperative Risk Calculator** — in sidebar")
st.markdown("- **Guidelines** — evidence-based protocols")
st.markdown("- **Resources** — downloads and links")
st.markdown("- **About** — mission and contacts")