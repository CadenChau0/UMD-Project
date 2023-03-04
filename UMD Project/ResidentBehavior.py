##################################################
# Tanner Kelly

# Create two pie graphs showing the most common crashes 
# between residents andc non resident sof the location in 
# which the fatal crash took place

# Then create a histogram beween the Residence and 
# Non-residence about the time of day in which the 
# fatal crash took place


##################################################
import plotly.express as px
import pandas as pd
from datetime import datetime as dt


residencedf = pd.read_csv("ZipMatch.csv")
nonresidencedf = pd.read_csv("ZipMismatch.csv")

# Quick interlude for proportion of Fatal Crashes in one's own community

x = float(len(residencedf))
y = float(len(nonresidencedf))
z = x + y
ans = x/z
print(f"{round(ans*100,3)}% of crashes took place in the driver's own community.")


# The Pie chart Part

fheventdf = pd.read_csv("fhevent.csv")
fheventdict = fheventdf.set_index("fhevent").to_dict()["Event"]

resscale = residencedf[["fhevent","dzip","z"]]
reslist = resscale["fhevent"].to_list()

rfheventlist = []
for i in reslist:
    rfheventlist.append(fheventdict[i])  
resscale["Event"] = rfheventlist    

nonscale = nonresidencedf[["fhevent","dzip","z"]]
nonlist = nonscale["fhevent"].to_list()

nfheventlist = []
for i in nonlist:
    nfheventlist.append(fheventdict[i])  
nonscale["Event"] = nfheventlist    

rescount = resscale.value_counts("Event").reset_index().head(5)
noncount = nonscale.value_counts("Event").reset_index().head(5)

figresidence = px.pie(rescount, values=0, names='Event', title='Most Common Crashe Type of Residents')
figresidence.show()

fignon = px.pie(noncount, values=0, names='Event', title='Most Common Crashe Type of Non-residents')
fignon.show()


# The Histogram part about time of crash
listresident = ["Resident"]
listresident *= len(residencedf)
residencedf['Community Resident?'] = listresident


listnon = ["Non-Resident"]
listnon *= len(nonresidencedf)
nonresidencedf['Community Resident?'] = listnon

alldf = pd.concat([residencedf, nonresidencedf], axis=0)
hourslist = alldf["crash_tm"].tolist()
hours = []
for i in hourslist:
    try:
        i = str(i)
        if len(i) < 5:
            i = "0" + i
        dto = dt.strptime(i,"%H:%M")
        hr = dto.hour
        hours.append(hr)
    except:
        hours.append("nan")


alldf['Hour'] = hours

fig = px.histogram(alldf,
                   x="Hour",
                   color='Community Resident?',
                   title="Time of Fatal Crashes, Filtered by Driver's Community",
                   color_discrete_map={"Non-Resident":"blue", "Resident": "red"}
)
fig.show()


######
# Pie Chart about the number of crashes which occured inside the drivers own zip code

match = pd.read_csv('/home/mids/m250024/UMD_Project/ZipMatch.csv')
mismatch = pd.read_csv('/home/mids/m250024/UMD_Project/ZipMismatch.csv')

df = pd.DataFrame({'Zip Code of Crash': ["Outside Driver's Community","In Driver's Community"],
                   'Zip Codes': [int(len(mismatch)),int(len(match))]})


fig = px.pie(df, values='Zip Codes', 
             names='Zip Code of Crash', 
             title="Percentage of Fatal Crashes Within a Driver's Own Community",
            )
fig.update_traces(textposition='inside', textinfo='percent+label')  
#fig = go.Figure(data=[go.Pie(labels= ['Inside Local Area', 'Outside Local Area'], values=[int(len(match)),int(len(mismatch))], pull=[0.2, 0])])                       
                                 
fig.show()
