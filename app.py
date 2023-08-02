# Libraries
import pandas as pd 
import plotly.express as px 
import streamlit as st


st.set_page_config(page_title="Partner calls",
                   page_icon=":bar_chart:",
                   layout='wide')


#read data 
df = pd.read_csv("Datos.csv",sep=";")


# sidebar to gather the user's filter 

st.sidebar.header("Please Filter Here:")

month = st.sidebar.multiselect(
    "Select the Month: ",
    options = df["Month"].unique(),
    default=df["Month"].unique()
)

task = st.sidebar.multiselect(
    "Select the Task: ",
    options = df["Task"].unique(),
    default = df["Task"].unique()
)

billable = st.sidebar.multiselect(
    "Billable: ",
    options = df["Billable"].unique(),
    default=df["Billable"].unique()
)

df_selection = df.query(
    "Month == @month & Task == @task & Billable == @billable"
)


# plotting dataframe
st.dataframe(df_selection)
