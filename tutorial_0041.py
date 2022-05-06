import pandas as pd
import streamlit as st

df = pd.read_csv("2020VAERSData.csv", encoding="cp1252", usecols=["VAERS_ID", "SEX", "SYMPTOM_TEXT", "RECVDATE", "NUMDAYS"], parse_dates=['RECVDATE']).dropna()

query = st.text_input('Query', placeholder='Enter a search term')

if query:
    num_results = st.slider('Number of results', min_value=1, max_value=100, value=10)
    sort_fields = st.multiselect("Sort by", ("VAERS_ID", "SEX", "SYMPTOM_TEXT", "RECVDATE", "NUMDAYS"))
    sort_ascending = st.checkbox('Ascending', True)

    results = df[df['SYMPTOM_TEXT'].str.contains(query)]

    results_page = results.iloc[0 : num_results]

    st.table(results_page.sort_values(sort_fields, ascending=sort_ascending))