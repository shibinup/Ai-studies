import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("sales_data_sample.csv",encoding='windows-1252')
print(df)
print(len(df))

#task1
total_sales=len(df)
print("total_sales=",total_sales)
print(df.columns)

print("------------------")

#task2 best selling product
best_selling_product= df.groupby("PRODUCTCODE")["SALES"].sum().sort_values(ascending=False)
top_selled_product= best_selling_product.head(1)
print(top_selled_product)


# starting plotting 
# monthly sales
#task 1 :

df["MonthNum"] = pd.to_datetime(df["ORDERDATE"]).dt.month
df["Months"]   = pd.to_datetime(df["ORDERDATE"]).dt.month_name()  
monthly_sales= df.groupby(["MonthNum", "Months"])["SALES"].sum().reset_index().sort_values("MonthNum")
print(monthly_sales)

plt.plot(monthly_sales["Months"],monthly_sales["SALES"])
plt.show()