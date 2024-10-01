import streamlit as st
from PIL import Image
st.set_page_config(page_title="PNAD COVID 19", page_icon=":house:",layout='wide')
image = Image.open("./imagens/covid.png")
st.image(image)


#Header
with st.container():

    st.title('Bem vindo(a)')
    st.title('Tech Challenge  Fase 3: PNAD-COVID 19')
    
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    st.write(
        """
        Estudo para a Pós Tech em Data Analytics da FIAP
        
        Grupo 66, Integrantes:
        - rm356228 - Joel Pedro Bellatto
        - rm356366 - Pedro de Almeida Matos
        - rm349836 - Micael Silva Lemos
        - rm355565 - Nathalia Alves da Silva Lima
        """
    )
