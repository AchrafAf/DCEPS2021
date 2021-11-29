
import streamlit as st
import pandas as pd
from EDA_IMDb_functions import *

def update_theme(primaryColor,backgroundColor,secondaryBackgroundColor,textColor,font):
    # Theme Base
    theme_data=['[theme]\n\n','primaryColor=\"%s\"\n'%(primaryColor),
    'backgroundColor=\"%s\"\n'%(backgroundColor),
    'secondaryBackgroundColor=\"%s\"\n'%(secondaryBackgroundColor),
    'textColor=\"%s\"\n'%(textColor),
    'font=\"%s\"\n'%(font)]
    theme_file=open('.streamlit/config.toml','w+')

    theme_file.writelines(theme_data)

primaryColor="#f5c518"
backgroundColor="#000000"
secondaryBackgroundColor="#222222"
textColor="#ffffff"
font="sans serif"
#update_theme(primaryColor,backgroundColor,secondaryBackgroundColor,textColor,font)

st.set_page_config(page_title='DataViz - Data Challenge 2021',
                   page_icon='https://www.aacc.fr/sites/default/files/styles/logo/https/ucarecdn.com//1033ec06-23ee-4ee6-b583-87f191f58308/type.png?itok=Z0q9Mgu5',
                   layout="wide")

st.sidebar.image('images/epsilonlogo.png', width=200)
st.sidebar.header('Data Challenge 2021')
st.sidebar.markdown('Analyse exploratoire des données Microfaune de Dataforgood')

 #   ("Statistiques descriptives",
 #    "Décomposition d'un signal",
 #    "Features spectrales", 
 #    "Notes musicales",
 #    ),
menu = st.sidebar.radio(
    "",
    ("Statistiques descriptives",
     "Décomposition d'un signal",
     "Décomposition d'un signal V2",
     "Features spectrales",
     "Notes musicales",
    ),
)

# Pone el radio-button en horizontal. Afecta a todos los radio button de una página.
# Por eso está puesto en este que es general a todo
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.markdown('---')
st.sidebar.write('Equipe Hibou')
st.sidebar.write('Décembre 2021')

if menu == 'Statistiques descriptives':
    set_stats_desc()
if menu == 'Features spectrales':
    set_features()
if menu == "Décomposition d'un signal":
    set_decomposition()
if menu == "Décomposition d'un signal V2":
    set_decomposition_v2()
if menu == "Notes musicales":
    set_notes()

elif menu == 'Data':
    set_data()
elif menu == 'Variables de estudio':
    set_variables()
elif menu == 'Otras variables':
    set_otras_variables()
elif menu == 'Relaciones entre variables':
    set_relations()
elif menu == 'Matrices de correlación':
    set_arrays()
