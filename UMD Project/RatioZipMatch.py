
import geopy
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

match = pd.read_csv('/home/mids/m250024/UMD_Project/ZipMatch.csv')
mismatch = pd.read_csv('/home/mids/m250024/UMD_Project/ZipMismatch.csv')

df = pd.DataFrame({'Zip Code of Crash': ['Inside Local Area', 'Outside Local Area'],
                   'Zip Codes': [int(len(match)),int(len(mismatch))]})


fig = px.pie(df, values='Zip Codes', 
             names='Zip Code of Crash', 
             title='Percentage of Fatal Crashes In vs. Outside of Zipcode',
             color_discrete_sequence=px.colors.sequential.RdBu_r)
fig.update_traces(textposition='inside', textinfo='percent+label')  
#fig = go.Figure(data=[go.Pie(labels= ['Inside Local Area', 'Outside Local Area'], values=[int(len(match)),int(len(mismatch))], pull=[0.2, 0])])                       
                                 
fig.show()