# Point class

The `Point` class describes a point within an _n_-dimensional volume.

The class' generic type describes the coordinate type of each dimension, and must be specified as a tuple:

```python
from bounden import Point

in_line = Point[tuple[int]]((0,))
in_rect = Point[tuple[int, int]]((0, 0))
in_cube = Point[tuple[int, int, int]]((0, 0, 0))
```

Coordinates are read from the `value` property:

```python
from bounden import Point

point = Point[tuple[int, int, int]]((1, 2, 3))
print(point.value)
# (1, 2, 3)
```
