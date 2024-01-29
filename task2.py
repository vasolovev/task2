# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

import streamlit as st

from streamlit_jupyter import StreamlitPatcher, tqdm

StreamlitPatcher().jupyter()


# https://www.kaggle.com/datasets/missionjee/students-dropout-and-academic-success-dataset
# -

df = pd.read_csv('file.csv', sep=";")

df.describe()

df.head()


df.columns

missing_values = df.isnull().sum()


# +
categorical_vars = ['Marital status', 'Application mode', 'Daytime/evening attendance\t', 'Previous qualification', 'Nacionality', 'Mother\'s qualification', 'Father\'s qualification', 'Mother\'s occupation', 'Father\'s occupation', 'Gender', 'International']
numeric_vars = ['Age at enrollment', 'Admission grade', 'Unemployment rate', 'Inflation rate', 'GDP']

for var in categorical_vars:
    print(f'Уникальные значения для {var}: {df[var].unique()}')
# -

st.set_option('deprecation.showPyplotGlobalUse', False)
df[numeric_vars].hist(bins=20, figsize=(15, 10))
plt.show()

df[(df['Age at enrollment']<20) & (df['Target'] == "Dropout")]

df[df['Age at enrollment'] > 25].__len__()


df[(df['Age at enrollment'] > 50) & (df["Target"]=="Graduate")]


# +
df.groupby('Marital status')['Age at enrollment'].mean()


# -

df[df['International'] == 1]


df[df['Target'] == "Graduate"]

df.groupby('Previous qualification')['Admission grade'].max()


df.groupby(['Marital status'])


# +

st.title('Student Data Analysis')

st.subheader('Raw Data')
st.write(df)

analysis_option = st.sidebar.selectbox('Choose Analysis', ['Descriptive Statistics', 'Correlation Analysis', 'Distribution Analysis'])

if analysis_option == 'Descriptive Statistics':
    st.subheader('Descriptive Statistics')
    st.write(df.describe())

elif analysis_option == 'Correlation Analysis':
    st.subheader('Correlation Analysis')
    correlation_matrix = df.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    st.pyplot()

elif analysis_option == 'Distribution Analysis':
    st.subheader('Distribution Analysis')
    selected_column = st.sidebar.selectbox('Select Column', df.columns)
    st.write(f'Distribution of {selected_column}')
    sns.histplot(df[selected_column], kde=True)
    st.pyplot()


st.subheader('Target Variable Distribution')
st.write(df['Target'].value_counts())


# +
st.subheader('Bar Charts')

st.write('Courses')
course_counts = df['Course'].value_counts()
st.bar_chart(course_counts)

st.write('Gender')
gender_counts = df['Gender'].value_counts()
st.bar_chart(gender_counts)

st.subheader('Target Variable Distribution')
st.write(df['Target'].value_counts())

st.write('Bar Chart for Age Distribution')
age_counts = df['Age at enrollment'].value_counts()
st.bar_chart(age_counts)

# -


