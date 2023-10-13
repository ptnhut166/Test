import streamlit as st


add_selectbox=st.sidebar.selectbox(
    "What Algorithm do you want to use?",
    ("Linear regression", "Logistic regression", "ARIMA","GRU","LSTM", "RNN","SSA")
)

