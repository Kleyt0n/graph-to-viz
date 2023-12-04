import networkx as nx
import torch_geometric

def summary_metrics(data):
    """Computes the summary metrics of the graph.

    Args:
        graph (networkx.classes.graph.Graph): Graph object.

    Returns:
        dict: Dictionary containing the summary metrics.
    """
    if not isinstance(data, nx.Graph):
        graph = torch_geometric.utils.to_networkx(data)
    else :
        graph = data

    import numpy as np
    summary = {}
    summary["Betweenness"] = nx.betweenness_centrality(graph)
    summary["Degree"] = nx.degree_centrality(graph)
    summary["Closeness"] = nx.closeness_centrality(graph)
    summary["Eigenvector"] = nx.eigenvector_centrality(graph)
    summary["Pagerank"] = nx.pagerank(graph)
    summary["Katz"] = nx.katz_centrality(graph)
    summary["Clustering"] = nx.clustering(graph)

    return summary
