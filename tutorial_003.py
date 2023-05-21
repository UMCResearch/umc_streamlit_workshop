import pandas as pd
import streamlit as st

df = pd.read_csv("2020VAERSDATA.csv", encoding="cp1252", usecols=["VAERS_ID", "SEX", "SYMPTOM_TEXT", "RECVDATE", "NUMDAYS"], parse_dates=['RECVDATE']).dropna()

query = st.text_input('Query', placeholder='Enter a search term')

if query:
    results = df[df['SYMPTOM_TEXT'].str.contains(query)]

    st.write(f"{len(results)} matches out of {len(df)} records")

    st.table(results)