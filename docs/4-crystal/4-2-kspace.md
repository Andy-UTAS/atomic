# The tight binding model

Learn the _reciprocal_ secrets of crystals[^1].

## Introduction

![](images/4-2-kspaceheader.jpg)

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

_based on chapters 13.1-13.2 & 14.1-14.2 of the book_  

!!! success "Expected prior knowledge"

    Before the start of this lecture, you should be able to:

    - describe crystal structures using crystallographic terminology (lattice, basis, unit cells, etc. as introduced in the previous lecture)
    - recall that waves will interfere constructively or destructively depending on their relative phase
    - describe the basic concepts of the reciprocal space

!!! summary "Learning goals"

    After this lecture you will be able to:

    - Define the reciprocal space, and explain its relevance
    - Construct a reciprocal lattice from a given real space lattice
    - Compute the intensity of X-ray diffraction of a given crystal
    - Interpret X-ray powder diffraction data

??? info "Lecture video"

    <iframe width="100%" height="315" src="https://www.youtube-nocookie.com/embed/0l8Z0p07YeM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


In the last lecture, we learned crystallographic terminology in order to describe crystal structures.
Now our goal is twofold, we will:
- Study what consequences does a lattice have in reciprocal space (with the goal of considering dispersion relations)
- Consider how to probe crystal structure using X-ray diffraction experiments.

## Reciprocal lattice motivation 1D case
In [lecture 7](7_tight_binding.md) we discussed the reciprocal space of a simple 1D lattice.
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

```python
# Define primitive lattice vectors
a1 = np.array([1,0])
a2 = np.array([0.5,sqrt(3)/2])
# Compute reciprocal lattice vectors
b1,b2 = np.linalg.inv(np.array([a1,a2]).T) @ np.eye(2)*2*pi

fig = make_subplots(rows=1, cols=2,shared_yaxes=True,subplot_titles=('Real Space', 'Reciprocal Space'))

# Generates the lattice given the lattice vectors
def lattice_generation(a1,a2,N):
    grid = np.arange(-N//2,N//2,1)
    xGrid, yGrid = np.meshgrid(grid,grid)
    return np.reshape(np.kron(xGrid.flatten(),a1),(-1,2))+np.reshape(np.kron(yGrid.flatten(),a2),(-1,2))


def subplot(a1,a2,col):
    N = 6
    lat_points = lattice_generation(a1,a2,N)
    line_a1 = np.transpose([[0,0],a1])
    line_a2 = np.transpose([[0,0],a2])
    dotLine_a1 = np.transpose([a1,a1+a2])
    dotLine_a2 = np.transpose([a2,a1+a2])


    fig.add_trace(
        go.Scatter(visible=False, x=line_a1[0],y=line_a1[1],mode='lines',line_color='red'
        ), row = 1, col = col
    )
    fig.add_trace(
        go.Scatter(visible=False, x=line_a2[0],y=line_a2[1], mode='lines',line_color='red'
        ), row = 1, col = col
    )
    fig.add_trace(
        go.Scatter(visible=False, x=dotLine_a1[0],y=dotLine_a1[1],mode='lines',line_color='red',line_dash='dot'
        ), row = 1, col = col
    )
    fig.add_trace(
        go.Scatter(visible=False, x=dotLine_a2[0],y=dotLine_a2[1],mode='lines',line_color='red',line_dash='dot'
        ), row = 1, col = col
    )

    fig.add_trace(
        go.Scatter(visible=False, x=lat_points.T[0],y=lat_points.T[1],mode='markers',marker=dict(
            color='Black',
            size = 10
            )
        ), row = 1, col = col
    )

# Generate subplots to be used by the slider
N_values = 10
for i in np.linspace(2.5,3.5,N_values):
    subplot(a1*i,a2*i,1)
    subplot(b1/i,b2/i,2)

# Define the default subplot
active = 4
for i in range(10):   
    fig.data[active*10+i].visible = True

steps = []
for i in range(N_values):
    step = dict(
        label = 'Lattice Constant',
        method="restyle",
        args=["visible", [False] * len(fig.data)],
    )
    for j in range(10):
        step["args"][1][i*10+j] = True  # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [dict(
    tickcolor = 'White',
    font_color = 'White',
    currentvalue_font_color = 'Black',
    active = active,
    name = 'Lattice Constant',
    steps = steps
)]

# Annotating lattice vectors
def text_dict(text,pos,ref=('x1','y1')):
    dic = {
            'x' : pos[0],
            'y' : pos[1],
            'xref' : ref[0],
            'ayref' : ref[1],
            'text' : text,
            'font' : {
                'size' : 15,
                'color' : 'black'
            },
            'showarrow' : False
    }
    return dic
annotations = [a.to_plotly_json() for a in fig["layout"]["annotations"]]
annotations.append(text_dict('$\mathbf{a}_1$',(1.5,-0.5)))
annotations.append(text_dict('$\mathbf{a}_2$',(0,1.3)))
annotations.append(text_dict('$\mathbf{b}_1$',(0.8,-1),('x2','y2')))
annotations.append(text_dict('$\mathbf{b}_2$',(-0.6,1.2),('x2','y2')))
fig["layout"]["annotations"] = annotations


plot_range = 5
fig.update_layout(
    sliders=sliders,
    showlegend = False,
    plot_bgcolor = 'rgb(254, 254, 254)',
    width = 800,
    height = 400,
    xaxis = dict(
        range=[-plot_range,plot_range],
        visible = False,
        showgrid = False,
    ),
    yaxis = dict(
      range = [-plot_range,plot_range],
      visible = False,
      showgrid = False,
    )
)
fig.update_xaxes(range=[-plot_range, plot_range], row=1, col=2, visible=False)
fig.update_yaxes(row=1, col=2, scaleanchor="x", scaleratio=1)
fig.update_yaxes(row=1, col=1, scaleanchor="x", scaleratio=1)
fig.show()

```

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

