import plotly.express as px
import pandas as pd
from datetime import datetime as dt

df = pd.read_csv("ZipsFile.csv")

count = df["z"].value_counts().head(10)

print(count)

driverzip = df["dzip"].value_counts().head(10)

print(driverzip)