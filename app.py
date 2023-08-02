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
#st.dataframe(df_selection)

df_selection.describe()


# -------MAINPAGE----------

st.title(":bar_chart: Partner dashboard")
st.markdown("##")


df_selection['Lead Price Total'] = df_selection['Lead Price Total'].str.replace('$', '')
total_lead_price = df_selection["Lead Price Total"].sum()

total_billable_leads = df_selection["Billable"].value_counts()['Yes']

print(total_lead_price)


left_column, right_column = st.columns(2)

with left_column:
    st.subheader("Total Sales:")
    st.subheader(f"US $ {total_lead_price:,}")
with right_column:
    st.subheader("Total Billable lead:")
    st.subheader(f" # {total_billable_leads}")


st.markdown("---")

