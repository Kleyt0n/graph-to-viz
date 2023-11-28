import networkx as nx

def summary_metrics(graph):
    """Computes the summary metrics of the graph.

    Args:
        graph (networkx.classes.graph.Graph): Graph object.

    Returns:
        dict: Dictionary containing the summary metrics.
    """

    import numpy as np
    summary = {}
    summary["betweenness_centrality"] = nx.betweenness_centrality(graph)
    summary["degree_centrality"] = nx.degree_centrality(graph)
    summary["closeness_centrality"] = nx.closeness_centrality(graph)
    summary["eigenvector_centrality"] = nx.eigenvector_centrality(graph)
    summary["pagerank"] = nx.pagerank(graph)
    summary["average_clustering"] = nx.average_clustering(graph)
    summary["average_shortest_path_length"] = nx.average_shortest_path_length(graph)
    summary["diameter"] = nx.diameter(graph)
    summary["radius"] = nx.radius(graph)
    summary["periphery"] = nx.periphery(graph)
    summary["center"] = nx.center(graph)
    summary["density"] = nx.density(graph)

    return summary
