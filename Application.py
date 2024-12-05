##################################

# Imports
import streamlit as st
from datetime import date, datetime, timedelta
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
from PIL import Image
import pandas as pd
import pytz
import ta

##################################

# Constants for defining data range
START = "2005-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

##################################

# Logo Images
img = Image.open('/Users/mariaeduardaduarte/Documents/SMP/logo.PNG')
img2 = Image.open('/Users/mariaeduardaduarte/Documents/SMP/logo2.PNG')

# Website Icon
st.set_page_config(page_title='SMP - Application', page_icon=img)

# Logo image
st.logo(img2)

##################################

# User Input for Stock Ticker
st.header('🔍 Stock Selection and Forecast Parameters')
selected_stock = st.text_input('Enter the stock ticker (e.g., AAPL, MSFT, AMZN) for prediction:', 'AAPL')
n_years = st.slider('Select the number of years to forecast into the future:', 1, 4, 3, help='Use the slider to choose a prediction period between 1 and 5 years.')
period = n_years * 365

##################################

# Function to Load Data from Yahoo Finance
@st.cache_data(show_spinner=True, ttl=86400)
def load_data(ticker):
    """Fetch historical stock data from Yahoo Finance based on the provided ticker."""
    st.write(f"Fetching data for **{ticker}** from {START} to {TODAY}...")
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

# Function to Plot Raw Data
def plot_raw_data(data):
    """Visualize the raw historical stock data (Open and Close prices) using Plotly."""
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="Opening Price", line=dict(color='royalblue', width=2)))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="Closing Price", line=dict(color='firebrick', width=2)))
    fig.update_layout(
        title=f'Historical Stock Prices for {selected_stock} (Open vs. Close)',
        xaxis_title='Date',
        yaxis_title='Price (USD)',
        xaxis_rangeslider_visible=True,
        legend_title="Price Type"
    )
    st.plotly_chart(fig)

# Load and Display Data
data = load_data(selected_stock)
st.subheader(f'Raw Data Overview for {selected_stock}')
st.write(f'Below is a snapshot of the most recent stock data for **{selected_stock}**. Analyze the latest trends before diving into forecasts!')
st.write(data.tail())

# Plot Raw Data
plot_raw_data(data)

# Function to Add Moving Averages
def plot_moving_averages(data):
    """Calculate and display 30-day and 90-day Simple Moving Averages (SMA) over time."""
    data['SMA30'] = data['Close'].rolling(window=30).mean()
    data['SMA90'] = data['Close'].rolling(window=90).mean()
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="Closing Price", line=dict(color='firebrick', width=2)))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['SMA30'], name="30-Day SMA", line=dict(color='green', dash='dot', width=2)))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['SMA90'], name="90-Day SMA", line=dict(color='orange', dash='dot', width=2)))
    
    fig.update_layout(
        title=f'{selected_stock} Price with 30 and 90 Day Moving Averages',
        xaxis_title='Date',
        yaxis_title='Price (USD)',
        xaxis_rangeslider_visible=True,
        legend_title="Price & Averages"
    )
    st.plotly_chart(fig)

# Display Moving Averages
st.subheader(f'Moving Averages (30 & 90 Day) for {selected_stock}')
st.write("""
Simple Moving Averages (SMA) help smooth out price fluctuations over time, making it easier to spot long-term trends. 
The **30-day SMA** highlights short-term trends, while the **90-day SMA** gives a clearer picture of the overall movement.
""")
plot_moving_averages(data)

# Prophet Model Forecasting
def create_forecast(data, period):
    """Fit the Prophet model on historical stock data and forecast future stock prices for the specified period."""
    df_train = data[['Date', 'Close']].rename(columns={"Date": "ds", "Close": "y"})
    model = Prophet(daily_seasonality=False, yearly_seasonality=True, weekly_seasonality=True)
    model.add_seasonality(name='monthly', period=30.5, fourier_order=5)
    model.fit(df_train)
    future = model.make_future_dataframe(periods=period)
    forecast = model.predict(future)
    return forecast, model

