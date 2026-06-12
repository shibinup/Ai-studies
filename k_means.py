import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
df=pd.read_csv("customer_kmeans_study.csv")
#print(df)
#plt.scatter(df["Age"],df["Income"])
#plt.show()
scalar = StandardScaler()
kmeans = KMeans(n_clusters=3, random_state=42)
scaled_data = scalar.fit_transform(df[["Age", "Income"]])
y_predicted= kmeans.fit_predict(scaled_data)
#print(y_predicted)
df["cluster"] = y_predicted
df1 = df[df.cluster==0]
df2 = df[df.cluster==1]
df3 = df[df.cluster==2]
plt.scatter(df1["Age"],df1["Income"],color="green")
plt.scatter(df2["Age"],df2["Income"],color="yellow")
plt.scatter(df3["Age"],df3["Income"],color="red")
plt.show()