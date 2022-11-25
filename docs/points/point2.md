# Point2 class

The `Point2` class wraps and simplifies the [`Point` class](./point.md) to describe a point in two-dimensional space.

The class requires two generic types: the types of the `x` and `y` axis respectively:

```python
from bounden import Point2

in_int_rectangle = Point2[int, int](2, 4)
in_float_rectangle = Point2[float, float](1.2, 1.4)
in_spreadsheet = Point2[str, int]("A", 7)
```

Coordinates are read from the `x` and `y` properties.
