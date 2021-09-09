# Crystal structure

Learn the _real_ secrets of crystals.

## Introduction

![](images/4-1-crystalheader.jpg)

Our journey to this point has seen our initial, somewhat crude models of solids receive enhancement in the form of microscopic models in one dimension, which gave rise to dispersion relations for both phonons and electrons, with many interesting predictions. Unfortunately, it is rare that the universe gives us one dimensional systems[^1] and thus we must consider systems in higher dimensions, and we are going to look in detail at three-dimensional solids. Specifically, we are going to limit ourselves to _ordered solids_, but to do this meaningfully, we must develop the tools and nomenclature to properly describe these systems.


!!! warning "Definition bashing"

    There are to be _many_ definitions to be introduced in this discussion.

!!! danger  "Expected competencies"

    It is assumed that you have familiarity with the following concepts/techniques:

    * Mathematics: Linear algebra, geometry and symmetry

!!! note  "Text reference"
    The material covered here is discussed in section(s) $\S 12$ of [The Oxford Solid State Basics](https://global.oup.com/academic/product/the-oxford-solid-state-basics-9780199680771?cc=au&lang=en&)

!!! info "Computational content"

    The Jupyter notebook associated with this section can be accessed by clicking the icon below:
    [<i class="fab fa-python fa-5x"></i>](https://jove2021.cloud.edu.au/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FAndy-UTAS%2FSolid-state&urlpath=tree%2FSolid-state%2F4-1-crystals.ipynb&branch=master){ .md-button .md-button--primary class="text-center" style="margin-left: 45%"}

---

## Crystal classification

Limiting ourselves to considering crystals may seem like a compromise, after all, not everything is a crystal. This is both true and false: crystals as we think of them (emeralds, sapphires, salt, etc.) are obviously not ubiquitous, but repeating motifs of atoms describe almost all systems at some length scale, and certainly for most systems of interest in solid-state physics, this is almost always true.

### Lattices and unit cells

Crystals are _highly ordered_ microscopic, where this microstructure can be reflected in the macrostructure. which are periodic multi-atomic structures.

!!! info  "Definition: crystal"

    A crystal is a periodic arrangement of particles (atoms, molecules, ...)

To describe periodic structures, we need a framework, and this framework is provided by the concept of a lattice

!!! info  "Definition: lattice"

    i) A lattice is an infinite set of points defined by an integer sums of a set of linearly independent primitive lattice vectors

Explicitly, in one dimension we can write

$$
\mathbf{R}_{\left[n_{1}\right]}=n_{1} \mathbf{a}_{1}, \quad \mathrm{for } \:\: n_{1}, \in \mathbb{Z},
$$

in two dimensions we can write

$$
\mathbf{R}_{\left[n_{1} n_{2}\right]}=n_{1} \mathbf{a}_{1}+n_{2} \mathbf{a}_{2}, \quad \mathrm{for } \:\: n_{1}, n_{2} \in \mathbb{Z},
$$

and in three dimensions we can write

$$
\mathbf{R}_{\left[n_{1} n_{2} n_{3}\right]}=n_{1} \mathbf{a}_{1}+n_{2} \mathbf{a}_{2}+n_{3} \mathbf{a}_{3}, \quad \mathrm{for } \:\: n_{1}, n_{2}, n_{3} \in \mathbb{Z}
$$

where $\mathbf{a}_i$ are the primitive lattice vectors. It should be clear that for a $n$ dimensional system, we require $n$ linearly independent primitive lattice vectors to span the entire lattice, but also the choice of these vectors is not unique.

The image below shows a simple two-dimensional square lattice, where each of the black dots are lattice points.

<figure>
  <img src="../images/4-1-simplelattice.svg">
</figure>

There exist multiple equivalent definitions of a lattice, which can be useful to consider in different circumstances.

!!! info  "Definition: lattice"

    ii) A lattice is a set of points where the environment of each point is the same
    iii) A lattice is an infinite set of vectors where the addition of any two vectors returns a vector in the set

