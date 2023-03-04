import pandas as pd
#import geopy as gpy
#import geopandas as gpa
#import folium
import numpy as np
import matplotlib.pyplot as plt
#from geopy.geocoders import Nominatim

csv = pd.read_csv("/home/mids/m250024/UMD_Project/Data_Washington Fatal Crash Survey.csv")

location_csv = csv[["case","x","y","county","co_char","city","trafid1","trafid2"]]
location_csv.to_csv("/home/mids/m250024/UMD_Project/Locations.csv", index=False)

case_info_csv = csv[["case","year","par","repjur"]]
case_info_csv.to_csv("/home/mids/m250024/UMD_Project/Case Info.csv", index=False)

crash_info = csv[["case","crash_dt","crash_tm","numfatal","crashtype"]]
crash_info.to_csv("/home/mids/m250024/UMD_Project/Crash Info.csv", index=False)

car_info = csv[["case","body","trailer","make","model","modelyr"]]
car_info.to_csv("/home/mids/m250024/UMD_Project/Car Info.csv", index=False)

People_info = csv[["case","age","sex","hispanic","race1","race2","race3","race4","race5","dzip","licstate","drhgt_in","weight","noncdl","noncdltype"]]
People_info.to_csv("/home/mids/m250024/UMD_Project/People Info.csv", index=False)