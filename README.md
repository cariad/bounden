# Bounden

**Bounden** describes points and regions within _n_-dimensional space.

## Points

The `Point` class describes a point in _n_-dimensional space.

The class's generic type describes the coordinate type of each dimension, and must be specified as a tuple:

```python
from bounden import Point

in_line = Point[tuple[int]]((0,))
in_rect = Point[tuple[int, int]]((0, 0))
in_cube = Point[tuple[int, int, int]]((0, 0, 0))
```

The position is read from the `position` property:

```python
from bounden import Point

point = Point[tuple[int, int, int]]((1, 2, 3))
print(point.position)
# (1, 2, 3)
```

## Installation

**Bounden** requires Python 3.10 or later and can be installed from [PyPI](https://pypi.org/project/bounden/).

```console
pip install bounden
```

## Support

Please raise bugs, feature requests and ask questions at [cariad/bounden/issues](https://github.com/cariad/bounden/issues).

## The Project

**Bounden** is &copy; 2022 Cariad Eccleston and released under the [MIT License](https://github.com/cariad/bounden/blob/main/LICENSE) at [cariad/nvalues](https://github.com/cariad/bounden).

## The Author

Hello! 👋 I'm **Cariad Eccleston** and I'm a freelance backend and infrastructure engineer in the United Kingdom. You can find me at [cariad.earth](https://cariad.earth), [github/cariad](https://github.com/cariad), [linkedin/cariad](https://linkedin.com/in/cariad) and on Mastodon at [@cariad@tech.lgbt](https://tech.lgbt/@cariad).
