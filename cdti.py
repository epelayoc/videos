import sqlite3
import pandas as pd
import streamlit as st
from PIL import Image


# Title
image = Image.open('he.jpg')
st.image(image)
st.title("Vídeos CDTI de Horizonte Europa")


conn = sqlite3.connect('videos.db')
df = pd.read_sql('SELECT * FROM videos', conn)
conn.close()
grupos = ['Clusters', 'General', 'Horizonte_Europa', 'Pilar_1', 'Pilar_3', 'Propuesta', 'Transversal']

grupo = st.selectbox('Selecione grupo de vídeos',grupos)
#grupo = 'Clusters'
dfg = df[df.Grupo == grupo].sort_values(by='Area')

dfg = dfg.drop('Grupo', 1)



# tabla
st.subheader(f'Vídeos de "{grupo}"')
st.dataframe(dfg)
