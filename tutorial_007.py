import math
import pandas as pd
import streamlit as st
import altair as alt

df = pd.read_csv("2020VAERSData.csv", encoding="cp1252", usecols=["VAERS_ID", "SEX", "SYMPTOM_TEXT", "RECVDATE", "NUMDAYS"], parse_dates=['RECVDATE']).dropna()

query = st.text_input('Query', placeholder='Enter a search term')

if query:
    results = df[df['SYMPTOM_TEXT'].str.contains(query)]

    with st.sidebar:
        n_results_per_page = st.slider('Number of results', min_value=1, max_value=100, value=10)
        n_results = len(results)
        n_pages = math.ceil(n_results / n_results_per_page)
        current_page = st.selectbox("Page", range(n_pages))

    st.write(f"{len(results)} matches out of {len(df)} records")

    start_index = current_page * n_results_per_page
    end_index = start_index + n_results_per_page
    results_page = results.iloc[start_index : end_index]

    col1, col2 = st.columns(2)
    
    chart1 = alt.Chart(results).mark_arc().encode(
        theta=alt.Theta('count(SEX)', stack=True),
        color='SEX',
        tooltip=["count(SEX)"]
    )
    
    col1.altair_chart(chart1, use_container_width=True)

    chart2 = alt.Chart(results).mark_bar().encode(
        x=alt.X('NUMDAYS', scale=alt.Scale(domain=[0, 100])),
        y='count()',
        tooltip=['count()']
    ).interactive()
    col2.altair_chart(chart2, use_container_width=True)

    chart3 = alt.Chart(results).mark_bar().encode(x='RECVDATE', y='count()', tooltip=['count()'])
    st.altair_chart(chart3, use_container_width=True)

    st.table(results_page)