We identify that definition (ii) is the more intuitive definition. For example, let's look a the well-known honeycomb structure:

<figure>
  <img src="../images/4-1-graphene-single.png">
</figure>

??? question  "4.1.1: Is the honeycomb structure a lattice?"

    <!-- No, despite seeming like it should be! It is most easily seen as the environment around all points should look the same, and if we look at the point at the tip of a given hexagon, and the point to either the left or right of this point, it is clear that they are not the same! -->

A vector connecting any two lattice points is called a **lattice vector**. Supposing that we choose two linearly independent lattice vectors $\mathbf{a}_1$ and $\mathbf{a}_2$, these two lattice vectors span an area which is called a **unit cell**:

!!! info  "Definition: unit cell"

    A unit cell is a region of space such that when many identical units are stacked together it tiles (completely fills) all of space and reconstructs the full structure

{% include images/4-1-simple_lattice.html %}

In the case of a 3D lattice, we need to choose three linearly independent lattice vectors and thus the unit cell will be a volume instead of an area. If the chosen unit cell only contains a single lattice point, this is called a **primitive unit cell**. The lattice vectors which construct the primitive unit cell are called **primitive lattice vectors**. Because the primitive unit cell is constructed out of a set of linearly independent primitive lattice vectors, the primitive unit cell can be repeated infinitely many times to map out the entire lattice!

The unit cell, which was conveniently chosen in panel `B`, defines a primitive unit cell. At first glance it might seem that there are four lattice point inside the primitive unit cell instead of one; however, each point only occupies the lattice by one quarter. Therefore, there is exactly $4 \times \frac{1}{4} = 1$ lattice point in the unit cell and is thus it is a primitive unit cell!

As previously mentioned, the choice of the primitive lattice vectors is _not_ unique. For example, we could have easily chosen another set of lattice vectors - as shown in panel `C` - which produce primitive unit cells.
Both choices are primitive unit cells and thus make it possible to map out the entire lattice!

??? Question "4.2.2: Looking the primitive cell in panel `C`, how much does each lattice point "occupy" the unit cell?"

    <!-- Two points occupy it for one eight and two points for three eights. -->

### Periodic structures.

Equipped with the basic definitions of a lattice, (primitive) lattice vectors, and (primitive) unit cells, we can now apply our knowledge to an actual periodic structure.
In the image below we show a periodic structure (panel `A`).

<object type="text/html" data="../images/4-1-periodic.html"  frameborder="0" width=650 height=650 class=center></object>

Again, it should be emphasised that there are several ways to assign lattice points to the periodic structure. For example, we could assign the lattice points to the stars themselves: this is a valid choice of a lattice for the periodic structure because each lattice point has the same environment. As the lattice points form triangles, this lattice is called a **triangular lattice**.

The choice of a lattice also defines two linearly independent primitive lattice vectors $\mathbf{a}_1$ and $\mathbf{a}_2$ (panel `B`):

$$
\mathbf{a}_1 = \hat{\mathbf{x}} = \left[ 1, 0\right], \quad \mathbf{a}_2 = \frac{1}{2}\hat{\mathbf{x}} + \frac{\sqrt{3}}{2} \hat{\mathbf{y}}= \left[1/2, \sqrt{3}/2\right].
$$

With these primitive lattice vector, the lattice is given by

$$
\mathbf{R}_{\left[n_{1}, n_{2}\right]}=n_{1} \left[ 1, 0 \right]+n_{2}
\left[ 1/2, \sqrt{3}/2 \right], \quad \mathrm{for} \:\: n_{1}, n_{2} \in \mathbb{Z}.
$$

However, our description so far is insufficient to describe the periodic structure. Although we have mapped out the entire lattice, we still do not have any information about the repeated motif. It incorporate this information, we introduce the concept of a **basis**[^2]:

!!! info  "Definition: basis"

          The description of objects with respect to the reference lattice point is known as a basis

