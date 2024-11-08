import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout="wide")

df_reviews  = pd.read_csv('datasets/customer reviews.csv')
df_top100_books = pd.read_csv('datasets/Top-100 Trending Books.csv')

price_max = df_top100_books["book price"].max()
price_min = df_top100_books["book price"].min()

max_price = st.sidebar.slider("Intervalo de Preço", price_min, price_max, price_max)
df_books = df_top100_books[df_top100_books["book price"] <= max_price]
df_books

fig = go.Figure()
fig.add_trace(go.Histogram(
    x=df_books["year of publication"],
    xbins=dict(
        size=5
    ),
    marker_color='red',
    opacity=0.70
))

fig.update_layout(
    title_text = "Ano das Publicações",
    xaxis_title_text='Anos',
    yaxis_title_text='Quantidade'
)

fig2 = go.Figure()
fig2.add_trace(go.Histogram(
    x=df_books["rating"],
    marker_color='red',
    opacity=0.70
))

fig2.update_layout(
    title_text = "Classificação por quantidade",
    xaxis_title_text='Avaliação',
    yaxis_title_text='Quantidade'
)

col1, col2 = st.columns(2)
col1.plotly_chart(fig)
col2.plotly_chart(fig2)
