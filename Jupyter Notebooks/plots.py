import streamlit as st
import pandas as pd
import numpy as np

import plotly.graph_objs as go
import matplotlib.pyplot as plt


__all__ = ["collect_traces", 
           "create_layout"]

# Burn in Plots

def collect_traces(df, list_of_column_names, type_of_plot, color_dict=None):
    '''
    Parameters
    ----------
    df : pd.DataFrame
        Simulation output.
    list_of_column_names : list
        List with columns names (e.g., ["KPI-1", "KPI-2"])
    type_of_plot : str
        Either "Scatter" or "Bar".
    color_dict : dictionary
        Dict with keys:values as KPI:plotting-color
    Returns
    -------
    data : list
        List with plotly trace objects
    '''
    x = df.index.values
    data = []
    
    for kpi in list_of_column_names:
        if color_dict == None:
            trace = go.Bar(
                x = x,
                y = df[kpi],
                name = kpi, # for legend
                marker_line_width = 0.1,
                opacity = 0.95,
                text = kpi)
        else:
            trace = go.Bar(
                x = x,
                y = df[kpi],
                name = kpi, # for legend
                marker_color = color_dict[kpi],
                marker_line_width = 0.1,
                opacity = 0.95,
                text = kpi)
        data.append(trace)
    
    return data
    
def create_layout(x_axis_title, y_axis_title, barmode = None):
    '''
    Parameters
    ----------
    x_axis_title : str
    y_axis_title : str
        
    Returns
    -------
    layout : plotly.graph_objects.go.Layout
    '''
    layout = go.Layout(
        xaxis = dict(title=x_axis_title, tick0 = 0, dtick = 10, zeroline=True, ticks="inside"),
        yaxis = dict(title=y_axis_title,tick0 = 0,zeroline=False, ticks = "inside"),
        showlegend = True, 
        legend = dict(traceorder='normal', orientation='h', yanchor='bottom', xanchor='center', y=1.002, x=0.5, font=dict(size=12)),
        barmode = barmode
    )
    
    return layout