import networkx as nx
import torch_geometric
import matplotlib.pyplot as plt
from pyvis.network import Network

def plot_graph(data, with_labels=False, node_color='gray', 
               node_size=500, alpha=0.8, linewidths=1, width=1.0, 
               edge_color='slategray', style='solid', font_size=12, font_color='k', 
               font_weight='normal', font_family='sans-serif'):
    """Plots the graph.

    Args:
        data (torch_geometric.data.Data): Data object containing the graph.
        with_labels (bool, optional): Whether to plot the node labels. Defaults to True.
        node_color (str, optional): Color of the nodes. Defaults to 'blue'.
        node_size (int, optional): Size of the nodes. Defaults to 500.
        alpha (float, optional): Opacity of the nodes. Defaults to 0.8.
        linewidths (int, optional): Width of the node borders. Defaults to 1.
        width (float, optional): Width of the edges. Defaults to 1.0.
        edge_color (str, optional): Color of the edges. Defaults to 'k'.
        style (str, optional): Style of the edges. Defaults to 'solid'.
        font_size (int, optional): Size of the node labels. Defaults to 12.
        font_color (str, optional): Color of the node labels. Defaults to 'k'.
        font_weight (str, optional): Weight of the node labels. Defaults to 'normal'.
        font_family (str, optional): Font family of the node labels. Defaults to 'sans-serif'.

    Returns:
        networkx.classes.graph.Graph: Graph object.
    """

    if not isinstance(data, nx.Graph):
        d = torch_geometric.utils.to_networkx(data)
    else :
        d = data
    pos = nx.spring_layout(d)
    fig = plt.figure(figsize=(5,5))
    nx.draw(d, pos=pos, with_labels=with_labels, node_color=node_color, node_size=node_size, alpha=alpha,
            linewidths=linewidths, width=width, edge_color=edge_color, style=style, font_size=font_size,
            font_color=font_color, font_weight=font_weight, font_family=font_family,
           )            
    plt.title("Graph")
    plt.axis("off")
    plt.show()