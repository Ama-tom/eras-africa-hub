import streamlit as st

st.title("Training Materials & Downloads")

st.subheader("ERAS Training Manuals (Participant & Facilitator Guides)")

# ERAS QI Program - Participant
with open("pages/manuals/eras-qi-program-participant.pdf.pdf", "rb") as file:
    st.download_button(
        label="ERAS QI Program – Participant Manual (PDF)",
        data=file,
        file_name="eras-qi-program-participant.pdf",  # clean name for download
        mime="application/pdf"
    )

# ERAS QI Program - Facilitator
with open("pages/manuals/eras-qi-program-facilitator.pdf.pdf", "rb") as file:
    st.download_button(
        label="ERAS QI Program – Facilitator Guide (PDF)",
        data=file,
        file_name="eras-qi-program-facilitator.pdf",
        mime="application/pdf"
    )

# Evidence Based Medicine - Participant
with open("pages/manuals/evidence-based-medicine-program-participant.pdf.pdf", "rb") as file:
    st.download_button(
        label="Evidence Based Medicine – Participant Manual (PDF)",
        data=file,
        file_name="evidence-based-medicine-participant.pdf",
        mime="application/pdf"
    )

# Evidence Based Medicine - Facilitator
with open("pages/manuals/evidence-based-medicine-program-facilitator.pdf.pdf", "rb") as file:
    st.download_button(
        label="Evidence Based Medicine – Facilitator Guide (PDF)",
        data=file,
        file_name="evidence-based-medicine-facilitator.pdf",
        mime="application/pdf"
    )

# Clinical Audit Program - Participant
with open("pages/manuals/clinical-audit-program-participant.pdf.pdf", "rb") as file:
    st.download_button(
        label="Clinical Audit Program – Participant Manual (PDF)",
        data=file,
        file_name="clinical-audit-program-participant.pdf",
        mime="application/pdf"
    )

# Clinical Audit Program - Facilitator
with open("pages/manuals/clinical-audit-program-facilitator.pdf.pdf", "rb") as file:
    st.download_button(
        label="Clinical Audit Program – Facilitator Guide (PDF)",
        data=file,
        file_name="clinical-audit-program-facilitator.pdf",
        mime="application/pdf"
    )

# TCC Program - Participant
with open("pages/manuals/tcc-program-participant.pdf.pdf", "rb") as file:
    st.download_button(
        label="TCC Program – Participant Manual (PDF)",
        data=file,
        file_name="tcc-program-participant.pdf",
        mime="application/pdf"
    )

# TCC Program - Facilitator
with open("pages/manuals/tcc-program-facilitator.pdf.pdf", "rb") as file:
    st.download_button(
        label="TCC Program – Facilitator Guide (PDF)",
        data=file,
        file_name="tcc-program-facilitator.pdf",
        mime="application/pdf"
    )

st.subheader("ERAS QI Program PowerPoint Slides")
with open("materials/ppts/Drains and Tubes in ERAS.pptx", "rb") as file:
    st.download_button(
        label="Download Drains and Tubes in ERAS PPTX",
        data=file,
        file_name="drains-tubes-in-eras.pptx",
        mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
    )

# Add more PPT buttons if needed

st.info("All materials are for internal training use. Contact admin for CEU certification.")