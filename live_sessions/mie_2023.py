# write your code here :)

import streamlit as st
import pandas as pd
from collections import Counter
import plotly.express as px

def get_vaers_data() -> pd.DataFrame:
    
    vaers_df = pd.read_csv("2020VAERSDATA.csv", encoding='cp1252', 
                           usecols=['VAERS_ID', 'SYMPTOM_TEXT', 'SEX', 'AGE_YRS']
                )
    
    return vaers_df

def make_sex_plot(df: pd.DataFrame):

    sex_counter = Counter(df['SEX'])
    sex_values = list(sex_counter.keys())
    sex_counts = list(sex_counter.values())
    sex_plot = px.pie(names=sex_values, values=sex_counts)

    return sex_plot

def make_age_plot(df: pd.DataFrame):

    ages_years = list(map(int,df['AGE_YRS'].dropna()))
    age_counter = Counter(ages_years)
    distinct_ages = list(age_counter.keys())
    age_counts = list(age_counter.values())

    return px.bar(x=distinct_ages, y=age_counts)

vaers_df = get_vaers_data()

st.set_page_config(layout='wide')

st.markdown("# MIE workshop 2023")

user_query = st.text_input("Write your query here;")

ages = vaers_df['AGE_YRS'].dropna()
min_age = min(ages)
max_age = max(ages)

age_range = st.slider(
    "Select max/min age", 
    min_value=min_age, 
    max_value=max_age,
    value=(min_age, max_age)
)

st.markdown(f"selected ages were {age_range}")

st.markdown(f"Your query was {user_query}")

st.file_uploader("upload your file")

narratives = vaers_df['SYMPTOM_TEXT'].fillna('')
filtered_data = vaers_df[narratives.str.contains(user_query)]
filtered_data = filtered_data[filtered_data['AGE_YRS'].between(age_range[0], age_range[1])]

sex_plot = make_sex_plot(filtered_data)
ages_plot = make_age_plot(filtered_data)

st.plotly_chart(sex_plot)
st.plotly_chart(ages_plot)
st.markdown(f'## {len(filtered_data)}/{len(vaers_df)} narratives matched the search')
st.table(filtered_data)