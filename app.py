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
import plotly.graph_objects as go

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

st.set_page_config(page_title='FanEasy',initial_sidebar_state="expanded",layout='wide')

#Set the Navbar for the app
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

# st.sidebar.markdown("""
# <div class="row">
#   <div class="col-3">
#     <div class="nav flex-column nav-pills" id="v-pills-tab" role="tablist" aria-orientation="vertical">
#       <a class="nav-link active" id="v-pills-home-tab" data-toggle="pill" href="#v-pills-home" role="tab" aria-controls="v-pills-home" aria-selected="true">Home</a>
#       <a class="nav-link" id="v-pills-profile-tab" data-toggle="pill" href="#how-much-a-player-s-price-has-increased-since-the-start-of-the-season" role="tab" aria-controls="v-pills-profile" aria-selected="false">Profile</a>
#       <a class="nav-link" id="v-pills-messages-tab" data-toggle="pill" href="#v-pills-messages" role="tab" aria-controls="v-pills-messages" aria-selected="false">Messages</a>
#       <a class="nav-link" id="v-pills-settings-tab" data-toggle="pill" href="#v-pills-settings" role="tab" aria-controls="v-pills-settings" aria-selected="false">Settings</a>
#     </div>
#   </div>
# </div>
#     """, unsafe_allow_html=True)

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

#Get data from football overload
data_over = pd.read_csv('http://fantasyoverlord.com/FPL/DataWithForecasts',encoding='iso8859_2')

#Import data from FPL API
url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
url_fix = 'https://fantasy.premierleague.com/api/fixtures/?future=1'
r_fixture = requests.get(url_fix)
fixture_json = r_fixture.json()
r = requests.get(url)
data_json = r.json()
elements_df = pd.DataFrame(data_json['elements'])
elements_types_df = pd.DataFrame(data_json['element_types'])
teams_df = pd.DataFrame(data_json['teams'])
fixture_df = pd.DataFrame(fixture_json)

data = elements_df[['first_name','second_name','team','element_type','selected_by_percent','now_cost','minutes','transfers_in','value_season','event_points','total_points',
'dreamteam_count','form','transfers_in_event', 'transfers_out', 'transfers_out_event','value_form','goals_scored','assists', 'clean_sheets','cost_change_event',
'cost_change_event_fall', 'cost_change_start','cost_change_start_fall','goals_conceded', 'own_goals','penalties_saved', 'penalties_missed', 'yellow_cards',
'red_cards','saves', 'bonus', 'bps','ict_index']]
data['position'] = data.element_type.map(elements_types_df.set_index('id').singular_name)
data['element_type'] = data['position']
data['team'] = data.team.map(teams_df.set_index('id').name)
data['value'] = data.value_season.astype(float)
data['ict_index'] = data.ict_index.astype(float)
data['selected_by_percent'] = data.selected_by_percent.astype(float)


#cols = ['FirstName', 'Surname', 'PositionsList', 'Team', 'Cost','PointsLastRound']
cols = ['first_name','second_name', 'position', 'team', 'now_cost','event_points']

#Top players untile this GW [Total]
cols.append('total_points')
st.header('Top Players in all the fantasy')
st.write(data.sort_values(by=['total_points'],ascending=False,ignore_index=True)[cols].head(50))
cols.remove('total_points')

#Top palyer in the last GW
st.header('Top Players in the Last Weak')
st.write(data.sort_values(by=['event_points'],ascending=False,ignore_index=True)[cols].head(50))

#Top selected Plyers
cols.append('selected_by_percent')
st.header('Top Players Selected by Users')
st.write(data.sort_values(by=['selected_by_percent'],ascending=False,ignore_index=True)[cols].head(50))
cols.remove('selected_by_percent')

#Top Transfers Out this round
cols.append('transfers_out_event')
st.header('Top Transfers Out in this round')
st.write(data.sort_values(by=['transfers_out_event'],ascending=False,ignore_index=True)[cols].head(50))
cols.remove('transfers_out_event')

#Top Transfers In this round
cols.append('transfers_in_event')
st.header('Top Transfers In in this round')
st.write(data.sort_values(by=['transfers_in_event'],ascending=False,ignore_index=True)[cols].head(50))
cols.remove('transfers_in_event')

#Top ICTIndex players
cols.append('ict_index')
st.header('Top ICT Index players')
st.write(data.sort_values(by=['ict_index'],ascending=False,ignore_index=True)[cols].head(50))
cols.remove('ict_index')


#How much a player’s price has increased since the start of the season
cols.append('cost_change_start')
st.header('How much a player’s price has increased since the start of the season')
st.write(data.sort_values(by=['cost_change_start'],ascending=False,ignore_index=True)[cols].head(50))
cols.remove('cost_change_start')

# How much a player’s price has increased this Gameweek.
cols.append('cost_change_event')
st.header('How much a player’s price has increased this Gameweek.')
st.write(data.sort_values(by=['cost_change_event'],ascending=False,ignore_index=True)[cols].head(50))
cols.remove('cost_change_event')

#How much a player’s price has decreased since the start of the season
cols.append('cost_change_start_fall')
st.header('How much a player’s price has decreased since the start of the season')
st.write(data.sort_values(by=['cost_change_start_fall'],ascending=False,ignore_index=True)[cols].head(50))
cols.remove('cost_change_start_fall')

