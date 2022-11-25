# Region class

The `Region` class describes a region of _n_-dimensional space.

## Construction

Two generic types are required:

1. Tuple of axis types
1. Tuple of axis length types

You must also initialise the region with:

1. The position of the region's origin
1. The lengths of each of the region's dimensions

### Construction examples

Given one-dimensional space with an integer axis, this code describes the region that starts at `(2)` and is 3 units wide:

```python
from bounden import Region

region = Region[
    tuple[int],   # Axes
    tuple[float], # Axis lengths
](
    (2,), (3,),
)

#  0  1  2  3  4  5  6
#  .  . [x  x  x] .  .
```

Given one-dimensional space with a string axis, this code describes the region that starts at `(C)` and is 3 strings wide:

```python
from bounden import Region

region = Region[
    tuple[str],   # Axes
    tuple[float], # Axis lengths
](
    ("C",), (3,),
)

#  A  B  C  D  E  F
#  .  . [x  x  x] .
```

Given two-dimensional space with integer axes, this code describes the region that starts at `(1, 2)`, is 3 units wide and 4 units tall:

```python
from bounden import Region

region = Region[
    tuple[int,   int],   # Axes
    tuple[float, float], # Axis lengths
](
    (1, 2), (3, 4),
)

#     0  1  2  3  4  5
#  0  .  .  .  .  .  .
#  1  .  .  .  .  .  .
#  2  . [x  x  x] .  .
#  3  . [x  x  x] .  .
#  4  . [x  x  x] .  .
#  5  . [x  x  x] .  .
#  6  .  .  .  .  .  .
```

Given two-dimensional space with a string y axis and integer x axis, this code describes the region that starts at `(B, 2)`, is 3 units wide and 4 units tall:

```python
from bounden import Region

region = Region[
    tuple[str,   int],   # Axes
    tuple[float, float], # Axis lengths
](
    ("B", 2), (3, 4),
)

#     A  B  C  D  E  F
#  0  .  .  .  .  .  .
#  1  .  .  .  .  .  .
#  2  . [x  x  x] .  .
#  3  . [x  x  x] .  .
#  4  . [x  x  x] .  .
#  5  . [x  x  x] .  .
#  6  .  .  .  .  .  .
```

## Properties

The region's position is read from the `position` property.

The lengths are read from the `lengths` property.
