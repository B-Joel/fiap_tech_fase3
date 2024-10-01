import streamlit as st
from PIL import Image
st.title('Desafio')
st.markdown("""
Imagine agora que você foi contratado(a) como Expert em Data Analytics 
por um grande hospital para entender como foi o comportamento da população 
na época da pandemia da COVID-19 e quais indicadores seriam importantes 
para o planejamento, caso haja um novo surto da doença. 

Apesar de ser contratado(a) agora, a sua área observou que a utilização 
do estudo do [PNAD-COVID 19 do IBGE](https://covid19.ibge.gov.br/pnad-covid/) seria uma ótima base para termos boas 
respostas ao problema proposto, pois são dados confiáveis. Porém, não será 
necessário utilizar todas as perguntas realizadas na pesquisa para enxergar 
todas as oportunidades ali postas. 

É sempre bom ressaltar que há dados triviais que precisam estar no 
projeto, pois auxiliam muito na análise dos dados: 

- Características clínicas dos sintomas; 
- Características da população; 
- Características econômicas da sociedade. 

O Head de Dados pediu para que você entrasse na base de dados do 
PNAD-COVID-19 do IBGE e organizasse esta base para análise, utilizando 
Banco de Dados em Nuvem e trazendo as seguintes características: 

a. Utilização de no máximo 20 questionamentos realizados na pesquisa; 

b. Utilizar 3 meses para construção da solução; 

c. Caracterização dos sintomas clínicos da população; 

d. Comportamento da população na época da COVID-19; 

e. Características econômicas da Sociedade; 

Seu objetivo será trazer uma breve análise dessas informações, como foi 
a organização do banco, as perguntas selecionadas para a resposta do problema 
e quais seriam as principais ações que o hospital deverá tomar em caso de um 
novo surto de COVID-19.

""")