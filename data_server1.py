import streamlit as st
import pandas as pd


st.title('⚙️KeyGold Project')
st.header('Discover Your Market/Micro-niche Profit Points')

# import general_keywords_data.csv to pandas dataframe
general_keywords_data_df = pd.read_csv("general_keywords_data.csv")
st.table(general_keywords_data_df)

