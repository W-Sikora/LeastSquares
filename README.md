# System Identification
Statistical methods applied to build mathematical models of dynamical systems from measured data.

## Requirements
- python 3.6,
- numpy,
- pandas,
- xlrd,
- scipy,
- matplotlib.

## To get started
Clone this git repository.

### Least squares
The method of least squares[^1] is a standard approach in regression analysis to approximate the solution of overdetermined systems[^2] (sets of equations in which there are more equations than unknowns) by minimizing the sum of squared residuals (the difference between an observed value, and the fitted value provided by a model).

[1^]: https://en.wikipedia.org/wiki/Least_squares
[2^]: https://en.wikipedia.org/wiki/Overdetermined_system

<img src="https://latex.codecogs.com/svg.latex?\large&space;$$\lim_{n \to \infty}\sum_{k=1}^n \frac{1}{k^2}= \frac{\pi^2}{6}$$">
<img src="https://latex.codecogs.com/svg.latex?\large&space;min\, S = \sum_{i=1}^{N}(e_i)^2=\sum_{i=1}^{N}(y_i-\hat{y}_i)^2 \\ S(a) = \sum_{i=1}^{N}(y_i-au_i-b)^2 = \sum_{i=1}^{N}(y_i^2-2y_iau_i+a^2u_i^2) = \sum_{i=1}^{N}y_i^2 - 2a\sum_{i=1}^{N}y_iu_i + a^2\sum_{i=1}^{N}u_i^2 \\ \frac{\partial S(a)}{\partial a} = \frac{\partial}{\partial a}\left(\sum_{i=1}^{N}y_i^2\right) - \frac{\partial}{\partial a}\left(2a\sum_{i=1}^{N}y_iu_i\right) + \frac{\partial}{\partial a}\left(a^2\sum_{i=1}^{N}u_i^2\right)\\ \frac{\partial S(a)}{\partial a} = 0 - 2\sum_{i=1}^{N}y_iu_i + 2a\sum_{i=1}^{N}u_i^2\\ \frac{\partial S(a)}{\partial a} = 0 <=> - 2\sum_{i=1}^{N}y_iu_i + 2a\sum_{i=1}^{N}u_i^2 = 0\\ -\sum_{i=1}^{N}y_iu_i + a\sum_{i=1}^{N}u_i^2 = 0\\ a = \frac{\sum_{i=1}^{N}y_iu_i}{\sum_{i=1}^{N}u_i^2}">
<img src="https://render.githubusercontent.com/render/math?math= Y = AU + E \\ \hat{Y} = AU \\ E = Y - \hat{Y}">
<img src="https://render.githubusercontent.com/render/math?math=S(A)=E^TE=(Y-UA)^T(Y-UA)=(Y^T-A^TU^T)(Y-UA)=Y^TY-Y^TUA-A^TU^TY%2BA^TU^TUA">
The transposition of scalars or the order of multiplication does not affect the result, so:
<img src="https://render.githubusercontent.com/render/math?math=Y^TUA=A^TU^TY">
<img src="https://render.githubusercontent.com/render/math?math=S(A)=Y^TY-2A^TU^TY %2B A^TU^TUA">
<img src="https://render.githubusercontent.com/render/math?math=\frac{\partial S(A)}{\partial A}=\frac{\partial}{\partial A}Y^TY-\frac{\partial}{\partial A}2A^TU^TY %2B \frac{\partial}{\partial A}A^TU^TUA">
<img src="https://render.githubusercontent.com/render/math?math=\frac{\partial S(A)}{\partial A}= 0 - 2U^TY %2B 2U^TUA">
<img src="https://render.githubusercontent.com/render/math?math=\frac{\partial S(A)}{\partial A}= 0">
<img src="https://render.githubusercontent.com/render/math?math=-2U^TY %2B 2U^TUA = 0">
<img src="https://render.githubusercontent.com/render/math?math=-U^TY %2B U^TUA = 0">
<img src="https://render.githubusercontent.com/render/math?math=U^TUA = U^TY">
<img src="https://render.githubusercontent.com/render/math?math=A=(U^TU)^{-1}U^TY">

![least_squares_fitting](/media/mls.png)

### Maximum likelihood estimation
![maximum_likelihood_estimation.png](/media/mle.png)

### Kernel density estimation
![kernel_density_estimation.py.png](/media/kde.png)

### Data
The data show areas and prices of flats located in Lubusz Voivodeship in the western part of Poland (data in ".xlsx" format).
