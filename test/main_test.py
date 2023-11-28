import sys
sys.path.append('./')

from torch_geometric.utils import scatter
from graphtoviz.datasets import read_data

loader = read_data("TUDataset")

for data in loader:
    x = scatter(data.x, data.batch, dim=0, reduce='mean')
    x.size()

from graphtoviz.plots import plot_graph
plot_graph(data[0])