import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

df= pd.read_csv("home_price_dataset.csv")
print(df)
plt.scatter(df["home_size_sqft"],df["price_usd"])
plt.show()
reg= linear_model.LinearRegression()
reg.fit(df[["home_size_sqft"]],df["price_usd"])
print(reg.predict([[33456]]))