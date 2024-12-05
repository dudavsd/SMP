##################################

# Imports
import streamlit as st
from PIL import Image

##################################

# Load logo images
img = Image.open('/Users/mariaeduardaduarte/Documents/SMP/logo.PNG')
img2 = Image.open('/Users/mariaeduardaduarte/Documents/SMP/logo2.PNG')

# Website Icon
st.set_page_config(page_title='SMP - Who We Are', page_icon=img)

##################################

# Title and introduction
st.title("👋 Who We Are")
st.markdown("""
It all began in 2024 at **Chapel School**, São Paulo, Brazil. Two students, **Duda Duarte** and **Vibha Komala**, embarked on a journey to bring their shared passion for **economics** and **technology** into the spotlight. What started as a **Computer Science class project** soon evolved into a platform aimed at merging these interests in a meaningful way.

The idea stemmed from their desire to create something that could bring value to others while allowing them to explore the intersection of **technology** and **economics**—a field they both find incredibly fascinating. With this project, they hope to not only excel in their class but also inspire other students to pursue their passions, be it in tech, business, or beyond.
""")

##################################

# Chapel image
img3 = Image.open('/Users/mariaeduardaduarte/Documents/SMP/Chapel.jpg')
st.image(img3, caption="Chapel School, São Paulo.", use_column_width=True)

##################################

# Mission and Vision
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Our Mission")
    st.write("""
    To provide innovative solutions that combine technology and economic insights, 
    helping students and professionals alike make informed decisions in a rapidly changing world.
    """)

with col2:
    st.subheader("Our Vision")
    st.write("""
    We envision a future where technology empowers everyone to better understand 
    and navigate the complex economic landscape, making knowledge accessible to all.
    """)

##################################

# Call to Action
st.markdown("---")
st.subheader("Want to Know More?")
st.write("""
Feel free to explore our platform or [contact us](#contact) for more information. 
We're always excited to share our passion for economics and technology with others!
""")

##################################

# Credits
st.markdown("---")
st.subheader("Credits")
st.write("""
- Special thanks to **Mr. Javier Rebagliati**, our Computer Science teacher, for his guidance and support.
- Logo, slogan, and name designed by **Lorena Cardoso**.
""")

##################################

# Footer
st.markdown("---")
st.write('**Stock Market Predicter** - Powered by Python, Prophet, Plotly, Yahoo Finance, and Streamlit. 🚀')
st.write("📈 Gain insights into the stock market with precise forecasting and data visualization. Stay informed and invest smarter!")

# Display logo at the bottom
_left, mid, _right = st.columns(3)
with mid:
    st.image(img2)
