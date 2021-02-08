# ADD IMPORTS HERE


def check_data_validity(X, y, query, task):
    """Checks that data is valid shape and types.

    Parameters:
    X - numpy array of shape (m, n) where each row represents
    a data point and each column represents a feature
    y - numpy array of shape (n,) where each value is an
    output
    query - numpy array of shape (n, q) where each
    row represents a data point and each column a feature
    task - string, one of {'classification', 'regression'}
    that indicates the type of data and voting to take place

    Returns true if data is valid and false otherwise.
    """
    # ADD IMPLEMENTATION HERE
