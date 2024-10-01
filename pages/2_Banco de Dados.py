import streamlit as st
from PIL import Image

st.title('Banco de Dados')

tab1, tab2 = st.tabs(["PNAD Covid-19","Big Query"])
with tab1:
    st.markdown("""
    ### PNAD COVID
    
    A Pesquisa Nacional por Amostra de Domicílios – COVID-19, ou simplesmente [PNAD Covid](https://covid19.ibge.gov.br/), é uma iniciativa do Instituto Brasileiro de Geografia e Estatística (IBGE) que visa compreender os impactos da pandemia no Brasil. Através dessa pesquisa, buscou-se mensurar os efeitos da COVID-19 em diversas esferas, o que exigiu a aplicação de um extenso questionário, abordando questões clínicas, socioeconômicas e demográficas da população.

    Sem uma pesquisa dessa magnitude, seria extremamente difícil avaliar os problemas gerados pela pandemia e identificar os grupos mais vulneráveis à maior crise sanitária do século. A análise dos dados coletados pela PNAD Covid possibilita a formulação de estratégias políticas que não apenas minimizam os impactos da pandemia, mas também previnem cenários semelhantes no futuro.

    ### Seleção das Perguntas
    
    Na seleção das perguntas para análise dos dados, considerou-se a relevância de temas relacionados aos sintomas da COVID-19, o impacto na saúde, o acesso a serviços médicos e as medidas preventivas adotadas durante a pandemia. Além disso, foram incluídos dados sociodemográficos para permitir uma análise mais detalhada. A identificação de sintomas característicos, como febre, perda de olfato ou paladar e tosse, foi destacada como essencial para a detecção de possíveis padrões clínicos na manifestação da doença.

    Dentre as questões priorizadas, destacaram-se aquelas relacionadas ao impacto na saúde e à procura por atendimento médico. Essas informações são cruciais para avaliar a gravidade da condição de saúde dos indivíduos, a necessidade de recursos médicos e o acesso aos serviços de saúde. A inclusão de perguntas sobre a posse de plano de saúde, por exemplo, evidencia as desigualdades no acesso ao atendimento. Outro aspecto relevante é o procedimento de entubação, que requer treinamento especializado. A escassez de profissionais capacitados para realizar entubações seguras ressaltou a necessidade de investimento na formação e no preparo de equipes de saúde.

    Considerando o contexto da pandemia de COVID-19, foram incluídas perguntas sobre as medidas preventivas adotadas, como restrições ao contato social e a disponibilidade de itens básicos de limpeza e proteção nos domicílios. Essas informações são essenciais para compreender as práticas preventivas adotadas pela população e seu impacto na contenção da disseminação do vírus.

    Por fim, a inclusão de variáveis sociodemográficas, como idade, sexo, etnia, escolaridade e unidade federativa, visa permitir uma análise mais detalhada e estratificada dos resultados, levando em consideração as especificidades de diferentes grupos populacionais. Dessa forma, a escolha das perguntas reflete a preocupação em obter dados abrangentes e significativos, que contribuam para uma melhor compreensão dos fenômenos em estudo e para o desenvolvimento de estratégias eficazes no âmbito da saúde pública.
   
    Veja abaixo os itens selecionados:
    #### Perguntas Clínicas
    | Pergunta | Código | Descrição |
    | --- | --- | --- |
    | 1 | B0011 | Na semana passada teve febre? |
    | 2 | B00110 | Na semana passada teve dor nos olhos? |
    | 3 | B00111 | Na semana passada teve perda de cheiro ou sabor? |
    | 4 | B00112 | Na semana passada teve dor muscular? |
    | 5 | B00113 | Na semana passada teve diarreia? |
    | 6 | B0012 | Na semana passada teve tosse? |
    | 7 | B0013 | Na semana passada teve dor de garganta? |
    | 8 | B0014 | Na semana passada teve dificuldade para respirar? |
    | 9 | B0015 | Na semana passada teve dor de cabeça? |
    | 10 | B0016 | Na semana passada teve dor no peito? |
    | 11 | B0017 | Na semana passada teve náusea? |
    | 12 | B0018 | Na semana passada teve nariz entupido ou escorrendo? |
    | 13 | B0019 | Na semana passada teve fadiga? |
    | 14 | B002 | Por causa disso, foi a algum estabelecimento de saúde? |
    | 15 | B006 | Durante a internação, foi sedado, entubado e colocado em respiração artificial com ventilador |
    | 16 | B007 | Tem algum plano de saúde médico, seja particular, de empresa ou de órgão público |
    | 17* | B009B | Qual o resultado? (SWAB) |
    | 17* | B009D | Qual o resultado? (Dedo) |
    | 17* | B009F | Qual o resultado? (Veia) |
    | 18 | B011 | Na semana passada, devido à pandemia do Coronavírus, em que medida o(a) Sr(a) restringiu o contato com as pessoas? |
    | 19 | F002A2 | Na semana passada, o(a) Sr(a) estava em trabalho remoto (home office ou teletrabalho)? |
    | 20 | F002A3 | No seu domicílio há os seguintes itens básicos de limpeza e proteção: máscaras |

    * Foi considerado apenas uma pergunta para essas 3, visto que juntas elas dão a resposta do teste para COVID de forma geral.

    #### Informações Pessoais
    | Código | Descrição |
    | --- | --- |
    | A002 | Idade do morador |
    | A003 | Sexo |
    | A004 | Cor ou raça |
    | A005 | Escolaridade |
    | UF | Unidade da Federação |
    | mês | Mês da pesquisa |
    | V1022 | Situação do domicílio |


    """)
with tab2:
    st.markdown("""
    ### BigQuery
    
    No trabalho mencionado, uma fonte fundamental de dados para a nossa análise foi o Google BigQuery. O Google BigQuery é um serviço de data warehouse e análise de dados na nuvem, oferecido pela Google Cloud Platform, que permite o processamento e a análise de grandes volumes de dados de maneira eficiente, com consultas rápidas e escalabilidade ajustável conforme a demanda.

    Os dados da Pesquisa Nacional por Amostra de Domicílios (PNAD) foram armazenados no Google BigQuery, podendo ser acessados através deste [link](https://basedosdados.org/dataset/c747a59f-b695-4d19-82e4-fef703e74c17?table=5894e1ac-dc08-465d-91a3-703683da85ba). Utilizando essa plataforma, foi possível acessar, explorar e analisar os dados da PNAD de forma ágil e eficiente, permitindo a execução de consultas complexas e a extração de insights relevantes para o nosso estudo.

    ### Procedimentos Executados

    Para a análise, foi realizada uma consulta em SQL para extrair todos os dados pertinentes dos meses de setembro a novembro de 2020. A consulta SQL utilizada está representada na imagem a seguir
    """)
    image = Image.open("./imagens/Base de Dados/2QueryBigQuery.png")
    st.image(image)
    st.markdown("""
    O resultado dessa extração foi armazenado no Google Cloud, no seguinte caminho: "techchallengepnad.Pnad91011.TabelaPrincipal09a11".
    """   )
    image = Image.open("./imagens/Base de Dados/3BaseAposQuery.png")
    st.image(image)
    image = Image.open("./imagens/Base de Dados/4detalhesBasePosQuery.png")
    st.image(image)
    st.markdown(""" 
    Em seguida, utilizamos o Google Colab para acessar essa base de dados previamente criada, onde novas consultas SQL foram realizadas. 
    
    Um exemplo de acesso via Google Colab pode ser visualizado na imagem abaixo:
       
    """   )
    image = Image.open("./imagens/Base de Dados/notebook.png")
    st.image(image)
