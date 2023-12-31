# -*- coding: utf-8 -*-
"""house_price_prediction_multiple_linear_regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ifRe8e8O1LUo8STk-m3l55YKK0aQyjfh
"""

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
# %matplotlib inline
import numpy as np 
import pandas as pd 
import os
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

"""# 1. Import Dataset

"""

df  = pd.read_csv('/content/home_price_dataset.csv')

df.head()

df.info()

df.describe().style.background_gradient(cmap='CMRmap')

"""# 2. Data Analysis"""

df.isna().sum()

"""* we can see here only bedrooms has null values"""

df['bedrooms'] = df['bedrooms'].fillna( df['bedrooms'].mean() )
df.head()

"""# 3. Data Visualization"""

plt.figure(figsize=(10, 7))
plt.title("Bedroom wise price increase.")

sns.barplot('bedrooms', 'price', data=df)
plt.xlabel('Bedrooms', )
plt.ylabel('Price')
plt.show()

plt.figure(figsize=(10, 5))

sns.scatterplot('bedrooms', 'price',data=df)
plt.title("Price vs Bedroom Scatter plot")

plt.xlabel("House Bedrooms")
plt.ylabel('House Price')
plt.show()

"""* Here we can see bedrooms and price linearly related, House's Price increased if bedroom size will increase."""

plt.figure(figsize=(10, 7))

sns.lmplot(x="bedrooms", y="price", data=df);
plt.title("Price and bedroom wise line plot")
plt.show()

"""# 4. Model Implementing"""

from sklearn.linear_model import LinearRegression

"""* Now, Create model instance from LinearRegression class"""

mdl = LinearRegression()

"""* Before fitting the model, create X and y for model fitting"""

X = df.drop(['price'], axis=1)
y = df['price']

df['bedrooms'] = df['bedrooms'].astype('int64')

df.info()

print(X)
print("-" * 25)
print(y)

"""* Now, We are going to fitting the training and testing data"""

mdl.fit( X, y  )

"""# Prediction 

"""

mdl.predict([[ 4000, 2, 50 ]])

"""- Show Coeficient"""

mdl.coef_

"""- Show intecept"""

mdl.intercept_

score = mdl.score( X, y )

print(score * 100)