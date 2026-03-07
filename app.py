import streamlit as st

st.set_page_configcol1, col2 = st.columns([1, 4])
with col1:
    st.image("icons/eras-192.jpg", width=100)  # your custom icon
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