# Create and Show Forecast
forecast, model = create_forecast(data, period)
st.subheader(f'{n_years}-Year Forecast for {selected_stock}')
st.write("""
Using advanced time series forecasting, Prophet predicts future stock prices based on historical data patterns. 
Below are the forecasted prices for the upcoming years:
""")
st.write(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

# Function to Plot Forecast
def plot_forecast(model, forecast):
    """Plot the forecasted stock prices along with the historical data."""
    fig = plot_plotly(model, forecast)
    fig.update_layout(title=f'{n_years}-Year Stock Price Forecast for {selected_stock}')
    st.plotly_chart(fig)

# Display Forecast Plot
st.write(f"### {n_years}-Year Forecast Plot for {selected_stock}")
plot_forecast(model, forecast)

# Forecast Components
st.subheader('Forecast Components Breakdown')
st.write("""
This section highlights the key components that influence the forecast, such as trends, yearly, weekly, and monthly patterns. 
Explore the underlying structure of the model and how it generates predictions.
""")
components_fig = model.plot_components(forecast)
st.write(components_fig)

# Function to Analyze Volume
def plot_volume(data):
    """Visualize trading volume of the selected stock."""
    fig = go.Figure()
    fig.add_trace(go.Bar(x=data['Date'], y=data['Volume'], name='Volume', marker_color='lightseagreen'))
    fig.update_layout(
        title=f'Trading Volume for {selected_stock}',
        xaxis_title='Date',
        yaxis_title='Volume',
        xaxis_rangeslider_visible=True
    )
    st.plotly_chart(fig)

# Process data to ensure it is timezone-aware and has the correct format
def process_data(data):
    if data.index.tzinfo is None:
        data.index = data.index.tz_localize('UTC')
    data.index = data.index.tz_convert('US/Eastern')
    data.reset_index(inplace=True)
    data.rename(columns={'Date': 'Datetime'}, inplace=True)
    return data

# Display Volume Data
st.subheader(f'Trading Volume Analysis for {selected_stock}')
st.write("""
Trading volume provides insights into market activity. A spike in volume can indicate significant interest in the stock, 
which may be driven by news, earnings reports, or broader market movements.
""")
plot_volume(data)

# Fetch stock data based on the ticker, period, and interval
def fetch_stock_data(ticker, period, interval):
    end_date = datetime.now()
    if period == '1wk':
        start_date = end_date - timedelta(days=7)
        data = yf.download(ticker, start=start_date, end=end_date, interval=interval)
    else:
        data = yf.download(ticker, period=period, interval=interval)
    return data

##################################

# Sidebar: Real-Time Trending
st.sidebar.header('🚀 Real-Time Trending Tickers')
st.sidebar.write("""
Stay updated with live prices and changes for trending stocks. 
Monitor some of the biggest players in the market right now!
""")

# Automatically Fetch Real-Time Data for Selected Symbols
stock_symbols = ['AAPL', 'GOOGL', 'AMZN', 'MSFT']
if 'real_time_data' not in st.session_state:
    st.session_state.real_time_data = {}

for symbol in stock_symbols:
    real_time_data = fetch_stock_data(symbol, '1d', '1m')
    if not real_time_data.empty:
        real_time_data = process_data(real_time_data)
        st.session_state.real_time_data[symbol] = real_time_data
    else:
        st.session_state.real_time_data[symbol] = None

# Display Sidebar Metrics for Real-Time Data
for symbol in stock_symbols:
    real_time_data = st.session_state.real_time_data.get(symbol)
    if real_time_data is not None:
        last_price = real_time_data['Close'].iloc[-1]
        change = last_price - real_time_data['Open'].iloc[0]
        pct_change = (change / real_time_data['Open'].iloc[0]) * 100
        st.sidebar.metric(f"{symbol}", f"{last_price:.2f} USD", f"{change:.2f} ({pct_change:.2f}%)")
    else:
        st.sidebar.write(f"{symbol}: Data not available")

# Sidebar information section
st.sidebar.subheader('About')
st.sidebar.info('Enter the stock ticker to choose which stock to analyze. Use the slider to select a forecast period (1–4 years). The app will show a summary of recent historical data and interactive charts of opening and closing prices. View 30-day and 90-day moving averages to spot short- and long-term trends. Analyze trading activity for market signals, then explore predicted prices using the Prophet model, with breakdowns of yearly and monthly patterns.')

##################################

# Footer
st.write('---')
st.write('**Stock Market Predictor** - Powered by Python, Prophet, Plotly, Yahoo Finance, and Streamlit. 🚀')
st.write("📈 Gain insights into the stock market with precise forecasting and data visualization. Stay informed and invest smarter!")

_left, mid, _right = st.columns(3)
with mid:
   st.image(img2)
