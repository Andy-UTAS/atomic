# Chemisty 101

!!! warning  "Cooking in progress"

    The content here is actively being developed; anything before this is "safe" and after this is unsafe.

## Introduction

![](../images/05_chemistry.png)

Our journey thus far has been considering the basic properties of solids, and our descriptions have been based around the properties of electrons and vibrations in solids, which can provide useful results but our endeavour is much grander: we would like to explain all the properties of all the solids. The first step on this journey is to no longer consider a collection of free electrons; solids are made up of many atoms, so we best find a way of baking this into whatever we do!

!!! danger  "Expected competencies"

    It is assumed that you have familiarity with the following concepts/techniques:

    * Quantum mechanics: the Schrödinger equation, wavefunction of the Hydrogen atom
    * Mathematics: linear algebra

!!! note  "Text reference"
    The material covered here is discussed in section(s) $\S 5, 6.3$ of [The Oxford Solid State Basics](https://global.oup.com/academic/product/the-oxford-solid-state-basics-9780199680771?cc=au&lang=en&)

!!! info "Computational content"

    The Jupyter notebook associated with this section can be accessed by clicking the icon below:
    [<i class="fab fa-python fa-5x"></i>](https://jove2021.cloud.edu.au/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FAndy-UTAS%2FSolid-state&urlpath=tree%2FSolid-state%2F05chemistry.ipynb&branch=master){ .md-button .md-button--primary class="text-center" style="margin-left: 45%"}

---

### A retrospective

Up to this point, we have:

  * Introduced reciprocal ($k$-space)
  * Postulated the dispersion relations for free electrons and oscillations in a solid
  * Calculated the heat capacity of free electrons and oscillations in a solid

which has premitted

  * The understanding of how materials can store heat via oscillations (Debye model)
  * The understanding of how free electrons conduct (Drude model) and store heat/energy (Sommerfeld model)

In constructing these models, we have made several approximations and postulations, and there are a few big questions to answer:

  * In the Debye model, Why is there a cutoff frequency for oscillations? Why are there no modes of ocillation beyond this frequency?
  * In the Drude model, we have electrons modelled as a gas, but why don't electrons scatter off from every the atoms in solid?
  * Why are some materials metallic, and others not metallic?

If we are to have a hope of understanding any of the above, we are going to have to understand better what is happening on the atomic scale.

## Atoms, how do they work?

It is no exaggeration to say that everything can be pretty-well described by the Schrödinger equation:

$$
\hat{H}ψ = Eψ,
$$

with $\hat{H}$ is the Hamiltonian of the system: the sum of kinetic and potential energies. For the hydrogen atom, the potential arises due to the Coulomb interaction between the electron and the nucleus:

$$
H=-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial {\mathbf r^2}} - \frac{e^2}{4\pi\varepsilon_0|r|}
$$

which you will have solved in detail elsewhere. If we move to the next-most-simple atom, helium, the Hamiltonian immediately becomes more complex,
containing not just the Coulomb interaction between the individual electrons and the nuclei, but also Coulomb repulsion between the two electrons:

$$
H=-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial {\mathbf r_1^2}} -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial {\mathbf r_2^2}}- \frac{2e^2}{4\pi\varepsilon_0|r_1|} - \frac{2e^2}{4\pi\varepsilon_0|r_2|} + \frac{e^2}{4\pi\varepsilon_0|r_1 - r_2|}.
$$

From a purely mathematical point of view, this means we need find eigenvalues and eigenvectors of a six-dimensional PDE, which is much tougher work than the three-dimensional PDE descirbing hydrogen. You have likely seen the variational method to construct appoximate wavefunctions, any even in this case it is a fair amount of work.

