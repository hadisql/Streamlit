import streamlit as st
import numpy as np
import pandas as pd


@st.cache
def load_data():
    df = pd.read_csv('./data/wines_cleaned_1.csv')
    df.drop(df.columns[0],axis=1,inplace=True)
    return df

st.header('Intro to streamlit')
st.title('Spanish wine DataFrame')

#df = load_data()
# Create a text element and let the reader know the data is loading.
#data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
df = load_data()
# Notify the reader that the data was successfully loaded.
#data_load_state.text('Loading done!(using st.cache)')
nrows_df = st.slider('Select a number of rows to show',0,10,3) #min,max,value
st.dataframe(df.head(nrows_df))

st.text(f'number of distinct wineries : {df.winery.nunique()}')
st.text(f'number of distinct wines : {df.wine.nunique()}')
st.text(f'type of wines listed : {df.type.nunique()}')
st.text(f'number of distinct regions : {df.region.nunique()}')

values=df.region.value_counts().tolist()[:10]
keys=df.region.value_counts().index[:10].tolist()

d = {k:v for (k,v) in zip(keys,values)}
bar_data = pd.DataFrame(data=d,index=range(1))
#st.dataframe(bar_data)
st.title("Top 10 wine producing regions")
st.bar_chart(bar_data)
