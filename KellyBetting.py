
# coding: utf-8

# In[6]:


import streamlit as st
import numpy as np
import pandas as pd


# In[13]:


st.title('Betting calculator')



def betting_calc(odds,capital):
    prob=1/odds
    bet_amount=((prob*odds-(1-prob))/odds)*capital
    return bet_amount

kurz=st.sidebar.number_input(
    label='Kurz',
    min_value=1.00,
    value=1.00,
    step=0.01,
    format="%.2f")

vklad=st.sidebar.number_input(
    label='Kapital',
    min_value=1.00,
    value=100.00,
    step=0.5,
    format="%.0f")

st.write("Odporucany vklad:", betting_calc(kurz,vklad))

