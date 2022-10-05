# importing all modules/ libraries requireed
import os
from platform import platform
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

# getting app root path
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# getting data root folder path
DATA_FOLDER = os.path.join(APP_ROOT, "data\\")

# reading data from csv and storing it in a dataframe df
df = pd.read_csv(DATA_FOLDER + "vg_sales.csv")

# setting up the steamlit page customizing the header and favicon and setting the layout to wide 
st.set_page_config(page_title="Game Sales Dashboard", page_icon=":video_game:", layout="wide") 

## ------------------ CUSTOM STYLES FOR DASHBOARD ------------------------------------ #
# custom css for the app
custom_css = '''
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
'''

# applying above css into the app through markdown by setting allow html to true
st.markdown(custom_css, unsafe_allow_html=True)

## ----------------------- SIDE BAR -------------------------------------------------- #

st.sidebar.header("Apply Filters Here :")

publisher = st.sidebar.selectbox(
    "by Publisher",
    options=df["Publisher"].unique()
)

pltform = st.sidebar.multiselect(
    "by Platform:",
    options=df["Platform"].unique(),
    default=df["Platform"].unique()[2:5]
)

set_all = False
if len(pltform) < 1 :
    set_all = True
    pltform = list(df["Platform"].unique())
    
df_selection = df.query(
    "Publisher == @publisher & Platform == @pltform"
)

## ----------------------- MAIN PAGE ------------------------------------------------ #
st.title(":game_die: Game Sales dashboard") # setting the page title :game_die: is a web emoji available in all browsers
st.markdown("##") # displays the passed string as markdwon

# key performance indicators
total_global_sales = round(df_selection["Global_Sales"].sum(),2)
average_sales = round(df_selection.groupby(["Platform"]).mean()["Global_Sales"].sum(),2)

left_column, right_column = st.columns(2)
with left_column:
    st.subheader("Total Global Sales") if set_all else st.subheader("Global Sales across platforms")
    st.subheader(f"${total_global_sales:,} million")

with right_column:
    st.subheader("Total Average Global Sales") if set_all else st.subheader("Average Global Sales across platform")
    st.subheader(f"${average_sales} million")

st.markdown("""---""")

# print(df.head())

# line graph : year - sales
# bar graph : country wise multibar 
# histogram : year sales (optional)
# piechart : genre based
# 

# print(df.nunique())
# print(df.groupby(["Platform"]).mean()["Global_Sales"].sum())

