import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

#Display text
st.text("We are IT@FITM")
#Display markdown
st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown(''' # Display string formatted as Markdown.
:red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
:gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
st.markdown("Here's a bouquet &mdash;\
:tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

# success
st.success("Success")
# info
st.info("Information")
# warning
st.warning("Warning")
# error
st.error("Error")
# Exception -This has been added later
exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)