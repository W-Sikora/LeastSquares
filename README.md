# System Identification
Statistical methods applied to build mathematical models of dynamical systems from measured data, 
[more information](https://en.wikipedia.org/wiki/System_identification "system identification") 

## To get started
Clone this git repository.

### Requirements
- python 3.6,
- numpy,
- pandas,
- xlrd,
- scipy,
- matplotlib.

### Least squares
The method of [least squares](https://en.wikipedia.org/wiki/Least_squares "least squares") is a standard 
approach in regression analysis to approximate the solution of [overdetermined systems](https://en.wikipedia.org/wiki/Overdetermined_system
"overdetermined system") (sets of equations in which there are more equations than unknowns) by minimizing the sum 
of squared residuals (the difference between an observed value, and the fitted value provided by a model).

![\large Y_{N\times1}](https://latex.codecogs.com/svg.latex?x%3D%5Cfrac%7B-b%5Cpm%5Csqrt%7Bb%5E2-4ac%7D%7D%7B2a%7D)

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
