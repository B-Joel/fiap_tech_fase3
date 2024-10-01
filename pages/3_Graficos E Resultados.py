import streamlit as st
from PIL import Image

st.title('Gráficos e Resultados')
st.markdown("""
    No presente estudo, utilizamos gráficos para realizar análises detalhadas das características demográficas e dos sintomas relatados pela população, com o intuito de compreender melhor a disseminação e os impactos da COVID-19. A seguir, apresentamos os resultados das análises de acordo com as variáveis estudadas.
    """)
tab1, tab2 = st.tabs(["Análise Demográfica","Análise de Sintomas"])

with tab1:
    st.markdown("""
    ## Análise Demográfica
    A análise demográfica visa examinar aspectos **sociais, clínicos e econômicos** da população participante.
    
    ### Gênero e Incidência
    O gráfico a seguir ilustra a distribuição de respostas da pesquisa por gênero e a porcentagem de testes positivos para COVID-19. 
    Observa-se uma participação majoritária de mulheres na pesquisa, com uma leve predominância de testes positivos entre elas.
    """)
    image = Image.open("./imagens/Graficos/barras_teste_positivo_por_sexo.png")
    st.image(image)

    st.markdown("""
    ### Faixa Etária e Porcentagem de Teste Positivo
    
    Na análise por faixa etária, é evidente que as faixas mais jovens (0 a 20 anos) apresentaram poucos casos positivos, enquanto a maior incidência de diagnósticos foi observada entre a população economicamente ativa e os idosos, refletindo o impacto desigual da pandemia.
    """)
    image = Image.open("./imagens/Graficos/teste_positivo_por_faixa_etaria.png")
    st.image(image)
    
    st.markdown("""
    ### Composição Geral por Etnia e Positividade de Teste
    
    A análise por etnia revela uma maior incidência de casos positivos entre a população indígena, grupo socialmente vulnerável que requer atenção especial por parte das políticas públicas de saúde, dada sua suscetibilidade a doenças infecciosas.
    """)
    image = Image.open("./imagens/Graficos/barras_teste_positivo_por_etnia.png")
    st.image(image)
    
    st.markdown("""
    ### Top 10 Estados por Porcentagem de Respondentes e Testes Positivos
    
    No gráfico que compara os estados, verificamos que o Maranhão apresentou uma maior porcentagem de testes positivos, enquanto Minas Gerais, que teve o maior número de respondentes, apresentou uma menor taxa de positividade. Cabe ressaltar que essa disparidade pode ser influenciada por diferentes políticas de testagem entre os estados, o que deve ser considerado na interpretação dos dados.
    """)
    image = Image.open("./imagens/Graficos/estadosEpositivos.png")
    st.image(image)
  
    st.markdown("""
    ### Composição por Escolaridade e Testes Positivos
    
    A análise por escolaridade indica uma maior incidência de testes positivos entre as pessoas com níveis educacionais mais altos. Uma possível explicação para esse fenômeno é que indivíduos com maior escolaridade tendem a ser mais economicamente ativos, o que pode resultar em uma maior exposição ao vírus.
    """)
    image = Image.open("./imagens/Graficos/escolaridadeEpositivos.png")
    st.image(image)
    
    st.markdown("""
    ### Distribuição de Plano de Saúde
    
    O gráfico de distribuição de plano de saúde mostra que a maior parte dos respondentes não possui plano de saúde complementar, dependendo exclusivamente do Sistema Único de Saúde (SUS). Este dado reforça a importância do SUS no atendimento à população durante situações emergenciais, como a pandemia.
    """)
    image = Image.open("./imagens/Graficos/pizzaPlanoSaude.png")
    st.image(image)
    
    st.markdown("""
    ### Uso de Máscaras
    
    Quase a totalidade dos respondentes reportou o uso de máscaras, o que sugere que as campanhas de conscientização e as políticas públicas voltadas para o uso dessa medida de proteção foram bem-sucedidas.
    """)
    image = Image.open("./imagens/Graficos/treeUsoMascara.png")
    st.image(image)
    
    st.markdown("""
    ### Isolamento Social
    
    A relação entre o isolamento social e a taxa de testes positivos mostra que pessoas que se expuseram menos ao risco de contato social tiveram menor chance de testar positivo para COVID-19, indicando a eficácia das medidas de distanciamento social.
    """)
    image = Image.open("./imagens/Graficos/RestricaovsPositivos.png")
    st.image(image)

with tab2:
    st.markdown("""
    ### Sintomas Mais Comuns x Sintomas Associados a Testes Positivos
    
    A análise dos sintomas mostra, à esquerda, os sintomas mais frequentemente relatados, como dor de cabeça, nariz entupido e tosse. À direita, observamos os sintomas mais fortemente associados a testes positivos para COVID-19, como dor de cabeça, tosse, dor muscular, febre, fadiga e dificuldade com cheiro e sabor. Sintomas menos comuns, como alteração no olfato e paladar, merecem maior atenção dos profissionais de saúde.
    """)
    image = Image.open("./imagens/Graficos/SintomasVsPositivos.png")
    st.image(image)
    
    st.markdown("""
    ### Percentual de Pessoas Entubadas por Sintoma
    
    Entre os pacientes que necessitaram de entubação, a maioria apresentou sintomas como dificuldade respiratória, tosse, febre, fadiga e dor muscular. No entanto, uma análise adicional revela que pessoas que relataram dor no peito, alterações no olfato e paladar, febre, náusea e fadiga na semana anterior à hospitalização apresentaram maior probabilidade de necessitar de ventilação mecânica.
    
    Sintomas das pessoas entubadas:
    """)
    image = Image.open("./imagens/Graficos/EntubadosTiveramSintomas.png")
    st.image(image)
    st.markdown("""
    Indice de entubação por sintoma:
    """)
    image = Image.open("./imagens/Graficos/SintomasVsEntubados.png")
    st.image(image)
