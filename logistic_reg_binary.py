import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
df= pd.read_csv("insurance_data_logistic.csv")
age_median = df.age.median()
df["age"] = df["age"].fillna(age_median)
print(df)
df= df.dropna(subset=["bought_insurance"])
print(df)
x= df[["age"]]
y=df["bought_insurance"]
plt.scatter(x,y=y)
#plt.show()
X_train, X_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train,y_train)
print(model.predict(X_test))
print(model.predict([[100]]))
