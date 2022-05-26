import sqlite3
import pandas as pd
import streamlit as st
from PIL import Image


# Title
image = Image.open('he.jpg')
st.image(image)
st.title("Vídeos CDTI de Horizonte Europa")

d_areas = {'Clusters': ['Espacio', 'Salud', '_5', 'Digital', 'Sociedad', 'Industria', '_6', 'Clima', 
                        'Seguridad', 'Movilidad', '5_6', 'Agricultura', '_4', 'Energía'], 
           'General': ['Conferencia'], 
           'Horizonte_Europa': ['Novedades', 'Conclusiones', 'ERA', 'Intro', 'Clausura'],
           'Pilar_1': ['General'], 'Pilar_3': ['EIC'], 
           'Propuesta': ['Novedades', 'Excelencia', 'Impacto', 'Parte_A', 'General', 'Implementación', 'Parte_B'], 
           'Transversal': ['Open_Science', 'General', 'Género', 'Etica', 'Legal_Financiero']}
grupos = ['Clusters', 'General', 'Horizonte_Europa', 'Pilar_1', 'Pilar_3', 'Propuesta', 'Transversal']


grupo = st.selectbox('Selecione grupo de vídeos',grupos)
options = st.multiselect(
     'Seleccione un área',d_areas[grupo],d_areas[grupo])
# grupo = 'Clusters'

conn = sqlite3.connect('videos.db')
df = pd.read_sql(f'SELECT * FROM videos WHERE videos.Grupo == "{grupo}"', conn)
conn.close()

df = df[df.Area.isin(options)]
df_display = df.drop(columns=['index', 'Grupo', 'Link']).sort_values(by='Area')
# tabla
st.subheader(f'Vídeos de "{grupo}"')
st.dataframe(df_display)
st.subheader('Selección de vídeo')
play_tit = st.selectbox('Selecione un vídeo para ser reproducido',list(df.Titulo))
play = df[df.Titulo == play_tit].Link.item()
st.markdown('**Descripción:**')
txt = df[df.Titulo == play_tit]['Descripción'].item()
st.write(txt)
st.video(play)
