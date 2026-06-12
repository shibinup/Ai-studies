import pandas as pd
from  sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

iris = load_iris()

df = pd.DataFrame(iris.data,columns=iris.feature_names)
print(df.head())
df["target"] = iris.target
print(df["target"].head())
df["flower_name"] = df.target.apply(lambda x: iris.target_names[x])
print(df["flower_name"].head())
x = df.drop(["target", "flower_name"], axis='columns')
y = df["target"]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)

model = SVC()
model.fit(x_train,y_train)
print(model.score(x_test,y_test))