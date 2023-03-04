import pandas as pd
import plotly.express as px
import numpy as np


#Histogram for age in home area
m = pd.read_csv("ZipMatch.csv")
m = m[["case","age","z","intersectiontype","make"]]
#print(m.z.value_counts())
m = m.loc[(m["z"]== 99301) | (m["z"]== 98951) | (m["z"]== 98584) | (m["z"]== 98022) | (m["z"]== 98944)] 
m['age_bins'] = pd.cut(x=m['age'], bins=[10, 19, 29, 39, 49, 59, 69, 79, 89])
m['age_by_decade'] = pd.cut(x=m['age'], bins=[10, 19, 29, 39, 49, 59, 69, 79, 89], labels=['10s', '20s', '30s', '40s', '50s', '60s', '70s', '80s'])
#print(m)
#print(m.age.value_counts())
fig = px.histogram(m, x= "z", color = "age_by_decade", barmode = "group", title = "Age Demographics-For Fatalities Occuring Inside of Residential Zipcode", labels = {"z":"Zipcodes"}, category_orders= {"age_by_decade": ["10s","20s","30s","40s","50s","60s","70s","80s"]})
fig.update_layout(yaxis_title_text='Number of People Per Age Group') 
fig.update_xaxes(type='category')
#fig.show()

#Histogram for age outside of home area
mis = pd.read_csv("ZipMismatch.csv")
mis = mis[["case","age","z","intersectiontype","make"]]
mis = mis[mis.age != 999]
mis = mis[mis.age != 998]
#print(mis.z.value_counts()) 
mis = mis.loc[(mis["z"]== 98951) | (mis["z"]== 98032) | (mis["z"]== 98188) | (mis["z"]== 98424) | (mis["z"]== 98408)] 
mis['age_bins'] = pd.cut(x=mis['age'], bins=[10, 19, 29, 39, 49, 59, 69, 79, 89, 99])
mis['age_by_decade'] = pd.cut(x=mis['age'], bins=[10, 19, 29, 39, 49, 59, 69, 79, 89], labels=['10s', '20s', '30s', '40s', '50s', '60s', '70s', '80s'])
#print(mis)
#print(mis.age.value_counts())
fig = px.histogram(mis, x= "z", color = "age_by_decade", barmode = "group", title = "Age Demographics-For Fatalities Occuring Outside of Residential Zipcode", labels = {"z":"Zipcodes"}, category_orders= {"age_by_decade": ["10s","20s","30s","40s","50s","60s","70s","80s"]})
fig.update_layout(yaxis_title_text='Number of People Per Age Group')
fig.update_xaxes(type='category')
#fig.show()



#Histogram for most common intersection involved in crashes in home area
interm = pd.read_csv("ZipMatch.csv")
hinter = pd.read_csv('intersectiontype.csv')
hinter = pd.merge(interm,hinter,on='intersectiontype')
#print(hinter.z.value_counts())
hinter = hinter.loc[(hinter["z"]== 99301) | (hinter["z"]== 98951) | (hinter["z"]== 98584) | (hinter["z"]== 98022) | (hinter["z"]== 98944)] 
#print(hinter.intersectiontype.value_counts())
fig = px.histogram(hinter, x= "z", color = "type", barmode = "group", title = "Intersection Type Demographics-For Number of Fatalities Occuring Inside of Residential Zipcode", labels = {"z":"Zipcodes"})
fig.update_layout(yaxis_title_text='Number of Each Intersection Type')
fig.update_xaxes(type='category')
#fig.show()

#Histogram for most common intersection involved in crashes outside of home area
intermis = pd.read_csv("ZipMismatch.csv")
ainter = pd.read_csv('intersectiontype.csv')
ainter = pd.merge(intermis,ainter,on='intersectiontype')
#print(ainter.z.value_counts())
ainter = ainter.loc[(ainter["z"]== 98951) | (ainter["z"]== 98032) | (ainter["z"]== 98188) | (ainter["z"]== 98408) | (ainter["z"]== 98424)] 
#print(ainter.intersectiontype.value_counts())
fig = px.histogram(ainter, x= "z", color = "type", barmode = "group", title = "Intersection Type Demographics-For Number of Fatalities Occuring Outside of Residential Zipcode", labels = {"z":"Zipcodes"} )
fig.update_layout(yaxis_title_text='Number of Each Intersection Type')
fig.update_xaxes(type='category')
#fig.show()



#Histogram for top car makes shown in fatal accidents occuring in vistims home zipcode
makem = pd.read_csv("ZipMatch.csv")
hmake = pd.read_csv('/home/mids/m250024/UMD_Project/carmake.csv')
hmake = pd.merge(makem,hmake,on='make')
#print(hmake.z.value_counts())
hmake = hmake.loc[(hmake["z"]== 99301) | (hmake["z"]== 98951) | (hmake["z"]== 98584) | (hmake["z"]== 98022) | (hmake["z"]== 98944)] 
#print(hmake.brand.value_counts())
hmake = hmake.loc[(hmake["brand"]== 'Ford') | (hmake["brand"]== 'Chevrolet') | (hmake["brand"]== 'Dodge') | (hmake["brand"]== 'Honda') | (hmake["brand"]== 'Toyota') | (hmake["brand"]== 'Subaru') | (hmake["brand"]== 'Datsun/Nissan')]
fig = px.histogram(hmake, x= "z", color = "brand", barmode = "group", title = "Car Brand Demographics-For Number of Fatalities Occuring Inside of Residential Zipcode", labels = {"z":"Zipcodes"},)
fig.update_layout(yaxis_title_text='Number of Each Car Brand')
fig.update_xaxes(type='category')
#fig.show()

#Histogram for top car makes shown in fatal accidents occuring outside victims home zipcode
makemis = pd.read_csv("ZipMismatch.csv")
amake = pd.read_csv('/home/mids/m250024/UMD_Project/carmake.csv')
amake = pd.merge(makemis,amake,on='make')
#print(amake.z.value_counts())
amake = amake.loc[(amake["z"]== 98951) | (amake["z"]== 98032) | (amake["z"]== 98188) | (amake["z"]== 98408) | (amake["z"]== 98424)] 
#print(amake.brand.value_counts())
amake = amake.loc[(amake["brand"]== 'Ford') | (amake["brand"]== 'Chevrolet') | (amake["brand"]== 'Honda') | (amake["brand"]== 'Toyota') | (amake["brand"]== 'Datsun/Nissan')]
fig = px.histogram(amake, x= "z", color = "brand", barmode = "group", title = "Car Brand Demographics-For Number of Fatalities Occuring Outside of Residential Zipcode", labels = {"z":"Zipcodes"},)
fig.update_layout(yaxis_title_text='Number of Each Car Brand')
fig.update_xaxes(type='category')
#fig.show()