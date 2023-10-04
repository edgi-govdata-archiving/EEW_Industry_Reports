import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="First streamlit sprint!!")

def intro():
    st.markdown(f'# {list(page_name_to_funcs.keys())[0]}')
    st.title(":)")
    st.write("Dear friends,")
    "My name is Selena. I am a sophomore in the College of Arts and Sciences studying a little bit of everything at this point. In my free" \
    "time, I enjoy going on foodie adventures and playing video games. I also really like cats, even though I have a pet dog." \
    " Hack is awesome."

    data = pd.read_csv("/Users/sese/Desktop/H4I_EEW_Industry_Reports/state_counties_corrected.csv")
    st.dataframe(data, column_order=("FAC_STATE", "FAC_COUNTY"))

    st.sidebar.success("woo")

def demoChart():

    st.markdown(f'# {list(page_name_to_funcs.keys())[1]}')


    data = pd.read_csv("/Users/sese/Desktop/H4I_EEW_Industry_Reports/state_counties_corrected.csv")
    st.dataframe(data)


page_name_to_funcs = {
    "-": intro,
    "Full Chart": demoChart
}

demo_name = st.sidebar.selectbox("Choose a demo", page_name_to_funcs.keys())
page_name_to_funcs[demo_name]()