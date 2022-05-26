

import pandas as pd
import streamlit as st
from PIL import Image


# Title
image = Image.open('he.jpg')
st.image(image)
st.title("Vídeos CDTI de Horizonte Europa")

df = pd.read_excel('videos_cdti.xlsx')
df1 = df.groupby('Grupo').first().reset_index()
grupos = list(df1.Grupo)
grupo = st.selectbox('Selecione grupo de vídeos',grupos)
#grupo = 'Clusters'
dfg = df[df.Grupo == grupo].sort_values(by='Area')

dfg = dfg.drop('Grupo', 1)

# CSS to inject contained in a string
hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)

# tabla
st.subheader(f'Vídeos de "{grupo}"')
# st.dataframe(dfg)


def make_clickable(link):
    # target _blank to open new window
    # extract clickable text to display for your link
    text = link.split('=')[1]
    return f'<a target="_blank" href="{link}">{text}</a>'

# link is the column with hyperlinks
dfg['Link'] = dfg['Link'].apply(make_clickable)


# # CSS to inject contained in a string
# hide_table_row_index = """
#             <style>
#             tbody th {display:none}
#             .blank {display:none}
#             </style>
#             """

# # Inject CSS with Markdown
# st.markdown(hide_table_row_index, unsafe_allow_html=True)

dfg = dfg.to_html(escape=False)
st.write(dfg, unsafe_allow_html=True)

