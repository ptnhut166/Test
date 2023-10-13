import streamlit as st
from main import selected_stock
import yfinance as yf
import main
add_selectbox=st.sidebar.selectbox(
    "What Algorithm do you want to use?",
    ("Linear regression", "Logistic regression", "ARIMA","GRU","LSTM", "RNN","SSA")
)
main()
stock_data = yf.Ticker(selected_stock)
stock_df = stock_data.history(period='1d', start='2020-01-01', end=None)