import pandas as pd

people_info = pd.read_csv("People Info.csv")

zip_codes = pd.read_csv("US20Codes20201320Data.csv")

zip_codes_header = {'ZIP': 'zip','LAT': 'x', 'LNG': 'y'}
people_info.rename(columns={'dzip': 'zip'}, inplace=True)

zip_codes.rename(columns=zip_codes_header, inplace=True)
people_info = pd.merge(people_info, zip_codes, on="zip", how='left')
people_info.to_csv("/home/mids/m250024/UMD_Project/People Info.csv", index=False)