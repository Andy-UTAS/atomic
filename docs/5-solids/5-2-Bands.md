# Band structure

## Introduction

![]()

!!! danger  "Expected competencies"

    It is assumed that you have familiarity with the following concepts/techniques:

    * Write down the dispersion and wavefunction of an electron in free space (solving the Schrödinger equation).
    * Describe how the periodicity of a band structure (= dispersion) is related to the reciprocal lattice.
    * Write down a Fourier series representation of a periodic function.
    * Diagonalize a 2x2 matrix (i.e., find its eigenvalues and eigenfunctions).

!!! note  "Text reference"
    The material covered here is discussed in section(s) $\S 16$ of [The Oxford Solid State Basics](https://global.oup.com/academic/product/the-oxford-solid-state-basics-9780199680771?cc=au&lang=en&)

!!! info "Computational content"

    The Jupyter notebook associated with this section can be accessed by clicking the icon below:
    [<i class="fab fa-python fa-5x"></i>](#){ .md-button .md-button--primary class="text-center" style="margin-left: 45%"}

---

## Band structure

How are material properties related to the band structure?

For a material to be a conductor, there should be available electron states at the Fermi level. Otherwise all the states are occupied, and all the currents cancel out.

A band structure of a 1D material may look similar to this:

![](figures/band_structure_sketch.svg)

We see several **energy bands** that may be separated by a **band gap** or overlapping.

When the Fermi level lies in the band gap, the material is called a semiconductor (or dielectric or insulator). When the Fermi level lies within a band, it is a conductor (metal).

### A simple requirement for insulators

In an insulator every single band is either completely filled or completely empty.

What determines if an energy band if fully occupied or only partly? To answer this we need to know the number of available states within an energy band, and the number of electrons in the system. We can find the number of states in a band by integrating the density of states $g(E)$, but this is hard. Fortunately, we can easily see how many states there are in an energy band by counting the number of $k$-states in the first Brillouin zone.  

For a single band:

$$ N_{states} = 2 \frac{L^3}{(2\pi)^3} \int_{BZ} dk_x dk_y dk_z  = 2 L^3 / a^3 $$

Here, $L^3/a^3$ is the number of unit cells in the system, so we see that a single band has room for 2 electrons per unit cell (the factor 2 comes from the spin).

We come to the important rule:

> Any material with an odd number of electrons per unit cell is a metal.

If the material has an even number of electrons per unit cell it may be a semiconductor, but only if the bands are not overlapping (see the figure above). For example: Si, Ge, Sn all have 4 valence electrons. Si (silicon, band gap 1.14 eV) and Ge (germanium, band gap 0.67 eV) are semiconductors, Sn (tin) is a metal. **Interesting feature: the heaviest material is a metal, why?**


## Fermi surface using a nearly free electron model

Sequence of steps (same procedure as in 1D, but harder because of the need to imagine a 2D dispersion relation):

1. Compute $k_f$ using the free electron model (remember this is our starting point).
2. Plot the free electron model Fermi surface and the Brillouin zones.
3. Apply the perturbation where the Fermi surface crosses the Brillouin zone (due to avoided level crossings).

The resulting band structure looks like this (in the extended Brillouin zone scheme):


```python
def E(k_x, k_y):
    delta = np.array([-2*pi, 0, 2*pi])
    H = np.diag(
        ((k_x + delta)[:, np.newaxis]**2
        + (k_y + delta)[np.newaxis]**2).flatten()
    )
    return tuple(np.linalg.eigvalsh(H + 5)[:3])

E = np.vectorize(E, otypes=(float, float, float))

momenta = np.linspace(-2*pi, 2*pi, 100)
kx, ky = momenta[:, np.newaxis], momenta[np.newaxis, :]
bands = E(kx, ky)

# Extended Brillouin zone scheme
pad = .3
first_BZ = ((abs(kx) < pi + pad) & (abs(ky) < pi + pad))
second_BZ = (
    ((abs(kx) > pi - pad) | (abs(ky) > pi - pad))
    & ((abs(kx + ky) < 2*pi + pad) & (abs(kx - ky) < 2*pi + pad))
)
third_BZ = (
    (abs(kx + ky) > 2*pi - pad) | (abs(kx - ky) > 2*pi - pad)
)

bands[0][~first_BZ] = np.nan
bands[1][~second_BZ] = np.nan
#bands[2][~third_BZ] = np.nan

# Actually plotting

fig = go.Figure(
    data = [
        go.Surface(
            z=band / 5,
            # colorscale=color,
            opacity=opacity,
            showscale=False,
            hoverinfo='none',
            colorscale='Reds',
            x=momenta,
            y=momenta,
        )
        for band, opacity
        in zip(bands[:2],
               # ['#cf483d', '#3d88cf'],
               (1, 0.9))
    ],
    layout = go.Layout(
        title='Nearly free electrons in 2D',
        autosize=True,
        hovermode=False,
        margin=dict(
            t=50,
            l=20,
            r=20,
            b=50,
        ),
        scene=dict(
            yaxis={"title": "k_y"},
            xaxis={"title": "k_x"},
            zaxis={"title": "E"},
        )
    )
)
py.iplot(fig, show_link=False)
```

Observe that the top of the first band is above the bottom of the lowest band. Therefore if $V$ is sufficiently weak, the material can be conducting even with 2 electrons per unit cell!

A larger $V$ makes the Fermi surface more distorted and eventually makes the material insulating.
Let's compare the almost parabolic dispersion of the nearly free electron model with a tight-binding model in 2D.

We now have a dispersion relation $E = E_0 - 2t(\cos k_x a + \cos k_y a)$, which looks like this:

```python
momenta = np.linspace(-pi, pi, 100)
kx, ky = momenta[:, np.newaxis], momenta[np.newaxis, :]
energies = -np.cos(kx) - np.cos(ky)
fig = go.Figure(
    data = [
        go.Surface(
            z=energies,
            # colorscale='#3d88cf',
            opacity=1,
            showscale=False,
            hoverinfo='none',
            x=momenta,
            y=momenta,
        )
    ],
    layout = go.Layout(
        title='Tight-binding in 2D',
        autosize=True,
        hovermode=False,
        margin=dict(
            t=50,
            l=20,
            r=20,
            b=50,
        ),
        scene=dict(
            yaxis={"title": "k_y"},
            xaxis={"title": "k_x"},
            zaxis={"title": "E"},
        )
    )
)
py.iplot(fig, show_link=False)
```

### Light absorption

Photons of external light can be reflected, transmitted, or absorbed by the material. Absorption, in turn requires energy transfer from the photon to electrons. In a filled band there are no available states where energy could be transferred (that's why insulators may be transparent).

When transition between two bands becomes possible due to photons having high energy, the absorption increases in a step-like fashion, see the sketch below for germanium.

![](figures/adsorption.svg)

Here $E'_G\approx 0.9eV$ and $E_G\approx 0.8 eV$. The two visible steps are due to the special band structure of Ge:

![](figures/direct_indirect.svg)

The band structure has two band gaps: *direct*, the band gap at $k=0$, $E'_G$ and *indirect* gap $E_G$ at any $k$. In Ge $E_G < E'_G$, and therefore it is an *indirect band gap semiconductor*. Silicon also has an indirect band gap. Direct band gap materials are for example GaAs and InAs.

Photons carry very little momentum and a very high energy since $E = c \hbar k$ and $c$ is large. Therefore to excite electrons at $E_G$, despite a lower photon energy is sufficient, there is not enough momentum. Then an extra phonon is required. Phonons may have a very large momentum at room temperature, and a very low energy since atomic mass is much higher than electron mass.

A joint absorbtion of a photon and a phonon collision may excite an electron across an indirect band gap, however this process is much less efficient, and therefore materials with an indirect bandgap are much worse for optics applications (light emitting diodes, light sensors, etc).

## Summary

* Each band can host two electrons per unit cell, therefore a material with an odd number of electrons is a metal; that with an even number of electrons may be an insulator.
* Light absorption is a tool to measure the band gap, and it distinguishes **direct** from **indirect** band gaps.

## Exercises

### Exercise 1: 3D Fermi surfaces
Using the [periodic table](../fermi_surfaces) of the Fermi surfaces (or the static images at https://www.phys.ufl.edu/fermisurface/ if 3D does not work for you), answer the following questions:

1. Find 4 elements that are well described by the nearly-free electron model and 4 that are poorly described by it.
2. Is the Fermi surface of lithium or potassium better described by the free electron model? What about nearly-free electron model? Why?
3. Do you expect a crystal with a simple cubic lattice and monovalent atoms to be conducting?
4. What Fermi surface shape would you expect the [NaCl crystal](https://en.wikipedia.org/wiki/Sodium_chloride) to have? Explain your answer using both the atomic valences and the optical properties of this crystal.

### Exercise 2: Tight-binding in 2D

Consider a rectangular lattice with lattice constants $a_x$ and $a_y$.
Suppose the hopping parameters in the two corresponding directions to be $-t_1$ and $-t_2$.
Consider a single orbital per atom and only nearest-neighbour interactions.

1. Write down a 2D tight-binding Schrödinger equation (expand to 2D the results of 1D).
2. Formulate the Bloch ansatz for the wave function.
3. Calculate the dispersion relation of this model.
4. What Fermi surface shape would this model have if the atoms are monovalent?
5. What Fermi surface shape would it have if the number of electrons per atom is much smaller than 1?

### Exercise 3: Nearly-free Electron model in 2D
_(based on exercise 15.4 of the book)_

Suppose we have a square lattice with lattice constant $a$, with a periodic potential given by $V(x,y)=2V_{10}(\cos(2\pi x/a)+\cos(2\pi y/a))+4V_{11}\cos(2 \pi x/a)\cos(2 \pi y/a)$.

1. Use the Nearly-free electron model to find the energy of state $\mathbf{q}=(\pi/a, 0)$.

    ??? hint
        This is analogous to the 1D case: the states that interact have $k$-vectors $(\pi/a,0)$ and $(-\pi/a,0)$; ($\psi_{+}\sim e^{i\pi x /a}$ ; $\psi_{-}\sim e^{-i\pi x /a}$).

2. Let's now study the more complicated case of  state $\mathbf{q}=(\pi/a,\pi/a)$. How many $k$-points have the same energy? Which ones?
3. Write down the nearly free electron model Hamiltonian near this point.
4. Find its eigenvalues.
