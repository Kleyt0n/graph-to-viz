from torch_geometric.datasets import TUDataset, KarateClub, Planetoid, Amazon, Actor, Coauthor
from torch_geometric.loader import DataLoader

datasets = {
    "TUDataset": TUDataset(root='/tmp/ENZYMES', name='ENZYMES', use_node_attr=True),
    "KarateClub": KarateClub(),
    "Planetoid": Planetoid(root='/tmp/Cora', name="Cora"),
    "AmazonComputers": Amazon(root='/tmp/Amazon', name = "Computers"),
    "AmazonPhoto": Amazon(root='/tmp/Amazon', name = "Photo"),
    "Actor": Actor(root='/tmp/Actor'),
    "Coauthor": Coauthor(name='CS', root='/tmp/Coauthor')
    }

def read_data(dataset_name):
    """Reads the dataset and returns a DataLoader object.

    Args:
        dataset_name (str): Name of the dataset to be read.
                            "TUDataset", "KarateClub", "Planetoid"

    Returns:
        DataLoader: DataLoader object containing the dataset.
    """
    if dataset_name in datasets.keys():
        loader = DataLoader(datasets[dataset_name], batch_size=32, shuffle=True)
        return loader
    else:
        raise ValueError("Dataset not found.")