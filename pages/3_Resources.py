import streamlit as st

st.subheader("Download ERAS Training Manuals")

# Example for one – repeat for all 6+ PDFs
with open("pages/manuals/materialsmanualseras-qi-program-participant.pdf.pdf", "rb") as file:
    st.download_button(
        label="ERAS QI Program – Participant Manual (PDF)",
        data=file,
        file_name="eras-qi-program-participant.pdf",
        mime="application/pdf"
    )

with open("pages/manuals/materialsmanualseras-qi-program-facilitator-guide.pdf.pdf", "rb") as file:
    st.download_button(
        label="ERAS QI Program – Facilitator Guide (PDF)",
        data=file,
        file_name="eras-qi-program-facilitator-guide.pdf",
        mime="application/pdf"
    )

# Add similar buttons for the other manuals (Smart Audit, Teamwork, Evidence Based Medicine)
# Example for PPTs
with open("pages/ppts/eras-qi-program-slides.pptx", "rb") as file:
    st.download_button(
        label="ERAS QI Program – 30 PPT Slides",
        data=file,
        file_name="eras-qi-program-slides.pptx",
        mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
    )