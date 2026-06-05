from matplotlib import pyplot as plt
import pandas as pd

df=pd.read_csv("weather_pandas_practice.csv")

plt.plot(df["temperature"],df["windspeed"])
plt.show()