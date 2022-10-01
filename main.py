import streamlit as st
import pickle
import numpy as np
from data import locations
with open("bangalore_house_prices_model.pickle",'rb') as f:
    model = pickle.load(f)
st.title("Bangalore :house:House Price:dollar: Prediction  ")
loc = st.selectbox('Select Location:',locations)
sqft = st.number_input('Enter Area (in sq. ft.)')
bath = st.number_input('Number of Bathrooms',min_value=1,step=1)
bhk = st.number_input('BHK',step=1,min_value=1)
submit = st.button('Predict')
if submit:
    X = np.zeros(3 + len(locations))
    X[0]=sqft
    X[1]=bath
    X[2]=bhk
    X[3+locations.index(loc)]=1
    st.success(f"The house price for the given type is Rs {round(model.predict([X])[0],2)} lakhs")