# Region2 class

The `Region2` class wraps and simplifies the [`Region` class](./region.md) to describe a region of two-dimensional space.

## Construction

Two generic types are required:

1. X axis type
1. Y axis type

You must also initialise the region with its x and y coordinates, width and height.

### Construction examples

Given a grid with integer axes, this code describes the region that starts at `(1, 2)`, is 3 units wide and 4 units tall:

```python
from bounden import Region2

region = Region2[int, int]((1, 2), (3, 4))

#     0  1  2  3  4  5
#  0  .  .  .  .  .  .
#  1  .  .  .  .  .  .
#  2  . [x  x  x] .  .
#  3  . [x  x  x] .  .
#  4  . [x  x  x] .  .
#  5  . [x  x  x] .  .
#  6  .  .  .  .  .  .
```

Given a grid with a string y axis and integer x axis, this code describes the region that starts at `(B, 2)`, is 3 units wide and 4 units tall:

```python
from bounden import Region

region = Region2[str, int]((1, 2), (3, 4))

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

The region's width and height are read from the `width` and `height` properties.
