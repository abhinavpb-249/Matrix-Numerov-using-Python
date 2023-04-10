# matrix-numerov

<b>Solving Schrodinger equation using Matrix Nuumerov method in Python</b>

Aim: To plot the stationary state of a quantum system using Python

The Schrödinger equation is a linear partial differential
equation that governs the wave function of a quantum-
mechanical system. On applying initial, boundary and
potential conditions, it gives us information on how a wave
behaves in a quantum realm.
The equation being a second order differential function,it's
not always possible to find an analytical solution. Hence
we employ numerical methods that involves high level of
computation to solve the Schrodinger Equation.
This has already been achieved by Mohandas Pillai, Joshua
Goglio, and Thad G. Walkera <a href="https://pages.physics.wisc.edu/~tgwalker/106.Numerov.pdf">(Department of Physics,
University of Wisconsin-Madison)</a> using Mathematica and
they published it in American Journal of Physics [1] .
Wolfram Mathematica is a premium paid software system
with built-in libraries for several areas of technical
computing. Higher cost of Mathematica makes it
inaccessible to a student.Hence alternate choice is always
preferred.
The aim of this project is to make a python code that does
the same using python programming language.



<b>Theory</b> <br>
We start by writing down the time-independent
schrodinger equation in Hamiltonian form. This looks
strikingly similar to a matrix transformation equation
where the eigen value is the total energy and the Eigen
vector is the wavefunction.
Therefore to find the Eigen vector -which is the
wavefunction- we just have to write the hamiltonian and
potential in matrix form and solve the matrix equation.
This can be done in python by using the numpy.linalg.eig()
function in python with the help of the numpy
module.
We can do this by first finding the Hamiltonian matrix,
which is the sum of Potential energy matrix and Kinetic
energy matrix and taking the Eigen vector of that.
However, there are some difficulties associated with this
as numpy automatically normalises the vectors and we
have to undo that to produce the desired results.
Finaly a graph is drawn plotting distance on the X-axis and
wavefunction on the Y-axis.
