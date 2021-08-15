# The diatomic chain

!!! danger  "Unbaked"

    The content here is still very much under development. Please come back soon!

## Introduction

![](../images/04_iron.jpg)

The kinetic theory of Drude was a great first step in trying to answer the question "metals, how do they work?", but it was clear from the outset that there were problems with the theory. But with the discovery of the Pauli exclusion principle, it seemed only logical that with the inclusion of _the_ fundamental property of the electrons, life would improve. Indeed it does...

!!! danger  "Expected competencies"

    It is assumed that you have familiarity with the following concepts/techniques:

    * Statistical mechanics: familiarity with Fermi-Dirac statistics
    * Quantum mechanics: Wavefunction of a free (unbound) electron

!!! info  "Text reference"
    The material covered here is discussed in section(s) $\S 4$ of [The Oxford Solid State Basics](https://global.oup.com/academic/product/the-oxford-solid-state-basics-9780199680771?cc=au&lang=en&)

---

_(based on chapters 10-11 of the book)_

!!! success "Expected prior knowledge"

    Before the start of this lecture, you should be able to:

    - Write down equations of motion and the LCAO Hamiltonian (similar to the previous lectures)
    - Solve an eigenvalue problem

!!! summary "Learning goals"

    After this lecture you will be able to:

    - formulate equations of motion for electrons or phonons in 1D, with multiple degrees of freedom per unit cell.
    - solve these equations to arrive at the dispersion relation.
    - derive the group velocity and density of states from the dispersion relation.
    - explain what happens with the band structure when the periodicity of the lattice is increased or reduced.

### More degrees of freedom per unit cell:
In the last lecture, we modeled phonons through a 1D homogeneous chain of atoms.
The model gave us insight into phonons and justified the crude approximations of the Debye model.
Despite the model's usefulness, we are not always able to model problems as a *homogeneous* chain.
Therefore, let us tackle a slightly more general problem.
Consider a chain of atoms with two masses, $m_1$ and $m_2$.
In our chain, an atom with mass $m_1$ is always followed by an atom of mass $m_2$ and vice versa.
Similar to before, the atoms interact via a harmonic potential with spring constant $κ$.
![](figures/phonons5.svg)

In the last lecture, we solved the homogenous chain problem by identifying its high level of symmetry.
However, the problem here is not as symmetric.
We need to re-think and generalize our ansatz.

First we identify a pattern that does repeat: an atom with mass $m_1$ followed by one with mass $m_2$.
This is called a **unit cell** (the smallest repeated element of the system)

We now label all degrees of freedom in a unit cell.
The two atoms in a unit cell have displacements $u_{1,n}$ and $u_{2,n}$, where the first index specifies the atom number within the unit cell and the second the unit cell number.
In our choice of unit cell, atom 1 has mass $m_1$ and atom 2 has mass $m_2$.

Having specified the degrees of freedom, let's write down the equations of motion:

$$
\begin{aligned}
m_1\ddot{u}_{1,n}&=κ(u_{2,n}-2u_{1,n}+u_{2,n-1})\\
m_2\ddot{u}_{2,n}&=κ(u_{1, n} - 2u_{2,n}+u_{1,n+1}).
\end{aligned}
$$

The new ansatz is conceptually the same as before: all unit cells should behave the same up to a phase factor:

$$
\begin{pmatrix}
u_{1,n}\\
u_{2,n}
\end{pmatrix} =
e^{iω t - ik na}
\begin{pmatrix}
A_{1}\\
A_{2}
\end{pmatrix}.
$$

Substituting this ansatz into the equations of motion (and assuming that the solution is nontrivial) we end up with an eigenvalue problem:
$$ω^2
\begin{pmatrix}
m_1 & 0 \\ 0 & m_2
\end{pmatrix}
\begin{pmatrix}
A_{1} \\ A_{2}
\end{pmatrix} = κ
\begin{pmatrix}
2 & -1 - e^{ika} \\ -1-e^{-ika} & 2
\end{pmatrix}
\begin{pmatrix}
A_{1}\\ A_{2}
\end{pmatrix},$$
with eigenfrequencies:
$$ω^2=\frac{κ(m_1+m_2)}{m_1m_2}\pm κ\left\{\left(\frac{m_1+m_2}{m_1m_2}\right)^2-\frac{4}{m_1m_2}\sin^2\left(\frac{1}{2}ka\right)\right\}^{\frac{1}{2}}$$

Looking at the eigenvectors we see that for every $k$ there are now two values of $ω$: one corresponding to in-phase motion (–) and anti-phase (+).

<!---
Should we mention that we choose omega > 0?
--->

```python
def dispersion_2m(k, kappa=1, M=1.4, m=1, acoustic=True):
    Mm = M*m
    m_harm = (M + m) / Mm
    root = kappa * np.sqrt(m_harm**2 - 4*np.sin(k/2)**2 / Mm)
    if acoustic:
        root *= -1
    return np.sqrt(kappa*m_harm + root)

# TODO: Add panels with eigenvectors
k = np.linspace(-2*pi, 6*pi, 300)
fig, ax = pyplot.subplots()
ax.plot(k, dispersion_2m(k, acoustic=False), label='optical')
ax.plot(k, dispersion_2m(k), label='acoustic')
ax.set_xlabel('$ka$')
ax.set_ylabel(r'$ω$')
pyplot.xticks([-pi, 0, pi], [r'$-\pi$', '$0$', r'$\pi$'])
pyplot.yticks([], [])
pyplot.vlines([-pi, pi], 0, 2.2, linestyles='dashed')
pyplot.legend()
pyplot.xlim(-1.75*pi, 3.5*pi)
pyplot.ylim(bottom=0)
draw_classic_axes(ax)
ax.annotate(s='', xy=(-pi, -.3), xytext=(pi, -.3),
            arrowprops=dict(arrowstyle='<->', shrinkA=0, shrinkB=0))
ax.text(0, -.55, '1st Brillouin zone', ha='center');
#draw_classic_axes(ax, xlabeloffset=.2)
```
The figure above shows a plot of the eigenfrequencies as a function of $ka$.
Just like last time, the plot is periodic in $k$, with $k$-values which differ by a multiple of $2 \pi / a$ corresponding to the same solution.
Therefore we only look at the $k$-values between $k - \pi / a$ and $k + \pi / a$.
This range (in between the dashed lines) is called the first **Brillouin zone**, and functions as a unit cell in reciprocal space.
The Brillouin zone will be explained in more detail in the lecture about X-ray diffraction.

Unlike the simple atomic chain, the dispersion relation now has two branches (or bands).
The reason an additional branch appears in the solution is due to the 2 degrees of freedom per unit cell.
If we had started with 3 different atoms, the eigenvalue problem would contain 3 equation, so that there would be three eigenfrequencies per $k$ and the dispersion relation would have 3 branches.

The lower branch is called _acoustic_ because its linear dispersion near $ω=0$ matches the behavior of regular sound waves.
The upper branch is the _optical branch_ because it can cross with the (linear) dispersion relation of photons, allowing these phonons to efficiently emit and absorb photons.

Like before, the phonon group velocity is $v=\textrm{d}ω/\textrm{d}k$, and the density of states is $g(ω)=\textrm{d}N/\textrm{d}ω = \frac{L}{2π} ∑| \textrm{d}k/\textrm{d} ω|$.
The sum goes over all states at a given energy.
In this case, the sum ensures we include the contribution to the DOS from both the positive and negative momenta.
Since the energy of this system is symmetric with respect to momentum reversal, the sum only introduces a factor of 2.

An intuitive way to visualize the density of states $g(ω)$ is to consider it a histogram of the samples drawn from the dispersion relation $ω(k)$:

```python
matplotlib.rcParams['font.size'] = 24
k = np.linspace(-.25*pi, 1.5*pi, 300)
k_dos = np.linspace(0, pi, 20)
fig, (ax, ax2) = pyplot.subplots(ncols=2, sharey=True, figsize=(10, 5))
ax.plot(k, dispersion_2m(k, acoustic=False), label='optical')
ax.plot(k, dispersion_2m(k), label='acoustic')
ax.vlines(k_dos, 0, dispersion_2m(k_dos, acoustic=False),
          colors=(0.5, 0.5, 0.5, 0.5))
ax.hlines(
    np.hstack((dispersion_2m(k_dos, acoustic=False), dispersion_2m(k_dos))),
    np.hstack((k_dos, k_dos)),
    1.8*pi,
    colors=(0.5, 0.5, 0.5, 0.5)
)
ax.set_xlabel('$ka$')
ax.set_ylabel(r'$ω$')
ax.set_xticks([0, pi])
ax.set_xticklabels(['$0$', r'$\pi$'])
ax.set_yticks([])
ax.set_yticklabels([])
ax.set_xlim(-pi/4, 2*pi)
ax.set_ylim((0, dispersion_2m(0, acoustic=False) + .2))
draw_classic_axes(ax, xlabeloffset=.2)

k = np.linspace(0, pi, 1000)
omegas = np.hstack((
    dispersion_2m(k, acoustic=False), dispersion_2m(k)
))
ax2.hist(omegas, orientation='horizontal', bins=75)
ax2.set_xlabel(r'$g(ω)$')
ax2.set_ylabel(r'$ω$')

# Truncate the singularity in the DOS
max_x = ax2.get_xlim()[1]
ax2.set_xlim((0, max_x/2))
draw_classic_axes(ax2, xlabeloffset=.1)
matplotlib.rcParams['font.size'] = 16
```

Note that $g(ω)$ is generally plotted along the vertical axis and $ω$ along the horizontal axis – the right plot above is just to demonstrate the relation between the dispersion and the DOS. The singularities in $g(ω)$ at the bottom and top of each branch are called _van Hove singularities_.

### Consistency check with 1 atom per cell
To check if our result is consistent with the previous lecture, we examine what happens when we take $m_1\rightarrow m_2$.
Physically, the system is then exactly the same as the 1D monatomic chain, so we would want our solutions to also be the same.
But at first glance the two solutions seem very different: the solution with one atom has only one band, but the solution with two atoms has two bands.

To reconcile the two pictures, let's plot two unit cells in reciprocal space.

```python
k = np.linspace(0, 2*pi, 300)
k_dos = np.linspace(0, pi, 20)
fig, ax = pyplot.subplots()
ax.plot(k, dispersion_2m(k, acoustic=False), label='optical')
ax.plot(k, dispersion_2m(k), label='acoustic')
omega_max = dispersion_2m(0, acoustic=False)
ax.plot(k, omega_max * np.sin(k/4), label='equal masses')
ax.set_xlabel('$ka$')
ax.set_ylabel(r'$ω$')
ax.set_xticks([0, pi, 2*pi])
ax.set_xticklabels(['$0$', r'$\pi/2a$', r'$\pi/a$'])
ax.set_yticks([])
ax.set_yticklabels([])
ax.set_xlim(-pi/8, 2*pi+.4)
ax.set_ylim((0, dispersion_2m(0, acoustic=False) + .2))
ax.legend(loc='lower right')
pyplot.vlines([pi, 2*pi], 0, 2.2, linestyles='dashed')
draw_classic_axes(ax, xlabeloffset=.2)
```
We must be careful when considering the lattice constant $a$.
In the 1D monatomic chain, $a$ was the distance between two neighbouring atoms, but in our diatomic chain $a$ is the size of the unit cell, which is twice as big.
Therefore we take the size of our unit cell in the diatomic case to be $2a$, so the physical systems are the same.

Looking at the graph we see that doubling the lattice constant "folds" the band structure on itself.
There are then $2$ possible values of $ω$ for each $k$, creating the $2$ branches of the non-periodic system.
We can look at the graph in two distinct ways:
We can consider the green line (monatomic chain solution). Its Brillouin zone extends from $0$ to $\pi / a$.
Alternatively, we consider the orange and blue lines together. In this case, the Brillouin zone is smaller ranging from $0$ to $\pi / 2a$ (because of the larger lattice constant).

Despite the two band structures look different, the density of states only changes very little: when $m_1 ≈ m_2$ only the states near the band touching point slightly move in frequency.

## Summary

* By using plane waves in real space as an ansatz, we found all normal modes of an atom chain with two different atoms. (Just like in the case of 1 degree of freedom per unit cell).
* The density of states can be derived graphically from the dispersion relation.
* The dispersion relation of a system with period $a$ in real space is periodic with period $2\pi/a$ in $k$-space.
* In a system with more than one degree of freedom per unit cell we need to consider independent amplitudes for each degree of freedom, and we get multiple bands.
* Systems with different band structures can have the same density of states.

## Exercises

### Warm-up questions
1. Verify that the expression for $ω^2$ is always positive. Why is this important?
2. Work out the expression of $ω^2$ in the case $m_1 = m_2$. Compare this to the solution for the monatomic chain.
3. When calculating the DOS, we only look at the first Brillouin zone. Why?

### Exercise 1: analyzing the diatomic vibrating chain
As we have derived, the eigenfreqencies of a diatomic vibrating chain with 2 different masses are:

$$ω^2=\frac{κ(m_1+m_2)}{m_1m_2}\pm κ\left\{\left(\frac{m_1+m_2}{m_1m_2}\right)^2-\frac{4}{m_1m_2}\sin^2\left(\frac{1}{2}ka\right)\right\}^{\frac{1}{2}},$$

where the plus sign corresponds to the optical branch and the minus sign to the acoustic branch.

1. Find the magnitude of the group velocity near $k=0$ for the _acoustic_ branch.

    ??? hint
        Make use of a Taylor expansion.

2. Show that the group velocity at $k=0$ for the _optical_ branch is zero.
3. Derive an expression of the density of states $g(ω)$ for the _acoustic_ branch and small $k$. Make use of your expression of the group velocity in 1.
Compare this expression with that of the derived density of states from [exercise 1](2_debye_model/#exercise-1-debye-model-concepts) of the Debye lecture.

### Exercise 2: the Peierls transition
In the previous lecture, we have derived the electronic band structure of an 1D, equally spaced atomic chain. Such chains, however, are in fact not stable and the equal spacing will be distorted. This is also known as the [Peierls transition](https://en.wikipedia.org/wiki/Peierls_transition).

The spacing of the distorted chain alternates between two different distances and this also causes the hopping energy to alternate between $t_1$ and $t_2$. We further set the onsite energies of the atoms to $\epsilon$. The situation is depicted in the figure below.

![](figures/peierls_transition.svg)

Due to the alternating hopping energies, we must treat two consecutive atoms as two different orbitals ($|n,1⟩$ and $|n,2 ⟩$ in the figure) from the same unit cell. The corresponding LCAO of this chain is given by
$$
\left|\Psi \right\rangle = \sum_n \left(\phi_n \left| n,1 \right\rangle + \psi_n \left| n,2 \right\rangle\right)
$$
As usual, we assume that all these atomic orbitals are orthogonal to each other.

1. Indicate the length of the unit cell $a$ in the figure.
2. Using the Schrödinger equation, write the equations of motion of the electrons.

    ??? hint
        To this end, find expressions for $E \left< n,1 \vert \Psi \right> = \left< n,1 \right| H \left|\Psi \right>$ and $E \left< n,2 \vert \Psi \right> = \left< n,2 \right| H \left|\Psi \right>$.

3. Using the trial solutions $\phi_n = \phi_0 e^{ikna}$ and $\psi_n = \psi_0 e^{ikna}$, show that the Schödinger equation can be written in matrix form: $$\begin{pmatrix} \epsilon & t_1 + t_2 e^{-i k a} \\  t_1 + t_2 e^{i k a}  & \epsilon \end{pmatrix} \begin{pmatrix} \phi_0 \\ \psi_0 \end{pmatrix} = E \begin{pmatrix} \phi_0 \\ \psi_0 \end{pmatrix}.$$
4. Derive the dispersion relation of this Hamiltonian. Does it look like the figure of the band structure shown on the [Wikipedia page](https://en.wikipedia.org/wiki/Peierls_transition#/media/File:Peierls_instability_after.jpg)? Does it reduce to the 1D, equally spaced atomic chain if $t_1 = t_2$?
5. Find an expression of the group velocity $v(k)$ and effective mass $m^*(k)$ of both bands.
6. Derive an expression for the density of states $g(E)$ of the entire band structure and make a plot of it. Does your result makes sense when considering the band structure?

### Exercise 3: atomic chain with 3 different spring constants
Suppose we have a vibrating 1D atomic chain with 3 different spring constants alternating like $\kappa_ 1$, $\kappa_2$, $\kappa_3$, $\kappa_1$, etc. All the the atoms in the chain have an equal mass $m$.

1. Make a sketch of this chain and indicate the length of the unit cell $a$ in this sketch.
2. Derive the equations of motion for this chain.
3. By filling in the trial solutions into the equations of motion (which should be similar to Ansazt used in the lecture), show that the eigenvalue problem is
   $$
   \omega^2 \mathbf{u} = \frac{1}{m}
   \begin{pmatrix} \kappa_1 + \kappa_ 3 &  -\kappa_ 1 & -\kappa_ 3 e^{i k a} \\
   -\kappa_ 1 & \kappa_1+\kappa_2 & -\kappa_ 2 \\
   -\kappa_ 3 e^{-i k a} & -\kappa_2 & \kappa_2 + \kappa_ 3
   \end{pmatrix} \mathbf{u}
   $$
4. In general, the eigenvalue problem above cannot be solved analytically, and can only be solved in specific cases. Find the eigenvalues $ω^2$ when $k a = \pi$ and $\kappa_1 = κ_2 = q$.

    ??? hint
        To solve the eigenvalue problem quickly, make use of the fact that the mass-spring matrix in that case commutes with the matrix $$ X = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{pmatrix}. $$ What can be said about eigenvectors of two matrices that commute?

5. What will happen to the periodicity of the band structure if $\kappa_ 1 = \kappa_ 2 = \kappa_3$?
