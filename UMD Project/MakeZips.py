
import geopy
import pandas as pd


# Source dataframe
df_Survey = pd.read_csv("/home/mids/m250024/UMD_Project/Data_Washington Fatal Crash Survey.csv")
df_Survey_XY = df_Survey[["y", "x"]]
lst_lat = df_Survey_XY['y']
lst_lon = df_Survey_XY['x']
print(df_Survey_XY)

n = 10
df_Survey10 = df_Survey.iloc[:n]


def get_zipcode(df, geolocator, lat_field, lon_field):
    
    location = geolocator.reverse((df[lat_field], df[lon_field]))
    dict_add = location.raw['address']
    
    try:
        return dict_add['postcode']
    except:
        print('error')
        return 00000
   


geolocator = geopy.Nominatim(user_agent='Determine zip from Lon,Lat coordinates for a UMD Info Challenge, m250024@usna.edu')

df = pd.DataFrame({
    'Lat': lst_lat,
    'Lon': lst_lon})
zipcodes = df.apply(get_zipcode, axis=1, geolocator=geolocator, lat_field='Lat', lon_field='Lon')

#zipcodes.to_csv('ZipsFile.csv')

#print(zipcodes)
#print(df_Survey10)

merging = df_Survey.merge(zipcodes.rename('z'), left_index=True,right_index=True)

print(merging)
merging.to_csv('/home/mids/m250024/UMD_Project/ZipsFile.csv')
