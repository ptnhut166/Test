import streamlit as st


add_selectbox=st.sidebar.selectbox(
    "What Algorithm do you want to use?",
    ("Linear regression", "Logistic regression", "ARIMA","GRU","LSTM", "RNN","SSA")
)

# Truy cập biến toàn cục
data = globals()["data"]

# In dữ liệu
print(data)