# The reciprocal lattice

Learn the _reciprocal_ secrets of crystals[^1].

## Introduction

![](images/4-2-kspaceheader.jpg)

The model of Sommerfeld saw the Fermionic nature of electrons cemented in Drude's kinetic theory of electrons, but as we saw in our discussion of [chemistry](../../2-chemistry/2-1-chemistry), electrons tend not to be free, but rather occupy states as governed by surrounding nuclei. It is from this point that we aim to marry our discussion of bonding theory in the LCAO framework with our recent progress on modelling solids in one dimension.  

!!! danger  "Expected competencies"

    It is assumed that you have familiarity with the following concepts/techniques:

    * Mathematics: vectors, the Fourier transform

!!! note  "Text reference"
    The material covered here is discussed in section(s) $\S 13.1, 13.2$ of [The Oxford Solid State Basics](https://global.oup.com/academic/product/the-oxford-solid-state-basics-9780199680771?cc=au&lang=en&)

!!! info "Computational content"

    The Jupyter notebook associated with this section can be accessed by clicking the icon below:
    [<i class="fab fa-python fa-5x"></i>](https://jove2021.cloud.edu.au/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FAndy-UTAS%2FSolid-state&urlpath=tree%2FSolid-state%2F4-2-kspace.ipynb&branch=master){ .md-button .md-button--primary class="text-center" style="margin-left: 45%"}

---

In the last lecture, we learned crystallographic terminology in order to describe crystal structures.
Now our goal is twofold, we will:
- Study what consequences does a lattice have in reciprocal space (with the goal of considering dispersion relations)
- Consider how to probe crystal structure using X-ray diffraction experiments.

## Reciprocal lattice motivation 1D case
Previously, we discussed the reciprocal space of a simple 1D lattice.
To obtain the dispersion relation we considered waves of the form
$$
e^{ikx_n} = e^{ikna}, \quad n \in \mathbb{Z},
$$
where $x_n = na$ is the 1D lattice point.
We then observed that these waves with wave vectors $k$ and $k+G$, where $G=2\pi m/a$ with integer $m$, are exactly the same:

$$
e^{i(k+G)na} = e^{ikna+im2\pi n} =  e^{ikna},
$$

where we used

$$
e^{iGx_n} = e^{i2\pi mn} =  1.
$$

The set of points $G=2\pi m/a$ forms the **reciprocal lattice**.
Let us now generalize the same idea to describe the reciprocal lattice in 3D.

## Extending to higher dimensions
We start from a lattice in real space:

$$
\mathbf{R}=n_1\mathbf{a}_1+n_2\mathbf{a}_2+n_3\mathbf{a}_1, \quad \{n_1, n_2, n_3\} \in \mathbb{Z},
$$

where $\mathbf{a}_1$, $\mathbf{a}_2$ and $\mathbf{a}_3$ are the lattice vectors.
The reciprocal lattice is also a lattice, but in the $k$-space:

$$
\mathbf{G}=m_1\mathbf{b}_1+m_2\mathbf{b}_2+m_3\mathbf{b_3}, \quad \{m_1, m_2, m_3\} \in \mathbb{Z}.
$$

The vectors $\mathbf{b}_1$, $\mathbf{b}_2$ and $\mathbf{b}_2$ are the **reciprocal lattice vectors**.
Let us now determine the reciprocal lattice vectors by requiring that waves that differ by a reciprocal lattice vector are indistinguishable.
In other words, we require that

$$
e^{i\mathbf{k}\mathbf{R}} = e^{i(\mathbf{k} + \mathbf{G})\mathbf{R}},
$$

for any $\mathbf{R}$ in the lattice.
Substituting the definitions of $\mathbf{R}$ and $\mathbf{G}$ we get

$$
\mathrm{e}^{i\mathbf{G}\cdot\mathbf{R}} = \mathrm{e}^{i\sum_{\{i,j\}=1}^{3} n_i m_j \mathbf{a}_i \cdot \mathbf{b}_j}=1.
$$

This relation holds only if

$$
\mathbf{a_i}\cdot\mathbf{b_j}=2\pi\delta_{ij}.
$$

Indeed, after expanding the dot products in the exponent, we get

$$
\mathrm{e}^{i\mathbf{G}\cdot\mathbf{R}} = \mathrm{e}^{2\pi i(n_1 m_1 + n_2 m_2 + n_3 m_3)}.
$$

Because $n_i$ and $m_j$ are both integers, the exponent evaluates to 1.

The relation $\mathbf{a_i}\cdot\mathbf{b_j}=2\pi\delta_{ij}$ means that if we write the lattice vectors as rows of a matrix, the reciprocal lattice vectors are $2\pi$ times the columns of the inverse of that matrix.

### 2D example: triangular lattice
In order to gain extra intuition of the properties of the reciprocal lattice, let us study a specific example.

In the previous lecture we studied the triangular lattice, which is shown in the figure below.
The left panel show the real-space lattice with lattice vectors $\mathbf{a}_1 = a \mathbf{\hat{x}}$ and $\mathbf{a}_2 = a/2\mathbf{\hat{x}} + \sqrt{3}a/2 \mathbf{\hat{y}}$.
While the right panel shows the corresponding reciprocal lattice and its reciprocal lattice vectors $\mathbf{b}_1$ and $\mathbf{b}_2$.


<object type="text/html" data="../images/4-2-reciprocal.html"  frameborder="0" width=850 height=450 class=center></object>

To find the reciprocal lattice vectors, we use the relation
$$
\mathbf{a_i}\cdot\mathbf{b_j}=2\pi\delta_{ij},
$$
which gives us the following equations:
$$
\mathbf{a}_1\cdot\mathbf{b}_2=\mathbf{a}_2\cdot\mathbf{b}_1=0,
$$
and
$$
\mathbf{a}_1\cdot\mathbf{b}_1=\mathbf{a}_2\cdot\mathbf{b}_2=2\pi.
$$
We substitute $\mathbf{a_i}\cdot\mathbf{b_i} = \lvert \mathbf{a_i} \rvert \lvert \mathbf{b_i} \rvert \cos(\theta_i)$:
$$
\lvert \mathbf{a}_1 \rvert \lvert \mathbf{b}_1 \rvert =\frac{2\pi}{\cos(\theta_1)} \:\: \text{and} \:\: \lvert \mathbf{a}_2 \rvert \lvert \mathbf{b}_2 \rvert =\frac{2\pi}{\cos(\theta_2)},
$$
where $\theta_i$ is the angle between the vectors $\mathbf{a}_i$ and $\mathbf{b}_i$.
To find the angles $\theta_1$ and $\theta_2$, we use the orthogonality relations above and the fact that the angle between $\mathbf{a}_1$ and $\mathbf{a}_2$ is $60^\circ$.
From this we conclude that $\theta_1 = \theta_2 = 30^\circ$.
Because $\lvert \mathbf{a}_1 \rvert = \lvert \mathbf{a}_2 \rvert = a$, we find
$$
\lvert \mathbf{b}_1 \rvert = \lvert \mathbf{b}_2 \rvert = \frac{4\pi}{a\sqrt{3}}.
$$
Unsurprisingly, we find that the lengths of the reciprocal lattice vectors are equal and inversely proportional to the lattice constant $a$.
With $\lvert \mathbf{b}_2 \rvert$ and $\mathbf{a}_1 \perp \mathbf{b}_2$, we easily find
$$
\mathbf{b}_2 = \frac{4\pi}{a\sqrt{3}} \mathbf{\hat{y}}.
$$

We follow the same procedure to find $\mathbf{b}_1$:

$$
\mathbf{b}_1 = \frac{4\pi}{a\sqrt{3}} \left(\frac{\sqrt{3}}{2} \mathbf{\hat{x}} - \frac{1}{2}\mathbf{\hat{y}} \right).
$$

??? Question "Is the choice of a set of reciprocal lattice vectors unique? If not, which other ones are possible?"
    There are many equivalent ways to choose lattice vectors of the reciprocal lattice. In the example above we could as well use
    $$
    \mathbf{b}_1 = \frac{4\pi}{a\sqrt{3}} \left(-\frac{\sqrt{3}}{2} \mathbf{\hat{x}} + \frac{1}{2}\mathbf{\hat{y}} \right) \quad \text{and} \quad \mathbf{b}_2 = -\frac{4\pi}{a\sqrt{3}} \mathbf{\hat{y}}.
    $$
    There is however only one choice that satisfies the relations $\mathbf{a_i}\cdot\mathbf{b_j}=2\pi\delta_{ij}$.

### 3D lattice example

Let us now consider a more involved example of the 3D lattice.
The explicit expression for the reciprocal lattice vectors in terms of their real space counterparts is:

$$
\mathbf{b}_1=\frac{2\pi(\mathbf{a}_2\times\mathbf{a}_3)}{ \mathbf{a}_1\cdot(\mathbf{a}_2\times\mathbf{a_3})}
$$

$$
\mathbf{b}_2=\frac{2\pi(\mathbf{a_3}\times\mathbf{a}_1)}{ \mathbf{a}_1\cdot(\mathbf{a}_2\times\mathbf{a_3})}
$$

$$
\mathbf{b_3}=\frac{2\pi(\mathbf{a}_1\times\mathbf{a}_2)}{ \mathbf{a}_1\cdot(\mathbf{a}_2\times\mathbf{a_3})}
$$

Note that the denominator $\mathbf{a}_1\cdot(\mathbf{a}_2\times\mathbf{a_3})$ is the volume $V$ of the real-space unit cell spanned by the lattice vectors $\mathbf{a}_1$, $\mathbf{a}_2$ and $\mathbf{a}_3$.

### The reciprocal lattice as a Fourier transform

One can also think of the reciprocal lattice as a Fourier transform of the real-space lattice.
For simplicity, we illustrate this for a 1D lattice (the same principles apply to a 3D lattice).
We model the real-space lattice as a density function consisting of delta peaks:

$$
\rho(x)=\sum_{n} \delta(x-na)
$$

We take the Fourier transform of this function to find:

$$
{\mathcal F}_{k}\left[\rho(x)\right]=\int_{-\infty}^\infty \mathrm{d}x\ \mathrm{e}^{ikx} \rho(x)=\sum_{n} \int_{-\infty}^\infty \mathrm{d}x\ \mathrm{e}^{ikx} \delta(x-na)=\sum_{n} \mathrm{e}^{ikna}
$$

This sum is non-zero only if $k=2\pi m/a$.
If we recall the beginning of the lecture, then these points correspond to reciprocal lattice points $G$.
Therefore, we rewrite this into the form

$$
{\mathcal F}_{k}\left[\rho(x)\right]=\frac{2\pi}{|a|}\sum_{m} \delta\left(k-G\right).
$$
Therefore, we see that the Fourier transform is non-zero only at reciprocal lattice points.
In other words, Fourier transforming a real-space lattice yields a reciprocal lattice!
The above result generalizes directly to three dimensions:

$$
{\mathcal F}_\mathbf{k}\left[\rho(\mathbf{r})\right]=\int \mathrm{d}\mathbf{r}\ \mathrm{e}^{i\mathbf{k}\cdot\mathbf{r}} \rho(\mathbf{r}) = \sum_\mathbf{G}\delta(\mathbf{k}-\mathbf{G}).
$$


## Periodicity of the reciprocal lattice
In order to describe a reciprocal lattice, we need to define a primitive unit cell in reciprocal space.
Previously, we learned that the choice of a primitive unit cell is not unique.
However, a general convention in reciprocal space is to use the Wigner-Seitz cell which is called the **1st Brillouin zone**.
Because the Wigner-Seitz cell is primitive, the 1st Brillouin zone (1BZ) contains a set of unique $\mathbf{k}$ vectors.
This means that all $\mathbf{k}$ vectors outside the 1st Brillouin zone are a copy of those inside the 1st Brillouin zone.
For example, any $\mathbf{k'}$ outside the 1BZ is related to a wave vector inside 1BZ $\mathbf{k}$ by shifting it by reciprocal lattice vectors: $\mathbf{k'} = \mathbf{k}+\mathbf{G}$

We have already learned how to construct Wigner-Seitz cells, however here is a reminder of how a Brillouin zone looks like:

![](images/brillouin_mod.svg)

### Miller planes
When fabricating crystals it is important to know both the orientation and the surface of the crystal.
Different cuts of a crystal lead to different surfaces.
In the chemical industry, this is especially significant because different surfaces lead to different chemical properties and thus is one of the foundations of research in catalysts.
Therefore, we seek a way to describe different planes of a crystal within our developed framework.
This leads us to a very important concept - **Miller planes**.
To explain Miller planes, let's start off with a simple cubic lattice:

![](images/4-2-cubic_mod.svg)

Where $|{\bf a}_1|=|{\bf a}_2|=|{\bf a}_3|\equiv a$.

We can cut multiple planes through the cubic lattice.
Miller planes describe such planes with a set of indices.
The plane designated by Miller indices $(u,v,w)$ intersects lattice vector ${\bf a}_1$ at $\frac{|{\bf a}_1|}{u}$, ${\bf a}_2$ at $\frac{|{\bf a}_2|}{v}$ and ${\bf a}_3$ at $\frac{|{\bf a}_3|}{w}$.

![](images/4-2-miller.svg)

Miller index 0 means that the plane is parallel to that axis (intersection at "$\frac{|{\bf a}_3|}{0}\rightarrow\infty$"). A bar above a Miller index means intersection at a negative coordinate.

If a crystal is symmetric under $90^\circ$ rotations, then $(100)$, $(010)$ and $(001)$ are physically indistinguishable.
Therefore, we use the notation $\{100\}$ to indicate a whole family of these symmetry-related planes.
In a cubic crystal, $[100]$ (this is a vector) is perpendicular to $(100)$ $\rightarrow$ proof in problem set.

Why are these Miller planes usefull?
It allows us to know the exact orientation of a crystal structure if the crystal structure is known.

---

## Conclusions

  * We described how to construct a reciprocal lattice from a real-space lattice.
  * Points in reciprocal space that differ by a reciprocal lattice vector are equivalent.

---

## Exercises
### Preliminary provocations

1. Calculate $\mathbf{a}_1 \cdot \mathbf{b}_1$ and $\mathbf{a}_2 \cdot \mathbf{b}_1$ using the definitions of the reciprocal lattice vectors given in the lecture. Is the result what you expected?

### Exercise 1: Equivalence of direct and reciprocal lattice

The volume of a primitive cell of a lattice with lattice vectors $\mathbf{a}_1, \mathbf{a}_2, \mathbf{a}_3$ [equals](https://en.wikipedia.org/wiki/Parallelepiped#Volume) $V = |\mathbf{a}_1\cdot(\mathbf{a}_2\times\mathbf{a}_3)|$.

1. Find the volume of a primitive unit cell $V^* = \left| \mathbf{b}_1 \cdot (\mathbf{b}_2 \times \mathbf{b}_3) \right|$ of the corresponding reciprocal lattice.
2. Derive the expressions for the lattice vectors $\mathbf{a}_i$ through the reciprocal lattice $\mathbf{b}_i$.

    ??? hint
        Make use of the vector identity
        $$\mathbf{A}\times(\mathbf{B}\times\mathbf{C}) = \mathbf{B}(\mathbf{A}\cdot\mathbf{C}) - \mathbf{C}(\mathbf{A}\cdot\mathbf{B})$$

3. Write down the primitive lattice vectors of the [BCC lattice](https://solidstate.quantumtinkerer.tudelft.nl/test_builds/lecture_9/9_crystal_structure/#body-centered-cubic-lattice) and calculate its reciprocal lattice vectors.
Which type of lattice is the reciprocal lattice of a BCC crystal?
4. Determine the shape of the 1st Brillouin zone.

### Exercise 2: Miller planes and reciprocal lattice vectors

Consider a family of Miller planes $(hkl)$ in a crystal.

1. Prove that the reciprocal lattice vector $\mathbf{G} = h \mathbf{b}_1 + k \mathbf{b}_2 + l \mathbf{b}_3$ is perpendicular to the Miller plane $(hkl)$.

    ??? hint
        Choose two vectors that lie within the Miller plane and are not parallel to each other.

2. Show that the distance between two adjacent Miller planes $(hkl)$ of any lattice is  $d = 2\pi/|\mathbf{G}_\textrm{min}|$, where $\mathbf{G}_\textrm{min}$ is the shortest reciprocal lattice vector perpendicular to these Miller planes.
3. Find the family of Miller planes of the BCC lattice that has the highest density of lattice points. To solve this problem use that the density of lattice points per unit area on a Miller plane is $\rho = d/V$. Here $V$ is the volume of the primitive unit cell and $d$ is the distance between adjacent planes given in 2.2.

### Exercise 3: Directions and Spacings of Miller planes

1. Explain what is meant by the terms Miller planes and Miller indices.
2. Consider a cubic crystal with one atom in the basis and a set of orthogonal primitive lattice vectors $a\hat{x}$, $a\hat{y}$ and $a\hat{z}$. Show that the direction $[hkl]$ in this crystal is normal to the planes with Miller indices $(hkl)$.
3. Show that this is not true in general. Consider for instance an orthorhombic crystal, for which the primitive lattice vectors are still orthogonal but have different lengths.
4. Any set of Miller indices corresponds to a family of planes separated by a distance $d$. Show that the spacing $d$ of the $(hkl)$ set of planes in a cubic crystal with lattice parameter $a$ is $d = \frac{a}{\sqrt{h^2 + k^2 + l^2}}$.

    ??? hint

        Recall that a family of lattice planes is an infinite set of equally separated parallel planes which taken all together contain all points of the lattice.

        Try computing the distance between the plane that contains the site $(0,0,0)$ of the conventional unit cell and a plane defined by the $(hkl)$ indices.

[^1]: This is only funny if you noticed the [tagline of the previous section](../../4-crystal/4-1-realspace/#crystal-structure)
