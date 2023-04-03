# -*- coding: utf-8 -*-
"""deployment2.2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13EayIVSy5g5nhvuAOeKHVN9mp1YTZ4JU
"""




pip install -r requirements.txt

import pickle
import streamlit as st
import pandas as pd
import numpy as np
!pip install matplotlib




import matplotlib.pyplot as plt
from PIL import Image
import warnings
warnings.filterwarnings("ignore")

#load the model
model = pickle.load(open('/content/forecast_model_doubleexp (1).pickle','rb'))


#load dataset to plot alongside predictions
df = pd.read_csv('/content/DayForecast (1).csv')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index(['Date'], inplace=True)


#page configuration
st.set_page_config(layout='centered')
image = Image.open('/content/project image].jpg')
st.image(image)

date = st.slider("Select number of dates",1,30,step = 1)

pred = model.forecast(date)
pred = pd.DataFrame(pred, columns=['Quantity'])

if st.button("Predict"):

        col1, col2 = st.columns([2,3])
        with col1:
             st.dataframe(pred)
        with col2:
            fig, ax = plt.subplots()
            df['Quantity'].plot(style='--', color='gray', legend=True, label='known')
            pred['Quantity'].plot(color='b', legend=True, label='prediction')
            st.pyplot(fig)
