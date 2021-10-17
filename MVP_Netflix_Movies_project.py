#!/usr/bin/env python
# coding: utf-8

# # Importing library

# In[30]:


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.offline import init_notebook_mode, iplot
import pandas as pd 
import seaborn as sns
import plotly.express as px


# In[8]:


df =  pd.read_csv("netflix_titles.csv")
df.head(10)


# ## Data Exploration

# In[3]:


df.info()


# In[4]:


#find the nulls value
df.isnull().sum()


# In[5]:


#find the unique value
df.nunique()


# #  Data Cleaning
# 

# In[14]:


#Replace null values with Null
df['country'].fillna('Null',inplace=True)
df['rating'].fillna('Null',inplace=True)
df.isnull().sum().sum()


# In[15]:


df.isnull().sum()


# In[16]:


#Converting into date-time format and adding two more features year and month.

df["date_added"] = pd.to_datetime(df['date_added'])
df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month


# # Data Visualization

# In[17]:


# Heatmap
# Correlation between the features
month_year_df = df.groupby('year_added')['month_added'].value_counts().unstack().fillna(0).T

plt.figure(figsize=(11,8))
sns.heatmap(month_year_df, linewidths=0.025, cmap="Greens")
plt.title("Content Heatmap")
plt.ylabel("Month")
plt.xlabel("Year")
plt.show()


# In[18]:


# Create the years and durations lists
years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

# Create a dictionary with the two lists
movie_dict = {'years': years, 'durations': durations}

# Draw a line plot of release_years and durations
line =plt.plot(years, durations , linewidth = 1 , color='g')

# Create a title
plt.title('Netflix Movie Durations 2011-2020',fontsize = 20,style='italic',weight='bold',rotation=0,color='purple');
plt.xlabel('YEARS',fontsize = 8, weight = 'bold',color='green');
plt.ylabel('MOVIE DURATIONS',fontsize = 8, weight = 'bold',color='green');

# Show the plot
plt.show()


# In[19]:


#plot Pie chart to show the percentage of content type
df['type'].value_counts().plot(kind='pie', autopct='%1.0f%%', legend=dict(x=0.1, y=1.1))
plt.title("Persentage of Content Type", y=1.02 , fontsize = 10,style='italic',weight='bold',rotation=0)


# In[55]:


data = df.set_index('title').country.str.split(', ', expand=True).stack().reset_index(level=1, drop=True);

plt.figure(figsize=(7,9))
g = sns.countplot(y = data, order=data.value_counts().index[:20] , palette= ["#7fcdbb","#edf8b1"])
plt.title('Top 20 Countries on Netflix' , family='serif',fontsize = 15,loc='center',color='r');
plt.xlabel('Titles')
plt.ylabel('Country')
plt.show()


# In[57]:


#How does the timeline look like for the addition of International Movies compared to International TV Shows?
d1 = df[df["type"] == "TV Show"]
d2 = df[df["type"] == "Movie"]

col = "year_added"

X1 = d1[col].value_counts().reset_index()
X1 = X1.rename(columns = {col : "count", "index" : col})
X1['percent'] = X1['count'].apply(lambda x : 100*x/sum(X1['count']))
X1 = X1.sort_values(col)


Y2 = d2[col].value_counts().reset_index()
Y2 = Y2.rename(columns = {col : "count", "index" : col})
Y2['percent'] = Y2['count'].apply(lambda x : 100*x/sum(Y2['count']))
Y2 = Y2.sort_values(col)


new_x = go.Scatter(x=X1[col], y=X1["count"], name="TV Shows", marker=dict(color="#EC7063"))
new_y = go.Scatter(x=Y2[col], y=Y2["count"], name="Movies", marker=dict(color="#1D8348"))
data = [new_x, new_y]
layout = go.Layout(title="Content added over the years",legend=dict(x=0.1, y=1.1, orientation="h"))
fig = go.Figure(data, layout=layout)
fig.show()


# In[65]:


order =  ['G', 'TV-Y', 'TV-G', 'PG', 'TV-Y7', 'TV-Y7-FV', 'TV-PG', 'PG-13', 'TV-14', 'R', 'NC-17', 'TV-MA']
plt.figure(figsize=(15,7))
g = sns.countplot(df.rating, hue=df.type, order=order, palette= ["#7fcdbb","#edf8b1"] );
plt.title("Ratings for Movies & TV Shows")
plt.xlabel("Rating")
plt.ylabel("Total Count")
plt.show()


# In[ ]:





# In[ ]:




