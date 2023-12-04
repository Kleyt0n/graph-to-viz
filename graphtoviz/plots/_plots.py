import networkx as nx
import torch_geometric
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns
import numpy as np

def plot_graph(data, with_labels=False, node_color='gray', 
               node_size=500, alpha=0.8, linewidths=1, width=1.0, 
               edge_color='slategray', style='solid', font_size=12, font_color='k', 
               font_weight='normal', font_family='sans-serif'):
    if not isinstance(data, nx.Graph):
        d = torch_geometric.utils.to_networkx(data)
    else :
        d = data
    pos = nx.fruchterman_reingold_layout(d, seed=42)
    fig = plt.figure(figsize=(5,5))
    nx.draw(d, pos=pos, with_labels=with_labels, node_color=node_color, node_size=node_size, alpha=alpha,
            linewidths=linewidths, width=width, edge_color=edge_color, style=style, font_size=font_size,
            font_color=font_color, font_weight=font_weight, font_family=font_family,
           )            
    plt.title("Graph")
    plt.axis("off")

def plot_centrality(G, measure_name, labels=False):
    if not isinstance(G, nx.Graph):
        d = torch_geometric.utils.to_networkx(G)
    else :
        d = G
    
    switch = {
        "Degree": nx.degree_centrality(d),
        "Betweenness": nx.betweenness_centrality(d),
        "Closeness": nx.closeness_centrality(d),
        "Eigenvector": nx.eigenvector_centrality(d),
        "Katz": nx.katz_centrality(d),
        "Pagerank": nx.pagerank(d),
        "Clustering": nx.clustering(d),
    }
    if measure_name not in switch.keys():
        raise ValueError("measure_name must be one of {}".format(switch.keys()))
    measures = switch[measure_name]
    pos = nx.spring_layout(d, seed=42)
    fig = plt.figure(figsize=(5,5))
    nodes = nx.draw_networkx_nodes(d, 
                                   pos, 
                                   node_size=400, 
                                   cmap=plt.cm.bwr, 
                                   node_color=list(measures.values()),
                                   nodelist=measures.keys(),
                                   alpha=0.8, 
                                   linewidths=1)
    nodes.set_norm(mcolors.SymLogNorm(linthresh=0.01, 
                                      linscale=1, 
                                      base=10))
    if labels is not False: labels = nx.draw_networkx_labels(d, 
                                                             pos, 
                                                             font_size=12, 
                                                             font_color='k', 
                                                             font_weight='normal', 
                                                             font_family='sans-serif')
    edges = nx.draw_networkx_edges(d, 
                                   pos, 
                                   edge_color='slategray', 
                                   style='solid')
    plt.title(measure_name)
    plt.colorbar(nodes, label=measure_name)
    plt.axis('off')

def plot_adjacency_matrix(data):
    if not isinstance(data, nx.Graph):
        d = torch_geometric.utils.to_networkx(data)
    else :
        d = data
    A = nx.adjacency_matrix(d).toarray()
    mask = np.triu(np.ones_like(A), k=1).astype(bool)
    fig, ax = plt.subplots(figsize=(15, 10))
    ax.set_title("Adjancency Matrix")
    sns.heatmap(A, cmap="bwr", square=True, mask=mask, linewidths=1)
    plt.xlabel("Node")
    plt.ylabel("Node")
    cbar = ax.collections[0].colorbar
    cbar.set_ticks([0, 1])
    cbar.set_ticklabels(["Not Connected", "Connected"])