The reference lattice point is the chosen lattice point to which we apply the lattice vectors in order to reconstruct the lattice. In our case, we chose the reference point as $[0, 0]$. With respect to the reference point, the motif is located at $[0, 0]$. In this particular example, the repeated motif and the lattice can be coincident, but more generally this will not be the case. The location of all the patterned object in the lattice with respect to the reference lattice point is then given by:

$$
\mathbf{R}_{\left[n_{1}, n_{2}\right]}^{\mathrm{motif}} = n_{1} \left[ 1, 0 \right]+n_{2}
\left[ 1/2, \sqrt{3}/2 \right], \quad \mathrm{for} \:\: n_{1}, n_{2} \in \mathbb{Z}.
$$

Another way to define the basis is in terms of the **fractional coordinates** of the primitive lattice vectors. In other words, we want to express the basis as a linear combination of the primitive lattice vectors:

$$
(f_1, f_2, \ldots, f_N) = \sum_{i = 1}^{N}f_i \mathbf{a}_i,
$$

where $f_i$ is the fractional coordinate of $\mathbf{a}_i$ and $N$ is the dimensionality of the system. In 2D this equation reduces to

$$
(f_1, f_2) = f_1 \mathbf{a}_1 + f_2 \mathbf{a}_2.
$$

In our case, the basis is `hourglass` $(0,0)$ which is specifying the location of the `hourglass` in the unit cell as $0 \mathbf{a}_1 +0 \mathbf{a}_2$. Whilst the is slightly contrived, we shall see its application to physical systems soon enough, and there we would simply replace `hourglass` with the relevant atom, for example, $\mathrm{C}(f_1, f_2)$ for carbon in the unit cell.

Similar to primitive lattice vectors, the choice of a lattice **not** unique. For example, shown in panel `C`, the same periodic structure is shown, but with the lattice translated by $1/2 \mathbf{a}_1$. The choice still fulfils the definition of a lattice: the environment of each lattice point is the same, with the only difference being that the lattice is translated and thus we keep using the same primitive lattice vectors.

??? Question "4.2.3: What is the basis for translated lattice as shown in panel `C`? What are the positions of each of the hourglasses in the lattice?"

<!-- The hourglasses are no longer situated on the lattice points, rather they are located at $[1/2,0]$, which is half of $\mathbf{a}_1$, and therefore the basis hourglass $(1/2, 0)$.

The location of the hourglasses throughout the periodic structure with respect to the reference lattice point is then given by

$$
\mathbf{R}_{\left[n_{1}, n_{2}\right]}^{\mathrm{star}} = \left[1/2, 0 \right] + n_{1} \left[ 1, 0 \right]+n_{2}
\left[ 1/2, \sqrt{3}/2 \right], \quad \mathrm{for} \:\: n_{1}, n_{2} \in \mathbb{Z}.
$$
-->

### Conventional unit cell

In the system we have been considering, it is clear that the primitive vectors are not orthogonal, and this is not ideal: we like orthogonal things!

!!! info  "Definition: conventional unit cell"

    A unit cell with an orthogonal set of lattice vectors

An example of such a unit cell is shown is panel `D`. In contrast to primitive unit cells, conventional unit cells may contain multiple lattice points, as shown in the example: there is an additional lattice point at the centre, and thus $1 + 4 \times \frac{1}{4} = 2 $ lattice points in the conventional unit cell.

Returning to our pattern, if we use the shown conventional unit cell, there is now a problem with the definition of the lattice vectors: no integer linear combination of lattice vectors is able to produce the lattice point in the centre of the unit cell. Therefore, in order to map out the entire lattice, we need to include an extra position the basis. Since there is one hourglass at the corner of the unit cell and one in the centre, the basis is: hourglass: $(0,0),(1/2,1/2)$. The corresponding locations of the stars with respect to the reference lattice point are then given by:

$$
\begin{align}
\mathbf{R}_{\left[n_{1}, n_{2}\right]}^{\mathrm{corner}} &= n_{1} \mathbf{a}_1 +n_2 \mathbf{a}_2 \\
\mathbf{R}_{\left[n_{1}, n_{2}\right]}^{\mathrm{centre}} &= \frac{1}{2}\left( \mathbf{a}_1 + \mathbf{a}_2 \right) + n_{1} \mathbf{a}_1 +n_2 \mathbf{a}_2,
\end{align}
$$

