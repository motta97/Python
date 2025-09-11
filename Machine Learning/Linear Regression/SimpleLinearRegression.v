import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x= np.random.rand(100,1)
y = 4 +3*x +np.random.rand(100,1)
lin_reg = LinearRegression()
lin_reg.fit(x,y)
x_new =[[0],[1]]
y_new = lin_reg.predict(x_new)

plt.scatter(x,y,color="blue")
plt.plot(x_new,y_new,color = "red")
plt.show()
