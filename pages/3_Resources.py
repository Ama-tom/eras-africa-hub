import streamlit as st

st.title("Resources & Training")
st.markdown("""
- ERAS Society LMIC adaptations: [link to ERAS Society site]
- Ethiopian scoping reviews (2024–2026)
- Training webinars and case studies
""")
# Example PDF download button (upload PDF to repo first)
with open("resources/eras-checklist.pdf", "rb") as file:
    st.download_button("Download ERAS Checklist", file, file_name="eras-checklist.pdf")