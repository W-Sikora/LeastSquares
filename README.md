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
<img src="https://render.githubusercontent.com/render/math?math=Y = UA %2B E">
<img src="https://render.githubusercontent.com/render/math?math=\hat{Y} = UA">
<img src="https://render.githubusercontent.com/render/math?math=E = Y - \hat{Y}">
<img src="https://render.githubusercontent.com/render/math?math=min%20 S = \sum_{i=1}^{N}(e_i)^2=(y_i-\hat{y}_i)^2">
<img src="https://render.githubusercontent.com/render/math?math=S(A)=E^TE=(Y-UA)^T(Y-UA)=(Y^T-A^TU^T)(Y-UA)=Y^TY-Y^TUA-A^TU^TY%2BA^TU^TUA">
The transposition of scalars or the order of multiplication does not affect the result, so:
<img src="https://render.githubusercontent.com/render/math?math=Y^TUA=A^TU^TY">
<img src="https://render.githubusercontent.com/render/math?math=S(A)=Y^TY-2A^TU^TY %2B A^TU^TUA">
<img src="https://render.githubusercontent.com/render/math?math=\frac{\partial S(A)}{\partial A}=\frac{\partial}{\partial A}Y^TY-\frac{\partial}{\partial A}2A^TU^TY %2B \frac{\partial}{\partial A}A^TU^TUA">
<img src="https://render.githubusercontent.com/render/math?math=\frac{\partial S(A)}{\partial A}= 0 - 2U^TY %2B 2U^TUA">
<img src="https://render.githubusercontent.com/render/math?math=\frac{\partial S(A)}{\partial A}= 0">
<img src="https://render.githubusercontent.com/render/math?math=- 2U^TY %2B 2U^TUA = 0">
<img src="https://render.githubusercontent.com/render/math?math=- U^TY %2B U^TUA = 0">
<img src="https://render.githubusercontent.com/render/math?math= U^TUA = U^TY">
<img src="https://render.githubusercontent.com/render/math?math= A=(U^TU)^{-1}U^TY">

![least_squares_fitting](/media/mls.png)

### Maximum likelihood estimation
![maximum_likelihood_estimation.png](/media/mle.png)

### Kernel density estimation
![kernel_density_estimation.py.png](/media/kde.png)

### Data
The data show areas and prices of flats located in Lubusz Voivodeship in the western part of Poland (data in ".xlsx" format).
