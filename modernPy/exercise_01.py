from collections import defaultdict
from functools import partial
from math import fsum, sqrt
from pprint import pprint
from random import sample
from typing import DefaultDict, Dict, Iterable, List, Sequence, Tuple

import numpy as np
from sklearn.datasets import load_iris

dataset = load_iris()

data = np.array(dataset.data)

observations = list(map(tuple, data))

Dimension = Tuple[int, ...]
Centroids = Dimension


def mean(data: Iterable[float]) -> float:
    data = list(data)
    return fsum(data) / len(data)


def dist(point1: Dimension, point2: Dimension) -> float:
    return sqrt(fsum((x - y)**2 for x, y in zip(point1, point2)))


def assing_points_to_clusters(
        observations: Iterable[Dimension],
        centroids: Sequence[Centroids]) -> Dict[Centroids, List[Dimension]]:
    '''Assign the observations to the closest centroids'''
    clusters = defaultdict(list)
    for point in observations:
        closest_centroid = min(centroids, key=partial(dist, point))
        clusters[closest_centroid].append(point)
    return dict(clusters)


def compute_centroids(
        clusters: Dict[Centroids, List[Dimension]]) -> List[Dimension]:
    '''Compute the centroids of the clusters'''
    return [tuple(map(mean, zip(*cluster))) for cluster in clusters.values()]


def k_means(observations: Iterable[Dimension],
            k,
            iterations=100) -> List[Centroids]:
    '''Compute the k-means clustering'''
    centroids = sample(observations, k)
    for i in range(iterations):
        clusters = assing_points_to_clusters(observations, centroids)
        new_centroids = compute_centroids(clusters)
        if new_centroids == centroids:
            return centroids
        centroids = new_centroids


if __name__ == '__main__':
    centroids = k_means(observations, 3)
    d = assing_points_to_clusters(observations, centroids)
    pprint(object=d, width=20)