for $ n_{1}, n_{2} \in \mathbb{Z}$.

Alternatively, one can think of the crystal structure being made up from two intersecting orthogonal lattices - one centred at $[0,0]$ and another at $[1/2,1/2]$, each with basis $(0,0)$.

??? Question "4.2.4: For what type of lattice is the conventional unit cell also primitive?"

    <!-- A simple square lattice -->

### Recipe for analysing periodic structures

When encountering periodic systems in the wild, we can come up with a recipe for analysing them. One such recipe is as follows:

  1. Choose origin (can be an atom, but this is not necessary)
  2. Find other lattice points (identical atoms)
  3. Choose lattice vectors that translate between these lattice points: either primitive or not primitive (in which case you require an additional basis point)
      - The lengths of lattice vectors and angle(s) between them fully define the crystal lattice
  4. Specify the basis

Much like a good recipe, the definition of a lattice and a basis allows one to cook up the location of every atom in the periodic structure and thus the crystal structure.

#### Example: Graphene

Let's put our skills to the test, analysing a real structure. Graphene, besides being super cool, is made out of a single layer of carbon atoms arranged in a honeycomb shape, with a nearest-neighbour interatomic distance of $a$. The locations of atomic positions is shown in panel `A` below:

<object type="text/html" data="../images/4-1-graphene.html"  frameborder="0" width=650 height=650 class=center></object>

Following our recipe above, the first task is to find suitable lattice points. We start by choosing a lattice point on the $(0,0)$ coordinate, and looking for all identical atoms. We see that not all carbon atoms have the same environment with respect to our chosen lattice point, and hence, not all carbon atoms coincide with lattice points!
Only those with the same environment are valid lattice points. Panel `B` shows the lattice, which we identify as a triangular lattice.

##### Primitive unit cell

Next, we find lattice vectors, and because lattice vectors are not unique, we are free to choose them. A natural choice for primitive lattice is shown in panel `C` and with a little geometry, we find that $\mathbf{a}_1$ and $\mathbf{a}_2$ are:

$$
\mathbf{a}_1 = [\sqrt{3}, 0] a, \quad \mathbf{a}_2 = [\sqrt{3}/2, 3/2] a.
$$

As usual, with these lattice vectors we are able to map out the entire lattice, but we must specify the repeated motif, that is, the basis. Each primitive unit cell contains two carbon atoms: one is at the reference point $(0,0)$ and the other is located at $(\sqrt{3},1)a$. When writing the basis, we want to express the coordinates as fractional coordinates of the chosen lattice vectors, and for the atom at the reference point this is easy: $\mathrm{C}(0,0)$.

In order to find the fractional coordinates of the second carbon atom, it is convenient to first look at the $y$ coordinate of the atom, which is $a$. Because only $\mathbf{a}_2$ has a nonzero $y$ component, we easily find the fractional coordinate of $\mathbf{a}_2$: it is simply $\frac{a}{3a/2} = 2/3$. To find the fractional coordinate of $\mathbf{a}_1$, we use the fractional coordinate of $\mathbf{a}_2$. Multiplying the $x$ component of $\mathbf{a}_2$ by $2/3$ yields $1/\sqrt{3}$.
We know that

$$
\begin{align}
\sqrt{3} &= f_1 a_{1,x} + f_2 a_{2,x}\\
&= f_1 \sqrt{3} + 1/\sqrt{3},
\end{align}
$$

Bringing $1/\sqrt{3}$ to the other side and dividing both sides by $\sqrt{3}$ yields $f_1 = 2/3$. Hence the basis of the second atom is $\mathrm{C}(2/3, 2/3)$.

##### Conventional unit cell

To show why one likes conventional unit cells, in panel `D` we show the conventional unit cell with the lattice vectors:

