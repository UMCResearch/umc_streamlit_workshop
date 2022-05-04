import math
import pandas as pd
import streamlit as st

df = pd.read_csv("2020VAERSData.csv", encoding="cp1252", usecols=["VAERS_ID", "SEX", "SYMPTOM_TEXT", "RECVDATE", "NUMDAYS"], parse_dates=['RECVDATE']).dropna()

query = st.text_input('Query', placeholder='Enter a search term')

if query:
    results = df[df['SYMPTOM_TEXT'].str.contains(query)]

    with st.sidebar:
        n_results_per_page = st.slider('Number of results', min_value=1, max_value=100, value=10)
        n_results = len(results)
        n_pages = math.ceil(n_results / n_results_per_page)
        current_page = st.selectbox("Page", range(n_pages))

    start_index = current_page * n_results_per_page
    end_index = start_index + n_results_per_page
    results_page = results.iloc[start_index : end_index]

    st.table(results_page)