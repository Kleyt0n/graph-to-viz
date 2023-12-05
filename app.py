import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

import sys
sys.path.append('./')


st.set_page_config(layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', False)

st.sidebar.title("graph2viz")

data_name = st.sidebar.selectbox("Select dataset:", ["KarateClub"])
if data_name == 'KarateClub':
    name = "The data was collected from the members of a university karate club by Wayne Zachary in 1977. Each node represents a member of the club, and each edge represents a tie between two members of the club. The network is undirected. An often discussed problem using this dataset is to find the two groups of people into which the karate club split after an argument between two teachers."
st.sidebar.caption(name)

centrality_name = st.sidebar.selectbox("Select centrality measure:", ["Degree", "Closeness", "Betweenness", "Eigenvector", "Katz", "Pagerank"])

if centrality_name == "Degree":
    metric = "The degree centrality for a node v is the fraction of nodes connected to it."
elif centrality_name == "Closeness":
    metric = "The closeness of a node is the distance to all other nodes in the graph or in the case that the graph is not connected to all other nodes in the connected component containing that node."
elif centrality_name == "Betweenness":
    metric = "Betweenness centrality of a node v is the sum of the fraction of all-pairs shortest paths that pass through v."
elif centrality_name == "Eigenvector":
    metric = "Eigenvector centrality computes the centrality for a node by adding the centrality of its predecessors."
elif centrality_name == "Katz":
    metric = "Katz centrality computes the centrality for a node based on the centrality of its neighbors. It is a generalization of the eigenvector centrality."
elif centrality_name == "Pagerank":
    metric = "PageRank computes a ranking of the nodes in the graph G based on the structure of the incoming links."
st.sidebar.caption(metric)

from torch_geometric.utils import scatter
from graphtoviz.datasets import read_data

loader = read_data(data_name)

from graphtoviz.plots import plot_graph, plot_centrality, plot_adjacency_matrix, visualize_communities
from graphtoviz.metrics import summary_metrics


tab1, tab2 = st.tabs(["Descrição do Projeto", "Visualizações"])

with tab1:
    st.title("graph2viz")
    st.markdown("Desenvolvido por Kleyton da Costa (2312730)")
    st.markdown("## Domínio do problema")
    st.markdown("O projeto foi desenvolvido para gerar visualizações em grafos, trazendo avaliações a partir do grau de centralidade dos nós.")
    st.markdown("A visualização de informações na forma de grafos é uma das maneiras mais eficientes para observarmos sistemas complexos em diferentes contextos. Um grafo (ou rede complexa) é um avanço da matemática discreta que possui dois elementos básicos: vértices e arestas. Os vértices representam entidades e as aretas representam a (in)existência de relacionamento entre estas entidades. O número de exmeplos de redes complexas é extenso, passando por fenômenos físicos, biológicos, sociais e tecnológicos.")
    st.markdown(" - Redes de transporte: aeroportos, portos, rodovias,...")
    st.markdown(" - Redes sociais: facebook, instagram, bluesky, linkedin,...")
    st.markdown(" - Redes de conhecimento: citações, registro de informações empresariais, ...")
    st.markdown("Podemos ilustrar um grafo da seguinte marneira:")
    st.image('imgs/networks-basic.svg')
    st.markdown("Em um contexto de redes sociais os vértices são os indívidos que fazem parte da rede e as arestas são as relações entre estes indivíduos, por exemplo, se o A segue B.")
    st.image('imgs/networks-social.svg')
    st.markdown("No caso de uma rede de transporte (como aeroportos) podemos construir da seguinte maneira:")
    st.image('imgs/networks-airplane.svg')
    st.markdown("Nessa rede temos diversos aeroportos e se existe uma conexão entre eles. Um ponto que chama a atenção é o aeroporto A10. Esse aeroporto pode ser considerado um hub, ou seja, possui conexão com inúmeros aeroportos. Assim, dizemos que o grau de centralidade do aeroporto A10 é alto. Sendo o grau de centralidade computado pela razão entre o número de arestas que chegam até o aeroporto e o número total de arestas que existem no grafo. As métricas de centralidade atuam como bons indicadores para descrever as características de uma rede complexa. Podemos computar diferentes tipos de centralidade, mas neste trabalho daremos ênfase para algumas delas.")    
    
    st.markdown("## Perguntas de análise")
    st.markdown("- As métricas de centralidade são instrumento intuitivos para a interpretação de um grafo?")
    st.markdown("- Ao introduzirmos contexto em um grafo, podemos melhorar a identificação de centralidades e comunidades?")

    st.markdown("## Datasets")
    st.markdown("Os dados foram obtidos através da biblioteca open-source  [PyG](https://pytorch-geometric.readthedocs.io/en/latest/modules/datasets.html)")
    st.markdown("Foi considerado o dataset KarateClub para ser analisado:")
    st.markdown(" - KarateClub: esta é a conhecida rede de clubes de Karate Zachary. Os dados foram coletados dos membros de um clube universitário de Karate por Wayne Zachary em 1977. Cada nó representa um membro do clube e cada aresta representa a existeência de um relacionamento fora do Karate entre dois membros do clube. A rede não é direcionada. Ao todo a rede possui 34 vértices e 156 arestas.")
    st.markdown("Zachary, W. W. (1977). An Information Flow Model for Conflict and Fission in Small Groups. Journal of Anthropological Research, 33(4), 452–473. doi:10.1086/jar.33.4.3629752")

    st.markdown("## Avaliação das visualizações")

    st.markdown("A avaliação foi feita a partir de uma entrevista. O entrevistado possui o seguinte perfil:")
    st.markdown("- mestrado em Ciência da Computação pela Technische Universität Munich (TUM)")
    st.markdown("- experiência em análise de dados")
    st.markdown("- sem experiência com análise de grafos")
    st.markdown("---")

    st.markdown("Com base no dataset KarateClub o entrevistado foi solicitado para responder às perguntas seguindo a seguinte dinâmica.")
    st.markdown("_(sem contexto): não é explicado sobre do que se trata o grafo e o que são métricas de centralidade_")
    st.markdown("_(com contexto): descrição do problema visualizado no grafo e explicação do que as métricas de centralidade apresentam_")
    st.markdown("**KarateClub**")
    st.markdown("1. (sem contexto) Como você separaria o grafo em dois grupos de vértices?")
    st.markdown("_Foi solicitado que ele utilizasse uma linha para separar os grupos_")
    st.markdown("**Resposta:**")
    st.image('imgs/q1.png')
    st.markdown("2. (com contexto) Quais membros do clube de Karate provalmente são amigos fora do clube?")
    st.markdown("**Resposta:**")
    st.markdown("- 0, 32 e 33 são populares. Possuem muitos amigos.")
    st.image('imgs/q2.png')
    st.markdown("3. (com contexto) Após um conflito entre dois instrutures o clube se dividiu em dois. Quais são os membros dos novos grupos?")
    st.markdown("_Foi solicitado que ele utilizasse uma linha para separar os grupos_")
    st.image('imgs/q3.png')
    st.markdown("4. Métricas de centralidade são fáceis de entender.")
    st.markdown("**Resposta:**")
    st.markdown("- Degree: concordo plenamente")
    st.markdown("5. Contexto me ajudou a definir melhor as comunidades no grafo.")
    st.markdown("**Resposta:**")
    st.markdown("- concordo")

    st.markdown("## Extra")
    st.markdown("Abaixo segue a divisão sugerido pelo algortimo de detecção de comunidades.")
    st.image('imgs/community.png')

with tab2:
    col1, col2 = st.columns(2, gap="medium")
    for data in loader:
        print(data)
        x = scatter(data.x, data.batch, dim=0, reduce='mean')
        x.size()

    with col1:
        fig = plot_graph(data, with_labels=True)
        st.pyplot(fig)

        adj = plot_adjacency_matrix(data)
        st.pyplot(adj)

    with col2:
        #label = st.toggle('Show Labels', False)
        #if label:
        #    label = True
        c = plot_centrality(data, centrality_name, labels=True)
        st.pyplot(c)

        cm = visualize_communities(data, 1)
        st.pyplot(cm)

    st.text(f"Table with {centrality_name} ranking for {data_name} dataset")
    metrics = summary_metrics(data)
    tab = pd.DataFrame.from_dict(metrics[centrality_name], orient='index', columns=[centrality_name]).sort_values(by=centrality_name, ascending=False).head(10)
    tab = tab.rename(index = {'0': 'Node'})
    st.table(tab)
