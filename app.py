import urllib.request
import json
import streamlit as st
import pandas as pd

heart = pd.read_csv('./data/heart.csv')

st.title("Web Data App | Dataset Heart")
st.markdown("Este é o projeto final para o módulo de Cloud e Infraestrutura para Ciência de Dados")


bt_prediction = st.button('Prediction')


st.write(heart)