#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 21:25:14 2020

@author: Prerit Saxena
"""

import yfinance as yf
import streamlit as st
import pandas as pd
from datetime import date, timedelta

st.write("""
         # Stock Price Summary
         
         """)
       

         
df = pd.DataFrame({
  'Company': ['GOOGL', 'FB', 'AAPL', 'MSFT', 'LYFT', 'ZM', 'TSLA', 'SM','ACMR', 'NIO','NVDA','AMZN','SQ','PYPL','FTCH','SNE']})
  
option = st.sidebar.selectbox(
    'Select Company',
     df['Company'])

'Shown below are the statistics for the selected company'

'Displaying Trend for: ', option
         
# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75

# Defining the ticker symbol

tickerSymbol = option

# get data on this ticker

tickerData = yf.Ticker(tickerSymbol)

Today = date.today().isoformat()   
Last_1_week = (date.today()-timedelta(days=7)).isoformat()

option2 = 'Last 5 years'
dates = pd.DataFrame({
  'Date_sel': ['Last 5 years', 'Last 1 year', 'Last 3 months', 'Last 1 month', 'Last 1 week', 'Today' ]
   })

option2 = st.sidebar.selectbox(
    'Select Time Period',
     dates['Date_sel'])

if option2 == 'Today':
    startdate=date.today().isoformat()
elif option2 =='Last 1 week':
    startdate=(date.today()-timedelta(days=7)).isoformat()
elif option2 == 'Last 1 month':
    startdate=(date.today()-timedelta(days=30)).isoformat()
elif option2 == 'Last 3 months':
    startdate=(date.today()-timedelta(days=90)).isoformat()
elif option2 == 'Last 1 year':
    startdate=(date.today()-timedelta(days=365)).isoformat()
elif option2 == 'Last 5 years':
    startdate=(date.today()-timedelta(days=1825)).isoformat()
# get the historical prices for this ticker

tickerDf = tickerData.history(period = '1d', start=startdate, end=date.today())

# Open High low Close Volume Dividends Stock Splits

st.line_chart(tickerDf.Close)

st.write("""**Analyst recommendations:** 
         
         """)
         
st.write(tickerData.recommendations.tail(10))

st.write("""**About the company:** 
         
         """)

st.write(tickerData.info['longBusinessSummary'])

expander = st.beta_expander("Major holders")
expander.write(tickerData.major_holders)

st.sidebar.write(""" \n \n \n Built by **Prerit Saxena** """)
