import streamlit as st
from main import selected_stock

add_selectbox=st.sidebar.selectbox(
    "What Algorithm do you want to use?",
    ("Linear regression", "Logistic regression", "ARIMA","GRU","LSTM", "RNN","SSA")
)

st.subheader(selected_stock)