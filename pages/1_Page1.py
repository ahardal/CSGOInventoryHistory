import streamlit as st


if 'df' not in st.session_state:
    st.write("No DataFrame available. Please upload your data in the home page.")
else:
    df = st.session_state.df
    st.write(df)

