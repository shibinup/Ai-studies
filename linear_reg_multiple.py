import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
df= pd.read_csv("housing_data_with_missing_values.csv")
print(df)
median_of_area = df.area.median()
median_of_bedroom =   df.bedroom.median()
median_of_age = df.age.median()
median_of_price = df.price.median()
df["area"] = df["area"].fillna(median_of_area)
df["bedroom"] = df["bedroom"].fillna(median_of_bedroom)
df["age"] = df["age"].fillna(median_of_age)
df["price"] = df["price"].fillna(median_of_price)
print(df)
reg_model = linear_model.LinearRegression()
reg_model.fit(df[["area","bedroom","age"]],df["price"])
print(reg_model.coef_)
print(reg_model.intercept_)
print(reg_model.predict([[1380,4,8]]))