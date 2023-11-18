"""
CSCC11 - Introduction to Machine Learning, Winter 2022, Assignment 4
B. Chan, S. Wei, D. Fleet
"""

import numpy as np

def kmeans_pp(K, train_X):
    """ This function runs K-means++ algorithm to choose the centers.

    Args:
    - K (int): Number of centers.
    - train_X (ndarray (shape: (N, D))): A NxD matrix consisting N D-dimensional input data.

    Output:
    - centers (ndarray (shape: (K, D))): A KxD matrix consisting K D-dimensional centers.
    """
    centers = np.empty(shape=(K, train_X.shape[1]))

    # ====================================================
    # TODO: Implement your solution within the box
    N = train_X.shape[0]
    X = np.copy(train_X)
    distances = np.zeros(shape=N, dtype=np.longdouble)
    centers[0] = X[np.random.randint(N)]
    for i in range(1, K):
        for j in range(N):
            minn = np.inf
            for k in range(i):
                if np.linalg.norm(X[j] - centers[k]) < minn:
                    minn = np.linalg.norm(X[j] - centers[k])
            distances[j] = minn
        prob = (distances**2)/sum(distances**2)
        centers[i] = X[np.random.choice(N, p=prob)]
    # ====================================================

    return centers

def random_init(K, train_X):
    """ This function randomly chooses K data points as centers.

    Args:
    - K (int): Number of centers.
    - train_X (ndarray (shape: (N, D))): A NxD matrix consisting N D-dimensional input data.

    Output:
    - centers (ndarray (shape: (K, D))): A KxD matrix consisting K D-dimensional centers.
    """
    centers = train_X[np.random.randint(train_X.shape[0], size=K)]
    return centers