# How much a player’s price has decreased this Gameweek.
cols.append('cost_change_event_fall')
st.header('How much a player’s price has decreased this Gameweek')
st.write(data.sort_values(by=['cost_change_event_fall'],ascending=False,ignore_index=True)[cols].head(50))
cols.remove('cost_change_event_fall')

# Forcasting
st.header('Forcasting The Top Players for the Next Week ')
st.write(data_over.sort_values(by=[data_over.columns[(data_over.columns.get_indexer(['NextFixture5'])+1)][0]],ascending=False,ignore_index=True)[['FirstName','Surname',data_over.columns[(data_over.columns.get_indexer(['NextFixture5'])+1)[0]]]].head(50))

#Get the top GK players
st.markdown('Top Players in GKL')
st.write(data_over[data_over.PositionsList == 'GLK'].sort_values(by=[data_over.columns[(data_over.columns.get_indexer(['NextFixture5'])+1)][0]],ascending=False,ignore_index=True)[['FirstName','Surname','Cost',data_over.columns[(data_over.columns.get_indexer(['NextFixture5'])+1)[0]]]].head(20))

#Get top def players
st.markdown('Top Players in DEF')
st.write(data_over[data_over.PositionsList == 'DEF'].sort_values(by=[data_over.columns[(data_over.columns.get_indexer(['NextFixture5'])+1)][0]],ascending=False,ignore_index=True)[['FirstName','Surname','Cost',data_over.columns[(data_over.columns.get_indexer(['NextFixture5'])+1)[0]]]].head(20))

#get top MED players
st.markdown('Top Players in MID')
st.write(data_over[data_over.PositionsList == 'MID'].sort_values(by=[data_over.columns[(data_over.columns.get_indexer(['NextFixture5'])+1)][0]],ascending=False,ignore_index=True)[['FirstName','Surname','Cost',data_over.columns[(data_over.columns.get_indexer(['NextFixture5'])+1)[0]]]].head(20))

#get top ATK players
st.markdown('Top Players in FWD')
st.write(data_over[data_over.PositionsList == 'FWD'].sort_values(by=[data_over.columns[(data_over.columns.get_indexer(['NextFixture5'])+1)][0]],ascending=False,ignore_index=True)[['FirstName','Surname','Cost',data_over.columns[(data_over.columns.get_indexer(['NextFixture5'])+1)[0]]]].head(20))

# Get data for selected players
#[data.columns[:(data.columns.get_indexer(['NextFixture5'])+2)[0]]]
st.header('Search for Players You Want')
player = st.multiselect("Select playres:",data['second_name'])
if player != []:
    st.write(data[data['second_name'].isin(player)].reset_index(drop=True))

#Plot comparson between fixtures
st.header('Fixtures Analysis')
for i in range(len(fixture_df.iloc[:10])):
    labels = ['Overall','Attack','Defence']
    
    h_name = teams_df['name'][teams_df['id'] == fixture_df['team_h'].iloc[i]].values[0]
    a_name = teams_df['name'][teams_df['id'] == fixture_df['team_a'].iloc[i]].values[0]
    
    h = [teams_df['strength_overall_home'][teams_df['id'] == fixture_df.team_h.iloc[i]].values[0],
    teams_df['strength_attack_home'][teams_df['id'] == fixture_df.team_h.iloc[i]].values[0],teams_df['strength_defence_home'][teams_df['id'] == fixture_df.team_h.iloc[i]].values[0]]

    a = [teams_df['strength_overall_away'][teams_df['id'] == fixture_df.team_a.iloc[i]].values[0],
    teams_df['strength_attack_away'][teams_df['id'] == fixture_df.team_a.iloc[i]].values[0],teams_df['strength_defence_away'][teams_df['id'] == fixture_df.team_a.iloc[i]].values[0]]

    fig = go.Figure(data=[
        go.Bar(name=h_name, x=labels, y=h),
        go.Bar(name=a_name, x=labels, y=a)
    ])
    # Change the bar mode
    fig.update_layout(barmode='group',title_text= h_name+' VS '+a_name )
    st.write(fig)

#Get the top selected players by top 100
st.header('Top Selected Players by Top 100 Users in the Fantasy')
# Get id for top # in the overall legue
def top_users(num):
    l =int(num / 50)
    lege_df = pd.DataFrame()
    for i in range(1,l):
        leg_url = 'https://fantasy.premierleague.com/api/leagues-classic/314/standings/?page_new_entries=1&page_standings='+str(i)
        r_lege = requests.get(leg_url)
        lege_json = r_lege.json()
        lege_df = lege_df.append(pd.DataFrame(lege_json['standings']['results']),ignore_index=True)
    return lege_df

top_100 = top_users(100)

def top_picks(user_id):
    players = []
    for i in user_id:
        pick_url = 'https://fantasy.premierleague.com/api/entry/'+str(i)+'/event/2/picks/'
        rr = requests.get(pick_url)
        pick_json = rr.json()
        p_df = pd.DataFrame(pick_json['picks'])
        p_df['element'] = p_df.element.map(elements_df.set_index('id').second_name)
        for j in range(15):
            players.append(p_df['element'].values[j])
    df_playesr = pd.DataFrame([players])
    return df_playesr

pk_100 = top_picks(top_100['entry'])
ply_val = dict(pk_100.T.value_counts(normalize=True)*100)
ply_df = pd.DataFrame(data=ply_val,index=['Precentage'])
st.write(ply_df.T.head(50))



