# Matrix Numerov method in Python

<b>Solving Schrodinger equation using Matrix Numerov method in Python</b>

Aim: To plot the stationary state of a quantum system using Python

## Introduction 

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

<img src="https://github.com/abhinavpb-249/matrix-numerov/blob/main/plot.png?raw=true">

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
Finally a graph is drawn plotting distance on the X-axis and
wavefunction on the Y-axis.

## Schrödinger’s Equation[2]
Schrodinger's equation is a fundamental equation in
quantum mechanics that describes the behavior of
quantum systems, such as atoms and molecules. It is
named after Erwin Schrodinger, who developed the
equation in 1925.
The equation is a partial differential equation that relates
the wave function of a quantum system to its energy. The
wave function is a mathematical function that describes
the state of a system, and it contains information about the
probability of finding a particle at a particular location.
The Schrödinger equation tells us how this wave function
evolves over time, and it allows us to predict the behavior
of quantum systems.
The Schrödinger equation is a linear equation, which
means that if we have two solutions, we can add them
together to get another solution. This property is essential
in quantum mechanics because it allows us to use
superposition, which is a fundamental concept in quantum
theory. Superposition means that a quantum particle can
exist in multiple states simultaneously. For example, an
electron can be in a state where it is spinning clockwise
and counterclockwise at the same time.
The Schrödinger equation has many applications in
physics, chemistry, and engineering. It is used to describe
the behavior of atoms, molecules, and other quantum
systems. The equation is also used to calculate the energy
levels and wave functions of these systems, which is
essential in understanding chemical reactions, the
behavior of materials, and the functioning of electronic
devices.
Time-Dependent Schrodinger’s Equation
The time-dependent Schrodinger equation is a
fundamental equation in quantum mechanics that
describes the time evolution of a quantum system. It is a
partial differential equation that describes how the wave
function of a system changes with time. The equation is
written in terms of the wave function Ψ, which represents
the probability amplitude of finding a particle in a
particular position and time.
The time-dependent Schrodinger equation is given by:
![Screenshot_2024-10-04_21-57-07](https://github.com/user-attachments/assets/6e0ee915-4fa8-4cf7-99c0-8520e5822f9c)

The time-dependent Schrodinger equation is a cornerstone
of quantum mechanics, as it provides a way to calculate
the time evolution of quantum systems. It has been used to
describe a wide range of physical phenomena, including
the behavior of atoms, molecules, and solid-state
materials. The solution to the time-dependent Schrodinger
equation provides information about the probability of
finding a particle in a particular position and time, as well
as the energy of the system.
Time-Independent Schrodinger’s Equation[3]
The time-independent Schrodinger equation is a
fundamental equation in quantum mechanics that
describes the stationary states of a quantum system. It is a
partial differential equation that describes the allowed
energy states of a quantum system. The equation is
written in terms of the wave function Ψ, which represents
the probability amplitude of finding a particle in a
particular position.
The time-independent Schrodinger equation is given by:

![Screenshot_2024-10-04_21-59-36](https://github.com/user-attachments/assets/da99fa36-77fb-4ede-96dc-1e488635f8c6)

The time-independent Schrodinger equation is an
eigenvalue equation, which means that the wave function
Ψ is an eigenvector of the Hamiltonian operator H with
corresponding eigenvalue E. The solution to the timeindependent Schrodinger equation provides information
about the allowed energy levels of a quantum system.
The time-independent Schrodinger equation is an
important equation in quantum mechanics, as it provides a
way to calculate the energy levels of a quantum system. It
has been used to describe a wide range of physical
phenomena, including the behavior of atoms, molecules,
and solid-state materials. The solution to the timeindependent Schrodinger equation provides information
about the allowed energy levels of a quantum system,
which can be used to predict the behavior of the system in
various physical situations.

More details are provided in the attached file <i> Project Report.pdf </i>
 
