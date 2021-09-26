# Doping


## Introduction

![]()

!!! danger  "Expected competencies"

    It is assumed that you have familiarity with the following concepts/techniques:

!!! note  "Text reference"
    The material covered here is discussed in section(s) $\S$ of [The Oxford Solid State Basics](https://global.oup.com/academic/product/the-oxford-solid-state-basics-9780199680771?cc=au&lang=en&)

!!! info "Computational content"

    The Jupyter notebook associated with this section can be accessed by clicking the icon below:
    [<i class="fab fa-python fa-5x"></i>](#){ .md-button .md-button--primary class="text-center" style="margin-left: 45%"}

---

In the previous lecture, we learned how to deal with partially filled bands.
The concept of electrons/holes established the foundations needed to understand semiconductors.
We saw that the filling in semiconductors can be controlled by tuning the temperature.
However, Fermi level control through temperature is still far too constrained and leads to equal electron and hole densities $n_e = n_h$.
The full utility of semiconductors is achieved through another Fermi level control method - **doping**.
In today's lecture, we will take a look at how doping allows the fine control of Fermi level and the practical applications that come with it.


## Adding an impurity to semiconductor

In order to understand doping, we need to remember some basic chemistry.
Most semiconductors are made up of group IV elements (Si, Ge) or binary compounds between group III-V elements (GaAs).
In both cases, there are 4 valance electrons per atom.
If we want to increase the average number of electrons per atom, we can add a group V element that has an extra valance electron.
We therefore refer to group V elements as **donor** impurities.
However, the extra donor electron is bound to the impurity because group V elements also have an extra proton.
In order to estimate the binding strength, we treat the lattice as a background and only consider the system of an electron bound to a proton.
We immediately recognize this system as a Hydrogen model with energy levels
$$
E_n = - \frac{m_e e^4}{8\pi^2\hbar^3\varepsilon^2_0n^2} = -R_E /n^2= -\frac{13.6\text{eV}}{n^2}.
$$
The spatial extent of the bound state is given by the Bohr radius:
$$
r_B = 4 \pi \varepsilon_0 \hbar^2/m_{\mathrm{e}} e^2.
$$
However, we have to remember that the above equations are written in the free space background.
In our case, the extra electron moves in the semiconductor's conduction band and not free space.
Therefore, there are a couple of differences from the Hydrogen model.
One difference is that the electron's mass is conduction band's effective mass.
Another difference is that the interactions between the electron and proton are screened by the lattice.
As a result, we need to introduce the following substitutions: $m_e \to m_e^*$, $\epsilon_0 \to \epsilon\epsilon_0$.
We thus estimate the energy of the bound state created by the impurity:
$$E = -\frac{m_e^*}{m_e \varepsilon^2} R_E = -0.01 \text{eV (in Ge)},$$
with Bohr radius $r_B = 4$ nm (vs $r_B = 0.5$ Å in Hydrogen).
The electron is very weakly bound to the impurity!
At room temperature (0.026 eV), the donor electron is easily thermally excited into the conduction band.

On the other hand, we can add a group III element to reduce the average number of electrons in the system.
Group III elements lacks 1 electron and 1 proton and are therefore known as **acceptors**.
We treat the absence of an electron as a hole and the lacking proton as an effective negative charge.
As a result, we once again end up with a Hydrogen model, except this time the charges are flipped (hole circles around a negative center).
That allows us to use the previous results and to conclude that an acceptor creates a weakly bound state above the valance band.

### Density of states with donors and acceptors

```python
E = np.linspace(-3, 3, 1000)
fig, ax = pyplot.subplots()

n_F = 1/(np.exp(2*(E - E_F)) + 1)
g_e = m_e * sqrt_plus(E - E_C)
g_h = m_h * sqrt_plus(E_V - E)
ax.plot(E, g_h, label="$g_h$")
ax.plot(E, g_e, label="$g_e$")

sigma = 0.01
g_D = np.exp(-(E_D - E)**2 / sigma**2)
g_A = .7 * np.exp(-(E_A - E)**2 / sigma**2)
ax.plot(E, g_D, label='$g_D$')
ax.plot(E, g_A, label='$g_A$')
ax.legend()
ax.set_xticks([E_V, E_C, E_A, E_D])
ax.set_xticklabels(['$E_V$', '$E_C$', '$E_A$', '$E_D$'])
ax.set_ylabel('$g$')
ax.set_xlabel('$E$')
draw_classic_axes(ax, xlabeloffset=.2)
```

In order to model **multiple** donor/acceptor states, we assume that they are all degenerate at the binding energy.
Therefore, we model the density of states of donors/acceptors as a Dirac delta function:
$$
g_D(E) = N_D \delta(E- E_D), \quad  g_A(E) = N_A \delta(E-E_A),
$$
where $N_D$ and $N_A$ are donor and acceptor concentrations respectively.
The binding energies of the donor and acceptor are defined as $E_A$ and $E_D$.

How good is this Dirac delta approximation?
That depends on the concentrations.
If we keep on adding impurities, then at some point the weakly bound states will begin to overlap.
The overlap will create an effective tight-binding model that leads to a formation of an "impurity" band which breaks our approximation.
We must therefore prevent the overlap of impurity bound states.
From the previous section, we know that the extent of the bound state is roughly 4 nm and thus the distance between impurity atoms cannot exceed that.
As a result, the impurity concentration is bounded to $N_D \lesssim (1/4\textrm{nm})^3$.

## Number of carriers

| Symbol | Meaning |
| - | - |
| $n_e$ | Concentration of electrons in the conduction band |
| $n_h$ | Concentration of holes in the valance band |
| $n_D$ | Concentration of electrons in the donor bound state|
| $n_A$ | Concentration of holes in the acceptor bound state|
| $N_D$ | Concentration of donor impurities|
| $N_A$ | Concentration of acceptor impurities|

We now have the necessary tools to determine how the Fermi level changes with doping.
The algorithm to determine the Fermi level of a semiconductor was outlined in the previous lecture and we continue to use it here.
The process is the same up until the third step - charge conservation.
The semiconductor now contains impurities that become charged through ionization.
For example, if the donor impurity bound state loses an electron - it becomes positively charged.
We determine the electron/hole occupation of the donor/acceptor states by applying Fermi-Dirac statistics to their simple Dirac delta density of states:
$$
n_D = N_D \frac{1}{e^{(E_D-E_F)/kT} + 1}, n_A = N_A \frac{1}{e^{(E_F-E_A)/kT} + 1}.
$$
Here we refer to $n_D$($n_A$) as the electron(hole) concentration inside donor(acceptor) bound state.
With this, the charge balance equation reads:
$$n_e - n_h + n_D - n_A = N_D - N_A.$$
The equation is not an easy one to solve: all of the terms on the lhs depend non-trivially on $E_F$.
In order to solve it, we require several approximations:

* Firstly, we assume that the Fermi level is far from both bands $E_F−E_v \gg kT$ and $E_c−E_F \gg kT$. The approximation allows us to use the law of mass action from the previous lecture:
$$
n_e n_h = N_C N_V e^{-E_g/kT} \equiv n_i^2.
$$
* Secondly, we determined that electrons/holes are weakly bound to the impurities. Therefore, at ambient temperatures, we assume that all the impurities are fully ionized and therefore $n_D = n_A = 0$.

The approximations allow us to simplify the charge balance equation:
$$
n_e - n_i^2/n_e = N_D - N_A,
$$
which is just the quadratic equation for $n_e$.
When $|N_D-N_A| \gg n_i$ the semiconductor is **extrinsic**, so that if $N_D > N_A$ ($n$-doped semiconductor), $n_e \approx N_D -N_A$ and $n_h = n_i^2/(N_D-N_A)$.
If $N_D < N_A$ ($p$-doped semiconductor), $n_h \approx N_A -N_D$ and $n_e = n_i^2/(N_A-N_D)$.

We can now easily find the Fermi level.
From the first approximation, we know that the simplified relation between $n_{e/h}$ and $E_F$ is:
$$
n_e \approx N_C e^{-(E_c - E_F)/kT},
$$
$$
n_h \approx N_V e^{(E_v-E_F)/kT}.
$$
We express the lhs with the quadratic equation solution and solve for Fermi level:
$$E_F = E_c - kT\ln[N_C/(N_D-N_A)], \textrm{ for } N_D > N_A$$
and
$$E_F = kT\ln[N_V/(N_A-N_D)], \textrm{ for } N_A > N_D$$

??? question "When is a semiconductor intrinsic, and when it is extrinsic?"
    By definition the semiconductor is intrinsic when $|N_D-N_A| \ll n_i$, so $kT \gtrsim E_G/\log[N_C N_V/(N_D-N_A)^2]$.

## Temperature dependence of the carrier density and Fermi level

It is instructive to consider how $E_F$, $n_e$ and $n_h$ depend on carrier concentrations.
In this case, we consider an n-doped semiconductor, however, the same logic applies to p-doped semiconductors.

![](figures/E_F_and_carrier_density.svg)

There are several relevant temperature limits:

* **Intrinsic limit** . If the temperature is sufficiently large, then $n_i \gg |N_D-N_A|$ and therefore $n_e = n_h = n_i$. Additionally, if holes are heavier than electrons, then $E_F$ has an upturn in this limit.
* **Extrinsic limit**. If we decrease the temperature, we decrease the number of intrinsic carriers to the point where most of the charge carriers come form the fully ionized donors. As a result, the number of carriers stays approximately constant in this temperature range.
* **Freeze-out limit**. Once the temperature is sufficiently low $kT \ll E_G - E_D$, we expect the electrons to "freeze away" from the conduction band to the donor band. The charge carriers still come from the donors, however, not all donors are ionized now.
* **Zero temperature**. There are no charge carriers in neither conduction nor valance bands. The highest energy electrons are in the donor band and therefore $E_F$ should match the donor band.

!!! check "Exercise"
    check that you can reproduce all the relevant limits in a calculation.

## Combining semiconductors: $pn$-junction

What happens if we bring two differently doped semiconductors together (one of $p$-type, one of $n$-type)?

### Band diagram

Previously we dealt with homogeneous materials, now the position coordinate (let's call it $x$) starts playing a role.
We represent the properties of inhomogeneous materials using the **band diagram**.
The main idea is to plot the dependence of various energies ($E_F$, bottom of conduction band $E_C$, top of the valence band $E_V$) as a function of position.

Let us build up the band diagram step by step:

```python


def trans(x, a, b):
    x = (x-a)/(b-a)
    return h(x)/(h(x) + h(1-x))


def h(x):
    return (x > 0) * np.exp(-1/x)

left_cutoff = 0.3
right_cutoff = 0.7
x = np.linspace(0, 1, 100)
mid_idx = (x > left_cutoff) * (x < right_cutoff)


Ef_p = 0.5
Ef_n = Ef_p + 0.25
Ef_delta = Ef_n - Ef_p

E_C_1 = 1
E_V_1 = 0.25

E_C = E_C_1 - trans(x, left_cutoff, right_cutoff)*Ef_delta
E_V = E_V_1 - trans(x, left_cutoff, right_cutoff)*Ef_delta

fig1 = go.Figure()

fig1.add_trace(go.Scatter(
        x = [0, left_cutoff],
        y = [E_V_1, E_V_1],
        line_color = 'red',
        mode = 'lines',
        name = r'$E_V$',
    ))

fig1.add_trace(go.Scatter(
        x = [0, left_cutoff],
        y = [E_C_1, E_C_1],
        line_color = 'blue',
        mode = 'lines',
        name = r'$E_C$',
    ))

# n bands (button 1)
fig1.add_trace(go.Scatter(
        x = [right_cutoff, 1],
        y = [E_V_1, E_V_1],
        line_color = 'red',
        mode = 'lines',
        showlegend=False
    ))

fig1.add_trace(go.Scatter(
        x = [right_cutoff, 1],
        y = [E_C_1, E_C_1],
        line_color = 'blue',
        mode = 'lines',
        showlegend=False
    ))

# p fermi
fig1.add_trace(go.Scatter(
        x = [0, left_cutoff],
        y = [Ef_p, Ef_p],
        line_color='black',
        mode = 'lines',
        line_dash='dot',
        name=r'$E_F$'

    ))

# n fermi (button 1)
fig1.add_trace(go.Scatter(
        x = [right_cutoff, 1],
        y = [Ef_n, Ef_n],
        line_color='black',
        mode = 'lines',
        line_dash='dot',
        name='r$E_f$',
        showlegend=False
    ))

fig1.add_trace(go.Scatter(
        x = [right_cutoff, 1],
        y = [E_V_1-Ef_delta, E_V_1-Ef_delta],
        line_color = 'red',
        mode = 'lines',
        showlegend=False,
        visible=False
    ))

fig1.add_trace(go.Scatter(
        x = [right_cutoff, 1],
        y = [E_C_1-Ef_delta, E_C_1-Ef_delta],
        line_color = 'blue',
        mode = 'lines',
        showlegend=False,
        visible=False
    ))


fig1.add_trace(go.Scatter(
        x = [0, 1],
        y = [Ef_p, Ef_p],
        line_color='black',
        mode = 'lines',
        line_dash='dot',
        name='r$E_F$',
        visible=False,

    ))


fig1.add_trace(go.Scatter(
        x = x[mid_idx],
        y = E_C[mid_idx],
        line_color='blue',
        line_dash='dot',
        visible=False,
        showlegend=False

    ))

fig1.add_trace(go.Scatter(
        x = x[mid_idx],
        y = E_V[mid_idx],
        line_color = 'red',
        line_dash='dot',
        visible=False,
        showlegend=False
    ))

base_annot = [
    dict(
    x = 1.065,
    y = -0.1,
    xref = "x", yref = "y",
    axref = "x", ayref = "y",
    text = "",
    ax = 0.9,
    ay = -0.1,
    showarrow=True,
    arrowhead=3,
    arrowsize=30,
    arrowwidth=0.1,
    arrowcolor='black'),

    dict(
    x = -0.05,
    y = 1.12,
    xref = "x", yref = "y",
    axref = "x", ayref = "y",
    text = "",
    ax = -0.05,
    ay = 1.1,
    showarrow=True,
    arrowhead=3,
    arrowsize=30,
    arrowwidth=0.1,
    arrowcolor='black'),

    dict(
    showarrow=False,
    x = 0.15,
    y = -0.05,
    xref = "x", yref = "y",
    axref = "x", ayref = "y",
    text = "p-region"),

    dict(
    showarrow=False,
    x = 0.5,
    y = -0.05,
    xref = "x", yref = "y",
    axref = "x", ayref = "y",
    text = "depletion region"),

    dict(
    showarrow=False,
    x = 0.85,
    y = -0.05,
    xref = "x", yref = "y",
    axref = "x", ayref = "y",
    text = "n-region")
]

annot = [
    dict(
    x = 0.85,
    y = 0.75,
    xref = "x", yref = "y",
    axref = "x", ayref = "y",
    ax = 0.85,
    ay = 0.9,
    showarrow=True,
    arrowhead=3,
    arrowsize=2,
    arrowwidth=1,
    arrowcolor='black'),

    dict(
    x = 0.85,
    y = 1,
    xref = "x", yref = "y",
    axref = "x", ayref = "y",
    ax = 0.85,
    ay = 0.849,
    showarrow=True,
    arrowhead=3,
    arrowsize=2,
    arrowwidth=1,
    arrowcolor='black'),

    dict(
    x = 0.8,
    y = 0.9,
    xref = "x", yref = "y",
    axref = "x", ayref = "y",
    text = r'$\delta \varphi$',
    font = dict(size=40),
    showarrow=False),

    *base_annot
        ]




updatemenus=list([
    dict(
        type="buttons",
        direction="down",
        active=0,
        buttons=list([
            dict(label="n and p",
                 method="update",
                 args=[{"visible": [True, True, True, True, True, True, False, False, False, False, False]}, {'annotations':base_annot}]),
            dict(label="Equilibrium",
                 method="update",
                 args=[{"visible": [True, True, False, False, False, False, True, True, True, False, False]},  {'annotations':annot}]),
            dict(label="Band Bending",
                 method="update",
                 args=[{"visible": [True, True, False, False, False, False, True, True, True, True, True]},  {'annotations':annot}]),
        ]),
    )
]
)

layout = dict(
    dragmode=False,
    showlegend = True,
    updatemenus=updatemenus,
    plot_bgcolor = 'rgb(254, 254, 254)',
    yaxis_range=[(E_V_1-Ef_delta)-0.1, 0.1+E_C_1],
    xaxis_range=[-0.05, 1.05],
    width = 800,
    height = 600,
    xaxis=dict(title=r'$x$', showticklabels=False),
    yaxis=dict(title=r'$E$', showticklabels=False),
    title='Band Diagram'
)


fig1.add_annotation(
    x = 1.065,
    y = -0.1,
    xref = "x", yref = "y",
    axref = "x", ayref = "y",
    text = "",
    ax = 0.9,
    ay = -0.1,
    showarrow=True,
    arrowhead=3,
    arrowsize=30,
    arrowwidth=0.1,
    arrowcolor='black')

fig1.add_annotation(
    x = -0.05,
    y = 1.12,
    xref = "x", yref = "y",
    axref = "x", ayref = "y",
    text = "",
    ax = -0.05,
    ay = 1.1,
    showarrow=True,
    arrowhead=3,
    arrowsize=30,
    arrowwidth=0.1,
    arrowcolor='black')

fig1.add_annotation(
    showarrow=False,
    x = 0.15,
    y = -0.05,
    xref = "x", yref = "y",
    axref = "x", ayref = "y",
    text = "p-region")

fig1.add_annotation(
    showarrow=False,
    x = 0.5,
    y = -0.05,
    xref = "x", yref = "y",
    axref = "x", ayref = "y",
    text = "depletion region")

fig1.add_annotation(
    showarrow=False,
    x = 0.85,
    y = -0.05,
    xref = "x", yref = "y",
    axref = "x", ayref = "y",
    text = "n-region")

fig1.update_xaxes(showline=True, linewidth=2, linecolor='black')
fig1.update_yaxes(showline=True, linewidth=2, linecolor='black')

fig1.update_layout(layout)
py.plot(fig1)
fig1.show()


```

The main difference between $n$-type and $p$-type semiconductors is the location of the Fermi level $E_F$ (see "n and p" tab above).
The Fermi level of an $n$-type semiconductor is close to the donor states.
On the other hand, the $p$-type semiconductor has its Fermi level near the acceptor states.
At equilibrium (no external fields), we do not expect to see any currents in the system and therefore the **Fermi level $E_F$ must be constant** across the system (see "Equilibrium" tab).
To achieve a homogenous Fermi level, we could bring up in energy the $p$-type region or bring down the $n$-type region until the Fermi levels are aligned.
However, a question arises: what happens at the junction?

We can understand the junction with a simple picture.
In physics, most of the time we expect things to change *continuously*.
Therefore, we expect that the valance $E_V$ and conduction $E_C$ bands connect continuously in the middle region as shown in the "Band Bending" tab.
On the contrary, if the bands were to be discontinuous, then an electric field must develop at a single point in the middle region to shift the bands in energy.
However, we do not expect such point-like electric fields to develop because electrons can move freely in semiconductors.

On a more microscopic level, the electrons at the junction in the $n$-type semiconductor will move into the $p$-type semiconductor to **recombine** with the holes.
After the recombination, the $n$ and $p$-type semiconductors lose an electron and a hole respectively.
As a result, a positive ionized donor dopant is not screened anymore and the $n$-type semiconductor obtains a positive overall charge.
Similarly, $p$-type region obtains a negative charge.
Therefore, an electric field develops across the junction.
As the recombination process continues, a larger charge density $\rho$ develops and thus the electric field grows until it is large enough to prevent the electrons/holes from crossing the junction.
Inside the region, energy deviates by $\delta \varphi \gg kT$ from the bulk value and thus the density of electrons/holes drops exponentially fast.
Therefore, we refer to the region as the **depletion region**.

The charge density $\rho$ distribution inside of a depletion region is shown below:

![](figures/pn_charge_density.svg)

The typical values of $w_n+w_p$ are $\sim 1 \mu \textrm{m}$ at $N_A,\,N_D \sim 10^{16} \textrm{cm}^{-3}$, and $\sim 0.1 \mu \textrm{m}$ at $N_A,\,N_D \sim 10^{18} \textrm{cm}^{-3}$, so it may be much larger than the distance between the dopant atoms.


### $pn$-junction diode

What happens if we apply voltage to a junction?

Because the conductivity of the $p$-region and $n$-region is much larger than that of the depletion region, most of the voltage difference will appear in the depletion region:

![](figures/pn_junction_bias.svg)


The number of majority carriers moving across the junction is proportional to their concentration.
Increasing the voltage bias "pushes" carriers up in energy, it depends exponentially on the voltage.

We therefore get the Shockley diode equation:

$$I = I_0 \left(\exp(eV/kT) -1\right)$$

### Solar cell

Light absorbed in the $pn$-junction creates electron-hole pairs.
The eletric field then moves electrons to the $n$-doped region, holes to the $p$-doped one, and therefore generates a voltage.

![](figures/solar_cell.svg)

### Semiconducting laser

A heavily doped $pn$-junction so that the Fermi level is in the conduction/valence band produces an extremely high rate electron-hole recombination with an extremely high rate, and makes the $pn$-junction function like a laser.

### MOSFET and quantum well

See the book for details.

## Summary

Density of states in a doped semiconductor:

```python
fig
```

Charge balance determines the number of electrons and holes as well as the position of the Fermi level.

If dopant concentration is low, then $n_e = n_h = n_i \equiv \sqrt{N_C N_V}e^{-E_G/2kT}$.

If dopant concentration is high, then in $n$-doped semiconductor $n_e = N_D - N_A$ and $n_h = n_i^2/n_e$ (or vice versa in $p$-doped one).

Temperature switches between intrinsic and extrinsic regimes, and controls the carrier density

Conductance combines the contributions of electrons and holes, and allows to determine $E_G$.

A $pn$-junction has a **depletion layer** in its middle with the potential in a $pn$-junction having the following shape (where the transition region is made out of two parabolas):

![](figures/band_diagram_solution.svg)

## Exercises

### Exercise 1: Crossover between extrinsic and intrinsic regimes

In the lecture we have identified the intrinsic and extrinsic regimes.
Let us now work out what happens when the semiconductor is at the border between these two regimes, and the dopant concentration $|N_D - N_A|$ is comparable to the intrinsic one $n_i$.

1. Write down the law of mass action and the charge balance condition for a doped semiconductor.
2. Solve this system of equations for $n_e$ and $n_h$ only assuming $E_G \gg k_B T$.
3. Verify that your solution reproduces intrinsic regime when $|N_D - N_A| ≪ n_i$ and the extrinsic regime when $|N_D - N_A| ≫ n_i$

### Exercise 2: Donor ionization

Let us examine when the full donor ionization is a good assumption.
For that we consider a doped semiconductor in the extrinsic regime.

1. Assume that all dopants are ionized, determine the position of the Fermi level.
2. Write down the concentration of dopants that are not ionized.
3. Determine at what donor concentration one cannot assume anymore that all donors are ionized in germanium at room temperature.

### Exercise 3: Performance of a diode

Consider a pn-junction diode as follows

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/PN_diode_with_electrical_symbol.svg/800px-PN_diode_with_electrical_symbol.svg.png" width="50%" alt="pn diode"></img>

??? info "source"

    By Raffamaiden [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0)), [Link](https://commons.wikimedia.org/wiki/File:PN_diode_with_electrical_symbol.svg)

The current flowing through a diode as a function of applied bias voltage is given by the Shockley diode equation:

$$ I(V) = I_s(T)\left(e^{\frac{eV}{kT}}-1\right)$$

where $I_s(T)$ is the saturation current.

1. What is the significance of adding dopant atoms to an intrinsic semiconductor?
   Can two intrinsic semiconductors joined together make a diode?
2. Discuss which processes carry current in a diode under reverse bias.
3. Based on this, estimate how the saturation current $I_s$ depends on temperature.

### Exercise 4: Quantum well heterojunction in detail
Consider a a quantum well formed from a layer of GaAs of thickness $L$, surrounded by layers of Al$_{x}$Ga$_{1−x}$As.

![Quantum Well](https://upload.wikimedia.org/wikipedia/commons/4/45/Quantum_well.svg)

??? info "source"

    Vectorised by User:Sushant savla from the work by Gianderiu - [Quantum well.svg](https://commons.wikimedia.org/w/index.php?curid=73413676), [CC-BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0 "Creative Commons Attribution-Share Alike 3.0").

Assume that the band gap of the Al$_{x}$Ga$_{1−x}$As is substantially larger than that of GaAs.
The electron effective mass in GaAs is 0.068 $m_{e}$, the hole effective mass is 0.45 $m_{e}$ with $m_{e}$ the mass of the electron.

1. Sketch the band diagram of this quantum well.
2. Write down the Schrödinger's equation for electrons and holes
3. Find the energies of electron and holes in the quantum well as a function of $k_x, k_y$.
4. Calculate the density of states of electron and holes in this quantum well.
5. If we want to design a quantum well with a bandgap 0.1 eV larger than that of bulk $GaAs$, what thickness $L$ do we need?
6. Why is this structure more useful for making a laser than a normal pn-junction?
7. What would be the advantage of doping the Al$_{x}$Ga$_{1−x}$As compared to the $GaAs$ in this quantum well?
