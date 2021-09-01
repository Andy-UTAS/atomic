# Placeholder

!!! failure  "Empty page"

    This page is a placeholder: the treasure you seek is in another castle

!!! danger  "Unbaked"

    The content here is still very much under development. Please come back soon!

## Introduction

![]()

<intro content>

!!! danger  "Expected competencies"

    It is assumed that you have familiarity with the following concepts/techniques:

!!! note  "Text reference"
    The material covered here is discussed in section(s) $\S$ of [The Oxford Solid State Basics](https://global.oup.com/academic/product/the-oxford-solid-state-basics-9780199680771?cc=au&lang=en&)

!!! info "Computational content"

    The Jupyter notebook associated with this section can be accessed by clicking the icon below:
    [<i class="fab fa-python fa-5x"></i>](#){ .md-button .md-button--primary class="text-center" style="margin-left: 45%"}

---

## Thermal expansion

While the quadratic approximation of the interatomic potential is certainly the most important, the anharmonic term $\kappa_3(r-a)^3/6$ also has physical significance.
Let us examine its role visually by comparing the harmonic and the third order approximations in the plot below.
Notice that the second-order approximation is symmetric around the minimum while the third-order term is not.

``` python
  r = np.linspace(-2, 2.5, 750)

  a = 0
  b = 0
  c = 1
  d = -0.2

  U_quadratic = a + b * r + c * r**2
  U_cubic =     a + b * r + c * r**2 + d * r**3

  r_min = -2
  r_max = 2.5
  U_min = -0.2
  U_max = 4

  E_t_min = 0.4
  E_t_max = 3.5
  N_values = 20
  l_width = 1.5
  N_active = 0

  # Create figure
  fig = go.Figure()

  def U_c(r):
      return a + b * r + c * r**2 + d * r**3


  def line(E_t):
      right = min(np.roots([c, b, a-E_t]))
      roots = np.roots([d, c, b, a-E_t])
      roots = np.real(roots[np.isreal(roots)])
      roots.sort()
      left = roots[1]
      return [left, right]

  def avg_pos_cubic(E_t):
      Z = integrate.simps(np.exp(- U_cubic / E_t), r)
      r_avg = integrate.simps(r * np.exp(- U_cubic / E_t), r)
      x = r_avg / Z
      return x


  # Add traces, one for each slider step
  for E_t in np.linspace(E_t_min, E_t_max, N_values):
      avg = avg_pos_cubic(E_t)
      fig.add_trace(
          go.Scatter(
              visible = False,
              x = r,
              y = U_quadratic,
              mode = 'lines',
              line_color = 'blue',
              name = "Quadratic potential",
          ))
      fig.add_trace(
          go.Scatter(
              visible = False,
              x = r,
              y = U_cubic,
              mode = 'lines',
              line_color = 'red',
              name = "Cubic potential",
          ))
      fig.add_trace(
          go.Scatter(
              visible = False,
              x = line(E_t),
              y = [E_t, E_t],
              mode = 'lines',
              line_color = 'black',
              name =  r'Thermal energy level'
          ))
      fig.add_trace(
          go.Scatter(
              visible = False,
              x = [0, 0],
              y = [0, E_t],
              mode = 'lines',
              line_color = 'blue',
              line_dash = 'dot',
              name =  r'$\langle r \rangle$ for the quadratic potential'
          ))
      fig.add_trace(
          go.Scatter(
              visible = False,
              x = [avg, avg],
              y = [U_c(avg), E_t],
              mode = 'lines',
              line_color = 'red',
              line_dash = 'dot',
              name =  r'$\langle r \rangle$ for the cubic potential'
          ))

  # Initial starting image
  N_trace = int(len(fig.data)/N_values) # Number of traces added per step
  for j in range(N_trace):
      fig.data[N_active*N_trace+j].visible = True

  # Creation of the aditional images
  steps = []
  for i in range(int(len(fig.data)/N_trace)):
      step = dict(
          method = "restyle",
          args = [{"visible": [False] * len(fig.data)}],
          value = str(0.1*(i+1))
      )
      for j in range(N_trace):
          step["args"][0]["visible"][N_trace*i+j] = True  # Toggle i'th trace to "visible"
      steps.append(step)

  # Creating the slider
  sliders = [dict(
      tickcolor = 'White',
      font_color = 'White',
      currentvalue_font_color = 'Black',
      active = N_active,
      name = r'Thermal Energy',
      font_size = 16,
      currentvalue = {"prefix": r'Thermal Energy k_B T: '},
      pad = {"t": 50},
      steps = steps,
  )]

  # Updating the images for each step
  fig.update_layout(
      sliders = sliders,
      showlegend = True,
      plot_bgcolor = 'rgb(254, 254, 254)',
      width = 700,
      height = 580,
      xaxis = dict(
          range=[r_min, r_max],
          visible = True,
          showticklabels = True,
          showline = True,
          linewidth = l_width,
          linecolor = 'black',
          gridcolor = 'white',
          tickfont = dict(size = 16)),
      yaxis = dict(
          range = [U_min, U_max],
          visible = True,
          showticklabels = True,
          showline = True,
          linewidth = l_width,
          linecolor = 'black',
          gridcolor = 'white',
          tickfont = dict(size = 16)),
      title = {'text': r'Thermal expansion of cubic potential',
          'y':0.9,
          'x':0.45,
          'xanchor': 'center',
          'yanchor': 'top'},
      xaxis_title = r'$r$',
      yaxis_title = r'$U [k_b T]$',
  )  

  # Edit slider labels and adding text next to the horizontal bar indicating T_E
  for i in range(N_values):
      fig['layout']['sliders'][0]['steps'][i]['label'] = ' %.1f ' % ((E_t_max-E_t_min)*i/(N_values-1) + E_t_min)

  # Showing the figure
  plt.plot(fig)
  fig.show()
```

The asymmetry due to nonzero $\kappa_3$ slows the growth of the potential when the interatomic distance increases.
On the other hand, when the interatomic distance decreases, the asymmetry accelerates the growth of the potential.
Therefore, stretching the material is more energetically favorable than contracting it.
As a result, thermal excitations increase the interatomic distance.
This gives us a simple model of *thermal expansion*.

## Van der Waals bond

While we focus on the mechanisms of covalent bonding, let us also review another bond type.

A *Van der Waals bond* originates from an attraction between the dipole moments of two atoms.
Suppose we have two atoms separated by an interatomic distance $r$.
If one atom has a dipole moment $\mathbf{p_1}$, it creates an electric field

$$ \mathbf{E} = \frac{\mathbf{p_1}}{4\pi \varepsilon_0 r^3} $$

at the position of the other atom.
The other atom then develops a dipole moment $\mathbf{p_2} = \chi \mathbf{E}$ with $\chi$ the *polarizability* of the atom.

The potential energy between between the two dipoles is
$$
\begin{align}
U(r) &= \frac{-|\mathbf{p_1}||\mathbf{p_2}|}{4\pi\varepsilon_0 r^3}\\
&= \frac{-|\mathbf{p_1}| \chi \mathbf{E}}{4\pi\varepsilon_0 r^3}\\
&= \frac{-|\mathbf{p_1}|^2 \chi}{(4\pi\varepsilon_0 r^3)^2}\\
&\propto \frac{1}{r^6}.
\end{align}
$$

The dipole attraction is much weaker than the covalent bonds but drops slower with increasing distance.

??? question "How does the strength of a covalent bond scale with distance?"

    The strength of the bond is determined by the interatomic hopping integral $-t = \langle 1 | H | 2 \rangle$. Since the wavefunction of a bound electron typically decays exponentially, so does the overlap integral.

Although the Van der Waals force is weak, it is the only force when there are no chemically active electrons or when the atoms are too far apart to form covalent bonds.
Therefore, there are materials where Van der Waals interactions are the dominant interactions.
An example of such a material is graphite.
The Van der Waals bonds in graphite hold layers of covalently bonded carbon atoms together:

![Graphite atomic layers](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Graphite-layers-side-3D-balls.png/320px-Graphite-layers-side-3D-balls.png)  
(image source: [Wikipedia](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Graphite-layers-side-3D-balls.png/320px-Graphite-layers-side-3D-balls.png))




## Looking ahead: multiple atoms
So far we have only considered the interatomic interactions between diatomic systems.
However, our aim is to understand electrons and phonons in solids containing $N\to\infty$ atoms.

Let us see what happens when we consider more than two atoms.

### Phonons
In order to understand phonons better, we need to understand how a vibrational motion in a solid arises.
To that end, we model an array of atoms that are connected by springs with a spring constant $\kappa$.
Our plan:

* Consider only a *harmonic potential* acting between the atoms ($\kappa$ is constant)
* Write down equations of motion
* Compute normal modes

<!-- ![](figures/phonons2.svg) -->
For simplicity we consider 1D motion, and let us start with a chain of 3 atoms:
```python

# Defining constants
y_max = 6
max_m = 3

# Off set for the new masses
deviation_arr = [+2, -2, -3.5]

def plot_spring(x1, x2, y, annotation  = r'$\kappa$'):
    L = (x2-x1)

    width, nturns = 1, 10
    N = 1000
    pad = 200

    # Make the spring, unit scale (0 to 1)
    x_spring = np.linspace(0, L, N) # distance along the spring
    y_spring= np.zeros(N)
    y_spring[pad:-pad] = width * np.sin(2*np.pi * nturns * x_spring[pad:-pad]/L)

    x_plot, y_plot = np.vstack((x_spring, y_spring))

    # And offset it
    x_plot += x1
    y_plot += y
    ax.plot(x_plot, y_plot, c='k')
    ax.annotate(annotation, ((x2+x1)/2,y+2), fontsize = 40)


def plot_mass(x,y, annotation = r'$m$'):
    mass = Circle((x, y), .5, fc='k')
    ax.add_patch(mass)
    ax.annotate(annotation, (x-.5,y+2), fontsize = 30)


def make_plot(u, deviation_arr, max_masses = 3):   
    # plotting initial masses
    plot_mass(0,0)
    plot_mass(0+deviation_arr[0],u, annotation = '')

    # Plot initial dotted lines
    pyplot.plot((0,0), (0,u-2.5), 'k--')
    pyplot.plot((deviation_arr[0], deviation_arr[0]), (u, u-2.5), 'k--')
#     pyplot.plot((0, deviation_arr[0]), (u-2.5, u-2.5), 'k--')
    pyplot.arrow(0, u-2.5, deviation_arr[0]-.5, 0, fc="k", ec="k", head_width=.25, head_length=.5)

    # Annotate the deviations
    annot_arr = [r'$u_1$', r'$u_2$', r'$u_3$']
    off_set = -1
    ax.annotate(annot_arr[0], (deviation_arr[0]/2+off_set+.4, u-3+off_set), fontsize = 30)

    # Annotate large arrow containing the interatomic distance
    pyplot.arrow( 0, u/3, 9, 0, fc="k", ec="k", head_width=.5, head_length=1)
    ax.annotate(r'$a$', (5, u/3+off_set), fontsize = 30)

    # Plotting other masses and springs
    for j in range(max_masses-1):
        # Equilibrium plot
        plot_spring(10*j,10*(j+1),0)
        plot_mass(10*(j+1), 0)

        # Plot containing deviations from it's equilibrium
        plot_spring(10*j+deviation_arr[j], 10*(j+1)+deviation_arr[j+1], u, annotation = '')
        plot_mass(10*(j+1)+deviation_arr[j+1], u, annotation = '')

        # Plot dotted lines
        pyplot.plot((10*(j+1), 10*(j+1)), (0,u-2.5), 'k--')
        pyplot.plot((10*(j+1)+deviation_arr[j+1], 10*(j+1)+deviation_arr[j+1]), (u, u-2.5), 'k--')
#         pyplot.plot((10*(j+1), 10*(j+1)+deviation_arr[j+1]), (u-2.5, u-2.5), 'k--')
        pyplot.arrow(10*(j+1), u-2.5, (deviation_arr[j+1]+.5), 0, fc="k", ec="k", head_width=.25, head_length=.5)

        # Annotations
        ax.annotate(annot_arr[j+1], (10*(j+1)+deviation_arr[j+1]/2+off_set+.4, u-3+off_set), fontsize = 30)

# Initializing figure
fig, ax = pyplot.subplots(figsize=(10,7))
pyplot.axis('off')
ax.set_xlim((-1,10*(max_m-1)+1))
ax.set_ylim((-y_max-4.5, y_max-2.5))

# Plottig system
make_plot(-y_max, deviation_arr, max_m);
fig.show()

```

Let us denote the deviation of atom $i$ from its equilibrium position by $u_i$.
Newton's equations of motion for this system are then given by

$$
\begin{aligned}
m \ddot{u}_1 &= - \kappa (u_1 - u_2) \\
m \ddot{u}_2 &= - \kappa (u_2 - u_1) - \kappa (u_2 - u_3) \\
m \ddot{u}_3 &= - \kappa (u_3 - u_2).
\end{aligned},
$$

We write this system of equations in matrix form

$$
m \ddot{\mathbf{u}} = -\kappa
\begin{pmatrix}
1 & -1 & 0\\
-1 & 2 & -1\\
0 & -1 & 1
\end{pmatrix}\mathbf{u}
$$

We are interested in phonons, patterns of motion that are periodic and have a fixed frequency $\omega$.
Hence we guess that the motion of the atoms is

$$
\mathbf{u}(t) = \mathbf{u}_0 e^{i\omega t}.
$$

We substitute our guess into the equations of motion to yield an eigenvalue problem:

$$
\omega^2 \mathbf{u}_0 = \frac{\kappa}{m}
\begin{pmatrix}
1 & -1 & 0\\
-1 & 2 & -1\\
0 & -1 & 1
\end{pmatrix}\mathbf{u}_0.
$$

The solutions to the eigenvalue problem are phonon modes.

### Electrons
We just looked at how a chain of atoms moves.
Let us now look at how the electrons of those atoms behave.
To that end, we consider a 3 atom chain without any motion.
<!--
Figure having 3 atoms with a hopping -t
-->
In order to understand how electrons behave, we use the LCAO model.
The LCAO model generalizes in a very simple way.
Let us consider the wavefunction:
$$
\vert \psi\rangle = \varphi_1 |1\rangle + \varphi_2 |2\rangle + \varphi_3 |3\rangle.
$$
Because the three atoms are identical, the onsite energy is the same on all atoms $\langle 1|H|1 \rangle = \langle2|H|2 \rangle = \langle3|H|3 \rangle = E_0$.
Furthermore, we assume hopping only between the nearest neighbors and assume that it is real valued: $\langle1|H|2\rangle = \langle2|H|3\rangle = -t$.
We also assume that the orbitals are orthogonal to eachother.
Just as we did in the previous lecture, we use the Schrödinger equation $H |\psi\rangle = E |\psi\rangle$ to set up a system of equations:

$$
\begin{align}
E \varphi_1 &= E_0 \varphi_1 - t \varphi_2\\
E \varphi_2 &= E_0 \varphi_2 - t \varphi_1 - t \varphi_3\\
E \varphi_3 &= E_0 \varphi_3 -t \varphi_2.
\end{align}
$$

Again, we write this in a matrix form:

$$
E \begin{pmatrix}
\varphi_1 \\ \varphi_2 \\ \varphi_3
\end{pmatrix} =
\begin{pmatrix}
E_0 & -t & 0 \\
-t & E_0 & -t \\
0 & -t & E_0
\end{pmatrix}
\begin{pmatrix}
\varphi_1 \\ \varphi_2 \\ \varphi_3.
\end{pmatrix}
$$

### Numerical test

Diagonalizing large matrices is unwieldy, but let's try and check it numerically to see if we notice a trend.
Let us first model 3 atoms on a chain.

The eigenfrequencies of the 3 atoms are: `[0.0 1.0 1.732050]`

```python
def DOS_finite_phonon_chain(n):
    rhs = 2 * np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)
    rhs[0, 0] -= 1
    rhs[-1, -1] -= 1
    pyplot.figure()
    pyplot.hist(np.sqrt(np.abs(np.linalg.eigvalsh(rhs))), bins=30)
    pyplot.xlabel("$\omega$")
    pyplot.ylabel("Number of eigenfrequencies")

DOS_finite_phonon_chain(3)
```

The eigenenergies of the 3 orbitals are: `[-1.41421356 0.0  1.41421356]`

```python
def DOS_finite_electron_chain(n):
    rhs = 2 * np.eye(n, k = 0) - np.eye(n, k = 1) - np.eye(n, k = -1)
    pyplot.figure()
    pyplot.hist(np.linalg.eigvalsh(rhs), bins=30)
    pyplot.xlabel("$E$")
    pyplot.ylabel("Number of eigenenergies")

DOS_finite_electron_chain(3)
```
However, 3 atoms are far too few to model an actual solid.
Hence, we need 'many more' atoms.

### From 3 atoms to 300

Phonon modes of the many atom chain are shown below.

```python
DOS_finite_phonon_chain(300)
```
We observe that when $\omega$ is small, we have a constant DOS.
This is in line with what we saw in the Debye model.
There the DOS of a 1D system was constant!
However, when the frequencies are higher, the DOS is not constant anymore.

A plot of electron energies in the many atom chain is shown below.

```python
DOS_finite_electron_chain(300)
```
The numerical results once again agree with the models we developed earlier.
In the Sommerfeld free electron model, the DOS in 1D is proportional to $\frac{1}{\sqrt{E}}$.
The above histogram also reflects this proportionality for small energies $E$.
However, when $E$ is higher, we observe a significant deviation from the $\frac{1}{\sqrt{E}}$ behavior.

In both cases, we find that our models agree with the numerical results whenever frequencies/energies are small.
When the frequencies/energies are high, we find that there is a significant deviation from the Debye/Sommerfeld models.
The nature of this deviation is the subject of the next lecture!

---

## Conclusions

  * The DOS of phonons used in the Debye model is justified by modeling the atoms as particles on a chain connected by a spring in the small $\omega$ limit.
  * The DOS of electrons in the Sommerfeld model is justified by modeling electrons as particles that can hop between atoms in the small $E$ limit.

## Exercises
### Preliminary provocations

  1. What does the LCAO matrix in the lecture notes look like if we also consider a next nearest-neighbour hopping $-\tilde{t}$?
  2. What does the LCAO matrix look like if we consider six atoms instead of three? You may assume that each atom has a single orbital, onsite energy $E_0$ and the hopping between neighbouring atoms $-t$.
  3. How do you determine which part of the interatomic potential is attractive and which is repulsive? You may assume that the interatomic potential is only a function of the interatomic distance $r$.

### Exercise 1: Linear triatomic molecule

  Consider carbon dioxide (C0$_2$) which is a linear triatomic molecule shown below

  <img src="https://upload.wikimedia.org/wikipedia/commons/a/af/Carbon-dioxide-3D-vdW.svg" width="50%" alt="carbon dioxide"></img>

  ??? info "source"

      By Jasek FH. - Own work, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/3.0 "Creative Commons Attribution-Share Alike 3.0"), [Link](https://commons.wikimedia.org/w/index.php?curid=2875238)


  1. How many normal modes does this molecule have assuming motion in only 1D?
  How many normal modes does it have if the atoms can move in all three dimensions?
  2. For simplicity, we only consider 1D motion of the atoms.
  Write down Newton's equations of motion for the atoms, you may assume that the spring constant is the same for both bonds.
  3. Consider a *symmetric* mode, for which the displacements of the oxygen atoms are equal in magnitude and have an opposite direction. Find the eigenfrequency of this mode.
  4. Now consider the antisymmetric mode when both of the oxygen atoms move in phase and have the same displacement.
  Find the ratio between the displacements of the carbon and oxygen atoms. Make sure that the center of mass of the molecule is at rest.
  5. Compute the eigenfrequency of the antisymmetric mode.

??? hint

    Compare your answers with [Wikipedia](https://en.wikipedia.org/wiki/Triatomic_molecule).


---


From Diatomic solids

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

---

## Conclusions

---

## Exercises

### Preliminary provocations

--8<-- "includes/abbreviations.md"