![](figures/brillouin_mod.svg)

## Diffraction

### Reciprocal lattice: Laue conditions

Reciprocal lattice manifests directly in the diffraction experiments.
A diffraction experiment uses the crystal as a target and scatters high energy particles (X-rays, neutrons, or electrons) off of it.
As a result of interference between mutiple waves, the scattered radiation reveals the reciprocal lattice of the crystal.
In order to find the relationship between the incoming wave and the scattered one, let us consider a lattice of atoms separated by a lattice vector $\mathbf{R}$.
An incoming wave with wave vector $\mathbf{k}$ is incident upon the lattice.
After scattering, the outgoing wave's wave vector is $\mathbf{k'}$.
We assume that the atomic scattering is elastic (does not cause an energy loss), such that $|\mathbf{k'}|=|\mathbf{k}|$.
Below we present a simple sketch of two different atoms scattering an incoming wave.

![](figures/scattering.svg)

Observe that the bottom ray travels a larger distance compared to the upper ray.
The difference in distance results in a relative phase shift between the rays $\Delta \phi$.
With a bit of geometry, we find that the extra distance traveled by the lower ray relative to the upper one is

$$
x_{\mathrm{extra}} = \Delta x_1+\Delta x_2 = \cos(\theta) \lvert R \rvert + \cos(\theta') \lvert R \rvert.
$$

As a result of the travel distance, the phase difference is:

$$
\begin{align}
\Delta \phi &= \lvert\mathbf{k} \rvert(\Delta x_1+\Delta x_2)\\
&= \lvert\mathbf{k}\rvert \lvert\mathbf{R}\rvert(\cos(\theta)+\cos(\theta'))\\
&= \mathbf{k'}\cdot \mathbf{R} - \mathbf{k}\cdot \mathbf{R} = (\mathbf{k'} - \mathbf{k}) \cdot \mathbf{R}.
\end{align}
$$

However, that is only a phase difference between waves scattered off of two atoms.
To find the outgoing wave's amplitude, we must sum over scattered waves from each and every atom in the lattice:

$$
A\propto\sum_\mathbf{R}\mathrm{e}^{i\left(\Delta \phi-\omega t\right)} = \sum_\mathbf{R}\mathrm{e}^{i\left((\mathbf{k'}-\mathbf{k})\cdot\mathbf{R}-\omega t\right)}.
$$

The above sum is non-zero if and only if the scattered waves interfere constructively i.e. the phase difference equals $2\pi n$, where $n$ is an integer.
Furthermore, we know that real and reciprocal lattice vectors are related by $\mathbf{G} \cdot \mathbf{R} = 2 \pi n$.
Therefore, we conclude that the difference between incoming and outgoing waves must be:

$$
\mathbf{k'}-\mathbf{k}=\mathbf{G}.
$$

In other words, if the difference of the wavevector between the incoming and outgoing wave vectors coïncides with a reciprocal lattice point, we expect constructive interference.
This requirement is known as the _Laue condition_.
As a result, the interference pattern produced in diffraction experiments is a direct measurement of the reciprocal lattice!

### Structure factor
Above we assumed that the unit cell contains only a single atom.
What if the basis contains more atoms though?
In the figure below we show a simple lattice which contains multiple atoms in the unit cell.
Note, the unit cell does not have to be primitive!

![](figures/laue_mod.svg)

Let $\mathbf{R}$ be the lattice and let $\mathbf{R}+\mathbf{r}_j$ be the location of the atoms in the unit cell.
The distance $\mathbf{r}_j$ is taken with respect to lattice point from which we construct the unit cell.
Similar to before, we calculate the amplitude of the scattered wave.
However, now there are multiple atoms in the unit cell and each of these atoms acquires a phase shift of its own.
In order to keep track of the atoms, we define $\mathbf{r}_j$ to be the location of atom $j$ in the unit cell.
The distance $\mathbf{r}_j$ is defined with respect to the lattice point from which we construct the unit cell.
In order to calculate the amplitude of the scattered wave, we must sum not only over all the lattice points but also over the atoms in a single unit cell:

$$
\begin{align}
A &\propto \sum_\mathbf{R} \sum_j f_j \mathrm{e}^{i\left(\mathbf{G}\cdot(\mathbf{R}+\mathbf{r}_j)-\omega t\right)}\\
&= \sum_\mathbf{R}\mathrm{e}^{i\left(\mathbf{G}\cdot\mathbf{R}-\omega t\right)}\sum_j f_j\ \mathrm{e}^{i\mathbf{G}\cdot\mathbf{r}_j}
\end{align}
$$

where $f_j$ is the scattering amplitude off of a single atom, and it is called the *form factor*.
The form factor mainly depends on the chemical element, nature of the scattered wave, and finer details like the electrical environment of the atom.
The first part of the equation above is the familiar Laue condition, and it requires that the scattered wave satisfies the Laue condition.
The second part gives the amplitude of the scattered wave, and it is called the **structure factor**:

$$
S(\mathbf{G})=\sum_j f_j\ \mathrm{e}^{i\mathbf{G}\cdot\mathbf{r}_j}.
$$    

In diffraction experiments, the intensity of the scattered wave is $I \propto A^2$
Therefore, the intensity of a scattered wave depends on the structure factor $I \propto S(\mathbf{G})^2$.
Because the structure factor depends on the form factors and the positions of the basis atoms, by studying the visibility of different diffraction peaks we may learn the locations of atoms within the unit cell.

### Non-primitive unit cell

Laue conditions allow scattering as long as the scattering wave vector is a reciprocal lattice vector.
However if we consider a non-primitive unit cell of the direct lattice, the reciprocal lattice contains more lattice points, seemingly leading to additional interference peaks.
Computing the structure factor allows us to resolve this apparent contradiction.

??? Question "Calculate the structure factor in which there is a single atom the unit cell located at the lattice point. Do any diffraction peaks dissapear?"
    $\mathbf{r}_1=(0,0,0)\rightarrow S=f_1$.
    In this case, each reciprocal lattice point gives one interference peak, none of which are absent.


As a demonstration of how it happens, let us compute the structure factor of the FCC lattice using the conventional unit cell in the real space.

![](figures/fcc_mod.svg)

The basis of the conventional FCC unit cell contains four identical atoms.
With respect to the reference lattice point, these attoms are located at

$$
\begin{aligned}
\mathbf{r}_1&=(0,0,0)\\
\mathbf{r}_2&=\frac{1}{2}(\mathbf{a}_1+\mathbf{a}_2)\\
\mathbf{r}_3&=\frac{1}{2}(\mathbf{a}_2+\mathbf{a}_3)\\
\mathbf{r}_4&=\frac{1}{2}(\mathbf{a}_3+\mathbf{a}_1),
\end{aligned}
$$
with $f_1=f_2=f_3=f_4\equiv f$. Let the reciprocal lattice be described by $\mathbf{G}=h\mathbf{b}_1+k\mathbf{b}_2+l\mathbf{b}_3$, where $h$, $k$ and $l$ are integers. Using the basis described above and the reciprocal lattice, we calculate the structure factor:

$$
\begin{aligned}
S&=f\left(\mathrm{e}^{i\mathbf{G}\cdot\mathbf{r}_1}+\mathrm{e}^{i\mathbf{G}\cdot\mathbf{r}_2}+\mathrm{e}^{i\mathbf{G}\cdot\mathbf{r}_3}+\mathrm{e}^{i\mathbf{G}\cdot\mathbf{r}_4}\right)\\
&=f\left(1+\mathrm{e}^{i(h\mathbf{b}_1\cdot\mathbf{a}_1+k\mathbf{b}_2\cdot\mathbf{a}_2)/2}+\mathrm{e}^{i(k\mathbf{b}_2\cdot\mathbf{a}_2+l\mathbf{b}_3\cdot\mathbf{a}_3)/2}+\mathrm{e}^{i(h\mathbf{b}_1\cdot\mathbf{a}_1+l\mathbf{b}_3\cdot\mathbf{a}_3)/2}\right)\\
&=f\left(1+\mathrm{e}^{i\pi(h+k)}+\mathrm{e}^{i\pi(k+l)}+\mathrm{e}^{i\pi(h+l)}\right).
\end{aligned}
$$
Because $h$, $k$ and $l$ are integers, all exponents are either $+1$ or $-1$, and the interference is only present if

$$
S =
\begin{cases}
    4f, \: \mathrm{if} \: h, \: k, \: \mathrm{and} \: l \: \mathrm{are \: all \: even \: or \: odd,}\\
    0, \: \mathrm{in \: all \: other \: cases}.
\end{cases}
$$
We now see that the reciprocal lattice points with nonzero amplitude exactly form the reciprocal lattice of the FCC lattice.

### Powder Diffraction
The easiest way to do diffraction measurements is to take a crystal, shoot an X-ray beam through it and measure the direction of outgoing waves.
However growing a single crystal may be hard because many materials are polycrystalline

A simple alternative is to perform **powder diffraction**.
By crushing the crystal into a powder, the small crystallites are now orientated in random directions.
This improves the chances of fulfilling the Laue condition for a fixed direction incoming beam.
The experiment is illustrated in the figure above.
The result is that the diffracted beam exits the sample via concentric circles at discrete **deflection angles** $2 \theta$.

```python
def add_patch(ax, patches, *args,**kwargs):
    for i in patches:
        ax.add_patch(i,*args,**kwargs)

def circle(radius,xy=(0,0),**kwargs):
    return patches.Circle(xy,radius=radius, fill=False, edgecolor='r', lw = 2, **kwargs)

fig, ax = plt.subplots(figsize=(7,7))

transform=mtransforms.Affine2D().skew_deg(0,-25) + ax.transData
# Create the screen
rect = patches.Rectangle((-0.5,-0.5),1,1, edgecolor = 'k', lw = 2, facecolor = np.array([217, 217, 217])/255,transform = transform)
circle_list = [circle(i,transform=transform) for i in np.array([0.001,0.02,0.08,0.15,0.2,0.22,0.25])*2]
add_patch(ax,[rect]+circle_list)

# Add sample
sample_pos = np.array([-0.6,-0.6])
ax.add_patch(patches.Circle(sample_pos,radius=0.1,color='k',zorder=10))
plt.annotate('Powder Sample',sample_pos+[-0.1,-0.2],fontsize=14)
#Reference line
ax.plot([sample_pos[0],0],[sample_pos[1],0],color='k',ls='--')

#X-Ray Beam
d_xray = sample_pos-np.array([-1+0.05,-1+0.05])
ax.add_patch(patches.Arrow(-1,-1, *d_xray, width=0.05, color='r'))
plt.annotate('X-Ray Beam',(-1,-0.85),fontsize=14,rotation = 45)

# Diffracted Beams
ax.add_patch(patches.Arrow(*sample_pos, 0.1, 0.8, width=0.05, color='r'))
ax.add_patch(patches.Arrow(*sample_pos, 0.8, 0.285, width=0.05, color='r'))

#Angle Arcs
ellipse_radius = 0.3
ax.add_patch(patches.Arc(sample_pos, ellipse_radius, ellipse_radius, 80, theta1=325, theta2=0))
plt.annotate('$ 2\\theta $',(-0.56,-0.44),fontsize=14)


plt.xlim([-1,0.5])
plt.ylim([-1,0.5])
plt.axis('off')
plt.show()
```


In order to deduce the values of $\theta$ of a specific crystal, let us put the Laue condition into a more practical form.
We first take the modulus squared of both sides:

$$
\left|\mathbf{G}\right|^2 = \left|\mathbf{k'}-\mathbf{k} \right|^2 \\
G^2 =  2k^2-2\mathbf{k'} \cdot \mathbf{k},
$$

where we used $|\mathbf{k'}| = |\mathbf{k}|$.
We then substitute the Laue condition $\mathbf{k'} = \mathbf{k}+\mathbf{G}$:

$$
\begin{align}
\lvert \mathbf{G} \rvert ^2 &= 2k^2-2 \left(\mathbf{k}+\mathbf{G}\right) \cdot \mathbf{k} \\
&= -2 \mathbf{G} \cdot \mathbf{k}.
\end{align}
$$

Using $\mathbf{k} \cdot \mathbf{G} = \lvert \mathbf{k} \rvert \lvert \mathbf{G} \rvert \cos(\phi)$,  we obtain

$$
\left| \mathbf{G} \right| = -2 \lvert \mathbf{k} \rvert \cos (\phi).
$$

Note, $\phi$ is the angle between the vector $\mathbf{k}$ and $\mathbf{G}$, which is not the same as the angle between the incoming and scattered waves $\theta$.
We are nearly there, but we are left with finding out the relation between $\phi$ and $\theta$.

Recall the concept of Miller planes.
These are sets of planes identified by their Miller indices $(h,k,l)$ which intersect the lattice vectors at $\mathbf{a}_1 / h$, $\mathbf{a}_22 / k$ and $\mathbf{a}_3 / l$.
It turns out that Miller planes are normal to the reciprocal lattice vector $\mathbf{G} = h \mathbf{b}_1 + k \mathbf{b}_2 + l \mathbf{b}_3$ and the distance between subsequent Miller planes is $d_{hkl} = 2 \pi/\lvert \mathbf{G} \rvert$ (you will derive this in [today's exercise](https://solidstate.quantumtinkerer.tudelft.nl/10_xray/#exercise-2-miller-planes-and-reciprocal-lattice-vectors)).
Substituting the expression for $\lvert \mathbf{G} \rvert$ into the expression for the distance between Miller planes we get:

$$
d_{hkl} \cos (\phi) = -\frac{\pi}{\lvert \mathbf{k} \rvert}.
$$

We know that $\lvert \mathbf{k} \rvert$ is related to the wavelength by $\lvert \mathbf{k} \rvert = 2\pi/\lambda$.
Therefore, we can write the equation above as

$$
2 d_{hkl} \cos (\phi) = -\lambda.
$$

Lastly, we express the equation in terms of the deflection angle through the relation $\phi = \theta + \pi/2$.
With this, one can finally derive **Bragg's Law**:

$$
\lambda = 2 d_{hkl} \sin(\theta)
$$

Bragg's law allows us to obtain atomic distances in the crystal $d_{hkl}$ through powder diffraction experiments!


### Miller planes
When fabricating crystals it is important to know both the orientation and the surface of the crystal.
Different cuts of a crystal lead to different surfaces.
In the chemical industry, this is especially significant because different surfaces lead to different chemical properties and thus is one of the foundations of research in catalysts.
Therefore, we seek a way to describe different planes of a crystal within our developed framework.
This leads us to a very important concept - **Miller planes**.
To explain Miller planes, let's start off with a simple cubic lattice:

![](figures/cubic_mod.svg)

Where $|{\bf a}_1|=|{\bf a}_2|=|{\bf a}_3|\equiv a$.

We can cut multiple planes through the cubic lattice.
Miller planes describe such planes with a set of indices.
The plane designated by Miller indices $(u,v,w)$ intersects lattice vector ${\bf a}_1$ at $\frac{|{\bf a}_1|}{u}$, ${\bf a}_2$ at $\frac{|{\bf a}_2|}{v}$ and ${\bf a}_3$ at $\frac{|{\bf a}_3|}{w}$.

![](figures/miller.svg)

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
2. Why is the amplitude of a scattered wave zero if $\mathbf{k'}-\mathbf{k} \neq \mathbf{G}$?
3. Suppose we have a unit cell with a single atom in it.
Can any intensity peaks dissapear as a result of the structure factor?
4. Can increasing the unit cell in real space introduce new diffraction peaks due to reciprocal lattice having more points?

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

### Exercise 3: X-ray scattering in 2D

*(adapted from ex 14.1 and ex 14.3 of "The Oxford Solid State Basics" by S.Simon)*

Consider a two-dimensional crystal with a rectangular lattice and lattice vectors $\mathbf{a}_1 = (0.468, 0)$ nm and $\mathbf{a}_2 = (0, 0.342)$ nm (so that $\mathbf{a}_1$ points along $x$-axis and $\mathbf{a}_2$ points along $y$-axis).

1. Sketch the reciprocal lattice of this crystal.
2. Consider an X-ray diffraction experiment performed on this crystal using monochromatic X-rays with wavelength $0.166$ nm. By assuming elastic scattering, find the magnitude of the wave vectors of the incident and reflected X-ray beams.
3. On the reciprocal lattice sketched in 3.1, draw the "scattering triangle" corresponding to the diffraction from (210) planes. To do that use the Laue condition $\Delta \mathbf{k} = \mathbf{G}$ for the constructive interference of diffracted beams.

### Exercise 4: Structure factors and powder diffraction

1. Compute the structure factor $\mathbf{S}$ of the BCC lattice.
2. Which diffraction peaks are missing?
3. How does this structure factor change if the atoms in the center of the conventional unit cell have a different form factor from the atoms at the corner of the conventional unit cell?
4. A student carried out X-ray powder diffraction on Chromium (Cr) which is known to have a BCC structure. The first five diffraction peaks are given below. Furthermore, the student took the liberty of assigning Miller indices to the peaks. Were the peaks assigned correctly? Fix any mistakes and explain your reasoning.
![](figures/cr_xray_exercise.svg)
5. Calculate the lattice constant, $a$, of the chromium bcc unit cell. Note that X-ray diffraction was carried out using Cu K-$\alpha$ ($1.5406 \unicode{xC5}$) radiation.

### Exercise 3: Directions and Spacings of Miller planes
*(adapted from ex 13.3 of "The Oxford Solid State Basics" by S.Simon)*

1. Explain what is meant by the terms Miller planes and Miller indices.
2. Consider a cubic crystal with one atom in the basis and a set of orthogonal primitive lattice vectors $a\hat{x}$, $a\hat{y}$ and $a\hat{z}$. Show that the direction $[hkl]$ in this crystal is normal to the planes with Miller indices $(hkl)$.
3. Show that this is not true in general. Consider for instance an orthorhombic crystal, for which the primitive lattice vectors are still orthogonal but have different lengths.
4. Any set of Miller indices corresponds to a family of planes separated by a distance $d$. Show that the spacing $d$ of the $(hkl)$ set of planes in a cubic crystal with lattice parameter $a$ is $d = \frac{a}{\sqrt{h^2 + k^2 + l^2}}$.

    ??? hint

        Recall that a family of lattice planes is an infinite set of equally separated parallel planes which taken all together contain all points of the lattice.

        Try computing the distance between the plane that contains the site $(0,0,0)$ of the conventional unit cell and a plane defined by the $(hkl)$ indices.

[^1]: This is only funny if you noticed the [tagline of the previous section](../../4-crystal/4-1-realspace/#crystal-structure)
