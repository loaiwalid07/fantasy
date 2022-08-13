'''
Fantasy App

By : Loai Nazeer
Date : 13/08/2022
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import time
import requests
import streamlit as st

#cong the web page
hide_menu ="""
<style>
#MainMenu{
    visibility : hidden;
 }
header{
    visibility : hidden;
 }
.css-z3au9t{
    visibility : hidden;
    content:'';
}

footer:after{
    content: 'Loai Nazeer';

.navbar-brand{
        display:inline;
        font-size: 30px;
}
<style>  
"""

st.set_page_config(page_title='FanEasy',initial_sidebar_state="auto",layout='wide')

#Set the Navbar for the app
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
st.markdown("""
<nav class="navbar fixed-top navbar-dark bg-dark">
  <a class="navbar-brand" href="#">
    <img src="https://cdn.dribbble.com/users/2086807/screenshots/4349700/pl-logo---kavishdesigns.gif" width="80" height="60" class="d-inline-block align-center" " alt="">
    FanEasy
  </a>
</nav>
""", unsafe_allow_html=True)

st.markdown(hide_menu,unsafe_allow_html=True)

#https://i.gifer.com/9lZ7.gif

def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    '''
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://images.pexels.com/photos/399187/pexels-photo-399187.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
             background-size: cover    
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

set_bg_hack_url()

st.title('Fantasy in Your Pocket')
st.image('Picture1.png')

#Get data from football overload
data = pd.read_csv('http://fantasyoverlord.com/FPL/DataWithForecasts',encoding='iso8859_2')

#Top players untile this GW [Total]
st.header('Top Players in all the fantasy')
st.write(data.sort_values(by=['TotalPoints'],ascending=False,ignore_index=True)[data.columns[:(data.columns.get_indexer(['NextFixture5'])+2)[0]]].head(50))

#Top palyer in the last GW
st.header('Top Players in the Last Weak')
st.write(data.sort_values(by=['PointsLastRound'],ascending=False,ignore_index=True)[data.columns[:(data.columns.get_indexer(['NextFixture5'])+2)[0]]].head(50))

#Top selected Plyers
st.header('Top Players Selected by Users')
st.write(data.sort_values(by=['SelectedByPercent'],ascending=False,ignore_index=True)[data.columns[:(data.columns.get_indexer(['NextFixture5'])+2)[0]]].head(50))

# Forcasting
st.header('Forcasting The Top Players for the Next Week ')
st.write(data.sort_values(by=[data.columns[(data.columns.get_indexer(['NextFixture5'])+1)][0]],ascending=False,ignore_index=True)[data.columns[:(data.columns.get_indexer(['NextFixture5'])+2)[0]]].head(50))

# Get data for selected players
st.header('Search for Players You Want')
player = st.multiselect("Select playres:",data['Surname'])
st.write(data[data['Surname'].isin(player)][['FirstName','Surname',data.columns[(data.columns.get_indexer(['NextFixture5'])+1)[0]]]].reset_index(drop=True))