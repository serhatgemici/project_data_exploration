import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st

from ziko_st_toc import table_of_contents

# globals
figsize = (6, 4)
width = 1100

st.title("Data Visualization")

with st.sidebar:
    table_of_contents()

df = pd.read_csv("train.csv")

st.header("Survivors")
fig, ax = plt.subplots(figsize=figsize)
sns.countplot(data=df, x="Survived", hue="Survived", ax=ax)
st.pyplot(fig, width=width)

st.header("Gender Distribution")
fig, ax = plt.subplots(figsize=figsize)
sns.countplot(data=df, x="Sex", hue="Sex", ax=ax)
ax.set_title("Distribution of passenger gender")
st.pyplot(fig, width=width)

st.header("Passenger Class Distribution")
fig, ax = plt.subplots(figsize=figsize)
sns.countplot(data=df, x="Pclass", hue="Pclass", ax=ax)
ax.set_title("Distribution of passenger class")
st.pyplot(fig, width=width)

st.header("Age Distribution")
fig, ax = plt.subplots(figsize=figsize)
sns.histplot(data=df, x="Age", kde=True, ax=ax)
ax.set_title("Distribution of passenger age")
st.pyplot(fig, width=width)

st.header("Survival by Gender")
fig, ax = plt.subplots(figsize=figsize)
sns.countplot(data=df, x="Survived", hue="Sex", ax=ax)
st.pyplot(fig, width=width)

st.header("Survival by Passenger Class")
fig, ax = plt.subplots(figsize=figsize)
sns.pointplot(data=df, x="Pclass", y="Survived", ax=ax)
st.pyplot(fig, width=width)

st.header("Correlation Matrix")
fig, ax = plt.subplots(figsize=figsize)
corr = df.select_dtypes(include=[np.number]).corr()
sns.heatmap(corr, annot=True, ax=ax)
st.pyplot(fig, width=width)
