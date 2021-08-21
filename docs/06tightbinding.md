# The tight binding model

!!! danger  "Unbaked"

    The content here is still very much under development. Please come back soon!

## Introduction

![](../images/04_iron.jpg)

The kinetic theory of Drude was a great first step in trying to answer the question "metals, how do they work?", but it was clear from the outset that there were problems with the theory. But with the discovery of the Pauli exclusion principle, it seemed only logical that with the inclusion of _the_ fundamental property of the electrons, life would improve. Indeed it does...

!!! danger  "Expected competencies"

    It is assumed that you have familiarity with the following concepts/techniques:

    * Statistical mechanics: familiarity with Fermi-Dirac statistics
    * Quantum mechanics: Wavefunction of a free (unbound) electron

!!! note  "Text reference"
    The material covered here is discussed in section(s) $\S 4$ of [The Oxford Solid State Basics](https://global.oup.com/academic/product/the-oxford-solid-state-basics-9780199680771?cc=au&lang=en&)

!!! info "Computational content"

    The Jupyter notebook associated with this section can be accessed by clicking the icon below:
    [<i class="fab fa-python fa-5x"></i>](#){ .md-button .md-button--primary class="text-center" style="margin-left: 45%"}

---

# Electrons and phonons in 1D
_(based on chapters 9.1-9.3 & 11.1-11.3 of the book)_

!!! success "Expected prior knowledge"

    Before the start of this lecture, you should be able to:

    - Derive Newton's equations of motion of a triatomic chain (previous lecture).
    - Write down the dispersion relation of phonons in the Debye model.
    - Express complex exponentials through trigonometric functions and vice versa.
    - Apply Taylor expansion trigonometric functions.
    - Take derivatives inverse trigonometric functions.

!!! summary "Learning goals"

    After this lecture you will be able to:

    - Formulate the equations of motion of electrons and phonons in 1D.
    - Derive the dispersion relation from the equations of motion.
    - Derive the group velocity, effective mass, and density of states from the dispersion relation.

Last lecture:

* Vibrational modes of few-atom chains (analyzed using Newton's equations)
* Orbital energies of electrons in few-atom chains (analyzed using LCAOs)

This lecture:

* Phonons and electrons in chains of infinitely many atoms.
* Main idea: use *periodicity* in space, similar to periodicity in time

To emphasize the similarities and the differences between electrons and phonons, we will deal with both types of particles at once.

## Equations of motion

### Phonons

![](figures/phonons2.svg)

In the Debye model, we assumed that the dispersion relation is strictly linear in $k$.
Now is the time to revisit this assumption.
To do that, let us consider a 1D homogeneous chain of atoms.
We assume that the atoms in the chain interact only with their nearest neighbors through a harmonic potential, like we derived in the [previous lecture](6_bonds_and_spectra.md).
In other words, we model the atoms as point masses connected by identical springs.

We denote the displacement of atom $n$ from equilibrium by $u_n$. Within this convention, Newton's equation of motion for the $n$-th atom is given by:

$$
m \ddot{u}_n = -\kappa (u_n - u_{n-1}) -\kappa (u_n - u_{n+1}).
$$

We use the periodic boundary conditions just like we did in the Sommerfield model.
The boundary conditions imply that in a system of size $L = Na$, we have $u_N = u_0$.

### Electrons

The following figure shows the interatomic potential with atoms placed at $x_k = ka$ with $k \in \mathbb{Z}$:

```python
x = np.linspace(0.001, 3, 200)

fig, ax = pyplot.subplots(1, 1)
ax.plot(x, 1.2-1/np.abs(np.sin(np.pi * x))**(1/2))
ax.set_ylim(-.7, .5)
ax.set_xlabel("$x$")
ax.set_ylabel("$U(x)$")
ax.set_xticks([-.05, 1, 2])
ax.set_xticklabels(["$0$", "$a$", "$2a$"])

draw_classic_axes(ax)
```

Similarly to the triatomic system case, we formulate the molecular orbital via the LCAO model:
$$
\vert \Psi \rangle = \sum_n \phi_n |n \rangle.
$$
We assume only nearest-neighbor hopping $-t$ and an on-site energy $E_0$.
The coupled Schrödinger equation of the $|n \rangle$ orbital is:
$$
E \phi_n = E_0 \phi_n - t \phi_{n+1} - t \phi_{n-1}.
$$

Again, the periodic boundary conditions imply $\phi_N = \phi_0$.

We now have the equations of motion of both phonons and electrons.
All that remains is to solve them.

### Key idea for solving these equations

In order to solve the equations of motion, we need to come up with a reasonable guess.
If we take a look at the equations of motion, we see that they are the same for all atoms.
To be specific, the structure of the equations is the same no matter what value of $n$ we choose.
Since these equations define the solutions, we reason that the solutions should also be independent of the choice of $n$.
As a result, we assume a plane wave solution, also called a *plane wave ansatz*, with the same amplitude for each atom.
In the case of phonons, we obtain
$$
u_n = Ae^{i \omega t - i k x_n},
$$
and the ansatz for electrons is given similarly by
$$
\phi_n = Be^{i E t/\hbar - i k x_n}.
$$
We wrote $x_n=na$ and we wrote the time-dependent solution of the Schrödinger equation to emphasize the similarity between the two systems.

We already know that the periodic boundary conditions only allow plane waves with $k$ being a multiple of $2\pi/L$.
In the case of the electron system, periodic boundary conditions give $\phi_0 = \phi_N$, which results in

$$
1 = e^{ik0} = e^{ikNa}.
$$

The above equation defines the allowed values of $k$:
$$
k = \frac{2 \pi p}{Na}, \quad \text{with} p \in \mathbb{Z}.
$$

We use the quantized values of $k$ in our plane wave ansatz: $e^{ikx_n} = e^{i p \frac{2\pi}{Na} n a} = e^{i \frac{2 \pi n p}{N}}$.
We notice something interesting if we investigate the case of $p→p+N$.
In this case, the plane wave ansatz becomes $e^{i \frac{2\pi n(p+N)}{N}} = e^{i \frac{2\pi np}{N} + i2\pi n} = e^{i \frac{2\pi np}{N}}$, which is exactly the same solution.
Counting the number of inequivalent plane waves, we find exactly $N$ different solutions in total.
All that is left is to find the energy of each solution!

The reason why solutions with different values of $k$ are identical is [aliasing](https://en.wikipedia.org/wiki/Aliasing#Sampling_sinusoidal_functions): because the plane wave is only defined at discrete positions, acquiring a phase factor of $2π$ between two atoms is equivalent to nothing happening:

```python
x = np.linspace(-.2, 2.8, 500)
fig, ax = pyplot.subplots()
ax.plot(x, np.cos(pi*(x)), label=r'$k=\pi/a$')
ax.plot(x, np.cos(3*pi*(x)), label=r'$k=3\pi/a$')
ax.plot(x, np.cos(5*pi*(x)), label=r'$k=5\pi/a$')
sites = np.arange(3)
ax.scatter(sites, np.cos(pi*(sites)), c='k', s=64, zorder=5)
ax.set_xlabel('$x$')
ax.set_ylabel('$u_n$')
ax.set_xlim((-.1, 3.2))
ax.set_ylim((-1.3, 1.3))
ax.legend(loc='lower right')
draw_classic_axes(ax)
ax.annotate(s='', xy=(0, -1.1), xytext=(1, -1.1),
            arrowprops=dict(arrowstyle='<->', shrinkA=0, shrinkB=0))
ax.text(.5, -1.25, '$a$', ha='center');
```

??? Question "How many different solutions did we expect to find?"
    We have a system with $N$ degrees of freedom (either $u_n$ or $\phi_n$), and therefore we expect $N$ normal modes (or eigenstates).

## Solving the equations of motion

### Phonons

We substitute the plane wave ansatz into the equations of motion:
$$
-m \omega^2 A e^{i\omega t - ikx_n} = \kappa A  e^{i\omega t}(-2 e^{-ikx_n} + e^{-ikx_n+ika}+ e^{-ikx_n-ika}).
$$

Searching for solutions with $A \neq 0$ we obtain
$$
-m \omega^2 = \kappa (-2 + e^{ika}+ e^{-ika})=\kappa [-2 + 2\cos(ka)].
$$

Or after a further simplification:
$$
\omega = \sqrt{\frac{2\kappa}{m}}\sqrt{1-\cos(ka)}= 2\sqrt{\frac{\kappa}{m}}|\sin(ka/2)|,
$$
where we substituted $1-\cos(x) = 2\sin^2(x/2)$.

We arrive at the phonon dispersion relation shown below.

```python
k = np.linspace(-2*pi, 6*pi, 500)
fig, ax = pyplot.subplots()

pyplot.plot(k, np.abs(np.sin(k/2)))

ax.set_ylim(bottom=0, top=1.2)
ax.set_xlabel('$ka$')
ax.set_ylabel(r'$\omega$')
pyplot.xticks(list(2*pi*np.arange(-1, 4)) + [-pi, pi],
              [r'$-2\pi$', '$0$', r'$2\pi$', r'$4\pi$', r'$6\pi$',
               r'$-\pi$', r'$\pi$'])
pyplot.yticks([1], [r'$2\sqrt{\frac{\kappa}{m}}$'])
pyplot.vlines([-pi, pi], 0, 1.1, linestyles='dashed')
pyplot.hlines([1], .1*pi, 1.3*pi, linestyles='dashed')
draw_classic_axes(ax);
# ax.annotate(s='', xy=(-pi, -.15), xytext=(pi, -.15),
#             arrowprops=dict(arrowstyle='<->', shrinkA=0, shrinkB=0))
# ax.text(0, -.25, '1st Brillouin zone', ha='center')
# ax.set_ylim(bottom=-.3);
```

The periodicity of the dispersion relation is a consequence of what we observed before: since plane waves with $k$-vectors differing by $2π/a$ are exactly the same, the repeated periods of the dispersion relation describe the same plane waves.

#### Comparison to the Debye model

**Sound velocity:** At small $k$, $\sin(ka/2)\approx ka/2$. Therefore $\omega \approx \sqrt{\kappa/m} k a = v_sk$, with $v_s$ the sound velocity.
We therefore justify the linear dispersion approximation in the Debye model!

**Cut-off frequency:**

The Debye model introduces the cutoff frequency $\omega_D$ to limit the number of phonon modes, and does not identify the origin of the cutoff.
Now because of the finite number of plane waves, the integration over the $k$-space has a finite size: $\sum_p → \frac{L}{2\pi}\int_{-\pi/a}^{\pi/a}dk$.
This automatically gives us a maximal frequency without additional assumptions.

### Electrons

Once again we substitute the plane wave ansatz into the equations of motion:

$$
E Ae^{iEt/\hbar-ikna} = E_0 Ae^{iEt/\hbar-ikna} - t Ae^{iEt/\hbar-ik(n+1)a} - t Ae^{iEt/\hbar-ik(n-1)a},
$$

Again, we are not interested in a trivial solution, hence we assume $A \neq 0$ and thus
$$
E = E_0 -te^{-ika} -te^{ika} = E_0 - 2t\cos(ka),
$$
which gives us the dispersion relation below.

```python
pyplot.figure()
k = np.linspace(-pi, pi, 300)
pyplot.plot(k, -np.cos(k))
pyplot.xlabel('$ka$'); pyplot.ylabel('$E$')
pyplot.xticks([-pi, 0, pi], [r'$-\pi$', 0, r'$\pi$'])
pyplot.yticks([-1, 0, 1], ['$E_0-2t$', '$E_0$', '$E_0+2t$']);
```

We see that the electron dispersion consists of a *band* of allowed energies $E_0 -2t < E < E_0 + 2t$.
That particles occupy bands of allowed energies is why a dispersion relation is also often called a *band structure*.
Due to the spin degeneracy, each band has 2$N$ possible states if we consider a system with $N$ atoms.

If each atom contains 2 electrons and a single orbital, all the states in the band must be occupied by electrons.
Because all the available states are occupied, there is always exactly the same number of electrons moving in the positive direction, as there are in the negative.
Hence, no matter what we do, our system is incapable of conducting electrons, and therefore we have derived the existence of insulators!

Let us also compare the electron band structure with the free electron model.
Focusing on the dispersion relation close to the band bottom at $k=0$, we approximate the energy as
$$
E \approx E_0 - 2t + t (ka)^2.
$$

If we compare this to the dispersion relation $E=\hbar k^2/2m$ of the free electrons model, we see that the band structure is similar, but the lowest available energy is $E_0-2t$ instead of $0$, and the electrons behave as if they had a different mass $m^*=\hbar^2/2ta^2$.

### Group velocity, effective mass, density of states

*(here we only discuss electrons; for phonons everything is the same except for replacing $E = \hbar \omega$)*

Let us think what happens if we apply an external electric field to the crystal:

```python
x = np.linspace(0.001, 3, 200)

fig, ax = pyplot.subplots(1, 1)
ax.plot(x, 1.2-1/np.abs(np.sin(np.pi * x))**(1/2) + .2 * (x - 1.5))
ax.plot(x, .2 * (x - 0.25), '--')
ax.set_ylim(-.7, .5)
ax.set_xlabel("$x$")
ax.set_ylabel("$U(x)$")
ax.set_xticks([-.05, 1, 2])
ax.set_xticklabels(["$0$", "$a$", "$2a$"])

draw_classic_axes(ax)
```

The full Hamiltonian of the system is

$$
H = \frac{p^2}{2m} + U_\textrm{atomic}(x) + e \mathcal{E} x,
$$
where $U_\textrm{atomic}$ is the potential created by the nuclei, and $\mathcal{E}$ the electric field.

A typical electric field is much smaller than the interatomic potential, and therefore we can start by obtaining the dispersion relation $E(k)$ without electric field (by applying the LCAO method), and then solve
$$ H = E(k) + e\mathcal{E}x.$$

To derive how particles with an arbitrary dispersion relation move, we recall the [Hamilton's equations](https://en.wikipedia.org/wiki/Hamiltonian_mechanics) for particle velocity $v$ and force $F$:

$$\begin{aligned}
v \equiv \frac{dr}{dt} &= \frac{\partial H(p, r)}{\partial p}\\
F \equiv \frac{dp}{dt} &= -\frac{\partial H(p, r)}{\partial r}.
\end{aligned}$$

Substituting $p = \hbar k$ into the first equation we arrive to the expression for the electron **group velocity** $v \equiv \hbar^{-1}\partial E/\partial k$.
From the second equation we obtain that the force acting on electron in a band stays $-e\mathcal{E}$, which in turn gives results in the acceleration
$$
\frac{dv}{dt} = \frac{∂v}{∂p}\frac{dp}{dt} = F/m.
$$
Comparing this expression with $dv/dt = F/m$, we arrive to the **effective mass**:
$$
m^* \equiv \left(\frac{∂v}{∂p}\right)^{-1} = \left(\frac{∂²E}{∂p²}\right)^{-1} = ħ²\left(\frac{∂²E}{∂k²}\right)^{-1}.
$$

The group velocity describes how quickly electrons with a certain $k$-vector move, while the effective mass describes how hard they are to accelerate by applying external force.

By using the dispersion relation we derived earlier, we obtain the effective mass like this:

```python
pyplot.figure(figsize=(8, 5))
k = np.linspace(-pi, pi, 300)
meff = 1/np.cos(k)
color = list(matplotlib.rcParams['axes.prop_cycle'])[0]['color']
pyplot.plot(k[meff > 0], meff[meff > 0], c=color)
pyplot.plot(k[meff < 0], meff[meff < 0], c=color)
pyplot.ylim(-5, 5)
pyplot.xlabel('$ka$'); pyplot.ylabel('$m^*$')
pyplot.xticks([-pi, 0, pi], [r'$-\pi$', 0, r'$\pi$']);
```

Notice that the effective mass can be negative, which implies the electrons accelerate in the direction opposite to the applied force.

### Density of states

The DOS is the number of states per unit energy. In 1D we have
$$g(E) = \frac{L}{2\pi}\sum |dk/dE| = \frac{L}{2\pi}\sum |v|^{-1}$$

The sum goes over all possible values of $k$ and spin which have the same energy $E$.
If we are working in two or more dimensions, we must integrate over the values of $k$ with the same energy.
Also take note that for energies below $E_0 - 2t$ or above $E_0 + 2t$, there are no values of $k$ with that energy, so there is nothing to sum over.

Once again, starting from
$$ E = E_0 - 2t \cos(ka), $$
we get
$$
ka = \pm\arccos[(E - E_0) / 2t],
$$
and
$$
|v| ^{-1} = \left|\frac{dk}{dE} \right| = \frac{1}{a}\frac{1}{\sqrt{4t^2 - (E - E_0)^2}}.
$$
You can get to this result immediately if you remember the derivative of arccosine. Otherwise you need to go the long way: compute $dE/dk$ as a function of $k$, express $k$ through $E$ as we did above, and take the inverse.

We now add together the contributions of the positive and the negative momenta as well both spin orientations, and arrive to the density of states
$$
g(E) = \frac{L}{2\pi}\frac{4}{a}\frac{1}{\sqrt{4t^2 - (E - E_0)^2}}.
$$
A quick check: when the energy is close to the bottom of the band, $E = E_0 - 2t + \delta E$, we get $g(E) \propto \delta E^{-1/2}$, as we expect in 1D.

The process of calculating the DOS at a given energy $E$ of a spin-independent Hamiltonian is done systematically with the following steps:

1. At a given energy $E$, determine *all* of the values of $k$ which correspond to that $E$ using the dispersion relation.
2. Compute $\rvert dk / dE \rvert$. Do this either by writing $k$ as a (multi-valued) function of $E$ and differentiating, or by computing $(dE / dk)^{-1}$.
3. Sum or integrate $dk / dE$ over the allowed values of $k$ found in 1 and multiply by any degeneracies (spin/polarization).
4. Multiply by spin degeneracy.

If the Hamiltonian depends on spin, then there is no spin degeneracy and the spin number $s$ must be treated in the same way as $k$.

## Summary

* By using plane waves in real space as an Ansatz we found all normal modes and energies for phonons and electrons in 1D
* Computing dispersion relations explains the problems we listed before (need for cutoff, lack of scattering with every single atom, existence of insulators).
* Electrons and phonons have a complicated nonlinear relation between momentum and velocity (**group velocity**), effective mass, and density of states.

## Exercises

### Warm-up questions
1. Compare the expression of the effective mass with Newton's second law. Do you observe any similarities?
2. Check the units of the group velocity. Is it what you expect?
3. Do the same for the effective mass.
4. Calculate the effective mass of the free-electron dispersion relation. Is this what was expected?
5. Under what condition is the effective mass the same for each electron?


### Exercise 1: Lattice vibrations

1. From the dispersion relation of a 1D monatomic chain given in the lecture notes, calculate the group velocity $v_g$.
2. Using the group veolcity found above, calculate the density of states $g(\omega)$.
3. Sketch them.
4. From the 1D dispersion relation $\omega(k)$ in the picture below, sketch the group velocity $v_g(k)$ and the density of states $g(\omega)$.

![](figures/NNNdispersion.svg)

### Exercise 2: Vibrational heat capacity of a 1D monatomic chain

1. Give the total energy $U$ of a 1D monatomic chain as an integral expression.
To do so, first derive the density of states from the phonon dispersion relation derived in the lecture notes.
2. Give an integral expression for the heat capacity $C$.
3. Compute the heat capacity numerically, using e.g. Python.
4. Do the same for $C$ in the Debye model and compare the two.
What differences do you see?

### Exercise 3: Next-nearest neighbors chain

Consider electrons in a 1D atomic chain again:

```python
x = np.linspace(0.001, 3, 200)

fig, ax = pyplot.subplots(1, 1)
ax.plot(x, 1.2-1/np.abs(np.sin(np.pi * x))**(1/2))
ax.set_ylim(-.7, .5)
ax.set_xlabel("$x$")
ax.set_ylabel("$U(x)$")
ax.set_xticks([-.05, 1, 2])
ax.set_xticklabels(["$0$", "$a$", "$2a$"])

draw_classic_axes(ax)
```

Let's expand the one-dimensional chain model by extending the range of the interaction further than the nearest neighbors:

$$ \langle \phi_n | H | \phi_{n+2}\rangle \equiv -t' ≠ 0.$$

1. Write down the new Schrödinger equation for this system.

    ??? hint "hint"
        There are now two more terms in the equation: $-t' \phi_{n-2} - t' \phi_{n+2}$.

2. Solve the Schrödinger equation to find the dispersion relation $E(k)$.

    ??? hint "hint"
        Use the same Ansatz as for the nearest neighbors case: $ \phi_n = \phi_0 \exp(ikna) $.

3. Calculate the effective mass $m^*$.
4. Sketch the effective mass as a function of $k$ for the cases $t=2t'$,$t=4t'$ and $t=10t'$.
