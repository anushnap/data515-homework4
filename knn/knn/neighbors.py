# ADD IMPORTS HERE


def calculate_distance(x1, x2):
    """Returns the distance between m-dimensional
    points x1 and x2.
    """
    # ADD IMPLEMENTATION HERE

def find_neighbor_indices(X, query):
    """Returns 1-dimensional numpy array of shape (m,)
    where each value is the argsort of the distance.

    See numpy's argsort().

    Parameters:
    X - numpy array of shape (m, n) where each row represents 
    a data point and each column represents a feature
    query - numpy array of shape (m, 1)

    Example:
    X = np.array([[3, 1], [6, 2], [6, 6]])
    query = np.array([8, 10])
    find_neighbor_indices(X, query)

    returns np.array([2, 1, 0]).
    """

    # ADD IMPLEMENTATION HERE
