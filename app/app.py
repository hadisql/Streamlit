import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler, StandardScaler, LabelEncoder, RobustScaler
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer, make_column_selector
from sklearn import set_config
set_config(display="diagram")

@st.cache
def load_data():
    df = pd.read_csv('./data/wines_cleaned_1.csv')
    df.drop(df.columns[0],axis=1,inplace=True)
    return df

st.header('Intro to streamlit')
st.title('Spanish wine DataFrame')

#df = load_data()
# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
df = load_data()
# Notify the reader that the data was successfully loaded.
data_load_state.text('Done!(using st.cache)')
nrows_df = st.slider('Select a number of rows to show',0,10,3) #min,max,value
st.dataframe(df.head(nrows_df))

st.text(f'nombre de producteurs différents : {df.winery.nunique()}')
st.text(f'nombre de vins différents : {df.wine.nunique()}')
st.text(f'types de vins différents : {df.type.nunique()}')
st.text(f'nombre de régions différentes : {df.region.nunique()}')

#fig,ax = plt.subplots()
#ax.bar(df.region.value_counts().index[:15],df.region.value_counts().tolist()[:15])
#ax.xticks(rotation=45)
#st.pyplot(fig)
st.bar_chart(x=df.region.value_counts().index[:10].tolist(),y=df.region.value_counts().tolist()[:10])
