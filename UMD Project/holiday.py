### Finding Amount of crashes during holiday
## Caden Chau

import pandas as pd
import random
import datetime
import plotly.express as px
import numpy as np
#random.seed(261026)

match = pd.read_csv('ZipMatch.csv')
mismatch = pd.read_csv('ZipMismatch.csv')
holiday = pd.read_csv('US Holiday Dates (2004-2021).csv')
holidaytest = pd.read_csv('US Holiday Dates (2004-2021).csv')

match['Date'] = pd.to_datetime(match['crash_dt'], format= '%m/%d/%Y')
mismatch['Date'] = pd.to_datetime(mismatch['crash_dt'], format= '%m/%d/%Y')

holiday['Date'] = pd.to_datetime(holiday['Date'] , format= '%Y-%m-%d')
holiday = holiday[holiday['Date'].dt.year <= 2021]
holiday = holiday[holiday['Date'].dt.year >= 2017]
holiday_date_list = holiday['Date'].to_list()
#print(holiday) 

holidaytest['Date'] = pd.to_datetime(holidaytest['Date'] , format= '%Y-%m-%d')
holidaytest = holidaytest[holidaytest['Date'].dt.year == 2019]
print(holidaytest[["Holiday","Month","Day"]])
#print(holidaytest['Year'].value_counts())  # 19 holidays in a year

holiday = holiday[['Date', 'Holiday']]
#print(holiday)

mismatch_list = mismatch.index.to_list()
mismatch_sample = random.sample(mismatch_list, len(match))
mismatch = mismatch[mismatch.index.isin(mismatch_sample)]


# # Finding any random day during the year
random_date_list = [] 
for year in range(2017, 2022):
#    for day in range(19):
        start_date = datetime.date(year, 1, 1)
        end_date   = datetime.date(year, 12, 31)
        num_days   = (end_date - start_date).days
        rand_days  = random.randint(1, num_days)
        random_date = start_date + datetime.timedelta(days=rand_days)

        while random_date in holiday_date_list:
            start_date = datetime.date(year, 1, 1)
            end_date   = datetime.date(year, 12, 31)
            num_days   = (end_date - start_date).days
            rand_days   = random.randint(1, num_days)
            random_date = start_date + datetime.timedelta(days=rand_days)
            #print('found another date')
        random_date_list.append(pd.Timestamp(random_date))
#print(random_date_list)
random_day = ["Random Day"] * len(random_date_list)

random_date = {'Date': random_date_list, "Holiday": random_day}
random_df = pd.DataFrame(data=random_date)
#print(random_df)
concat = [holiday, random_df]

days_df = pd.concat(concat)
#print(days_df)

match = pd.merge(match, days_df, on='Date', how='left')
mismatch = pd.merge(mismatch, days_df, on='Date', how='left')

match = match[match.Holiday.notnull()]
mismatch = mismatch[mismatch.Holiday.notnull()]

match['Crash in ZIP Code?'] = "Yes"
mismatch['Crash in ZIP Code?'] = "No"


dataframes = [match, mismatch]
comparison = pd.concat(dataframes)
#print(comparison)

fig = px.histogram(comparison, x="Holiday", color="Crash in ZIP Code?", barmode='group', title='Fatal Accidents during Holidays')
fig.update_xaxes(categoryorder='array', categoryarray= ["New Year's Day", 
                                                        'Martin Luther King, Jr. Day', 
                                                        "Valentine’s Day", 
                                                        "Washington's Birthday", 
                                                        'Western Easter', 
                                                        'Eastern Easter', 
                                                        'Memorial Day', 
                                                        'Juneteenth', 
                                                        '4th of July', 
                                                        'Labor Day Weekend', 
                                                        'Labor Day', 
                                                        'Columbus Day', 
                                                        'Veterans Day', 
                                                        'Thanksgiving Eve', 
                                                        'Thanksgiving Day', 
                                                        'Christmas Eve', 
                                                        'Christmas Day', 
                                                        "New Year’s Eve", 
                                                        'Random Day'])
fig.show()