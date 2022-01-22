import random

import taichi as ti

def test_minimization():
    from taichi.examples.autodiff.minimization import reduce, gradient_descent, x, y, n, L

    for i in range(n):
        x[i] = random.random()
        y[i] = random.random()

    for k in range(100):
        with ti.Tape(loss=L):
            reduce()
        gradient_descent()

    for i in range(n):
        assert x[i] == ti.approx(y[i], rel=1e-3)
