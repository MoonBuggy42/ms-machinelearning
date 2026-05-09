import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.ensemble import RandomForestClassifier
st.title('🤖 Machine Learning App')

st.info("This app Builds a machine learning model!")
# Raw Data
with st.expander("Data"):
  st.write("**Raw data**")
  df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
  df

  st.write('**X**')
  X_raw = df.drop("species", axis=1)
  X_raw

  st.write("**y**")
  y_raw =df.species
  y_raw
# Data Visuals
with st.expander("Data Visualization"):
  fig1 = px.scatter(df, x="bill_length_mm", y="body_mass_g", color="species", hover_data=["island"])
  fig1.update_layout(xaxis_title="Bill Length (mm)", yaxis_title="Body Mass (g)")
  st.plotly_chart(fig1)
# Additional Data Prep
with st.sidebar:
  st.header("Input Features")
  island = st.selectbox("Island", ('Biscoe', 'Dream', 'Torgersen'))
  bill_length_mm = st.slider("Bill Length (mm)", 32.1, 59.6, 43.9)
  bill_depth_mm = st.slider("Bill Depth (mm)", 13.1, 21.5, 17.2)
  flipper_length_mm = st.slider("Flipper Length (mm)", 172.0, 231.0, 201.0)
  body_mass_g = st.slider("Body Mass (g)", 2700.0, 6300.0, 4207.0)
  gender = st.selectbox("Gender", ('male', 'female'))

  
  # Create DataFrame for the input features
  data = {'island': island, 
          'bill_length_mm': bill_length_mm, 
          'bill_depth_mm': bill_depth_mm, 
          'flipper_length_mm': flipper_length_mm, 
          'body_mass_g': body_mass_g, 
          'sex': gender}
  input_df = pd.DataFrame(data, index=[0])
  input_penguins = pd.concat([input_df, X_raw], axis=0)
with st.expander('Input Features'):
  st.write("**Input Penguin**")
  input_df
  st.write("**Conbined Penguins Data**")
  input_penguins
# Data Prep
# Encode X
encode = ['island', 'sex']
df_penguins = pd.get_dummies(input_penguins, prefix=encode)
input_row = df_penguins[:1]

# Encode y
target_mapper = {'Adelie': 0, 
                 'Chinstrap': 1, 
                 'Gentoo': 2}
def target_encode(val):
  return target_mapper[val]

y = y_raw.apply(target_encode)


with st.expander("Data Preparation"):
  st.write('**Encoded X (Input Penguin)**')
  input_row
  st.write("**Encoded y**")
  y
  

