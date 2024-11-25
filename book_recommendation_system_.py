# -*- coding: utf-8 -*-
"""Book recommendation system.

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cAU3IzulFeXiMpq6PIIAA6TDvImAWaOt
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import neighbors
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("1books#.csv")

df.head()

df.isnull().sum()

df.describe()

top_ten = df[df['ratings_count'] > 1000000]
top_ten.sort_values(by='average_rating', ascending=False)

print(plt.style.available)

plt.style.use('seaborn-v0_8-darkgrid')

plt.figure(figsize=(10, 10))

data = top_ten.sort_values(by='average_rating', ascending=False).head(10)
sns.barplot(x="average_rating", y="title", data=data, palette='inferno')

most_books = df.groupby('authors')['title'].count().reset_index().sort_values('title', ascending=False).head(10).set_index('authors')
plt.figure(figsize=(15,10))
sns.barplot(x=most_books.index, y='title', data=most_books, palette='inferno')
plt.xticks(rotation=90)
plt.show()
ax.set_title('Authors with most books')
total = sum(most_books['title'])

most_rated = df.sort_values('ratings_count', ascending = False).head(10).set_index('title')

"""# New Section"""

plt.figure(figsize=(15,10))

ax = sns.barplot(x=most_rated.index, y='ratings_count', data=most_rated, palette='inferno')
plt.xticks(rotation=90)
plt.show()
ax.set_title('Books with most ratings')