#import required libraries
import streamlit as st
import yfinance as yf
from datetime import datetime
from datetime import date
st.set_page_config(
    page_title="Stock Tool",
    page_icon="",
)

#ticker search feature in sidebar
st.subheader("""Stock Tool Web App""")
selected_stock = st.text_input("Enter a valid stock ticker...")
button_clicked = st.button("SEARCH")
if button_clicked == "SEARCH":
    main()


#main function
def main():
    st.subheader("""Daily **closing price** for """ + selected_stock)
    #get data on searched ticker
    stock_data = yf.Ticker(selected_stock)
    #get historical data for searched ticker
    stock_df = stock_data.history(period='1d', start='2020-01-01', end=None)
    #print line chart with daily closing prices for searched ticker
    st.line_chart(stock_df.Close)

    st.subheader("""Last **closing price** for """ + selected_stock)
    #define variable today 
    today = datetime.today().strftime('%Y-%m-%d')
    #get current date data for searched ticker
    stock_lastprice = stock_data.history(period='1d', start=today, end=today)
    #get current date closing price for searched ticker
    last_price = (stock_lastprice.Close)
    #if market is closed on current date print that there is no data available
    if last_price.empty == True:
        st.write("No data available at the moment")
    else:
        st.write(last_price)
    
    #get daily volume for searched ticker
    st.subheader("""Daily **volume** for """ + selected_stock)
    st.line_chart(stock_df.Volume) 

    
if __name__ == "__main__":
    main()


