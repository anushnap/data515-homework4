# ADD IMPORTS HERE


def vote(y, neighbor_array, n_neighbors):
    """Returns majority vote for classification tasks.
    In case of tie, return the output of highest
    frequency across the full dataset added to model.
    If that is also a tie, return list with those values.

    Parameters:
    y - numpy array of shape (n,) where each value is an output
    neighbor_index_array - numpy array of shape (m,) that
    indicates the argsort for each data point. See
    neighbors.find_neighbor_indices.
    n_neighbors - number of data points to consider for voting

    Returns: string or list of strings
    """
    # ADD IMPLEMENTATION HERE
