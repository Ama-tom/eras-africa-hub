import streamlit as st

st.title("Training Materials & Downloads")

st.subheader("ERAS Training Manuals (Participant & Facilitator Guides)")

# Example for one manual – repeat for all 8
with open("materials/manuals/eras-qi-program-participant.pdf", "rb") as file:
    st.download_button(
        label="ERAS QI Program – Participant Manual (PDF)",
        data=file,
        file_name="eras-qi-program-participant.pdf",
        mime="application/pdf"
    )

# Add more buttons for other manuals
st.subheader("ERAS QI Program PowerPoint Slides")
with open("materials/ppts/eras-qi-program-slides.pptx", "rb") as file:
    st.download_button(
        label="Download 30 PPT Slides (PPTX)",
        data=file,
        file_name="eras-qi-program-slides.pptx",
        mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
    )

st.info("All materials are for internal training use. Contact admin for certification or questions.")