
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
                   layout="centered")


st.sidebar.image('images/epsilonlogo.png', width=200)
st.sidebar.header('Data Challenge 2021')
st.sidebar.markdown('Analyse exploratoire des données Microfaune de Dataforgood')


menu = st.sidebar.radio(
    "",
    ("Intro", "Data", "Variables de estudio", 'Otras variables', "Relaciones entre variables", "Matrices de correlación"),
)

# Pone el radio-button en horizontal. Afecta a todos los radio button de una página.
# Por eso está puesto en este que es general a todo
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.markdown('---')
st.sidebar.write('Equipe Hibou')
st.sidebar.write('Décembre 2021')

if menu == 'Intro':
    set_home()
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