$$
\mathbf{a}_1 = [\sqrt{3}, 0] a, \quad \mathbf{a}_2 = [0, 3] a.
$$

The price one pays for the convenience of orthogonal lattice vectors: the unit cell now contains four carbon atoms which need to be specified in the basis. Fortunately, the task is much more straightforward and the basis in fractional coordinates is: $\mathrm{C}(0,0), \: \mathrm{C}(0,1/3), \: \mathrm{C}(1/2, 1/2)$ and $\mathrm{C}(1/2, 5/6)$.

### Wigner-Seitz unit cell

Primitive unit cells are not unique; however, there exists a unique primitive cell which is the locus of points which are closer to a given lattice point than all other lattice points, and is known as the _Wigner-Seitz cell_. Much like our other unit cells, we can use a recipe to cook it up:

  1. From a given lattice point, find all neighbouring lattice points
  2. Draw lines between the reference lattice point and the neighbouring lattice points
  3. Draw perpendicular bisectors of each line
  4. Extend the perpendicular bisectors until they intersect

This procedure will produce the Wigner-Seitz cell, and panel `E` in the graphene example shows the Wigner-Seitz cell for graphene. We note that the Wigner-Seitz cell only contains a single lattice point in the middle, but it does however contain other atoms, which must be specified in the basis.

??? Question "How many carbon atoms are inside the Wigner-Seitz cell of graphene?"

    There are two methods to calculate this. We either translate the lattice and thus the Wigner-Seitz cell a bit and observe that there are two carbon atoms inside the cell.
    Another way to calculate the number of atoms inside the cell is by realizing that there is an atom at the lattice point itself and there is 1/3'rd of an atom at three corners of the cell.
    This results in $1+3\times 1/3 = 2$ atoms being inside the unit cell.

For the moment, one can think of the Wigner-Seitz cell as a bit of an abstraction, but we shall see its importance as we continue on our journey.

## Three dimensional lattices (d++)

Thus far we have looked at two-dimensional periodic structures, but as mentioned: most crystal structures are three dimensional. Fortunately, the tools used to describe lattices in any dimensional are applicable in other dimension. For the duration of this course, we shall be mainly concerned with _cubic_ lattices (and closely-related friends), which have the delightful property that the lattice vectors $\mathbf{a_1}$, $\mathbf{a_2}$, and $\mathbf{a_3}$ are colinear with $\mathbf{\hat{x}}$, $\mathbf{\hat{y}}$, and $\mathbf{\hat{z}}$. In the case that the magnitude of each vector is identical (lattice constant $a$), this is called a _simple cubic lattice_.

!!! example "Lattices: cubic and friends"

    === "Cubic lattice"

        <figure>
          <img src="../images/4-1-cubic.png">
          <figcaption> All cell edge lengths equal</figcaption>
        </figure>      

    === "Tetragonal"

        <figure>
          <img src="../images/4-1-tetragonal.png">
          <figcaption> Two cell edge lengths equal</figcaption>
        </figure>

    === "Orthorhombic"

        <figure>
          <img src="../images/4-1-orthorhombic.png">
          <figcaption> All cell edge lengths unequal</figcaption>
        </figure>


??? Question "4.2.5: How many lattice points are there in the unit cell for the simple cubic lattice?"

    <!-- Each corner of the cell contains a lattice point, but only one eighth of each lattice point is in the cell, thus there is a single lattice point in the cell and it is therefore a primitive unit cell. -->

The only mineral which has a simple cubic lattice structure is a metallic allotrope of Polonium, but given the nature of polonium, there are no pretty pictures to show. Rather, shown below is the mineral pyrite (iron (II) disulphide), which at the macroscale has a very satisfying cubic structure:

<figure>
  <img src="../images/4-1-pyrite.jpg">
  <figcaption> An incredible sample of pyrite, sourced from <a href="https://commons.wikimedia.org/w/index.php?curid=20844289">wikipedia</a> and used under the creative commons licence <a href="https://creativecommons.org/licenses/by-sa/3.0">CC BY-SA 3.0</a></figcaption>
