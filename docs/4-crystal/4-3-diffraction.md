# The tight binding model

One-dimensional chains have been doing well, so why stop?

## Introduction

![](images/4-3-diffractionheader.jpg)

The model of Sommerfeld saw the Fermionic nature of electrons cemented in Drude's kinetic theory of electrons, but as we saw in our discussion of [chemistry](../../2-chemistry/2-1-chemistry), electrons tend not to be free, but rather occupy states as governed by surrounding nuclei. It is from this point that we aim to marry our discussion of bonding theory in the LCAO framework with our recent progress on modelling solids in one dimension.  

!!! danger  "Expected competencies"

    It is assumed that you have familiarity with the following concepts/techniques:

    * Solid-state physics: 1D model of a solid, LCAO

!!! note  "Text reference"
    The material covered here is discussed in section(s) $\S 11$ of [The Oxford Solid State Basics](https://global.oup.com/academic/product/the-oxford-solid-state-basics-9780199680771?cc=au&lang=en&)

!!! info "Computational content"

    The Jupyter notebook associated with this section can be accessed by clicking the icon below:
    [<i class="fab fa-python fa-5x"></i>](https://jove2021.cloud.edu.au/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FAndy-UTAS%2FSolid-state&urlpath=tree%2FSolid-state%2F3-3-tightbinding.ipynb&branch=master){ .md-button .md-button--primary class="text-center" style="margin-left: 45%"}

---

## Tight binding

In our discussion of covalent bonding, we were able to obtain a solution to the Schrödinger equation using the variational method in the framework known as [LCAO](../../2-chemistry/2-1-chemistry#the-linear-combination-of-atomic-orbitals-lcao). We are going to apply the same framework to an infinite chain of atoms, but before we do this, we are going to consider a gentle extension to the simple 2 atom case that we originally considered.

### A triatomic molecule

Let us consider a one-dimensional triatomic system as illustrated below:  

![](images/3-3-triatomic.png)

We are going to make the exact same assumptions that we made when we formulated LCAO, namely we are looking at a frozen molecule (no vibrations) with fixed nuclear positions (the Born-Oppenheimer approximation). We assume that the atoms are identical, and the electrons are tightly bound to a given nucleus so that we have

$$
(\hat{K} + \hat{V}_n)|n\rangle = \epsilon_\textrm{atomic} |n\rangle
$$

where $\hat{K}$ is the usual kinetic energy operator, $\hat{V}_n$ is the potential due to the nucleus $n$ and $\epsilon$ is the energy of the bound electronic state. We again make the crude approximate that our orbitals are orthogonal[^1], such that

$$
\langle i|j\rangle = \delta_{i,j}.
$$

Now, we can do exactly what we did for a diatomic molecule, namely, consider the trail wavefunction:

$$
\vert \psi \rangle = \varphi_1 |1\rangle + \varphi_2 |2\rangle + \varphi_3 |3\rangle.
$$

By performing the exact same logic and mathematics we arrive at the matrix equation

$$
E \begin{pmatrix}
\varphi_1 \\ \varphi_2 \\ \varphi_3
\end{pmatrix} =
\begin{pmatrix}
\epsilon_0 & -t & 0 \\
-t & \epsilon_0 & -t \\
0 & -t & \epsilon_0
\end{pmatrix}
\begin{pmatrix}
\varphi_1 \\ \varphi_2 \\ \varphi_3.
\end{pmatrix}
$$

where $\epsilon_0 = \epsilon_\textrm{atomic} + V_0$ with $V_0 =  \sum_{m \ne j} \langle m | V_j | m \rangle$ the energy shift due to the presence of all other nuclei. It is assumed that hopping occurs only between the nearest neighbours such that

$$
\langle1|H|2\rangle = \langle2|H|3\rangle = -t.
$$

??? question  "3.3.1: Apply the exact same logic and mathematics to arrive at the above matrix equation"

Obtaining solutions to such a problem can be unwieldy, but fortunately, we have the perfect tool for the job.

#### Number cruncher

We can use our computational toolkit to solve for the eigenvalues of a matrix. For example, with $\epsilon_0 = 2$ and $t=1$, we find that the eigenvalues for the matrix above are approximately $(0.59, 2.00, 3.41)$. But what use is this? Well, let's look at a simple case of varying $t$.

??? question  "3.3.2: Make a plot of the energy eigenvalues as a function of $t$ running from $(0, \epsilon)$ and interpret your result. Ensure to include your code."

<!-- Using the definitions that already exist in this section's notebook, one can do something like the following

```python
eigen = [] # Initalise a list for the eigenvalues
tvals = np.linspace(0,2,20) # Make an array for the values of t to be plotted

# Retrieve the eigenvalues at different values of t
for tv in tvals:
    ei = DOS_finite_electron_chain(3, t = tv) # Get the eigenvalues
    eigen.append(ei) # Add the values to the list
toplot = np.transpose(eigen) # Transpose the list to get a list of arrays for each eigenstate

# Make the plot
fig, ax = plt.subplots(1, 1)

labs = ['$E_+$','$E_0$','$E_-$'] # Set a label for each plot
for n, en in enumerate(toplot):
    ax.plot(tvals, en, label = labs[n])

# Make the plot pretty
ax.set_xlabel("$t$")
ax.set_ylabel("$E$")
ax.set_title('Energy eigenvalues for a triatomic molecule')
plt.legend()
ax.set_aspect(.15)

plt.savefig('3-3-trievals.svg', facecolor='white', transparent=False, bbox_inches='tight')

plt.show()
```

Which produces the plot shown below:

![](images/3-3-trievals.svg)

As $t$ characterises the hopping between atoms, as this becomes larger, the existence of the bonding and antibonding states becomes more prevalent, and more and less energetically favourable respectively. We also note the existence of a third state at fixed energy, which arises due to equal attraction to both neighbours. But this is in line with what we have seen previously, namely, that the number of states should equal the number of degrees of freedom in the system. -->

Perhaps the most useful thing to do is similar to that which was introduced in the [last section](../../3-1d/3-2-diatomic#density-of-states), which is using to produce a histogram sampling of the energy eigenvalues in order to visualise the density of states. If we go ahead an do this:

![](images/3-3-DOS-3.svg)

The density of states is not a particularly useful concept with few states, but fortunately, this system scales well and "grows diagonally" with an increased number of atoms: as the hopping is limited to nearest neighbours and states are orthogonal, only the diagonal and first-off diagonal elements will be non-zero. So let's go ahead and crank the handle!

!!! example "To infinity and beyond"

    === "$n = 3$"

        ![](images/3-3-DOS-3.svg)

    === "$n = 10$"

        ![](images/3-3-DOS-10.svg)

    === "$n = 100$"

        ![](images/3-3-DOS-100.svg)

    === "$n = 1000$"

        ![](images/3-3-DOS-1000.svg)

    === "$n = 10000$"

        ![](images/3-3-DOS-10000.svg)

    === "$n = 100000$"

        <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/dik_wnOE4dk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen class=center></iframe>

        LOL: good luck! That would be one big matrix, much large than my meagre computer can handle.

??? question  "3.3.3: How do these results compare with what we have seen previously?"

<!-- The numerical results mostly agree with the models we developed earlier: for example, in the Sommerfeld model, the DoS in 1D is proportional to $\frac{1}{\sqrt{E}}$ and the large $n$ histograms reflect this proportionality for small energies $E$. But for larger values of $E$, there is  significant deviation form this behaviour. -->

## An infinite chain

The above extension of the diatomic system to a triatomic system, especially when coupled with some computational assistance to hone our intuition, we are now going to consider the case of an infinite number of atoms, as depicted below:

![](images/3-3-chain.png)

The potential for the above system, assuming that the locations of atoms are $x_n = na$ with $n \in \mathbb{Z}$, is then:

![](images/3-3-potential.svg)

Now we can redeploy the machinery that we used for the diatomic and triatomic systems, namely we formulate the molecular orbital via the LCAO model:

$$
\vert \Psi \rangle = \sum_n \phi_n |n \rangle
$$

and write the effective Schrödinger as

$$
\sum_m H_{nm} \phi_m = E \phi_n
$$

where the matrix elements of the Hamiltonian are given by

$$  
H_{nm} = \langle n | \hat{H} | m \rangle
$$

It is a bit of work, but one can show that these matrix elements evaluate to

$$
H_{nm} = \epsilon_0 \delta_{n,m} - t \left(\delta_{n+1,m} + \delta_{n-1,m}\right)
$$

with the same definitions for $\epsilon_0 = \epsilon_\textrm{atomic} + V_0$ and $V_0 =  \sum_{m \ne j} \langle m | V_j | m \rangle$ as in the triatomic case.

### Solving the tight-binding chain

It will perhaps come as little surprise that the method that we are going to use to solve our effective Schrödinger equation is similar to the method we have use to solve for vibrations in a chain, namely to look for plane-wave solutions:

$$
\phi_n = \frac{e^{-ikna}}{\sqrt{N}}
$$

??? question  "3.3.4: How does this form of solution compare to the assumed form of solutions for oscillations?"

<!-- In the case of oscillations, we considered solutions of the form $e^{i\omega t - ikna}$, which was because we were looking for time dependent solutions. In this case, we are seeking variational solution to the time-independent Schödinger equation, and therefore do not require any time dependence. -->

We then crank the handle:

$$
\begin{align}
E \phi_n & = E \times \frac{e^{-ikna}}{\sqrt{N}} \\
& = \sum_m H_{nm} \phi_m = \epsilon_0 \frac{e^{-ikna}}{\sqrt{N}} - t \left(\frac{e^{-ik(n+1)a}}{\sqrt{N}} - \frac{e^{-ik(n-1)a}}{\sqrt{N}}\right)
\end{align}
$$

which yields the energy eigenvalue

$$
E = \epsilon_0 - t \left(e^{-ika} + e^{ika}\right) = \epsilon_0 - 2t\cos(ka)
$$

which is plotted below:

![](images/3-3-edispersion.svg)

There are obvious similarities to the dispersion of oscillations, or phonons, but there are stark differences as compared to the Sommerfeld free electron model: now only a range of energies can be occupied, and this range is referred to as an energy band, and the energy difference between the top and the bottom of this band is called the bandwidth[^2].

Further considering the band structure as compared to the free electron model, let us focus on the dispersion relation close to the base of the band at $k=0$, where we approximate the energy as

$$
E \approx \epsilon_0 - 2t + t (ka)^2 \equiv E_0 + t (ka)^2.
$$

If we compare this to the free-electron dispersion relation

$$
E=\frac{\hbar^2 k^2}{2m}
$$

we see that the band structure is similar, but with the lowest available energy is $E_0$ instead of $0$, and the electrons behave as if they had a different _effective mass_

$$
m^*=\frac{\hbar^2}{2ta^2}.
$$

For the moment, we leave this as an observation, but we shall return to it later in the course.

### Filling bands

Let us now consider a system of $N$ atoms. Due to the spin degeneracy, at each value $k$ there are 2 possible states which can be occupied, which means for the system there are $2N$ possible states. The implications of this are significant.

!!! example "Band filling"

    === "Divalent system"

        Let us consider an atom with two valance electrons: there will be as many electrons as states and thus the every state in the band will be occupied, as illustrated below:

        ![](images/3-3-divalentband.svg)

    === "Monovalent system"

        Now let us consider monovalent atoms: there will be twice as many states as there are electrons, and thus the band will only be half filled:

        ![](images/3-3-monovalentband.svg)

        Note that there is now a Fermi surface - well, Fermi points.

    === "Monovalent system with electric field"

        A Fermi surface means that nearby electrons can occupy neighbouring states, for example, under the influence of an electric field:

        ![](images/3-3-monovalentbandwithE.svg)


??? question  "3.3.5: What is the implication of the plots shown in the _band filling_ content block?"

<!-- This is the existence of conduction and insulation! For monovalent systems in the presence of an electric field, there can be an imbalance of electrons with either $+k$ or $-k$, so there will be a net charge migration, whereas with divalent atoms, one can never achieve a preference for either $\pm k$. -->

---

## Conclusions

  * Diffraction experiments reveal information about crystal structure.
  * Laue condition: difference between wavevectors of incoming and diffracted waves matches a reciprocal lattice vector, necessary for constructive interference.
  * Structure factor: describes the contribution of the atoms in a unit cell to the diffraction pattern.
  * Powder diffraction and relating its experimental results to the crystal structure via Bragg's law.

---

## Exercises
### Preliminary provocations

  1. Compare the expression of the effective mass with Newton's second law. Do you observe any similarities?
  2. Check the units of the effective mass. Is it what you expect?
  4. Calculate the effective mass of the free-electron dispersion relation. Is this what was expected?
  5. Under what condition is the effective mass the same for each electron?


### Exercise 1: The next-nearest neighbour chain

  Let's expand our one-dimensional chain model by extending the range of interaction to include the next-nearest neighbours:

  $$ \langle \phi_n | H | \phi_{n+2}\rangle \equiv -t' ≠ 0.$$

  1. Write down the new Schrödinger equation for this system.
  2. Solve the Schrödinger equation to find the dispersion relation $E(k)$.
  3. Calculate the effective mass $m^*$.
  4. Sketch the effective mass as a function of $k$ for the cases $t=2t'$,$t=4t'$ and $t=10t'$.

[^1]: This is not necessary but makes the calculation much simpler, and the qualitative behaviour reproduces that in which we are interested
[^2]: Original, hey?
