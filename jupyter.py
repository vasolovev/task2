# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: .venv
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

# +

st.title('Student Data Analysis')

st.subheader('Raw Data')
st.write(df)

analysis_option = st.sidebar.selectbox('Choose Analysis', ['Descriptive Statistics', 'Distribution Analysis'])

st.set_option('deprecation.showPyplotGlobalUse', False)

if analysis_option == 'Descriptive Statistics':
    st.subheader('Descriptive Statistics')
    st.write(df.describe())

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


# +
st.title('Анализ данных студентов')

# Выбор переменных для анализа
st.sidebar.title("Выбор переменных")
options = st.sidebar.multiselect(
    'Выберите переменные для анализа',
    df.columns,
    ['Age at enrollment', 'Admission grade', 'Previous qualification (grade)']
)

# Отображение статистического обзора выбранных данных
if options:
    st.write("Статистический обзор выбранных переменных:")
    st.write(df[options].describe())

# График корреляции
if st.sidebar.checkbox("Показать корреляционную матрицу"):
    st.write("Корреляционная матрица:")
    fig, ax = plt.subplots()
    sns.heatmap(df[options].corr(), annot=True, fmt=".2f", cmap='coolwarm', ax=ax)
    st.pyplot(fig)

# Pairplot
if st.sidebar.checkbox("Показать парный график"):
    st.write("Парный график для выбранных переменных:")
    fig = sns.pairplot(df[options])
    st.pyplot(fig)

# -


