# Electrons in metals I

## Introduction

![](../images/03_metals.jpg)

Metals are awesome, and this has long been known. People have been drawn to their shininess since the first chunks of the stuff were found, and it mustn't have been long before it was realised that they were different to other materials. To nail down exactly what is the difference would take some time (of order 10,000 years!) but it boils down to metals being conductive, and this comes from the ability of electrons in the material to move more freely. It turns out that one can apply a somewhat crude kinetic theory to understand the transport of electrons in metals, in the same way kinetic theory can be used to understand the transport of gasses.

!!! danger  "Expected competencies"

    It is assumed that you have familiarity with the following concepts/techniques:

    * Electromagnetism: The influence of fields of charged particles
    * Mechanics: Construct and solve equations of motion
    * Thermal physics: Kinetic theory of gases

!!! note  "Text reference"
    The material covered here is discussed in section(s) $\S 3$ of [The Oxford Solid State Basics](https://global.oup.com/academic/product/the-oxford-solid-state-basics-9780199680771?cc=au&lang=en&)

!!! info "Computational content"

    The Jupyter notebook associated with this section can be accessed by clicking the icon below:
    [<i class="fab fa-python fa-5x"></i>](https://jove2021.cloud.edu.au/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FAndy-UTAS%2FSolid-state&urlpath=tree%2FSolid-state%2F03metalsI.ipynb&branch=master){ .md-button .md-button--primary class="text-center" style="margin-left: 45%"}

---

## The kinetic theory of ~~gases~~ electrons

Ohm's law is an empirical observation of conductors, which states that voltage is proportional to current $V=IR$. Since we are interested in the properties of materials, we would like to express this in a relation that does not depend on the conductor geometry. We achieve this by expressing the terms in Ohm's law with their microscopic equivalents.

Consider a conducting wire with cross-sectional area $A$ and length $l$. Such a wire has resistance $R = \rho l / A$ where $\rho$ is the material-dependent resistivity. An applied voltage $V$ in the wire creates an electric field $E = V/l$. The resulting current $I$ in the wire is described by the current density $j \equiv I / A$. Returning these relations to Ohm's law, we get:

$$
V = I ρ \frac{l}{A} ⇒ E = ρ j,
$$

which relates the _local_ quantities $E$ and $j$. Our mission is to understand how this relation arises by considering motion of individual electrons in metals. This path was first trodden by Drude, who applied Boltzmann's kinetic theory of gases to a "gas" of electrons. The assumptions of Boltzmann's kinetic theory are that:

  * Electrons scatter randomly at uncorrelated times. The average time between scattering is $\tau$. Therefore, the probability of scattering in a time interval $dt$ is $dt / \tau$
  * After each scattering event, the electron's momentum randomizes with a zero average $⟨\mathbf{p}⟩=0$

It is also important to bake in the difference between neutral atoms or molecules in a gas and electrons, namely:

  * Electrons are charged particles with charge $-e$, and consequently they respond to electric and magnetic fields through the Lorentz force ($\mathbf{F}=-e\left(\mathbf{E}+\mathbf{v}×\mathbf{B}\right)$)

Even under these simplistic assumptions, the trajectory of the electrons is hard to calculate. As you will have seen elsewhere, with random scattering events, each trajectory is very different. A simple animation below shows several example trajectories, which are markedly different:

![type:video](../images/03_scattering.mp4)

### Equations of motion

Keep in your mind that our goal is to find electric current density $j$. Each electron with charge $-e$ and velocity $\mathbf{v}$ carries current $-e\mathbf{v}$. Therefore, if the electron density is $n$, the *average* current they carry is $-ne⟨\mathbf{v}⟩$. Thus, our goal shifts to compute the *average* velocity. Underpinning this calculation is idea that although it is difficult to calculate the motion of an individual electron, computing the average motion of the electrons is a much more tractable task.

For convenience from now on, we will omit the average brackets, and write $\mathbf{v}$ instead of $⟨\mathbf{v}⟩$.
This also applies to $F$.
We derive an equation of motion for the "average" electron in the following way:
Consider everything that happens in an (infinitesimal) time interval $dt$.
A fraction $dt/τ$ of the electrons scatters, and their average velocity becomes zero.
$$
m\mathbf{v}(t + dt) = 0
$$
The rest of the electrons $(1 - dt/τ)$ are accelerated by the Lorentz force $F$, so their velocity becomes
$$
m\mathbf{v}(t + dt) = m\mathbf{v}(t) + \mathbf{F}⋅dt.
$$
To find the average velocity, we take a weighted average of these two groups of particles:
$$
\begin{aligned}
m\mathbf{v}(t+dt)  &= [m\mathbf{v}(t) + F dt]\left(1 - \frac{dt}{\tau}\right) + 0⋅\frac{dt}{\tau} \\
  &= [m\mathbf{v}(t) + \mathbf{F} dt] \left(1 - \frac{dt}{\tau}\right) \\
                  &= m\mathbf{v}(t) + dt \left[\mathbf{F} - m\frac{\mathbf{v(t)}}{\tau}\right] - \frac{\mathbf{F}}{\tau} dt^2
\end{aligned}
$$
We now neglect the term proportional to $dt²$ (it vanishes when $dt → 0$).
Finally, we recognize that $\left[\mathbf{v}(t+dt) - \mathbf{v}(t)\right]/dt = d\mathbf{v}(t)/dt$, which results in
$$
m\frac{d\mathbf{v}}{dt} = -m\frac{\mathbf{v}}{τ} + \mathbf{F}.
$$
Observe that the first term on the right-hand side has the same form as a drag force: it always decelerates the electrons.

This equation equation of motion of the average electron is our main result: now we only need to apply it.

### Consequences of the Drude model

Let us first consider the case without magnetic fields, $\mathbf{B} = 0$, and with constant electric field $\mathbf{E}$. For many properties of interest, we are interested in the steady-state behaviour of the system, i.e. $d\mathbf{v}/dt = 0$, which upon solving the equation of motion yields:

$$
\mathbf{v}=\frac{-eτ}{m}\mathbf{E}=-|μ|\mathbf{E}.
$$

In the above equation, we define the *mobility* $μ\equiv |e|τ/m$ to be the ratio between the electron drift velocity and the electric field. The mobility is an extremely important quantity: it describes the response of the electron to an electric field. We can then substitute the steady-state velocity into the definition of current density:

$$
\mathbf{j}=-en\mathbf{v}=\frac{n e^2τ}{m}\mathbf{E}=\sigma\mathbf{E}
$$

where $\sigma$ is the conductivity

$$
\sigma=\frac{ne^2τ}{m}=ne\mu
$$

such that $ρ=1/\sigma$.

### The Hall effect

Let us now consider the case where both and electric field $\mathbf{E}$ and magnetic field $\mathbf{B}$ are non-zero. Imagine a conductor with a current $I$ flowing perpendicular to an external magnetic field $\mathbf{B}$ as shown below:

![](../images/03_Hall-effect.png)

Looking at the equations of motion:

$$
m\frac{d\mathbf{v}}{dt} = -m\frac{\mathbf{v}}{τ} - e(\mathbf{E} + \mathbf{v}\times\mathbf{B})
$$

we once again consider the steady state $d\mathbf{v}/dt = 0$. After substituting $\mathbf{v} = -\mathbf{j}/ne$, we arrive at

$$
\mathbf{E}=\frac{m}{ne^2τ}\mathbf{j} + \frac{1}{ne}\mathbf{j}\times\mathbf{B}.
$$

The first term is the same as before and describes the electric field parallel to the current, while the second is the electric field **perpendicular** to the current flow. In other words, if we send a current through a sample and apply a magnetic field, a voltage develops in the direction perpendicular to the current. This phenomenon is known as the *Hall effect*, with the perpendicular voltage called the *Hall voltage*, and the proportionality coefficient $B/ne$ the *Hall resistivity*.

Because of the Lorentz force, the electrons are deflected in a direction perpendicular to $\mathbf{B}$ and $\mathbf{j}$. The deflection creates a charge imbalance, which in turn creates the electric field $\mathbf{E}_\mathrm{H}$ compensating the Lorentz force.

The above relation between the electric field and the current is linear, which allows us to write it in matrix form

$$
\mathbf{E} = \bar{\rho} \mathbf{j}
$$

where $\bar{\rho}$ the *resistivity matrix*. Its diagonal elements are $\rho_{xx}=\rho_{yy}=\rho_{zz}=m/ne^2\tau$, which is the same as without magnetic field. The only nonzero off-diagonal elements when $\mathbf{B}$ points in the $z$-direction are

$$
ρ_{xy}=-ρ_{yx}=\frac{B}{ne}\equiv -R_\mathrm{H}B,
$$

where $R_H=-1/ne$ is the *Hall coefficient*. So by measuring the Hall voltage and knowing the electron charge, we can determine the density of free electrons in a material.

While most materials have $R_\mathrm{H}<0$, interestingly some materials are found to have $R_\mathrm{H}>0$.

??? question "3.1 What would be the implications of a negative hall coefficient?"

    With the density is negative, or that the charge carrier has a positive charge and thus not an electron.

### Thermal transport

Given that Drude had cobbled together a kinetic theory for electrons, he decided that it was worthwhile to keep going, and make predictions about the properties of the "gas" in the same way as Boltzmann.

#### Thermal conductivity

Explicitly, Boltzmann derived the thermal conductivity $\kappa$:

$$
\kappa = \frac{1}{3}n c_v \langle v \rangle \lambda
$$

where $c_v$ is the heat capacity per particle, $\langle v \rangle$ is the average thermal velocity and $\lambda = \langle v \rangle \tau$ is the scattering length. For a monatomic gas

$$
c_v = \frac{3}{2} k_{\mathrm{B}}
$$

and

$$
\langle v \rangle = \sqrt{\frac{8 k_{\mathrm{B}} T}{\pi m}}
$$

Without any grounds for justification, we can just give these a whirl and see how they go for electrons:

$$
\kappa = \frac{4}{\pi}\frac{n \tau k_{\mathrm{B}} T}{m}
$$

which still holds the phenomenological scattering rate $\tau$, meaning makes independent measurement impossible. However, the conductivity $\sigma$ also contains $\tau$, so by measuring their ratio we can eliminate the dependence and define the Lorenz number:

$$
L = \frac{\kappa}{T\sigma} = \frac{4}{\pi}\left(\frac{k_{\mathrm{B}}}{e}\right) \approx 1 \times 10^{-8}~\mathrm{W\Omega~K^{-2}}
$$

which was close to the measured values of the Lorenz number (within a factor of 2 or so), and given there had never been any explanation at all for this behaviour, this result served was hailed as a major accomplishment.

#### The Peltier effect

<figure>
  <img src="../images/03_peltier.jpg">
  <figcaption> A stack of peltier (thermoelectric cooling) devices can be used for highly-effective heat transfer </figcaption>
</figure>

Aside from being amazingly cool, we look at the Peltier effect to see that whilst the model well predicts the Lorenz number, this is actually somewhat of a fluke. The _Peltier effect_ arises when a current flows through a material, as that current necessarily transports heat. The Peltier coefficient is defined by

$$
\mathbf{j}^q = \Pi \mathbf{j}
$$

Where $\mathbf{j}^q$ is the heat current density and $\mathbf{j}$ is the electrical current density. In kinetic theory, the thermal current is

$$
\mathbf{j}^q = \frac{1}{3} (c_v T) n \mathbf{v}
$$

where $c_v T$ is the heat carried by one particle and $c_v = 3 k_{\mathrm{B}}/2$ the heat capacity per particle, $n$ the density of particles, and the factor of 1/3 from geometry. The electric current is

$$
\mathbf{j} = -en\mathbf{v}
$$

and thus

$$
\Pi = \frac{-c_v T}{3 e} = \frac{-k_\mathrm{B} T}{2 e}
$$

which yield the temperature independent ratio

$$
S = \frac{\Pi}{T} = \frac{-k_{\textrm{B}}}{2e} = -4.3 \times 10^{-4} \mathrm{V/K}
$$

where $S$ is _Seebeck coefficient_ (also the thermopower). And how well does this agree? Well, unlike $\kappa$ which was only a factor of 2 from the measure values, most values of $S$ are on the order of  $10^{-6} \mathrm{V/K}$.

So unfortunately, whilst the Drude model gives us a "broad brushstrokes" picture of what is happening in a metal, it fails to accurately predict the specific behaviour and the quantities about which we care.

---

## Conclusions

  1. Drude theory is a kinetic theory and microscopic justification of the Ohm's law.
  2. We can calculate the resistivity from the characteristic scattering time $\tau$.
  3. The Lorentz force leads to the Hall voltage that is perpendicular to the direction of both the electric current and the magnetic field.
  4. Drude theory does some things well, but ultimately falls short.

---

## Exercises

### Preliminary provocations

  1. How does the resistance of a purely 2D material depend on its size?
  2. Check that the units of mobility and the Hall coefficient are correct.  
     (As you should always do!)
  3. Explain why the scattering times due to different types of scattering events add up in a reciprocal way.

### Exercise 1: Extracting quantities from basic Hall measurements

We apply a magnetic field $\bf B$ along the $z$-direction to a planar (two-dimensional) sample that sits in the $xy$ plane. The sample has width $W$ in the $y$-direction, length $L$ in the $x$-direction and we apply a current $I$ along the $x$-direction.

??? question "What is the relation between the electric field and the electric potential?"
    $V_b - V_a = -\int_{\Gamma} \mathbf{E} \cdot d\mathbf{\ell}$ if $\Gamma$ is a path from $a$ to $b$.

1. Suppose we measure a Hall voltage $V_H$. Express the Hall resistance $R_{xy} = V_H/I$ as a function of magnetic field. Does $R_{xy}$ depend on the geometry of the sample? Also express $R_{xy}$ in terms of the Hall coefficient $R_H$.

2. Assuming we control the magnetic field $\mathbf{B}$, what quantity can we extract from a measurement of the Hall resistance? Would a large or a small magnetic field give a Hall voltage that is easier to measure?

3. Express the longitudinal resistance $R=V/I$, where $V$ is the voltage difference over the sample along the $x$ direction, in terms of the longitudinal resistivity $ρ_{xx}$. Suppose we extracted $n$ from a measurement of the Hall resistance, what quantity can we extract from a measurement of the longitudinal resistance? Does the result depend on the geometry of the sample?

### Exercise 2: Motion of an electron in a magnetic and an electric field.

Consider an electron in free space experiencing a magnetic field $\mathbf{B}$ along the $z$-direction. Assume that the electron starts at the origin with a velocity $v_0$ along the $x$-direction.

  1. Write down the Newton's equation of motion for the electron, compute $\frac{d\mathbf{v}}{{dt}}$.
  2. What is the shape of the motion of the electron? Calculate the characteristic frequency and time-period $T_c$ of this motion for $B=1$ Tesla.
  3. Now we accelerate the electron by adding an electric field $\mathbf{E} = E \hat{x}$. Adjust the differential equation for $\frac{d\mathbf{v}}{{dt}}$ found in (1) to include $\mathbf{E}$. Sketch the motion of the electron.


### Exercise 3: Temperature dependence of resistance in the Drude model

   We consider copper, which has a density of 8960 kg/m$^3$, an atomic weight of 63.55 g/mol, and a room-temperature resistivity of $ρ=1.68\cdot 10^{-8}$ $\Omega$m. Each copper atom provides one free electron.

  1. Calculate the Drude scattering time $τ$ at room temperature.
  2. Assuming that electrons move with the thermal velocity $\langle v \rangle = \sqrt{\frac{8k_BT}{\pi m}}$, calculate the electron mean free path $\lambda$, defined as the average distance an electron travels in between scattering events.
  3. The Drude model assumes that $\lambda$ is independent of temperature. How does the electrical resistivity $ρ$ depend on temperature under this assumption? Sketch $ρ(T)$.
  5. Compare your sketch of $ρ(T)$ with that in the lecture notes. In what respect do they differ? Discuss possible reasons for differences.

### Exercise 4: The Hall conductivity matrix and the Hall coefficient
We apply a magnetic field $\bf B$ along the $z$-direction to a current carrying 2D sample in the xy plane. In this situation, the electric field $\mathbf{E}$ is related to the current density $\mathbf{j}$ by the resistivity matrix:

$$\mathbf{E} = \begin{pmatrix} ρ_{xx} & ρ_{xy} \\ ρ_{yx} & ρ_{yy} \end{pmatrix} \mathbf{j}$$

  1. Sketch the expressions for $ρ_{xx}$ and $ρ_{xy}$ derived in the lecture notes as a function of the magnetic field $\bf{B}$.
  2. Invert the resistivity matrix to obtain the conductivity matrix,

     $$ \begin{pmatrix} \sigma_{xx} & \sigma_{xy} \\ \sigma_{yx} & \sigma_{yy} \end{pmatrix}$$

     allowing you to express $\mathbf{j}$ as a function of $\mathbf{E}$.


--8<-- "includes/abbreviations.md"
