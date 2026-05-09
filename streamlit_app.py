import streamlit as st
import pandas as pd
import plotly.express as px
st.title('🤖 Machine Learning App')

st.info("This app Builds a machine learning model!")
with st.expander("Data"):
  st.write("**Raw data**")
  df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
  df

  st.write('**X**')
  X = df.drop("species", axis=1)
  X

  st.write("**y**")
  y=df.species
  y
with st.expander("Data Visualization"):
  fig1 = px.scatter(df, x="bill_length_mm", y="body_mass_g", color="species", hover_data=["island"])
  fig1.update_layout(xaxis_title="Bill Length (mm)", yaxis_title="Body Mass (g)")
  st.plotly_chart(fig1)
