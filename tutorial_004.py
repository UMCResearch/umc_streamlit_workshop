import pandas as pd
import streamlit as st

st.set_page_config(page_title="VAERS search", layout="wide")

df = pd.read_csv("2020VAERSData.csv", encoding="cp1252", usecols=["VAERS_ID", "SEX", "SYMPTOM_TEXT", "RECVDATE", "NUMDAYS"], parse_dates=['RECVDATE']).dropna()

query = st.text_input('Query', placeholder='Enter a search term')

if query:
    results = df[df['SYMPTOM_TEXT'].str.contains(query)]
    st.table(results)