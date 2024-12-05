##################################

# Imports
import streamlit as st
from PIL import Image

##################################

# Load logo images
img = Image.open('/Users/mariaeduardaduarte/Documents/SMP/logo.PNG')
img2 = Image.open('/Users/mariaeduardaduarte/Documents/SMP/logo2.PNG')

# Website Icon
st.set_page_config(page_title='SMP - Introduction', page_icon=img)

# Logo image
st.logo(img2)

##################################

# Title and introduction
st.title('📊 Welcome to the Stock Market Predicter!')
st.write("""
    Explore the stock market with cutting-edge time series forecasting using **Prophet**. This application enables users to view detailed historical stock data, moving averages, volume analysis, and forecast future stock prices. It's designed for both enthusiasts and professionals to gain insights into stock trends and future predictions.
""")

##################################

# Body
st.write("""
    In today's fast-paced financial landscape, staying ahead of market trends is crucial for making informed investment decisions. Our Stock Market Predicter leverages advanced algorithms to analyze historical data and predict future stock movements, offering users an intuitive interface to visualize trends and insights. Whether you're a seasoned investor or just starting your trading journey, this tool provides you with the resources needed to understand market dynamics and optimize your portfolio strategies.
""")

# Video
st.video("/Users/mariaeduardaduarte/Documents/SMP/SMP_2.mp4")

_left, mid, _right = st.columns(3)
with mid:
    st.write("""
        **Fast, easy and accurate.**
""")

##################################

# Footer
st.write('---')
st.write('**Stock Market Predicter** - Powered by Python, Prophet, Plotly, Yahoo Finance, and Streamlit. 🚀')
st.write("📈 Gain insights into the stock market with precise forecasting and data visualization. Stay informed and invest smarter!")

# Show the logo at the bottom
_left, mid, _right = st.columns(3)
with mid:
    st.image(img2)


    