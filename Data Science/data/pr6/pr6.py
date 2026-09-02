import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Read dataset
df = pd.read_csv('Data Science/data/pr6/Housing.csv')

# Label Encoding
le = LabelEncoder()

df['mainroad'] = le.fit_transform(df['mainroad'])
df['guestroom'] = le.fit_transform(df['guestroom'])
df['basement'] = le.fit_transform(df['basement'])
df['hotwaterheating'] = le.fit_transform(df['hotwaterheating'])
df['airconditioning'] = le.fit_transform(df['airconditioning'])
df['prefarea'] = le.fit_transform(df['prefarea'])
df['furnishingstatus'] = le.fit_transform(df['furnishingstatus'])

# Input and Output
x = df[['area']].values
y = df[['price']].values

# Split the dataset
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

reg = LinearRegression()

reg.fit(x_train, y_train)

y_pred = reg.predict(x_test)

score = r2_score(y_test, y_pred)

print("\nR2 Score:", score)

mse= mean_squared_error(y_test,y_pred)
print("Mean Square Error",mse)