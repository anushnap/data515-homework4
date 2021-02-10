# ADD IMPORTS HERE


def predict(X, y, query, n_neighbors, task):
    """Predicts outputs for the given data and query after
    checking for data validity for all parameters.

    Parameters:
    X - numpy array of shape (m, n) where each
    row represents a data point and each column represents a feature
    y - numpy array of shape (n,) where each value is an output
    query - numpy array of shape (n, q) where each
    row represents a data point and each column a feature
    n_neighbors - number of data points to consider for voting
    task - string, one of {'classification', 'regression'}
    that indicates the type of data and voting to take place

    Returns 1-dimensional numpy array of shape (q,) of output
    predictions.
    """
    # ADD IMPLEMENTATION HERE
