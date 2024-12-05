##################################

# Imports
import streamlit as st
from PIL import Image

##################################

# Load logo images
img = Image.open('/Users/mariaeduardaduarte/Documents/SMP/logo.PNG')
img2 = Image.open('/Users/mariaeduardaduarte/Documents/SMP/logo2.PNG')

# Website Icon
st.set_page_config(page_title='SMP - FaQ', page_icon=img)

# Logo image
st.logo(img2)

##################################

# FAQ Header
st.title("Frequently Asked Questions (FAQ)")
st.write("""
Here you will find answers to the most common questions about using our Stock Market Predicter (SMP) platform. If you have further inquiries, feel free to reach out to us through the contact form or support email.
""")

##################################

# FAQ Sections
faq_data = {
    "1. What is Stock Market Predicter (SMP)?": "SMP is an advanced stock forecasting and analysis tool powered by machine learning and financial data to help users make informed decisions about stock investments.",
    "2. How does SMP forecast stock prices?": "SMP uses the Prophet time series forecasting model to predict future stock prices based on historical data and seasonal trends.",
    "3. Can I rely on these forecasts for real trading decisions?": "While the forecasts are based on historical patterns and statistical models, they are not guaranteed. Use them as one of many tools for investment decisions.",
    "4. How do I select a stock for prediction?": "Simply enter the stock ticker symbol (e.g., AAPL for Apple) in the text input field on the main page. SMP will fetch and display historical data and predictions for the selected stock.",
    "5. What are Moving Averages, and why are they important?": "Moving Averages (30 and 90-day SMAs) help smooth out stock price fluctuations, making it easier to identify long-term trends and reduce short-term volatility in the data.",
    "6. How frequently is the data updated?": "The stock data is fetched in real-time from Yahoo Finance, and the predictions are recalculated every time you interact with the page.",
    "7. What if I don't see the stock ticker I am interested in?": "Make sure the ticker symbol you are entering is correct. SMP supports most popular stock symbols. If you're unsure, search for the ticker symbol on financial websites like Yahoo Finance or Google Finance.",
    "8. How far into the future can SMP predict?": "You can forecast stock prices for up to 4 years ahead, depending on the duration you select on the slider. The predictions are based on historical data patterns.",
    "9. How do I interpret the forecast results?": "The results include a range of predicted prices (yhat) along with lower (yhat_lower) and upper (yhat_upper) bounds, providing a range of possible outcomes. The central prediction represents the most likely scenario, but the bounds show potential fluctuations."
}

# Displaying the FAQs with Expander Sections
for question, answer in faq_data.items():
    with st.expander(question):
        st.write(answer)

# Contact information
st.write('---')
st.write('If you have any more questions, feel free to contact our support team at **support@stockmarketpredicter.com**.')
st.write('Thank you for using SMP!')

##################################

# Footer
st.write('---')
st.write('**Stock Market Predicter** - Powered by Python, Prophet, Plotly, Yahoo Finance, and Streamlit. 🚀')
st.write("📈 Gain insights into the stock market with precise forecasting and data visualization. Stay informed and invest smarter!")

# Display logo at the bottom 
_left, mid, _right = st.columns(3)
with mid:
   st.image(img2)
