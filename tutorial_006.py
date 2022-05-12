import math
import pandas as pd
import streamlit as st

df = pd.read_csv("2020VAERSData.csv", encoding="cp1252", usecols=["VAERS_ID", "SEX", "SYMPTOM_TEXT", "RECVDATE", "NUMDAYS"], parse_dates=['RECVDATE']).dropna()

query = st.text_input('Query', placeholder='Enter a search term')

if query:
    with st.sidebar:
        n_results_per_page = st.slider('Number of results', min_value=1, max_value=100, value=10)

        results = df[df['SYMPTOM_TEXT'].str.contains(query)]

        n_results = len(results)
        n_pages = math.ceil(n_results / n_results_per_page)
        current_page = st.selectbox("Page", range(n_pages))

        sort_fields = st.multiselect("Sort by", ("VAERS_ID", "SEX", "SYMPTOM_TEXT", "RECVDATE", "NUMDAYS"))
        sort_ascending = st.checkbox('Ascending', True)

    st.write(f"{len(results)} matches out of {len(df)} records")

    start_index = current_page * n_results_per_page
    end_index = start_index + n_results_per_page
    results_page = results.iloc[start_index : end_index]

    st.table(results_page.sort_values(sort_fields, ascending=sort_ascending))