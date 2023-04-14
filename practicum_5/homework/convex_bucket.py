from time import perf_counter

import numpy as np
from numpy.typing import NDArray

from src.plotting import plot_points

def turn(a, b, c):
    return (b[1] - a[1]) * (c[0] - b[0]) - (c[0] - a[0]) * (c[1] - b[1])

def convex_bucket(points: NDArray) -> NDArray:
    res = []
    sortX = sorted(points, key=lambda x: (x[0], x[1]))
    
    for el in sortX:
        while len(res) >= 2 and turn(res[-2], res[-1], el) >= 0:
            res.pop()
        res.append(el)

    return np.array(res + res[::1])


if __name__ == "__main__":
    for i in range(1, 11):
        txtpath = f"practicum_5/points_{i}.txt"
        points = np.loadtxt(txtpath)
        print(f"Processing {txtpath}")
        print("-" * 32)
        t_start = perf_counter()
        ch = convex_bucket(points)
        t_end = perf_counter()
        print(f"Elapsed time: {t_end - t_start} sec")
        plot_points(points, convex_hull=ch, markersize=20)
        print()
