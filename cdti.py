import sqlite3
import pandas as pd
import streamlit as st
from PIL import Image

# Title
image = Image.open('he.jpg')
st.image(image)
st.title("Vídeos CDTI de Horizonte Europa")

grupos = ['Clusters', 'General', 'Horizonte_Europa', 'Pilar_1', 'Pilar_3', 'Propuesta', 'Transversal']
grupo = st.selectbox('Selecione grupo de vídeos',grupos)
# grupo = 'Clusters'

conn = sqlite3.connect('videos.db')
df = pd.read_sql(f'SELECT * FROM videos WHERE videos.Grupo == "{grupo}"', conn)
conn.close()

# tabla
st.subheader(f'Vídeos de "{grupo}"')
st.dataframe(df)
