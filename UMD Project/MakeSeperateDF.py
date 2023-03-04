
import geopy
import pandas as pd

df_Main = pd.read_csv('/home/mids/m250024/UMD_Project/ZipsFile.csv')
print(df_Main)
#print(df_Main[df_Main['dzip']])
#print(df_Main[df_Main['z']])
df_Main['z'] = pd.to_numeric(df_Main['z'])
df_Main['dzip'] = pd.to_numeric(df_Main['dzip'])

matches = df_Main[df_Main['dzip']==df_Main['z']]
print(matches)
matches.to_csv('/home/mids/m250024/UMD_Project/ZipMatch.csv')

mismatches = df_Main[(df_Main['dzip']!=df_Main['z']) & (df_Main['z']!=0) ]
print(mismatches)
mismatches.to_csv('/home/mids/m250024/UMD_Project/ZipMismatch.csv')