Let us now turn to another system, a single copper atom. Copper has 29 electrons, so to find the energy spectrum of copper we would need to solve an 87-dimensional Schrödinger equation. Such things are totally intractable: there is simply no way to solve such a thing, even with _really_ big computers. It is this growth in complexity with the number of interacting quantum particles is why *many-body quantum physics* is very much an active research area in solid-state physics and quantum chemistry. But we need not have an analytic solution for everything in order to be satisfied, on the contrary, we can use physical insight and approximations to construct models of complex systems based on simpler, easier to handle systems.

To some extent, this is exactly where chemisty takes over: it is often said that Chemisty is applied physics, but they should simply be thought of as the same thing, but with a focus on different parts of the spectrum: the complexity of solving problems in chemistry is the reason why we need to accept empirical observations as *chemical laws*, even though they work with limited precision and ultimately consequences of the underlying physics as modelled by the Schrödinger equation.

### Quantum numbers and shell filling

The electrons in a hydrogen atom can be described by the following four quantum numbers: $|n, l, l_z, m_s⟩$

Quantum numbers:

* $n=1,2,\ldots$ is the azimuthal (principal) quantum number
* $l=0, 1, \ldots, n-1$ is the angular momentum (also known as $s, p, d, f$ orbitals)
* $l_z=-l, -l+1\ldots, l$ is the $z$-component of angular momentum
* $m_s$ is the $z$-compoment of the spin

Below is an illustration of several lowest energy orbitals in hydrogen:

