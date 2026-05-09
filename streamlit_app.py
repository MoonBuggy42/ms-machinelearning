import streamlit as st
import pandas as pd
import plotly.express as px
st.title('🤖 Machine Learning App')

st.info("This app Builds a machine learning model!")
# Raw Data
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
# Data Visuals
with st.expander("Data Visualization"):
  fig1 = px.scatter(df, x="bill_length_mm", y="body_mass_g", color="species", hover_data=["island"])
  fig1.update_layout(xaxis_title="Bill Length (mm)", yaxis_title="Body Mass (g)")
  st.plotly_chart(fig1)
# Additional Data Prep
with st.sidebar:
  st.header("Input Features")
  island = st.selectbox("Island", ('Biscoe', 'Dream', 'Torgersen'))
  gender = st.selectbox("Gender", ('male', 'female'))
  bill_length_mm = st.slider("Bill Length (mm)", 32.1, 59.6, 43.9)
  bill_depth_mm = st.slider("Bill Depth (mm)", 13.1, 21.5, 17.2)
  flipper_length_mm = st.slider("Flipper Length (mm)", 172.0, 231.0, 201.0)
  body_mass_g = st.slider("Body Mass (g)", 2700.0, 6300.0, 4207.0)