</figure>

To understand this, and other systems, we must consider additional classes of cubic lattices.

### The body-centred cubic lattice

<object type="text/html" data="../images/4-1-fcc.html"  frameborder="0" width=650 height=650 class=center></object>

The image above (panel `A`) shows a simple cubic lattice. Now, perhaps the simplest adjustment one can imagine making the simple cubic structure is the addition of a lattice point to the centre of the simple cubic cell, which is shown in panel `B`. This structure is known as the  **Body-Centred Cubic** (**BCC**) lattice. In the BCC lattice, there are 8 lattice points on the corners of the cell and one in the centre and thus the conventional unit cell contains $8\times 1/8+1 = 2$ lattice points, and is therefore not primitive.

??? Question "What is the basis of the bcc lattice?"

    $(0,0,0)$ and $(1/2, 1/2, 1/2)$

<figure>
  <img src="../images/4-1-iron.jpg">
  <figcaption> Iron at normal temperatures has a body-centred cubic structure </figcaption>
</figure>

### The face-cantered cubic lattice

Another way we can alter the simple cubic lattice is by adding a lattice point in every face of the simple cubic cell, which is shown in panel `C`. Such a structure is referred to as the **Face-Centred Cubic** (**FCC**) lattice. There is $1/2$ of a lattice point at each face inside the lattice, in addition to the corner lattice points and thus there are a total of $8 \times 1/8 + 6\times 1/2 = 4$ lattice points inside the unit cell, and thus it is not primitive.

<figure>
  <img src="../images/4-1-diamond.jpg">
  <figcaption> Materials which have a face-centred cubic lattice structure include diamond </figcaption>
</figure>

### Filling factor

Each of the three crystal structures above have a different configuration and number of atoms in the unit cell. This results in a different fraction of an unit cell being occupied by atoms. The **filling factor**, commonly called the **atomic packing factor**, measures the fraction of a volume of the unit cell that is occupied by atoms.
It assumes that the atoms are solid spheres with a volume $V_{\mathrm{atom}} = \frac{4 \pi}{3} R^3$, where $R$ is the radius of the sphere. For mono-atomic lattices, the filling factor $F$ is defined as follows:

$$
F = \frac{ N_{\mathrm{atom}} V_{\mathrm{atom}} }{V_{\mathrm{cell}}}.
$$

Here $N_{\mathrm{atom}}$ is the number of atoms in the unit cell and $V_{\mathrm{cell}}$ is the volume of the unit cell. To calculate the filling factor we first need to find out what $V_{\mathrm{atom}}$ is. To do this, we need to "blow up" the atoms simultaneously until each atom touches its neighbour, and we use this "blown up" geometry to find an expression for $R$ in terms of known quantities, such as the lattice constant.

!!! example "Filling factor of the FCC lattice"

    <object type="text/html" data="../images/4-1-filling.html"  frameborder="0" width=650 height=650 class=center></object>

    The lattice is shown in panel `A` of the image above. We first need to increase the size of the atoms until they touch each other. The faces of the FCC are rotationally symmetric and we obtain that all four corner atoms touch the centre atom (panel `B`). We identify that on the diagonal, the atoms touch each other, meaning that as the atoms have a radius $R$, the length of the diagonal is $4R$. Given the sides of the unit cell are length $a$, the diagonal of the unit cell will be equal to $\sqrt{2}a$.

    This implies that

    $$
    R = \frac{a}{2\sqrt{2}}.
    $$

    With the deduced radius of the atom, we can calculate $V_{\mathrm{atom}}$:

    $$
    V_{\mathrm{atom}} = \frac{4\pi}{3}R^3 = \frac{4\pi}{3} \left( \frac{a}{2\sqrt{2}} \right)^3 = \frac{\pi a^3}{12 \sqrt{2}}.
    $$

    The only thing that is left for us to determine is the number of atoms in the unit cell, which we earlier noted to be 4. Therefore we calculate the filling factor to be

    $$
    \begin{align}
    F &= \frac{ N_{\mathrm{atom}} V_{\mathrm{atom}} }{V_{\mathrm{cell}}}\\
    &= \frac{4 \times \frac{\pi a^3}{12\sqrt{2}}}{a^3}\\
    &= \frac{\pi}{3\sqrt{2}} \approx 0.74
    \end{align}
    $$

    or put another way, approximately $74 \%$ of the FCC unit cell is occupied by atoms.

