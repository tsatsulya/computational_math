# Report of 3rd Laboratory

## Warning
Before using install `sympy`
```
pip install sympy
```

## Methodology

Various methods can be used to solve nonlinear equations and systems, and methods are given in this paper:

This work also uses Newton's and iterative decomposition methods.

#### Single equations:

$$
\begin{flalign}
  & 2x^2 - 5x + 3 = 0 &
\end{flalign}
$$

![](img/root.jpg)

![](img/root_in.jpg)

| Method    |   Found root   |
| :-------- | :------------: |
| Iterative | $1.0\pm\sigma$ |
| Newton's  | $1.0\pm\sigma$ |


#### System of equations:

$$
\begin{flalign}
&
  \begin{cases} 
  sin(x+1) - y = 1.2 \\
  2x + cos(y) = 2 \\
  \end{cases}
&
\end{flalign}
$$

| Method    |          Found root          | Iteration count |
| :-------- | :--------------------------: | :-------------: |
| Iterative | $x=0.51015016, y=0.20183842$ |       10        |
| Newton's  | $x=0.51015016, y=0.20183842$ |        5        |

![](img/system_iter.jpg)

![](img/system_newton.jpg)
>[Back to Methodology](#methodology)
