# Electrons in metals II

## Introduction

Previously, we saw how an empirical observation describing the behaviour of the specific heat of solids motivated the development of atomic-scale models of solids in order to understand and predict their behaviour. This marked the beginning of using theories which involved the quantisation of certain observables to accurately predict previously unexplained behaviour, but as we shall see, one must continue down the rabbit hole of quantisation in order to better model physical systems.

!!! danger  "Expected competencies"

    It is assumed that you have familiarity with the following concepts/techniques:

    * Wave mechanics: acoustic waves in solids (sound)

!!! info  "Text reference"
    The material covered here is discussed in section(s) $\S 4$ of [The Oxford Solid State Basics](https://global.oup.com/academic/product/the-oxford-solid-state-basics-9780199680771?cc=au&lang=en&)

_(based on chapter 4 of the book)_  

!!! success "Expected prerequisites"

    Before the start of this lecture, you should be able to:

    - Write down the Fermi-Dirac distribution function.
    - Write down the Schrödinger equation and solve it in free space.
    - Apply periodic boundary conditions, and compute the density of states
      given a sufficiently simple dispersion relation.

!!! summary "Learning goals"

    After this lecture you will be able to:

    - Calculate the electron density of states in 1D, 2D, and 3D using the Sommerfeld free-electron model.
    - Express the number and energy of electrons in a system in terms of integrals over k-space for $T = 0$.
    - Use the Fermi-Dirac distribution to extend the previous learning goal to $T > 0$.
    - Calculate the electron contribution to the specific heat of a solid.
    - Describe terms such as the Fermi energy and the Fermi wavevector.

## Electrons vs phonons

> Two electrons are sitting on a bench. Another one approaches and asks: "May I join you guys?"
> The first two immediately reply: "Who do you think we are? Bosons?"

In the [Debye model](2_debye_model.md), we learned the properties and physical behavior of phonons.  
The *Sommerfeld* model applies the same conceptual approach to electrons in metals.
Sommerfeld considered the electrons as _free particles_ that are not interacting with atomic nuclei, which is why the model is also called the *free electron model*.
Similar to the Debye model, we consider a cubic box of size $L \times L \times L$ with periodic boundary conditions.
The solutions to the Schrödinger equation of a free particle are plane waves:
$$
\psi \propto \exp(i\mathbf{k} \cdot \mathbf{r}),
$$
with $\mathbf{k}$ is the electron wave vector.
Because of the periodic boundary conditions, $\mathbf{k}$ must take discrete values $\frac{2\pi}{L} (n_x, n_y, n_z)$.
The plane waves have eigenenergies given by the dispersion relation

$$
\varepsilon(\mathbf{k}) = \frac{\hbar^2 \mathbf{k}^2}{2m},
$$

with $m$ being the mass of the electron.
Let us plot $\varepsilon(k)$ as a function of $k$ for a 1D system:

```python
kf = 3;
extrapol = 1.1;
ks = np.arange(-kf, kf+1);
kcont = np.linspace(-extrapol*kf, extrapol*kf, 200);

Edis = ks**2;
Econt = kcont**2;

fig = pyplot.figure();
ax = fig.add_subplot(111);
ax.plot(kcont, Econt);
ax.plot(ks, Edis, 'k.', markersize=10);
for i in range(2*kf + 1):
    ax.plot([ks[i], ks[i]], [0.0, Edis[i]], 'k:');
ax.set_xlim(-3.75, 3.75);
ax.set_ylim(0.0, 11);

ax.set_xlabel(r"$k \: \left[ \frac{2 \pi}{L} \right]$");
ax.set_ylabel(r"$\varepsilon$");

ax.set_xticklabels([""] + ks.tolist() + [""]);
ax.set_yticks([]);

draw_classic_axes(ax, xlabeloffset = .6);
```

Here each black dot is a possible electron state.

In addition to having a quadratic dispersion and not linear dispersion, electrons also obey fermionic, and not bosonic statistics.
As a result, the occupation of electron states is described by the Fermi-Dirac distribution

$$
n_{F}(\beta(\varepsilon-\mu)) = \frac{1}{e^{\beta(\varepsilon-\mu)}+1}.
$$

Here $\beta = 1/k_{B}T$, $\varepsilon$ is the energy, and $\mu$ the _chemical potential_ of an electron.
The Fermi-Dirac distribution defines the number of electrons in the system:

$$
\begin{align}
N &= 2 \sum_{\mathbf{k}} n_{F}(\beta(\varepsilon-\mu))\\
&= 2 \left( \frac{L}{2 \pi} \right)^3 \int n_{F}(\beta(\varepsilon-\mu))\mathrm{d} \mathbf{k}.
\end{align}
$$

Just like with phonons, we replaced a discrete sum over $k$ with a volume integral.
The factor 2 here accounts for the number of distinct electron states per $\mathbf{k}$ value.

??? question "Check: why is there a degeneracy of 2? Weren't there 3 polarizations?"

    The factor $2$ accounts for the spin degeneracy. To keep track of the origin of this term we will denote the spin degeneracy as $2_s$.

Similar to the tota energy of phonons in the Debye model, the expression for the total energy of electrons is

$$
E = 2_s \left( \frac{L}{2 \pi} \right)^3 \int \varepsilon(\mathbf{k}) n_{F}(\beta(\varepsilon-\mu)) \mathrm{d} \mathbf{k}.
$$

There are only two differences: the distribution is $n_{F}$ instead of $n_B$ and the degeneracy is 2 instead of 3.
In the table below we summarize the properties of both phonons and electrons.

|   | Phonons | Electrons |
| - | - | - |
| Dispersion relation | $\omega = v_s \lvert\mathbf{k}\rvert$ | $\varepsilon = \frac{\hbar^2\mathbf{k}^2}{2m}$ |
| Statistics | Bose-Einstein | Fermi-Dirac |
| $n(\varepsilon) =$ | $1/(e^{\beta \varepsilon} - 1)$ | $1/(e^{\beta(\varepsilon - \mu)} + 1)$ |
| Degeneracy per $\mathbf{k}$ | 3 (polarization) | 2 (spin) |
| Total particle number | temperature-dependent | constant |

!!! note "About $\hbar$"

    Within quantum mechanics energy and frequency are related by Planck's constant: $\varepsilon = \hbar\omega$.
    Similarly, $p = \hbar k$ relates a particle's momentum with its wave vector.
    This relation is so unambiguous that you may encounter these terms used synonymously in scientific literature.

The last difference is important: warming a material up creates more thermally excited phonons.
The number of electrons, on the other hand, stays the same: the electrons may not appear out of nowhere.[^1]

## The Fermi sea

To determine the chemical potential $\mu$ let us consider a 2D system with zero temperature and a finite number of electrons.
At $T=0$, the Fermi-Dirac distribution becomes a step function
$$
n_{F}(\beta(\varepsilon-\mu)) = \Theta(-(\varepsilon-\varepsilon_F)).
$$
The chemical potential at $T=0$ is called the _Fermi energy_ $\varepsilon_F$.
All electron states with lower energies are occupied, and all the states with higher energies are empty.
In the reciprocal space, the occupied $\mathbf{k}$-states form a circle (in 1D it is a line and in 3D a sphere).

```python
# creating grid
N = 10
x = np.linspace(-N//2, N//2, N+1)
xx, yy = np.meshgrid(x,x)

# Initialzing figure
fig = pyplot.figure(figsize = (10,10));
ax = fig.add_subplot(111);

# Creating figure
bound = N//3
ax.scatter(xx[np.sqrt(xx**2+yy**2)<=bound],yy[np.sqrt(xx**2+yy**2)<=bound], color = 'k')
ax.scatter(xx[np.sqrt(xx**2+yy**2)>bound],yy[np.sqrt(xx**2+yy**2)>bound], facecolors='none', edgecolors='k')
ax.add_patch(pyplot.Circle((0, 0), bound+0.05, color='k', fill=False))
ax.set_xlim([-N//2, N//2])
ax.set_ylim([-N//2, N//2])
ax.set_xticks([1,2,N//2-0.5]);
ax.set_yticks([1,2,N//2-0.5]);
ax.set_xticklabels([r'$\frac{2 \pi}{L}$',r'$\frac{4 \pi}{L}$',r"$k_x$"])
ax.set_yticklabels([r'$\frac{2 \pi}{L}$',r'$\frac{4 \pi}{L}$',r"$k_y$"])
draw_classic_axes(ax, xlabeloffset = .8, ylabeloffset = 0.2);

```

A good metaphor for describing this state of many electrons is a sea: electrons occupy a finite area in reciprocal space, starting from the "deepest" points with the lowest energy all the way up to the chemical potential—also called Fermi level.
The border of the Fermi sea is called the Fermi surface (you should notice a pattern here), and in the free electron model it is a sphere with the radius equal to *Fermi wave vector*.
To clarify the relation between these concepts let us take a look at the dispersion relation in 1D:

```python
kf = 3.0;
extrapol = 4.0/3.0;
kfilled = np.linspace(-extrapol*kf, extrapol*kf, 100);
kstates = np.linspace(-extrapol*kf, extrapol*kf, 500);

Efilled = kfilled**2;
Estates = kstates**2;

fig = pyplot.figure();
ax = fig.add_subplot(111);

# Creating plot
trans = 1
ax.plot([kf, kf], [0.0, kf*kf], 'k:');
ax.plot(kstates, Estates, color = 'lightblue', linestyle = '-',alpha = trans);
ax.scatter(kfilled[np.abs(kfilled)<=kf], Efilled[np.abs(kfilled)<=kf], color = 'k', s = 3.3**2, zorder = 10);
ax.scatter(kfilled, Efilled, facecolors='none', edgecolors='k', s = 3.3**2, zorder = 10);
ax.axhline(kf*kf, linestyle = "dotted", color='k');

ax.set_xticks([kf]);
ax.set_yticks([kf*kf + 0.4]);
ax.set_xticklabels([r"$k_F$"]);
ax.set_yticklabels([r"$ε_F$"]);

ax.set_xlabel(r"$k$");
ax.set_ylabel(r"$ε$");

ax.set_xlim(-kf*extrapol, kf*extrapol)
ax.set_ylim(0.0, kf*kf*extrapol);
draw_classic_axes(ax, xlabeloffset=.6);
```

By using the dispersion relation, we arrive to the relation
$$
\varepsilon_F = \frac{\hbar^2 \mathbf{k}_F^2}{2m}.
$$

The Fermi wavevector $\mathbf{k}_F$ also defines the _Fermi momentum_ $\mathbf{p}_F = \hbar \mathbf{k}_F$ and the _Fermi velocity_:

$$
\mathbf{v}_F = \frac{\mathbf{p}_F}{m} = \frac{\hbar \mathbf{k}_F}{m}.
$$

??? question "The Fermi energy of copper is ~7 eV. What is the corresponding Fermi velocity?"

    The Fermi velocity $v_F\approx$ 1700 km/s or 0.3% of the speed of light, and much faster than the Drude theory drift velocity!


## Density of states

Like before, in order to compute heat capacity, we need to find the density of states—the number of states per energy interval.
Once again, we compute the density of states at the energy $\varepsilon$ as a derivative of the total number of states below that energy.
$$
g(\varepsilon) = \frac{dN}{d\varepsilon}.
$$
Let us calculate the density of states for a 3D system.
Because the dispersion of the free electron is isotropic[^2], we utilize spherical coordinates.
The total number of states is then
$$
\begin{align}
N &\overset{\mathrm{3D}}{=}2_s \left(\frac{L}{2\pi}\right)^3\int_{\varepsilon(\mathbf{k}) < \varepsilon}\mathrm{d}{\mathbf{k}}\\
&=2_s \left(\frac{L}{2\pi}\right)^3 4\pi\int k^2\mathrm{d}k\\
&=\frac{V}{\pi^2}\int k^2\mathrm{d}k,
\end{align}
$$
We rewrite the expression above by substituting $k=\hbar^{-1}\sqrt{2m\varepsilon}$ and $\mathrm{d}k=\hbar^{-1}\sqrt{m/2\varepsilon} d\varepsilon$:
$$
\begin{align}
N &=\frac{V}{\pi^2}\int\frac{2m \varepsilon}{\hbar^3}\sqrt{\frac{m}{2\varepsilon}}\mathrm{d}\varepsilon\\
&=\frac{Vm^{3/2}}{\pi^2\hbar^3}\int\sqrt{2\varepsilon}\ \mathrm{d}\varepsilon
\end{align}
$$

Therefore we find the density of states:
$$
\begin{align}
g(\varepsilon) &= \frac{ \mathrm{d}N}{ \mathrm{d}\varepsilon}\\
& =\frac{Vm^{3/2}\sqrt{2\varepsilon}}{\pi^2\hbar^3} \propto\sqrt{\varepsilon}
\end{align}
$$

We observe that the density of states of a 3D solid is proportional to a square root of energy:
$$
g(\varepsilon) \propto\sqrt{\varepsilon}
$$

Repeating the similar derivations, we find the density of states of 1D and 2D systems:

* 1D: $g(\varepsilon) = \frac{2 L}{\pi} \frac{ \mathrm{d}k}{ \mathrm{d}\varepsilon} \propto 1/\sqrt{\varepsilon}$
* 2D: $g(\varepsilon) = \frac{k L^2}{\pi} \frac{ \mathrm{d}k}{ \mathrm{d}\varepsilon} \propto \text{constant}$

We plot these three behaviors of $g(\varepsilon)$ below for a comparison.

```python
E = np.linspace(0.001, 2, 500)
fig, ax = pyplot.subplots()

# Plotting the figure
ax.plot(E, 1/np.sqrt(E), label = '1D')
ax.plot(E, 9*np.ones(len(E)), label = '2D')
ax.plot(E, 15*np.sqrt(E), label = '3D')

ax.set_ylabel(r"$g(\varepsilon)$")
ax.set_xlabel(r"$\varepsilon$")
ax.legend()
draw_classic_axes(ax, xlabeloffset=.2)
```

## Relationship between the Fermi energy and the system parameters
We would like to relate the Fermi energy $\varepsilon_{F}$ to the system parameters the number of electrons in the system ($N$) and the volume of the box $V = L^3$.
To do so, we calculate the number of electrons in the system at $T = 0$ using the previously found density of states:
$$
\begin{align}
N &= \int \limits_0^{\infty} n_{F}(\beta(\varepsilon-\mu)) g(\varepsilon) \mathrm{d}\varepsilon\\
&\overset{\mathrm{T = 0}}{=}\int \limits_0^{\varepsilon_F}g(\varepsilon)\mathrm{d}\varepsilon \\
&\overset{\mathrm{3D}}{=} \frac{V}{3\pi^2\hbar^3}(2m\varepsilon_F)^{3/2}.
\end{align}
$$
Inverting the above equation yields:
$$
\varepsilon_{F} = \frac{\hbar^2}{2m}\left( 3\pi^2\frac{N}{V} \right)^{\frac{2}{3}}.
$$
We use the dispersion relation ($\varepsilon(\mathrm{k}) = \frac{\hbar^2 \mathbf{k}^2}{2m}$) to express the Fermi wavevector $k_{F}$:
$$
k_F = \left( 3\pi^2\frac{N}{V} \right)^{\frac{1}{3}}.
$$
Using the Fermi wavevector, we calculate _Fermi wavelength_ $\lambda_F\equiv 2\pi/k_F$ and observe that it is on the order of the atomic spacing for typical free electron densities in metals[^3].

## Heat capacity

We now extend our discussion to $T > 0$ by taking a closer look at the Fermi-Dirac distribution
$$
n_{F}(\beta(\varepsilon-\mu)) = \frac{1}{e^{\beta(\varepsilon-\mu)}+1}.
$$
The Fermi-Dirac distribution $n_{F}(\beta(\varepsilon-\mu))$ for $T = 0$ and $T > 0$ are shown below.
For both cases we have the same chemical potential $\mu = \varepsilon_F$.

```python
fig = pyplot.figure()
ax = fig.add_subplot(1,1,1)
xvals = np.linspace(0, 2, 200)
mu = .75
beta = 20
ax.plot(xvals, xvals < mu, ls='dashed', label='$T=0$')
ax.plot(xvals, 1/(np.exp(beta * (xvals-mu)) + 1),
        ls='solid', label='$T>0$')
ax.set_xlabel(r'$\varepsilon$')
ax.set_ylabel(r'$n_{F}(\varepsilon, T)$')
ax.set_yticks([0, 1])
ax.set_yticklabels(['$0$', '$1$'])
ax.set_xticks([mu])
ax.set_xticklabels([r'$\mu = \varepsilon_{F}$'])
ax.set_ylim(-.1, 1.1)
ax.legend()
draw_classic_axes(ax)
pyplot.tight_layout()
```

At a finite temperature $T>0$, thermal excitations _smear out_ the sharp change in the number of occupied electrons near $\varepsilon_F$.
Because the Fermi energy is typically in the range of electronvolts, the temperature of $\sim 10 000$K would be required in order for thermal excitations to give an electron a similar amount of energy!
Therefore at room temperature $T = 300$K the electron distribution over energies is very similar to that at $T=0$.

Below we compare the number of occupied electron states at each energy $g(\varepsilon) n_{F}(\beta(\varepsilon-\mu))$ at $T = 0$ (blue shaded area) with $T > 0$ (orange shaded area).

```python
E = np.linspace(0, 2, 500)
fig, ax = pyplot.subplots()
ax.plot(E, np.sqrt(E), linestyle='dashed')
ax.text(1.7, 1.4, r'$g(ε)\propto \sqrt{ε}$', ha='center')
ax.fill_between(E, np.sqrt(E) * (E < 1), alpha=.3)

n = np.sqrt(E) / (1 + np.exp(20*(E-1)))
ax.plot(E, n)
ax.fill_between(E, n, alpha=.5)
w = .17
ax.annotate(s='', xy=(1, 1), xytext=(1-w, 1),
            arrowprops=dict(arrowstyle='<->', shrinkA=0, shrinkB=0))
ax.text(1-w/2, 1.1, r'$\sim k_BT$', ha='center')
ax.plot([1-w, 1+w], [1, 0], c='k', linestyle='dashed')
ax.annotate(s='', xy=(1, 0), xytext=(1, 1),
            arrowprops=dict(arrowstyle='<->', shrinkA=0, shrinkB=0))
ax.text(1.2, .7, r'$g(ε_F)$', ha='center')
ax.set_xticks([1])
ax.set_xticklabels([r'$ε_F$'])

ax.set_ylabel(r"$g(ε)$")
ax.set_xlabel(r"$ε$")
draw_classic_axes(ax, xlabeloffset=.2)
```

In order to estimate the electron energy increase, we approximate difference between the blue and orange areas by triangles, as shown in the figure.
This approximation is appropriate because the thermal smearing happens at the energies $E ∼ k_B T$, and it is much smaller than the Fermi energy $\varepsilon_{F}$.

!!! note "Sommerfeld expansion"

    A more rigorous way to estimate the energy of electrons at a finite temperature is to apply the [Sommerfeld expansion](https://en.wikipedia.org/wiki/Sommerfeld_expansion).
    It still uses on the smallness of $k_B T$ compared to $\varepsilon_F$, but computes the electron energy without approximating the resulting integrals.

At a finite temperature, the electrons occupying the top triangle (blue) are thermally excited to occupy the bottom triangle (orange).
The base of the triangle is proportional to $k_BT$ and the height is $\sim g(\varepsilon_F)$.
Hence the number of excited electrons is $N_\mathrm{exc} \approx g(\varepsilon_F)k_BT$ (neglecting constants not depending on $\varepsilon_{F}$).

These electrons gain $k_BT$ of thermal energy, such that the total extra energy is
$$
\begin{align}
E(T) &= E(T = 0) + N_\mathrm{exc}k_BT\\
&\approx  E(T = 0) + g(\varepsilon_F)k_B^2T^2.
\end{align}
$$
Therefore, the electron heat capacity $C_e$ is
$$
\begin{align}
C_e &= \frac{ \mathrm{d}E}{ \mathrm{d}T}\\
 &\approx 2 g(ε_F)k_B^2T\\
 &\overset{\mathrm{3D}}{=} 3 Nk_B\frac{T}{T_F}\\
 &\propto T,
\end{align}
$$
where we used $N=\frac{2}{3}\varepsilon_Fg(\varepsilon_F)$ and defined the _Fermi temperature_ $T_F \equiv \varepsilon_F/k_B$.

How does $C_e$ relate to the phonon contribution $C_p$?

- At room temperature $C_\mathrm{p}\approx 3Nk_B\gg C_e \propto k_B T / T_F$, because $T \ll T_F$.
- Near $T=0$, the phonon heat capacity $C_p\propto k_B (T/T_D)^3$, and it becomes smaller than the electron heat capacity at $T \lesssim \sqrt{T_D^3/T_F}$

## Useful trick: scaling of $C$

Similar to how we understood the low temperature heat capacity of the Debye model, the behavior of $C_e$ can be quickly memorized and understood using the following argument:

> Particles within an energy range of $\sim k_{B}T$ to the Fermi energy $\varepsilon_F$ become thermally excited, and each carries an extra energy $k_{B}T$.

### Example 1: 3D free electrons

In 3D, $g(\varepsilon_F)$ is roughly constant.
Thus the total energy obtained through thermal excitation is proportional to $T \times \left( T\times g(\varepsilon_F) \right)$, from which it follows that $C_e \propto T$.

### Example 2: graphene

Graphene has a Fermi energy $\varepsilon_F = 0$ and a density of states $g(\varepsilon) \propto \varepsilon$.
Therefore, within the energy range of $k_BT$, $g(\varepsilon) \propto k_BT$.
Thus the total energy is proportional to $T \times T^2$ and the heat capacity $C_e \propto T^2$.

## Conclusions

1. The Sommerfeld free electron model treats electrons as free particles with energy dispersion $\varepsilon = \frac{\hbar^2k^2}{2m}$.
2. The density of states $g(\varepsilon)$ follows from the dispersion relation by using a general procedure that is analogous to that for phonons.
3. The Fermi-Dirac distribution gives the probability of an electron state to be occupied.
4. The electron contribution to the heat capacity is proportional to $T$. It is much lower than phonon heat capacity at high temperatures, and much higher at low temperatures.
5. The scaling of heat capacity with $T$ can be quickly estimated by estimating the number of particles in an energy range $k_BT$ from the Fermi energy.

## Exercises

### Warm-up questions

1. List the differences between electrons and phonons from your memory.
2. Write down the expression for the total energy of particles with the density of states $g(\varepsilon)$ and the occupation number $n_{F}(\beta(\varepsilon - \mu))$.
3. Explain what happens if a material is heated up to its Fermi temperature (assuming that material where this is possible exists).
4. Why can we not use the Sommerfeld expansion with a Fermi energy of the order of the thermal energy?
5. Is the heat capacity of a solid at temperatures near $T=0$ dominated by electrons or phonons?

### Exercise 1: potassium
The Sommerfeld model provides a good description of free electrons in alkali metals such as potassium (element K), which has a Fermi energy of $\varepsilon_{F} =  2.12$ eV (data from Ashcroft, N. W. and Mermin, N. D., Solid State Physics, Saunders, 1976.).

1. Check the [Fermi surface database](http://www.phys.ufl.edu/fermisurface/). Explain why potassium and (most) other alkali metals can be described well with the Sommerfeld model.
2. Calculate the Fermi temperature, Fermi wave vector and Fermi velocity for potassium.
3. Why is the Fermi temperature much higher than room temperature?
4. Calculate the free electron density $n$ in potassium.
5. Compare this with the actual electron density of potassium, which can be calculated by using the density, atomic mass and atomic number of potassium. What can you conclude from this?

### Exercise 2: the $n$-dimensional free electron model.
In the lecture, it has been explained that the density of states of the free electron model is proportional to $1/\sqrt{\varepsilon}$ in 1D, constant in 2D and proportional to $\sqrt{\varepsilon}$ in 3D. In this exercise, we are going to derive the density of states of the free electron model for an arbitrary number of dimensions.
Suppose we have a $n$-dimensional hypercube with length $L$ for each side that houses free electrons.

1. What is the distance between nearest-neighbour points in $\mathbf{k}$-space? Assume periodic boundary conditions.
What is the density of $\mathbf{k}$-points in n-dimensional $\mathbf{k}$-space?
2. The number of $\mathbf{k}$-points between $k$ and $k + dk$ is given by $g(k)dk$.
Using the answer for 1, find $g(k)$ for 1D, 2D and 3D.
3. Now show that $g(k)$ for $n$ dimensions is given by
  $$g(k) = \frac{1}{\Gamma(n/2)} \left( \frac{L }{ \sqrt{\pi}} \right)^n \left( \frac{k}{2} \right)^{n-1},$$ where $\Gamma(z)$ is the [gamma function](https://en.wikipedia.org/wiki/Gamma_function).

	??? hint
		You will need the area of an $n$-dimensional sphere and this can be found on [Wikipedia](https://en.wikipedia.org/wiki/N-sphere#Volume_and_surface_area) (blue box on the right).

4. Check that this equation is consistent with your answers in 2.

	??? hint
		Check [Wikipedia](https://en.wikipedia.org/wiki/Particular_values_of_the_gamma_function) to find out how to deal with half-integer values in the gamma function.

5. Using the expression in 3, calculate the density of states (do not forget the spin degeneracy).
6. Give an integral expression for the total number of electrons and for their total energy in terms of the density of states, the temperature $T$ and the chemical potential $\mu$ (_you do not have to work out these integrals_).
7. Work out these integrals for $T = 0$.

### Exercise 3: a hypothetical material
A hypothetical metal has a Fermi energy $\varepsilon_F = 5.2 \, \mathrm{eV}$ and a density of states $g(\varepsilon) =  2 \times 10^{10} \, \mathrm{eV}^{-\frac{3}{2}} \sqrt{\varepsilon}$.

1. Give an integral expression for the total energy of the electrons in this hypothetical material in terms of the density of states $g(\varepsilon)$, the temperature $T$ and the chemical potential $\mu = \varepsilon_F$.
2. Find the ground state energy at $T = 0$.
3. In order to obtain a good approximation of the integral for non-zero $T$, one can make use of the [Sommerfeld expansion](https://en.wikipedia.org/wiki/Sommerfeld_expansion) (the first equation is all you need and you can neglect the $O\left(\frac{1}{\beta \mu}\right)^{4}$ term).
Using this expansion, find the difference between the total energy of the electrons for $T = 1000 \, \mathrm{K}$ with that of the ground state.
4. Now, find this difference in energy by calculating the integral found in 1 numerically. Compare your result with 3.

	??? hint
		 You can do numerical integration in python with [`scipy.integrate.quad(func, xmin, xmax)`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.quad.html)

5. Calculate the heat capacity for $T = 1000 \, \mathrm{K}$ in eV/K.
6. Numerically compute the heat capacity by approximating the derivative of energy difference found in 4 with respect to $T$. To this end, make use of the fact that $$\frac{dy}{dx}=\lim_{\Delta x \to 0} \frac{y(x + \Delta x) - y(x - \Delta x)}{2 \Delta x}.$$ Compare your result with 5.

### Exercise 4: graphene
One of the most famous recently discovered materials is [graphene](https://en.wikipedia.org/wiki/Graphene). It consists of carbon atoms arranged in a 2D honeycomb structure.
In this exercise, we will focus on the electrons in bulk graphene. Unlike in metals, electrons in graphene cannot be treated as 'free'.
However, close to the Fermi level, the dispersion relation can be approximated by a linear relation:
$ \varepsilon(\mathbf{k}) = \pm c|\mathbf{k}|.$ Note that the $\pm$ here means that there are two energy levels at a specified $\mathbf{k}$.
The Fermi level is set at $\varepsilon_F = 0$.

1. Make a sketch of the dispersion relation.
What other well-known particles have a linear dispersion relation?
2. Using the dispersion relation and assuming periodic boundary conditions, derive an expression for the density of states of graphene.
Do not forget spin degeneracy, and take into account that graphene has an additional two-fold 'valley degeneracy' (hence there is a total of a fourfold degeneracy instead of two).
Your result should be linear with $|\varepsilon|$.

	??? hint
		 It is convenient to first start by only considering the positive energy contributions $\varepsilon(\mathbf{k}) = + c|\mathbf{k}|$ and calculate the density of states for it. Then account for the negative energy contributions $\varepsilon(\mathbf{k}) = - c|\mathbf{k}|$ by adding it to the density of states for the positive energies. You can also make use of $\frac{\rm{d} |k|}{\rm{d}k} = \frac{k}{|k|}$.

3. At finite temperatures, assume that electrons close to the Fermi level (i.e. not more than $k_B T$ below the Fermi level) will get thermally excited, thereby increasing their energy by $k_B T$. Calculate the difference between the energy of the thermally excited state and that of the ground state $E(T)-E_0$. To do so, show first that the number of electrons that will get excited is given by $$n_{ex} = \frac{1}{2} g(-k_B T) k_B T.$$
4. Calculate the heat capacity $C_e$ as a function of the temperature $T$.

[^1]: This is not completely true, as we will see when learning about [semiconductors](13_semiconductors)
[^2]: An [isotropic](https://en.wikipedia.org/wiki/Isotropic_solid) material means that the material is the same in all directions.
[^3]: The mean inter-particle distance is related to the electron density $n = \frac{N}{V}$ by
$$
\langle r \rangle \propto \frac{1}{n^{\frac{1}{3}}}.
$$
The exact proportionality constant depends on the properties of the system.

--8<-- "includes/abbreviations.md"
