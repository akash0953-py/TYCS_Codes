import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('Data Science\pr6\Housing.csv')

x = df[['area']]
y = df[['price']]

x_trian,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

reg = LinearRegression()
reg.fit(x_trian,y_train)

y_pred = reg.predict(x_test)

mse = mean_squared_error(y_test,y_train)
r2 = r2_score(y_test,y_train)

house_price = reg.predict([[5000]])
print(house_price)

plt.scatter(x_test,y_test)
plt.plot(x_test,y_pred,color = 'red')
plt.xlabel("area")
plt.ylabel('price')
plt.show()