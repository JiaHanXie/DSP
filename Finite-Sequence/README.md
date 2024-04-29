## Finite Sequence of Complex Number

- environment: python 3.10.12

```python
from ComplexSequence import *
```

###  create a random finite sequence of complex number

```python
Finite_Sequence(name, first_index, last_index, min_value, max_value)
```

- example: create a sequence x[n] with random number, -1 <= x <= 1 and -3 <= n <= 3

```python
x = Finite_Sequence('x', -3, 3, -1, 1)
```


### set sequence value
- index must be an integer list, and value can be an integer, float or complex number list

```python
sequence.set_sequence(index, value):
```

```python
#example: set x[n] = {2+3j, 4+4j, -1+6j, 3+6j, -3+4j}, -2 <= n <= 2
index = [-2, -1, 0, 1, 2]
value = [complex(2, 3), complex(4, 4), complex(-1, 6), complex(3, 6), complex(-3, 4)]
x.set_sequence(index, value)
```

### get index of x

```python
index = x.get_index()
```

### get value of x

```python
value = x.get_value()
```

### get real part of x

```python
real = x.get_real()
```

### get imaginary part of x

```python
imag = x.get_imaginary()
```

### get name of x

```python
name = x.get_name()
```

### time inverse: x[-n]

```python
x.time_inverse()
```

### conjugate: x*[n]

```python
x.conjugate_seq()
```

### conjugate and time inverse: x*[-n]

```python
x.conj_ti()
```

### minus conjugate and time inverse: -x*[-n]

```python
x.minus_conj_ti()
```

### time shift: x[n-k]

```python
sequence.time_shift(k)
```

- example: x[n-3]

```python
x.time_shift(3)
```

### Conjugate Symmetric Decomposition
- any sequence can be expressed as conjugate symmetric (CS) and conjugate antisymmetric (CA) part
- x[n] = xcs[n] + xca[n]

```python
#function will returnt a list which contains cs[n] and ca[n]
xcs_xca = x.conj_sym_decomp()
xcs = xcs_xca[0]
xca = xcs_xca[1]
```

### plot Real Part, Imaginary Part, n of x[n]

```python
sequence.plot_3d(figure)
```

- example: plot x[n] in 3D and figure number: 1

```python
x.plot_3d(1)
```

### plot Real Part of x[n]

```python
sequence.plot_R(figure)
```

- example:

```python
x.plot_R(2)
```

### plot Imaginary Part of x[n]

```python
sequence.plot_I(figure)
```

- example:

```python
x.plot_I(3)
```

### create an unit sample: $\delta[n]$

```python
sequence = unit_sample(first_index, last_index)
```

- example: d[n], -5<=n<=5

```python
d = unit_sample(-5, 5)
#plot
d.plot_3d(1)
d.plot_R(2)
d.plot_I(3)
```
<table>
  <tr>
    <td align="center">
<img alt="" width="400" src="https://github.com/JiaHanXie/DSP/blob/main/unit_sample_3d.png" alt=""></img>
</td>
<td align="center">
<img alt="" width="400" src="https://github.com/JiaHanXie/DSP/blob/main/unit_sample_R.png" alt=""></img>
</td>
    <td align="center">
<img alt="" width="400" src="https://github.com/JiaHanXie/DSP/blob/main/unit_sample_I.png" alt=""></img>
</td>
  </tr>
  <tr>
    <th align="center">3-D plot</th>
    <th align="center">R</th>
	<th align="center">I</th>
  </tr>
</table>

### create an unit step: $\mu[n]$

```python
sequence = unit_step(first_index, last_index)
```

- example: $\mu[n], -5<=n<=5$

```python
u = unit_step(-5, 5)
#plot
u.plot_3d(4)
u.plot_R(5)
u.plot_I(6)
```

<table>
  <tr>
    <td align="center">
<img alt="" width="400" src="https://github.com/JiaHanXie/DSP/blob/main/unit_step_3d.png" alt=""></img>
</td>
<td align="center">
<img alt="" width="400" src="https://github.com/JiaHanXie/DSP/blob/main/unit_step_R.png" alt=""></img>
</td>
    <td align="center">
<img alt="" width="400" src="https://github.com/JiaHanXie/DSP/blob/main/unit_step_I.png" alt=""></img>
</td>
  </tr>
  <tr>
    <th align="center">3-D plot</th>
    <th align="center">R</th>
	<th align="center">I</th>
  </tr>
</table>

### calculate power of a complex number
- $\alpha^n$, $\alpha$ is a complex number, and n is an integer

```python
result = cpower(alpha,n)
```

### create a complex exponential sequence
- x[n] = $A*\alpha^n$, A and $\alpha$ is complex number, and n is an integer

```python
sequence = complex_exponential(first_index, last_index, A, alpha)
```

- example: $x[n]=e^{(-\frac{1}{12}+j\frac{\pi}{6})n)}=e^{-\frac{n}{12}}cos(\frac{\pi n}{6})+e^{-\frac{n}{12}}sin(\frac{\pi n}{6})$

```python
A = 1
alpha = cmath.exp(complex(-1/12,cmath.pi/6))
complex_exponential = complex_exponential(0, 40, A, alpha)

#plot
complex_exponential.plot_3d(7)
complex_exponential.plot_R(8)
complex_exponential.plot_I(9)
```

<table>
  <tr>
    <td align="center">
<img alt="" width="400" src="https://github.com/JiaHanXie/DSP/blob/main/complexexponential_3d.png" alt=""></img>
</td>
<td align="center">
<img alt="" width="400" src="https://github.com/JiaHanXie/DSP/blob/main/complexexponential_R.png.png" alt=""></img>
</td>
    <td align="center">
<img alt="" width="400" src="https://github.com/JiaHanXie/DSP/blob/main/complexexponential_I.png" alt=""></img>
</td>
  </tr>
  <tr>
    <th align="center">3-D plot</th>
    <th align="center">R</th>
	<th align="center">I</th>
  </tr>
</table>