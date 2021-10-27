# Assignment 5: the reciprocal lattice and scattering

The fifth assignment can be found [here](../assignments/Assignment five.pdf)

## Exercise 1 - The reciprocal lattice

Following the normal conventions, let us denote $\mathbf{a}_i$ and $\mathbf{b}_i$ as the real-space and reciprocal space lattice vectors.

1. A construction of lattice vectors can be achieved using the relation
\[
\mathbf{b}_i = 2\pi \frac{\mathbf{a}_j \times \mathbf{a}_k}{\mathbf{a}_1 \cdot (\mathbf{a}_2 \times \mathbf{a}_3)}
\]
Explicitly compute $\mathbf{a}_1 \cdot \mathbf{b}_1$, $\mathbf{a}_2 \cdot \mathbf{b}_1$, and $\mathbf{a}_3 \cdot \mathbf{b}_1$. Do these computations accord with the definition of the reciprocal lattice?

    The computation of these vectors is aided by knowledge of [properties of the scalar triple product](https://en.wikipedia.org/wiki/Triple_product#Scalar_triple_product). In calculating the product:

    $$
    \mathbf{a}_i \cdot \mathbf{b}_1 = 2\pi \frac{\mathbf{a}_i \cdot (\mathbf{a}_2 \times \mathbf{a}_3)}{\mathbf{a}_1 \cdot (\mathbf{a}_2 \times \mathbf{a}_3)}
    $$

    it should be immediately obvious that $\mathbf{a}_2 \times \mathbf{a}_3$ is orthogonal to both $\mathbf{a}_2$ and $\mathbf{a}_3$, so the dot product between $\mathbf{a}_2$ and $\mathbf{a}_3$ will be zero. In the case of $\mathbf{a}_1$, we then have identical vector products on both numerator and denominator and therefore the product evaluates to $2\pi$.

    The construction of the reciprocal lattice is baser around the identity

    $$
    e^{i\mathbf{G}\cdot\mathbf{R}} = 1
    $$

    for any lattice point $\mathbf{R}$ and any reciprocal lattice point $\mathbf{G}$. That relation only holds when

    $$
    \mathbf{a}_i \cdot \mathbf{b}_j = 2\pi \delta_{ij}
    $$

    and hence our relations above are looking good.

2. The volume of a primitive unit cell with lattice vectors $\mathbf{a}_i$ is given by $V = \left|\mathbf{a}_1 \cdot (\mathbf{a}_2 \times \mathbf{a}_3) \right|$. Find the volume of the corresponding primitive unit cell in reciprocal space.

    The volume in reciprocal space $V'$ should be computed using the same method as provided:

    $$
    \begin{align}
    V' & = \left|\mathbf{b}_1 \cdot (\mathbf{b}_2 \times \mathbf{b}_3) \right| \\
    & = 2\pi \left| \frac{(\mathbf{a}_2 \times \mathbf{a}_3)}{\mathbf{a}_1 \cdot (\mathbf{a}_2 \times \mathbf{a}_3)} \cdot (\mathbf{b}_2 \times \mathbf{b}_3) \right| \\
    & = \frac{2\pi}{V}\left| (\mathbf{a}_2 \times \mathbf{a}_3) \cdot (\mathbf{b}_2 \times \mathbf{b}_3) \right| \\
    & = \frac{2\pi}{V}\left| (\mathbf{a}_2 \cdot \mathbf{b}_2)(\mathbf{a}_3 \cdot  \mathbf{b}_3) - ( \mathbf{a}_2 \cdot \mathbf{b}_3)( \mathbf{a}_3 \cdot \mathbf{b}_2) \right| \\
    & = \frac{(2\pi)^3}{V}
    \end{align}
    $$

3. Show that the general direction $[hkl]$ in a cubic crystal is normal to the planes with Miller indices $(hkl)$.

    Consider a (real-space) lattice with basis vectors $\mathbf{a}$, $\mathbf{b}$, and $\mathbf{c}$ which are assumed orthogonal (cubic crystal). Let the lengths of these vectors be $a$, $b$, and $c$ respectively. The plane $(hkl)$ will have intercepts with the axes at (a/h, 0, 0), (0, b/k, 0), (0, 0, c/l), and from these 3 points, one can construct a vector normal to the plane (which defines the plane) by taking the cross products between any two vectors between the points above. For example,     consider

    $$
    \begin{align}
    \mathbf{n} & = (\mathbf{a}/h - \mathbf{b}/k) \times (\mathbf{a}/h - \mathbf{c}/k) \\
    & = \frac{abc}{hkl} \left( \frac{h}{a^2}\mathbf{a} + \frac{k}{b^2}\mathbf{b} + \frac{l}{c^2}\mathbf{c} \right)
    \end{align}
    $$

    and this is only parallel to the vector $[hkl]$ in the case of $a = b = c$.

4. Is the above statement true for an orthorhombic crystal? Justify your response.

    No, it is not true, see the question above!

5. Show that the distance between two adjacent Miller planes $(hkl)$ of any lattice is $d=2\pi/|\mathbf{G}_{\textrm{min}}|$, where $\mathbf{G}_{\textrm{min}}$ is the shortest reciprocal lattice vector perpendicular to these Miller planes.

    The unit vector normal to the plane can be computed via

    $$
    \hat{\mathbf{n}} = \frac{\mathbf{G}}{|\mathbf{G}|}.
    $$

    Let us consider a very simple case in which we have the miller planes $(h00)$. For lattice planes, there is always a plane intersecting the zero lattice point $(0,0,0)$. As such, the distance from this plane to the closest next one is given by

    $$
    d = \hat{\mathbf{n}} \cdot \frac{\mathbf{a_1}}{h} = \frac{2\pi}{|\mathbf{G}|}
    $$

6. Find the family of Miller planes of the BCC lattice that has the highest density of lattice points. It may of useful to think about the density of lattice points per unit area on a Miller plane which is given by $\rho=d/V$.

    Since $\rho=d/V$, to maximise $\rho$ me must either must maximize $d$ or minimise $V$, the latter of which is fixed. Therefore, to maximise $d$, we minimize must $|\mathbf{G}|$ and thus the smallest possible reciprocal lattice vectors are the (100) family of planes (in terms of FCC primitive lattice vectors).

## Exercise 2 - Lattice planes

In assignment four, you looked at the  structure of zincblende (ZnS) (zinc atoms are yellow, sulphur atoms are grey).

![](../images/A5-2-Zincblende.png)

1. Draw a simplified plan view (don't worry about indicating heights) down the [001] axis, and indicate the [210] direction and the (210) family of planes

    The plan, planes and reciprocal lattice vector are shown below:

    ![](../images/A5-2-210.png){: .center}

2. The confidence tester: explain why the family of planes above is or is not a family of lattice planes.

    * If it is a family of lattice planes, do nothing and be content with your decision
    * If it is not a family of lattice planes, what would be a family of lattice planes in the same direction?

    The lattice type is a Face-centred cubic (FCC), and clearly the lattice planes do capture all atoms, and thus the spacing must be decreased, or the reciprocal lattice vector doubled, so (420) would define a family of lattice planes.

## Exercise 3 - Scattering

1. What is the origin of the Laue condition? That is, why is the amplitude of a scattered wave zero if $\mathbf{k'} - \mathbf{k} \ne \mathbf{G}$?

    If $\mathbf{k'} - \mathbf{k} \ne \mathbf{G}$, then the argument of the exponent has a phase factor dependent on the real-space lattice points. Because we sum over each of these lattice points, each argument has a different phase. Summing over all these phases results in an average amplitude of 0, resulting in no intensity peaks.

2. Consider a two-dimensional crystal with a rectangular lattice and lattice vectors $\mathbf{a}_1 = (0.468, 0) \mathrm{nm}$ and $\mathbf{a}_2 = (0, 0.342) \mathrm{nm}$ (so that $\mathbf{a}_1$ points along $x$-axis and $\mathbf{a}_2$ points along $y$-axis)

    1. Sketch the reciprocal lattice of this crystal

    ![](../images/A5-3-i.svg){: .center}

    2. Consider an X-ray diffraction experiment performed on this crystal using monochromatic X-rays with wavelength $0.166\mathrm{nm}$. Assuming elastic scattering, find the magnitude of the wave vectors of the incident and reflected X-rays

    With elastic scattering, we have $|k| = |k'| = 2\pi\lambda = 37.9 \mathrm{nm^{-1}}$

    3. On your sketch of the reciprocal lattice, draw the "scattering triangle" corresponding to the diffraction from (210) planes. Explicitly, use the Laue condition $\Delta \mathbf{k} = \mathbf{G}$ for constructive interference of diffracted X-rays

    ![](../images/A5-3-iii.svg){: .center}

## Exercise 4 - Diffraction and structure

1. Compute the structure factor $S$ of the BCC lattice

    The structure factor $S(\mathbf{G})$ is given by

    $$
    \sum_j f_j e^{i\mathbf{G} \cdot \mathbf{r}_j}
    $$

    where the sum over $j$ is the atoms in the unit cell. We can write this explicitly as

    $$
    \sum_j f_j e^{2\pi i hu_j + kv_j + lw_j} f_j
    $$

    where $(hkl)$ are the miller indices of $\mathbf{G}$ and $[u_j, v_j, w_j]$ are the positions of atom $j$ in the unit cell. To compute this, we write a BCC lattice as a simple cubic with a basis [0,0,0] and [1/2, 1/2, 1/2], and therefore we get the structure factor

    $$
    \begin{align}
    S & = f_{\textrm{Cr}} + f_{\textrm{Cr}} e^{2\pi i(h/2 + k/2 + l/2)} \\
    & = f_{\textrm{Cr}}\left(1 + (-1)^{h+k+l}\right)
    \end{align}
    $$

2. Which diffraction peaks are missing?

    From above, it is clear that the structure vanishes whenever $h+k+l$ is odd, and we can write

    $$
    S = \left\{ \begin{array}{ll} 2f_{\textrm{Cr}} \quad h+k+l~\textrm{even} \\ 0 \quad h+k+l~\textrm{odd} \end{array} \right.
    $$

3. How does this structure factor change if the atoms in the centre of the conventional unit cell have a different form factor from the atoms at the corner of the conventional unit cell?

    If we write the atomic form factors of the different atoms $f_1$ and $f_2$

    $$
    S = \left\{ \begin{array}{ll} f_1 + f_2 \quad h+k+l~\textrm{even} \\ f_1 - f_2 \quad h+k+l~\textrm{odd} \end{array} \right.
    $$

4. A student carried out X-ray powder diffraction on chromium (Cr) which is known to have a BCC structure, and the first five diffraction peaks are given below. Delightfully, the student took the liberty of assigning Miller indices to the peaks. Were the peaks assigned correctly? Fix any mistakes and explain your reasoning.
![](../images/A5-Cr.svg)

    The values of $(hkl)$ must satisfy the selection rules above, which means that the peaks should be $(110), (200), (211), (220), (310)$ from lowest angle to highest angle.

5. The X-ray diffraction was carried out using Cu $K_\alpha$ radiation ($\lambda = 1.5406 \mathrm{\unicode{x212B}}$). Use this information to calculate the lattice constant $a$ of the chromium BCC unit cell, and provide an estimate for uncertainty of this value.

    To calculate the lattice spacing, one must use the relations that for a given lattice spacing $d_{(h,k,l)}$, the Bragg condition holds:

    $$
    d_{(h,k,l)} = \frac{\lambda}{2 \sin\theta}
    $$

    In a cubic lattice, one also has the relation that

    $$
    d_{(h,k,l)} = \frac{a}{\sqrt{h^2 + k^2 + l^2}}
    $$

    so then the lattice constant $a$ can be calculated through

    $$
    a = \frac{\lambda\sqrt{h^2 + k^2 + l^2}}{2 \sin\theta}
    $$

    One can the calculate a value for each angle (and Miller index) to return a list of lattice constants, from which a range an uncertainty can be derived. I have just used the mean and standard deviation - no weighted means, no uncertainty in peak location, just raw statistical deviation from my _very_ rough extraction of the scattering angle.

    ``` python
    lamb = 1.5406 #[\unicode{x212B}]
    def lat(h, k, l, t):
      return (np.sqrt(h**2 + k**2 + l**2) * lamb)/(2*np.sin(t))

    angles = np.array([44, 63, 81, 97, 113])
    miller = np.array([[1,1,0], [2,0,0], [2,1,1], [2,2,0], [3,1,0]])

    touse = []
    for (n, p) in enumerate(miller):
      touse.append(np.append(p, np.deg2rad(angles[n]/2)))

    avals = []
    for d in touse:
      avals.append(lat(*d))

    print(f"The lattice spacing was determined to be {np.mean(avals):.3f} with a standard deviation of {np.std(avals):.3f}")
    ```

    My result was $a = 2.918 \pm 0.016 \mathrm{\unicode{x212B}}$
