import streamlit as st
import main

add_selectbox=st.sidebar.selectbox(
    "What Algorithm do you want to use?",
    ("Linear regression", "Logistic regression", "ARIMA","GRU","LSTM", "RNN","SSA")
)

st.line_chart(main.stock_df.Close)