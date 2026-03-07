import streamlit as st

# Optional: password protection (uncomment if needed)
# password = st.text_input("Enter password", type="password")
# if password != "your_secret_password":
#     st.warning("Access restricted.")
#     st.stop()

st.set_page_config(
    page_title="ERAS Africa",
    page_icon="🏥",
    layout="wide"
)

# Header with logo (adjust path if your icon is in icons/ folder)
col1, col2 = st.columns([1, 5])
with col1:
    st.image("icons/eras-192.jpg", width=100)  # your custom icon
with col2:
    st.title("Enhanced Recovery After Surgery – Africa")

st.markdown("""
Central hub for ERAS implementation, tools, guidelines, and resources in African/LMIC settings.
""")

st.markdown("### Quick Access")
st.markdown("- Use the **sidebar** to navigate sections")
st.markdown("- **Postoperative Risk Calculator** — predict prolonged stay and complications")
st.markdown("- Guidelines, resources, and about coming soon")