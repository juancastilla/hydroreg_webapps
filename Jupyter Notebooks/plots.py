import streamlit as st
import pandas as pd
import numpy as np

import plotly.graph_objs as go
import matplotlib.pyplot as plt


__all__ = ["collect_traces"]

# Burn in Plots


def collect_traces(df, list_of_column_names, type_of_plot):
    '''
    Parameters
    ----------
    df : pd.DataFrame
        Simulation output.
    list_of_column_names : list
        List with columns names (e.g., ["KPI-1", "KPI-2"])
    type_of_plot : str
        Either "Scatter" or "Bar".
    '''
    x = df.index.values
    data = []
    
    for kpi in list_of_columns_names:
        trace = go.Bar(
            x = x,
            y = df[kpi],
            name = kpi, # for legend
            #marker_color = "purple",
            marker_line_width = 0.1,
            opacity = 0.95,
            text = kpi)
        data.append(trace)
    
    return data
    
