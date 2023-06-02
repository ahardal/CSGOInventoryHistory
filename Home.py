import streamlit as st
import pandas as pd 


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
    layout="wide",
)



st.write("# Welcome to CSGO Inventory History!")

st.sidebar.success("Testing")

st.write("SOME TEXT ...")
st.write("Upload your CSGO Inventory History")

st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a CSV file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Initialize session state
    if 'df' not in st.session_state:
        st.session_state['df'] = df

    st.subheader('DataFrame')
    st.write(df)


    # Value counts of EventDescription, events that you traded with people gathered together for value counts table. 
    val_counts = df.value_counts('EventDescription')
    filtered_rows = val_counts[val_counts.index.str.contains('You traded')]
    filtered_rows_series = pd.Series([filtered_rows.sum()], index=["You traded with .."])

    res = val_counts[~val_counts.index.str.contains('You traded')]
    df_value_counts = pd.concat([res, filtered_rows_series]).sort_values(ascending=False)

    st.subheader('Value counts of Events')
    st.write(df_value_counts)


    st.header('Show spesific events.')

    option = st.selectbox(
        'Selected an event',
        (df_value_counts.index))

    option_df = df[df['EventDescription'].str.contains(option)]
    st.write(option_df)
    st.markdown(f""" 
        You '{option}' {option_df.shape[0]} times.
    """)

    

else:
    st.info('☝️ Upload a CSV file')


