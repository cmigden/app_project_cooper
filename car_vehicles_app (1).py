#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly_express as px
import streamlit as st
#import needed packages


# In[2]:


data = pd.read_csv('/Users/coopermigden/data_sets/vehicles_us (1).csv')
#Brings the data into the program

data.describe
#gives general information about the data and it shows how it looks
# In[3]:
data.isna().sum()
#shows the amount of unknown values in each column

columns_to_replace = ['model_year','cylinders','odometer','paint_color','is_4wd']
for column in columns_to_replace:
    data[column] = data[column].fillna('unknown')
#to replace all NaN values with the word 'unknown'

data.isna().sum()
#check to see if the previous function worked

data['model'].sort_values().unique()
#went through list of model names to check if any are spelled incorrectly. none are spelled incorrectly.

data.columns
#determins the titles of the columns. Columns are in the appropriate snake_case


data.to_csv('cleaned_vehicles_us.csv', index = True)
#to create a new csv file for the cleaned data
st.title('##Car Sales Data')


# In[4]:


st.write(data.head())
#displays data table


# In[5]:


st.header('#Interactive Scatterplot')


# In[6]:


def interactive_plot(data):
    x_axis_val = st.selectbox('Select X-Axis Value', options=data.columns)
    y_axis_val = st.selectbox('Select Y-Axis Value', options=data.columns)
    
    plot = px.scatter(data,x=x_axis_val,y=y_axis_val)
    st.plotly_chart(plot)
#This is a function that creates a scatterplot in which the user is able to choose the x and y axis based upon the columns in the data dataframe.


# In[7]:


interactive_plot(data)


# In[8]:


st.header('Histogram Via Type of Car and Price')
color_opt=st.checkbox('Please select this checkbox if you want this graph to have color.')
color ='type' if color_opt else None
#determines if the graph has color

hist =px.histogram(data_frame=data,x='type',y='price',color=color)

st.plotly_chart(hist)


# In[9]:


#This is a function that creates a histogram in which the user is able to choose


# In[10]:
