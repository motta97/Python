import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x=pd.read_csv(r"C:\Users\Mostafa\Downloads\Visual\python\Machine Learning\train_energy_data.csv")
y=x["Energy Consumption"]
x=x.drop(columns=["Energy Consumption"])
from sklearn.preprocessing import LabelEncoder
categorical_columns = ["Building Type","Day of Week"]
for col in categorical_columns:
    le = LabelEncoder()
    x[col]=le.fit_transform(x[col])

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x= scaler.fit_transform(x)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.25,random_state=67)


from sklearn.linear_model import LinearRegression
lin_leg = LinearRegression()
lin_leg.fit(x_train,y_train)
y_pred=lin_leg.predict(x_test)

from sklearn.metrics import r2_score
r2_train=r2_score(y_train,lin_leg.predict(x_train))
print(r2_train)
r2_test=r2_score(y_test,y_pred)
print(r2_test)

plt.scatter(y_test,y_pred,color="blue")
plt.xlabel("Actual Energy Consumption")
plt.ylabel("Predicted Energy Consumption")
plt.show()
