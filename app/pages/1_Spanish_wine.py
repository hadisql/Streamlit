import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import altair as alt

@st.cache
def load_data():
    df = pd.read_csv('././data/wines_cleaned_1.csv')
    df.drop(df.columns[0],axis=1,inplace=True)
    return df
#############
st.title('Spanish wine DataFrame')

#df = load_data()
# Create a text element and let the reader know the data is loading.
#data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
df = load_data()
# Notify the reader that the data was successfully loaded.
#data_load_state.text('Loading done!(using st.cache)')
if st.checkbox("Show DataFrame"):
    nrows_df = st.slider('Select a number of rows to show',0,10,3) #min,max,value
    st.dataframe(df.head(nrows_df))

st.text(f'number of distinct wineries : {df.winery.nunique()}')
st.text(f'number of distinct wines : {df.wine.nunique()}')
st.text(f'type of wines listed : {df.type.nunique()}')
st.text(f'number of distinct regions : {df.region.nunique()}')


#############
st.header("Top 10 wine producing regions")
#st.bar_chart(bar_data) # autre option possible
topwines = pd.DataFrame(df.region.value_counts()[:10])
pie = px.pie(topwines,values='region',names=topwines.index)
pie.update_layout(legend=dict(
    yanchor="top",
    y=0.90,
    xanchor="left",
    x=0.80
))
st.plotly_chart(pie)
#############
st.header("Price of wine with ratings")
fig = px.scatter(df, x='rating', y='price', color='region',
                 labels={"price":'price', 'rating':'rating'})


st.plotly_chart(fig, theme='streamlit',use_container_width=True)

#############
st.header('Distribution of Wine prices')
left_height = st.slider('Live adjustable subplot-width',.2,.8,.5)
fig = make_subplots(rows=2, cols=1,
                    subplot_titles=("Distribution of wine prices",
                                    "Boxplot of wine prices"),
                    row_heights=[left_height,1-left_height])

fig.add_trace(go.Histogram(x=df.price), row=1, col=1)

fig.add_trace(go.Box(x=df.price), row=2, col=1)

fig.update_layout(height=600, width=800,
                  title_text="How are the prices distributed ?",
                  showlegend=False)


st.plotly_chart(fig,use_container_width=False)
st.selectbox('select a size',['S','M','L','XL'])
