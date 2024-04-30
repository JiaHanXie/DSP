## Linear Shift-invariant System

- environment: python 3.10.12

```python
import sys
sys.path.append('../Finite-Sequence/')
from Complex_Sequence import *
```

### Convolution

- $y[n]=\sum_{k=-\infty }^{\infty}x[k]h[n-k]$

```python
y = conv(x,h)
```

- example:
```python
a = Finite_Sequence('a', 0, 4)
b = Finite_Sequence('b', 0, 2)
a.set_sequence([-1, 0, 1, 2, 3, 4], [5, 0, 3, 1, 2, -1])
b.set_sequence([-2, -1, 0, 1, 2], [4, 6, 3, 2, 1])
y = conv(a, b)
print('y index: ' + str(y.get_index()))
print('y value: ' + str(y.get_value()))
y_ = conv(b, a)
print('y bar index: ' + str(y_.get_index()))
print('y bar value: ' + str(y_.get_value()))
```