from typing import List, Dict, Iterable, Tuple, Set, Optional
from math import sqrt, fsum
from collections import defaultdict
from pprint import pprint
from functools import partial

Point = Tuple[int, ...]

points = [
    (10, 41, 23),
    (22, 30, 29),
    (11, 42, 5),
    (22, 30, 4),
    (12, 40, 12),
    (21, 36, 23),
]

centroids = [(10, 41, 23), (22, 30, 29)]


def euclidean_distance(point1: Point,
                       point2: Point,
                       fsum=fsum,
                       sqrt=sqrt,
                       zip=zip) -> float:
    return sqrt(fsum((x - y)**2 for x, y in zip(point1, point2)))


def mean(data: Iterable[float]) -> float:
    data = list(data)
    return fsum(data) / len(data)


def assign_points_to_clusters(
        points: List[Point],
        centroids: List[Point]) -> Dict[Point, List[Point]]:
    clusters = defaultdict(list)
    for point in points:
        closest_centroid = min(centroids,
                               key=partial(euclidean_distance, point))
        clusters[closest_centroid].append(point)
    return clusters


def compute_centroids(clusters: Dict[Point, List[Point]]) -> List[Point]:
    return [tuple(map(mean, zip(*cluster))) for cluster in clusters.values()]


pprint(assign_points_to_clusters(points, centroids), width=90)


def k_means(points: List[Point], centroids: List[Point]) -> List[Point]:
    clusters = assign_points_to_clusters(points, centroids)
    new_centroids = compute_centroids(clusters)
    if new_centroids == centroids:
        return centroids
    return k_means(points, new_centroids)


pprint(k_means(points, centroids))