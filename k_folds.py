import pandas as pd
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold
import numpy as np
from sklearn.model_selection import cross_val_score
digits = load_digits()
X_train, X_test, y_train, y_test = train_test_split(digits.data,digits.target,test_size=0.3)

logi_reg = LogisticRegression()
logi_reg.fit(X_train,y_train)
print("ogistice regreesion acurarcy is ",logi_reg.score(X_test,y_test))

svm =SVC()
svm.fit(X_train,y_train)
print("svm score is",svm.score(X_test,y_test))

rand_forest = RandomForestClassifier(n_estimators=40)
rand_forest.fit(X_train,y_train)
print("random forest  accuracy is ",rand_forest.score(X_test,y_test))
kf = KFold(n_splits=5,shuffle=False, random_state=None)

logi_reg_score = []
svm_score = []
rand_forest_score = []
def get_score(model,X_train, X_test, y_train, y_test):
    model.fit(X_train,y_train)
    return model.score(X_test,y_test)
for train_index, test_index in kf.split(digits.data):
    X_train = digits.data[train_index]
    X_test =digits.data[test_index]
    y_train = digits.target[train_index]
    y_test = digits.target[test_index]

    logi_reg_score.append(get_score(LogisticRegression(),X_train, X_test, y_train, y_test))
    svm_score.append(get_score(SVC(),X_train, X_test, y_train, y_test))
    rand_forest_score.append(get_score(RandomForestClassifier(),X_train, X_test, y_train, y_test))
print("logi_reg_score ",np.array(logi_reg_score))
print("svm_score",np.array(svm_score).mean())
print("rand_forest_score",np.array(rand_forest_score).mean())

print("crosss val score of logi",cross_val_score(LogisticRegression(),digits.data,digits.target))