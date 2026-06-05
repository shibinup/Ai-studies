import pandas as pd
df=pd.read_csv("weather_pandas_practice.csv")
print(df)
grp= df.groupby("city")["temperature"].mean()
print(grp)

