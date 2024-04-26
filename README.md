# Digital Signal Processing

## Finite Sequence of Complex Number

-  create a random finite sequence of complex number

```python
Finite_Sequence(name, first_index, last_index, min_value, max_value)
```

example: create a sequence x[n] with random number, -1 <= x <= 1 and -3 <= n <= 3
```python
x = Finite_Sequence('x', -3, 3, -1, 1)
```


- set sequence value, index must be an integer number list and value can be an integer, float or complex number list.

```python
sequence.set_sequence(index, value):
```

example: set x[n] = {2+3j, 4+4j, -1+6j, 3+6j, -3+4j}, -2 <= n <= 2
```python
index = [-2, -1, 0, 1, 2]
value = [complex(2, 3), complex(4, 4), complex(-1, 6), complex(3, 6), complex(-3, 4)]
x.set_sequence(index, value)
```

- get index of x

```python
index = x.get_index()
```

- get value of x

```python
value = x.get_value()
```

-get real part of x

```python
real = x.get_real()
```

- get imaginary part of x

```python
imag = x.get_imaginary()
```

- get name of x

```python
name = x.get_name()
```

- time inverse: x[-n]

```python
x.time_inverse()
```

- conjugate: x*[n]

```python
x.conjugate_seq()
```

- conjugate and time inverse: x*[-n]

```python
x.conj_ti()
```

- minus conjugate and time inverse: -x*[-n]

```python
x.minus_conj_ti()
```

- time shift: x[n-k]

```python
sequence.time_shift(k)
```

example: x[n-3]
```python
x.time_shift(3)
```

- plot Real Part, Imaginary Part, n of x[n]

```python
sequence.plot_3d(figure)
```

example: plot x[n] in 3D and figure number: 1
```python
x.plot_3d(1)
```

- plot Real Part

```python
sequence.plot_R(figure)
```

example:
```python
x.plot_R(2)
```

- plot Imaginary Part

```python
sequence.plot_I(figure)
```

example:
```python
x.plot_I(3)
```

- create an unit sample: $\delta[n]$

```python
sequence = unit_sample(first_index, last_index)
```

example: $\delta[n], n from -2 to 2$
```python
delta = unit_sample(-2, 2)
```

- create an unit step: $\mu[n]$

```python
sequence = unit_step(first_index, last_index)
```

example: $\mu[n], n from -2 to 2$
```python
mu = unit_step(-2, 2)
```