[![Hydrogen atomic orbitals](https://upload.wikimedia.org/wikipedia/commons/5/5c/Atomic_orbitals_n123_m-eigenstates.png)](https://commons.wikimedia.org/wiki/File:Atomic_orbitals_n123_m-eigenstates.png#/media/File:Atomic_orbitals_n123_m-eigenstates.png){: style="width:50%"}

(image source: Wikipedia © Geek3 CC-BY-SA)


It turns out that electrons in other atoms occupy orbitals similar to those of hydrogen, however the electron energies are very different due to the Coulomb interaction.
Therefore, we can use our knowledge of the hydrogen orbitals to describe other atoms.

When we consider an atom with multiple electrons, we need to determine which orbitals are filled and which are not.
The order of orbital filling is set by several rules:

* _Aufbau principle_: electrons first fill a complete shell (all electrons with the same $n$) before going to the next one
* _Madelung's rule_: electrons first occupy the shells with the lowest $n+l$. If there are several orbitals with equal $n+l$, electrons occupy those with smaller $n$

Combining the two rules, we obtain the shell filing order: 1s, 2s, 2p, 3s, 3p, 4s, 3d, etc.

While these rules accurately predict the electronic structure of most elements, they are only approximate, and fail to describe some of the [heavier elements](https://en.wikipedia.org/wiki/Aufbau_principle#Exceptions_in_the_d-block).

Shell filing is important to us because the valence electrons (those in the outermost shell) are the only ones participating in chemical reactions and electric conduction.
From the valence electrons' point of view, the inner shell electrons act like a negatively charged cloud.
The electrostatic repulsion between them reduces the effective charge of the atomic nucleus, but does not play any further role.

## Covalent bonds and linear combination of atomic orbitals

### Two atoms

Consider two atoms next to each other which form a diatomic molecule.
The total Hamiltonian of the system is
$$
H = V₁ + V₂ + K,
$$
with $V₁$ the potential due to the first nucleus, $V₂$ due to the second nucleus, and $K$ is the kinetic energy of the electron.

Since different orbitals of an atom are separated in energy, we consider one orbital per atom (even though this is often a bad starting point and it should only work for $s$-orbitals).

Let's additionally consider the atoms being sufficiently far apart, such that the shape of the orbitals barely changes due to the presence of the other atom.

Let's denote the wave function of an electron bound to the first and second atom $|1⟩$ and $|2⟩$ respectively:
$$
\begin{align}
(V₁ + K)|1⟩ = ɛ_0|1⟩,\\
(V₂ + K)|2⟩ = ɛ_0|2⟩.
\end{align}
$$

Our main idea is to search for a solution in the form:
$$
|ψ⟩ = φ_{1}|1⟩ + φ_{2}|2⟩.
$$

where $φ_{1}$ and $φ_{2}$ are the probability amplitudes of the respective orbitals.
The orbital $|ψ⟩$ is called a _molecular orbital_ because it describes the entire orbital of the diatomic molecule.
The molecular orbital is created as a *Linear Combination of Atomic Orbitals (LCAO)*.

For simplicity, we assume that the atomic orbitals are orthogonal[^1], i.e. $⟨1|2⟩=0$.
Orthogonality ensures that $|ψ⟩$ is normalized whenever $|φ_1|^2 + |φ_2|^2 = 1$.

We apply the Hamiltonian to the molecular orbital $|ψ⟩$:
$$
H|ψ⟩ = E|ψ⟩ = φ_{1}H|1⟩ + φ_{2}H|2⟩.
$$

Taking the left inner product with $⟨1|$, we obtain

$$
⟨1|E|ψ⟩ = φ_{1}⟨1|H|1⟩ + φ_{2}⟨1|H|2⟩ = E φ_{1}.
$$

Similarly, taking the inner product with $⟨2|$ yields:

$$
E φ_2 = φ_{1}⟨2|H|1⟩ + φ_{2}⟨2|H|2⟩.
$$

We combine these two equations into an eigenvalue problem:
$$
E \begin{pmatrix} φ_1 \\ φ_2 \end{pmatrix}
= \begin{pmatrix}
⟨1|H|1⟩ & ⟨1|H|2⟩ \\ ⟨2|H|1⟩ & ⟨2|H|2⟩
\end{pmatrix}
\begin{pmatrix} φ_1 \\ φ_2\end{pmatrix}.
$$

The eigenvalue problem depends only on two parameters: the **onsite energy** $⟨1|H|1⟩ = ⟨2|H|2⟩ \equiv E_0$ that gives the energy of an electron occupying either of the orbitals, and the **hopping integral** (or just **hopping**) $⟨1|H|2⟩ \equiv -t$ that characterizes the energy associated with the electron moving between the two orbitals.

Let us examine what contitutes the onsite energy and the hopping:
$$
E_0 = ⟨1|H|1⟩ = ⟨1|V₁ + V₂ + K|1⟩ = ɛ_0 + ⟨1|V_2|1⟩,
$$
where we used that $V₁ + K|1⟩ = ɛ_0|1⟩$.
In other words the onsite energy is the combination of the energy of the original orbital plus the energy shift $⟨1|V_2|1⟩$ of the electron due to the potential of the neighboring atom.
Turning to the hopping, we obtain
$$
t = -⟨1|H|2⟩ = -⟨1|V₁ + V₂ + K|2⟩ = -⟨1|V₁|2⟩.
$$

All orbitals $|n⟩$ are purely real because we consider bound state solutions of the Schrödinger equation.
Hence $t$ is real as well.

The eigenvalue problem we obtained describes a particle with a discrete $2×2$ Hamiltonian:
$$
H = \begin{pmatrix} E_0 & -t \\ -t & E_0 \end{pmatrix}.
$$

Diagonalizing this LCAO Hamiltonian yields the following two eigenvalues:
$$
E_{±} = E_0 ∓ t.
$$

The eigenvector corresponding to the eigenvalue $E_+ = E_0 - t$ is even and symmetric:

$$
|ψ_{+}⟩ = \tfrac{1}{\sqrt{2}}(|1⟩ + |2⟩),
$$
while the eigenvector with energy $E_- = E_0 + t$
$$
|ψ_{-}⟩ = \tfrac{1}{\sqrt{2}}(|1⟩ - |2⟩)
$$
is odd/antisymmetric.

The molecular orbitals are shown in the figure below.
According to the *node theorem* of quantum mechanics, wave functions with lower energies have fewer points where $ψ=0$.
Because $ψ_- = 0$ between the two atoms, and $ψ_+$ is not, we conclude that $E_+ < E_-$, and therefore $t > 0$.

![](figures/two_atoms.svg)

### Bonding vs antibonding
If we decrease the interatomic distance, the two atoms get closer and their atomic orbitals have more overlap.
The increase in orbital overlap increases the hopping $t$.
We plot the symmetric and anti-symmetric energies as a function of the inter-atomic distance:

![](figures/bonding.svg)

When an electron (or two, because there are two states with opposite spin) occupies $|ψ_+⟩$, the atoms attract (or *bond*) because the total energy is lowered.
Therefore, if $t$ is positive, $|ψ_+⟩$ is called the **bonding orbital**.

If an electron occupies the $|ψ_{-}⟩$ orbital, the molecular energy increases with decreasing interatomic distance.
This means that the atoms repel each other.
Hence, if $t$ is positive, $|ψ_{-}⟩$ is called the **antibonding orbital**.

Therefore if each atom has a single electron in the outermost shell, these atoms attract because the bonding orbital hosts two electrons with opposite spins.
On the other hand, if each atom has 0 or 2 electrons in the outermost shell, the net force from the bonding and antibonding orbitals cancels out, but Coulomb repulsion remains.

### Summary

* Electrons in atoms occupy shells, with only electrons in the outermost shell (valence electrons) contributing to interatomic interactions.
* The molecular orbital can be written as a Linear Combination of Atomic Orbitals (LCAO)
* The LCAO method reduces the full Hamiltonian to a finite size problem written in the basis of individual orbitals.
* If two atoms have one orbital and one electron each, they occupy the bonding orbital.

## Exercises
### Warm-up questions
1. Is the assumption that the atomic orbitals are orthogonal always a reasonable assumption?
2. What happens if the hopping $t$ is chosen to be negative?
3. How does the size of the Hamiltonian matrix change with the number of atoms?
4. How does the size of the Hamiltonian matrix change if each atom now has two orbitals?
5. Assuming that we have two atoms with a single orbital each, what is the size of the Hamiltonian matrix if we also consider the spin of the electron?

### Exercise 1: Shell-filling model of atoms
1. Describe the shell-filling model of atoms.
2. Use Madelung’s rule to deduce the atomic shellfilling configuration of the element tungsten, which has atomic number 74.
3. Although Madelung’s rule for the filling of electronic shells holds extremely well, there are a number of exceptions to the rule. Here are a few of them:
$$Cu = [Ar] 4s^1 3d^{10}$$
$$Pd = [Kr] 5s^0 4d^{10}$$
$$Ag = [Kr] 5s^1 4d^{10}$$
$$Au = [Xe] 6s^1 4f^{14} 5d^{10}$$
What should the electron configurations be if these elements followed Madelung’s rule and the Aufbau principle?
What could be the reason for the deficiency of Madelung's rule?

### Exercise 2: Application of the LCAO model to the delta-function potential

Consider an electron moving in 1D between two negative delta-function shaped potential wells.
The complete Hamiltonian of this one-dimensional system is then:
$$
\hat{H} = \frac{\hat{p}^2}{2m}-V_0\delta(x_1-x)-V_0\delta(x_2-x),
$$
where $V_0>0$ is the potential strength, $\hat{p}$ the momentum of the electron, and $x_1$, $x_2$ the positions of the potential wells.

??? hint "Properties of a single $\delta$-function potential"

    A delta function $\delta(x_0 - x)$ centered at $x_0$ is defined to be zero everywhere except for $x_0$, where it tends to infinity.
    Further, a delta function has the property:
    $$
    \int_{-\infty}^{\infty} f(x)\delta(x_0-x)dx = f(x_0).
    $$

    The procedure to find the energy and a wave function of a state bound in a $\delta$-function potential, $V=-V_0\delta(x-x_0)$, is similar to that of a quantum well:

    1. Assume that we have a bound state with energy $E<0$.
    2. Compute the wave function $\phi$ in different regions of space: namely $x < x_0$ and $x > x_0$.
    3. Apply the boundary conditions at $x = x_0$. The wave function $\phi$ must be continuous, but $d\phi/dx$ is not. Instead due to the presence of the delta-function:
       $$
       \frac{d\phi}{dx}\Bigr|_{x_0+\epsilon} - \frac{d\phi}{dx}\Bigr|_{x_0-\epsilon}= -\frac{2mV_0}{\hbar^2}\phi(x_0).
       $$
    4. Find at which energy the boundary conditions at $x = x_0$ are satisfied. This is the energy of the bound state.
    5. Normalize the wave function.

Let us apply the LCAO model to solve this problem. Consider the trial wave function for the ground state to be a linear combination of two orbitals $|1⟩$ and $|2⟩$:
$$|ψ⟩ = φ_1|1⟩ + φ_2|2⟩.$$
The orbitals $|1⟩$ and $|2⟩$ correspond to the wave functions of the electron when there is only a single delta peak present:

$$H_1 |1⟩ = \epsilon_1 |1⟩,$$
$$H_2 |2⟩ = \epsilon_2 |2⟩.$$

We start of by calculating the wavefunction of an electron bound to a single delta-peak.
To do so, you first need to set up the Schrödinger equation of a single electron bound to a single delta-peak.
You do not have to solve the Schrödinger equation twice—you can use the symmetry of the system to calculate the wavefunction of the other electron bound to the second delta-peak.

1. Find the expressions for the wave functions of the states $|1⟩$ and $|2⟩$: $ψ_1(x)$ and $ψ_2(x)$.
Also find an expression for their energies $\epsilon_1$ and $\epsilon_2$.
Remember that you need to normalize the wave functions.
2. Construct the LCAO Hamiltonian. To simplify the calculations, assume that the orbitals are orthogonal.
3. Diagonalize the LCAO Hamiltonian and find an expression for the eigenenergies of the system.
It was previously mentioned that $V_0>0$.
Using this, determine which energy corresponds to the bonding energy.


### Exercise 3: Polarization of a hydrogen molecule

Consider a hydrogen molecule as a one-dimensional system with two identical nuclei at $x=-\frac{d}{2}$ and $x=+\frac{d}{2}$, so that the center of the molecule is at $x=0$.
Each atom contains a single electron with charge $-e$.
The LCAO Hamiltonian of the system is given by


$$
H_{\textrm{eff}} = \begin{pmatrix}
          E_0&&-t \\
          -t&&E_0
          \end{pmatrix}.
$$

1. Let us add an electric field $\mathcal{E} \hat{\bf{x}}$ to the system.
   Which term needs to be added to the Hamiltonian of each electron?

    ??? hint "The electric potential is given by"
        $$
        V_{\mathbf{E}}=-\int_{C} \mathbf{E} \cdot \mathrm{d} \boldsymbol{\ell}
        $$

2. Compute the LCAO Hamiltonian of the system in presence of the electric field.
   What are the new onsite energies of the two orbitals?
3. Diagonalize the modified LCAO Hamiltonian. Find the ground state wavefunction $ψ$.
4. Find the polarization $P$ of the molecule in the ground state.

    ??? hint "Reminder: polarization"
        The polarization $P$ of a molecule with $n\leq 2$ electrons at its ground state $|ψ⟩$ is:
        $$
        P = n e ⟨ψ|x|ψ⟩.
        $$
        Use that ground state you found in 3.2 is a linear superposition of two orthogonal orbitals centered at $-\frac{d}{2}$ and $+\frac{d}{2}$.

[^1]: See the book exercise 6.5 for relaxing the orthogonality assumption.

*[LCAO]: Linear combination of atomic orbitals