??? Question "4.2.5: Can you think of another lattice structure with a higher filling factor?"

    <!-- The packing limit was theorized by Kepler in 1571 – 1630 and proven by Hales _et al._ in 1998!. -->

### Other lattice structures

It should be noted that there exist three dimensional lattices with non-orthogonal axes (and indeed are common), and the method for their description as introduced here is identical, but just a bit messier. Perhaps surprisingly, there are only [14 distinct lattices from which all other lattices from which all other lattices can be constructed](https://en.wikipedia.org/wiki/Crystal_system#Bravais%20lattices)!

---

## Conclusions

  * Lattices can be used to describe periodic systems
  * Several important concepts to describe crystal structure were introduced: lattice, lattice vectors, basis, primitive & conventional unit cells
  * The crystal structures with orthogonal lattice vectors were introduced, in addition to their different centring types: simple cubic, FCC, and BCC

---

## Exercises
### Preliminary provocations

  1. State the definition of a primitive unit cell.
  What can be said about its volume?
  2. Draw the conventional unit cell of a FCC and the BCC.
  Write down the primitive lattice vectors and the basis of each lattice.
  3. Suppose you find the primitive unit cell of a diatomic crystal.
  How many basis vectors do you minimally need to describe the crystal?
  Can a diatomic crystal require more basis vectors?
  4. Calculate the filling factor of a simple cubic lattice.
  5. Sketch the $(110),(1\bar{1}0),(111)$ miller planes of a simple cubic lattice.

### Exercise 1: Diatomic crystal

Consider the following two-dimensional diatomic crystal:

<figure>
  <img src="../images/4-1-diatomiclattice.svg">
</figure>

  1. Sketch the Wigner-Seitz unit cell and two other possible primitive unit cells of the crystal.
  2. If the distance between the filled cirles is $a=0.28$ nm, what is the area of the primitive unit cell?
  How would this area change if all the empty circles and the filled circles were identical?
  3. Write down one set of primitive lattice vectors and the basis for this crystal.
  What happens to the number of elements in the basis if all empty and filled circles were identical?
  4. Imagine expanding the lattice into the perpendicular direction $z$. We can define a new three-dimensional crystal by considering a periodic structure in the $z$ direction, where the filled circles have been displaced by $\frac{a}{2}$ in both the $x$ and $y$ direction from the empty circles.
  The figure below shows the new arrangement of the atoms.
  What lattice do we obtain?
  Write down the basis of the three-dimensional crystal.
  5. If we consider all atoms to be the same, what lattice do we obtain?
  Compute the filling factor in the case where all atoms are the same.

<object type="text/html" data="../images/4-1-diatomic.html"  frameborder="0" width=650 height=650 class=center></object>

### Exercise 2: Diamond lattice

Consider a the [diamond crystal structure](https://en.wikipedia.org/wiki/Diamond_cubic) structure. The following illustration shows the arrangement of the carbon atoms in a conventional unit cell.

<object type="text/html" data="../images/4-1-diamond.html"  frameborder="0" width=650 height=650 class=center></object>

The side of the cube is $ a = 0.3567$ nm.

  1. How is this crystal structure related to the fcc lattice?
  Write down one set of primitive lattice vectors and compute the volume of the corresponding primitive unit cell.
  2. How many atoms are in the primitive unit cell?
  Write down the basis.
  3. Determine the number of atoms in the conventional unit cell and compute its volume.
  4. What is the distance between nearest neighbouring atoms?
  5. Compute the filling factor.

[^1]: Although the do exist, and hopefully we shall discuss some later in the semester.
[^2]: Not to be confused with the basis from linear algebra!
