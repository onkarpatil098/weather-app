import os
from pyowm.weatherapi25.forecast import Forecast
import pytz
import pyowm
import streamlit as st
from matplotlib import dates
from datetime import datetime
import matplotlib.pyplot as plt

from pyowm.owm import OWM
owm = OWM('f3c9d54664509651fe2371e7bfe9b3f8')

st.title("Weather Forecast")
st.write('### write the city name and select the temprature unit and graph type from the sidebar')

place = st.text_input("Name of the city:","")
if place == None:
    st.write("Input a City!")


unit = st.selectbox("Select Temperature Unit",("celcius","fahrenheit"))
g_type = st.selectbox("Select Graph Type",("Line Graph","Bar Graph"))

owm = pyowm.OWM('f3c9d54664509651fe2371e7bfe9b3f8')
mgr = owm.weather_manager()

x=["02/12","03/12","04/12","05/12","06/12","07/12","08/12","09/12","10/12","11/12"]
y=[27,28,29,30,31,31,32,33,34,35]
plt.plot(x,y)
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.show()

# from pyowm.owm import OWM
# owm = OWM('from pyowm.owm import OWM')
# owm = OWM('f3c9d54664509651fe2371e7bfe9b3f8')

