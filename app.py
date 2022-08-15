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
             background: url("https://img.freepik.com/premium-photo/sport-stadium-background-flashing-lights-glowing-stadium-lights_327072-1327.jpg");
             background-size: cover    
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

set_bg_hack_url()

st.title('Fantasy in Your Pocket',)
st.image('http://www.uptheclarets.com/wp-content/uploads/2019/06/fantasy-premier-league-2019-20-banner.jpg',use_column_width=True)
#st.image('Picture1.png')

#Get data from football overload
data = pd.read_csv('http://fantasyoverlord.com/FPL/DataWithForecasts',encoding='iso8859_2')
cols = ['FirstName', 'Surname', 'PositionsList', 'Team', 'Cost','PointsLastRound']

#Top players untile this GW [Total]
cols.append('TotalPoints')
st.header('Top Players in all the fantasy')
st.write(data.sort_values(by=['TotalPoints'],ascending=False,ignore_index=True)[cols].head(50))
cols.remove('TotalPoints')

#Top palyer in the last GW
st.header('Top Players in the Last Weak')
st.write(data.sort_values(by=['PointsLastRound'],ascending=False,ignore_index=True)[cols].head(50))

#Top selected Plyers
cols.append('SelectedByPercent')
st.header('Top Players Selected by Users')
st.write(data.sort_values(by=['SelectedByPercent'],ascending=False,ignore_index=True)[cols].head(50))
cols.remove('SelectedByPercent')

#Top Transfers Out this round
cols.append('TransfersOutRound')
st.header('Top Transfers Out in this round')
st.write(data.sort_values(by=['TransfersOutRound'],ascending=False,ignore_index=True)[cols].head(50))
cols.remove('TransfersOutRound')

#Top Transfers In this round
cols.append('TransfersInRound')
st.header('Top Transfers In in this round')
st.write(data.sort_values(by=['TransfersInRound'],ascending=False,ignore_index=True)[cols].head(50))
cols.remove('TransfersInRound')

#How much a player’s price has increased since the start of the season
cols.append('PriceRise')
st.header('How much a player’s price has increased since the start of the season')
st.write(data.sort_values(by=['PriceRise'],ascending=False,ignore_index=True)[cols].head(50))
cols.remove('PriceRise')

# How much a player’s price has increased this Gameweek.
cols.append('PriceRiseRound')
st.header('How much a player’s price has increased this Gameweek.')
st.write(data.sort_values(by=['PriceRiseRound'],ascending=False,ignore_index=True)[cols].head(50))
cols.remove('PriceRiseRound')

#How much a player’s price has decreased since the start of the season
cols.append('PriceFall')
st.header('How much a player’s price has decreased since the start of the season')
st.write(data.sort_values(by=['PriceFall'],ascending=False,ignore_index=True)[cols].head(50))
cols.remove('PriceFall')

# How much a player’s price has decreased this Gameweek.
cols.append('PriceFallRound')
st.header('How much a player’s price has decreased this Gameweek')
st.write(data.sort_values(by=['PriceFallRound'],ascending=False,ignore_index=True)[cols].head(50))
cols.remove('PriceFallRound')

# Forcasting
st.header('Forcasting The Top Players for the Next Week ')
st.write(data.sort_values(by=[data.columns[(data.columns.get_indexer(['NextFixture5'])+1)][0]],ascending=False,ignore_index=True)[['FirstName','Surname',data.columns[(data.columns.get_indexer(['NextFixture5'])+1)[0]]]].head(50))

#Get the top GK players
st.markdown('Top Players in GKL')
st.write(data[data.PositionsList == 'GLK'].sort_values(by=[data.columns[(data.columns.get_indexer(['NextFixture5'])+1)][0]],ascending=False,ignore_index=True)[['FirstName','Surname','Cost',data.columns[(data.columns.get_indexer(['NextFixture5'])+1)[0]]]].head(20))

#Get top def players
st.markdown('Top Players in DEF')
st.write(data[data.PositionsList == 'DEF'].sort_values(by=[data.columns[(data.columns.get_indexer(['NextFixture5'])+1)][0]],ascending=False,ignore_index=True)[['FirstName','Surname','Cost',data.columns[(data.columns.get_indexer(['NextFixture5'])+1)[0]]]].head(20))

#get top MED players
st.markdown('Top Players in MID')
st.write(data[data.PositionsList == 'MID'].sort_values(by=[data.columns[(data.columns.get_indexer(['NextFixture5'])+1)][0]],ascending=False,ignore_index=True)[['FirstName','Surname','Cost',data.columns[(data.columns.get_indexer(['NextFixture5'])+1)[0]]]].head(20))

#get top ATK players
st.markdown('Top Players in FWD')
st.write(data[data.PositionsList == 'FWD'].sort_values(by=[data.columns[(data.columns.get_indexer(['NextFixture5'])+1)][0]],ascending=False,ignore_index=True)[['FirstName','Surname','Cost',data.columns[(data.columns.get_indexer(['NextFixture5'])+1)[0]]]].head(20))

# Get data for selected players
st.header('Search for Players You Want')
player = st.multiselect("Select playres:",data['Surname'])
if player != []:
    st.write(data[data['Surname'].isin(player)][data.columns[:(data.columns.get_indexer(['NextFixture5'])+2)[0]]].reset_index(drop=True))
