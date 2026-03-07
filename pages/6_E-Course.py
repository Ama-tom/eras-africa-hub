import streamlit as st

st.title("ERAS QI Program E-Course")

st.markdown("""
**Earn 15 CEUs per program** (total 60 across 4 programs)  
Certified by ERAS Africa, Federal Ministry of Health Ethiopia, African Union, CDC Africa.
""")

st.subheader("Start the Course")
if st.button("Begin ERAS QI Program E-Course"):
    st.session_state.course_started = True
    st.success("Course started! Complete modules to earn CEUs.")
    st.markdown("Module 1: Introduction to ERAS QI...")
    # Add more modules, quizzes (use st.radio for questions), progress bar with session_state