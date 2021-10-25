#### IMPORTS
import pandas as pd
import numpy as np
import os

import plotly.graph_objs as go
import matplotlib.pyplot as plt
from plotly.offline import plot

import streamlit as st
import streamlit.components.v1 as components


#### GENERAL CONFIGURATION
stdir = os.getcwd()   # App dir

# Page config:
st.set_page_config(page_title="NRAR Data Visualisation",   # Title shown in the browser tab
                   page_icon=":corn:",
                   layout='wide',                          # Wide layout
                   initial_sidebar_state='auto')

# Title of the App:
st.title('NRAR ---')

# Sidebar:
st.sidebar.title('NRAR Web Apps')

selection = st.sidebar.radio("Go to",['Home','Experiment - Penalties','Trade-Off Analysis','About'])

st.sidebar.title('About')

st.sidebar.info("NRAR's interdisciplinary behavioural and cost optimisation model: A collection of Streamlit web apps for data analysis, data visualisation and exploratory modelling")



#### MAIN PAGE:

if selection == "Home":
    # Instructions for users
    st.markdown("""bla bla""")
    


elif selection == 'Experiment - Penalties':
    # Instructions:
    st.markdown('''
    This experiments aims to test the effect of penalties by increasing fines' amount and frequency.
    The base situation characterises a basin composed of 500 farmers who display an average compliance level between 30%-50%. NRAR's activity in the basin is characterized by an average of 4% routine inspections, leading to a "perceived compliance" (i.e., by NRAR) of about X%.
    Scenario parameters include:
    1. Fine Amount: Between 1.000AUD and 100.000AUD
    2. Audit Frequency: We consider an increase of the overall audit activity at the basin x2 and x3.
    3. Water Restriction: To acknowledge hydrological conditions, we test results across 3 separate scenarios (good, moderate, bad).
    ''')
    
    # Load Data:
    @st.cache
    def load_data():
        '''
        Loads all CSV files located in a folder called "Exp - Penalties".
        Returns a tuple with all the dataframes.
        '''
        exp_folder_path = os.path.join(os.path.dirname(os.getcwd()), "data", "Exp - Penalties")
        files = [f for f in os.listdir(exp_folder_path) if os.path.isfile(os.path.join(exp_folder_path, f))]
        dfs = []
        for f in files:
            dfs.append(pd.read_csv(os.path.join(exp_folder_path, f), index_col = 0))
        dfs = tuple(dfs)
        print("all ok")
        return dfs
    
    data_load_state = st.text('Loading data...')
    dfs = load_data()
    data_load_state.text('Loading data done! (Using st.cache)') 
    st.text(str(len(dfs)) + " files loaded")
    
    # Show burn in for validation purposes:
    if st.checkbox('Show Scenario Setup (Burn-in)'):
        st.text("Overall Compliance level")
        
        # Creating 2 columns:
        col1, col2 = st.columns(2)
        
        # First check the overall compliance level reached:
        with col1:
            res = dfs[0].loc[:, ["KPI-total-investigations", "KPI-total-audits"]]
            data = []
            trace = go.Bar(
                x = res.index.values,
                y = res["KPI-total-investigations"],
                name = "KPI-total-investigations", # for legend
                #marker_color = "purple",
                marker_line_width = 0.1,
                opacity = 0.95,
                text = "KPI-total-investigations")
            data.append(trace)
        
        #use_container_width=True)
        st.text("NRAR's activity")
    
    choice = st.selectbox("Select metric to analyze:", ["Farmers Real Compliance", "NRAR's activity"])
    
    if choice == "Farmers Real Compliance":
        
        # Plot:
        res = dfs[0].loc[:, ["KPI-farmers-compliance"]]
        data = []
        trace = go.Bar(
            x = res.index.values,
            y = res["KPI-farmers-compliance"],
            name = "KPI-farmers-compliance", # for legend
            #marker_color = "purple",
            marker_line_width = 0.1,
            opacity = 0.95,
            text = "KPI-farmers-compliance")
        data.append(trace)
        
        # DEFINE LAYOUT
        layout = go.Layout(width= 1000, height= 600, 
                           xaxis= dict(title= '<b>Simulation Time (weeks)<b>', tick0 = 0, dtick = 10, zeroline=True, ticks="inside"),
                           yaxis= dict(title= '<b>Farmers<b>',tick0 = 0,zeroline=False, ticks = "inside"),
                           showlegend = True, legend=dict(traceorder='normal',orientation='h',yanchor='bottom',xanchor='center',y=1.002,x=0.5,font=dict(size=12)),
                           annotations=[dict(x=0.5,y=1.12,align="right",valign="top",text='<b>Legend<b>',font=dict(size=15),showarrow=False,xref="paper",yref="paper",xanchor="center",yanchor="top")])
        
        # CREATE FIGURE
        fig = go.Figure(data = data, layout = layout)
        
        # PLOT FIGURE
        st.plotly_chart(fig)
        

#if st.checkbox('Show raw data'):
#    st.subheader('Raw data')
#    st.write(data)
#
#st.subheader('Number of pickups by hour')
#hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
#st.bar_chart(hist_values)
#
#
#hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
#filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
#st.subheader(f'Map of all pickups at {hour_to_filter}:00')
#st.map(filtered_data)


