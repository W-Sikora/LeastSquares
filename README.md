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

#### Solving the least squares problem
Coming soon

#### Results
![least_squares_fitting](/media/mls.png)

### Maximum likelihood estimation
[Maximum likelihood estimation](https://en.wikipedia.org/wiki/Maximum_likelihood_estimation "maximum likelihood estimation")
(MLE) is a method of estimating the parameters of a probability distribution by maximizing a [likelihood function](https://en.wikipedia.org/wiki/Likelihood_function "likelihood function"),
so that under the assumed statistical model the observed data is most probable.

#### Solving the MLE problem
Coming soon 

#### Results
![maximum_likelihood_estimation.png](/media/mle.png)

### Kernel density estimation
[Kernel density estimation](https://en.wikipedia.org/wiki/Kernel_density_estimation "kernel density estimation") (KDE) 
is a non-parametric way to estimate the probability density function of a random variable. Kernel density estimation is
a fundamental data smoothing problem where inferences about the population are made, based on a finite data sample. 

#### Results
![kernel_density_estimation.py.png](/media/kde.png)

### Data
The data show areas [sqm] and prices [PLN] of flats located in Lubusz Voivodeship in the western part of Poland (data in ".xlsx" format).