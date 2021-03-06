# -*- coding: utf-8 -*-
"""Preço Carbono.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dNo_VRqU9y99VJcs8FZPRLDIjB0oWOcT
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import plotly.express as px

data = pd.read_excel('/content/Dados de preço de carbono.xlsx')

data

data.isnull().sum()

data.dtypes

is_NaN = data.isnull()

row_has_NaN = is_NaN.any(axis=1)

rows_with_NaN = data[row_has_NaN]

rows_with_NaN

df = data.dropna()

df.describe()

valor = df['Price_rate_1_2021']
country = df['Name of the initiative']

plt.rcParams["figure.figsize"] = (15,15)
plt.scatter(valor, country)
plt.title('Carbon Price')
plt.xlabel('US$')

plt.rcParams["figure.figsize"] = (10,15)
fig, ax = plt.subplots()


ax.barh(country, valor, align='center')
ax.set_yticks(country)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('US$ VALUES')
ax.set_title('CARBON PRICE')