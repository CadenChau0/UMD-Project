
from geopy import *
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from geopandas import *
#from pyshp import *
from shapely import *
import numpy as np

match = pd.read_csv('/home/mids/m250024/UMD_Project/ZipMatch.csv')
mismatch = pd.read_csv('/home/mids/m250024/UMD_Project/ZipMismatch.csv')
full = pd.read_csv('/home/mids/m250024/UMD_Project/ZipsFile.csv')


top10commonm= full['z'].value_counts()[1:11].index.tolist()
#print(top10commonm)
d_match = {}
for i in top10commonm:
    d_match[i] = match['z'].value_counts()[i]
print(d_match) # top 10 most fatal crash zips in local area and num of crashes 
d_mismatch = {}
for i in top10commonm:
    d_mismatch[i] = mismatch['z'].value_counts()[i]
print(d_mismatch) # top 10 most fatal crash zips out of local area and num of crashes 

# for zip with the most out of local area crashes, most common zipcode to crash there
top10OutOfArea = mismatch['z'].iloc[:10].tolist()
#print(top10OutOfArea)
d_mismatchCommonDriverZips = {}
for i in top10OutOfArea:
    top10DriversOutOfArea = mismatch[mismatch['z']==i]['dzip']
    
    print(top10DriversOutOfArea)



d_mismatchCommonDriverZips = {}
for i in top10OutOfArea:
    d_mismatchCommonDriverZips[i] = mismatch['z'].value_counts()[i]
print(d_mismatchCommonDriverZips) # for zip with the most out of local area crashes, most common zipcode to crash there

if False:

    top10m = []

    top10match = match['z'].value_counts()[:10].index.tolist()
    #print(match)
    top10county = match[match['z'].isin(top10match)]['co_char'].unique()
    print(top10county)
    for item in top10county:
        print(item)
    for item in top10match:
        itme = str(item)
        top10m.append(itme)

    top10match_val= match['z'].value_counts()[:10].tolist()
    #print(top10match_val)
    #print(top10m)

    top10mismatch = mismatch['z'].value_counts()[:10].index.tolist()

    #['99301', '98951', '98584', '98022', '98944', '98532', '98277', '98837', '98632', '98579']

    fips = ['53021']
    values = [24] #22, 14, 13, 12, 11, 10, 10, 9, 9]

    #fig = ff.create_choropleth(fips=fips, values=values)
    #fig.layout.template = None
    #fig.show()

    fips = ['06021', '06023', '06027',
            '06029', '06033', '06059',
            '06047', '06049', '06051',
            '06055', '06061']
    values = range(len(fips))

    fig = ff.create_choropleth(fips=fips, values=values)
    fig.layout.template = None
    fig.show()
