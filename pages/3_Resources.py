import streamlit as st

st.title("Training Materials & Downloads")

st.subheader("ERAS Training Manuals (Participant & Facilitator Guides)")

# Use exact path & name from GitHub
with open("pages/manuals/materialsmanualseras-qi-program-participant.pdf.pdf", "rb") as file:
    st.download_button(
        label="ERAS QI Program – Participant Manual (PDF)",
        data=file,
        file_name="eras-qi-program-participant.pdf",  # clean name for download
        mime="application/pdf"
    )

with open("pages/manuals/materialsmanualseras-qi-program-facilitator-guide.pdf.pdf", "rb") as file:
    st.download_button(
        label="ERAS QI Program – Facilitator Guide (PDF)",
        data=file,
        file_name="eras-qi-program-facilitator-guide.pdf",
        mime="application/pdf"
    )

# Repeat for other manuals (Smart Audit, Teamwork, Evidence Based Medicine)

st.subheader("ERAS QI Program PowerPoint Slides")
with open("materials/ppts/Drains and Tubes in ERAS.pptx", "rb") as file:  # use exact name
    st.download_button(
        label="Download ERAS QI Program PPTs (30 slides)",
        data=file,
        file_name="eras-qi-program-slides.pptx",
        mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
    )

st.info("Materials for training use. Contact admin for CEU certification.")