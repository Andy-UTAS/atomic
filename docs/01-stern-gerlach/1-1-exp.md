# The Stern-Gerlach Experiment

_Time to do the same experiment lots of times and get different results_

## Introduction

![](header.png){ title="Stern-Gerlach separation of a Bose-Einstein condensate of Rubdiuim-87" }

Our journey begins with what may be the most famous experiment in the context of quantum mechanics, which was undertaken in the early part of the twentieth century. The nascent ideas of quantum mechanics were being explored, and a delightfully simple experiment managed to break our understanding of how the world works. We shall explore the rich physics of this foundational experiment and use it as our foundation for introducing quantum mechanics using Dirac notation and matrix mechanics.

!!! danger  "Expected competencies"

    It is assumed that you have familiarity with the following concepts/techniques:

    * Kinematics of particles in magnetic fields

!!! note  "Text reference"

    The material covered here is discussed in section(s) $\S1.1$ of [Quantum Mechanics, A Paradigms Approach (2nd edition)](https://www.cambridge.org/wf/academic/subjects/physics/quantum-physics-quantum-information-and-quantum-computation/quantum-mechanics-paradigms-approach?format=AR)

<!-- !!! info "Computational content"

    The Jupyter notebook associated with this section can be accessed by clicking the icon below:

    [:fontawesome-brands-python:](https://jove2021.cloud.edu.au/){ .md-button .md-button--primary class="text-center" style="margin-left: 45%; font-size:60px"} -->

---

## The year was 1921...

A touch over 100 years ago, Otto Stern and Walther Gerlach performed the following experiment:

* Creating a beam of neutral silver atoms
* Passing the beam through an inhomogeneous magnetic field
* Measuring the beam profile after the magnetic field

A schematic of the experiment is shown below:

<figure markdown>
  ![](SGsetup.svg){width="800"}
  <figcaption>A schematic of the Stern-Gerlach experiment</figcaption>
</figure>

The experiment is conceptually very simple, and despite the experiment being extremely difficult to execute, they were able to [obtain the following result](https://link.springer.com/article/10.1007/BF01326983):

<figure markdown>
  ![](Stern-gerlach.webp)
  <figcaption>"Bohr was right after all", Walther Gerlach</figcaption>
</figure>

Without context, it is somewhat difficult to appreciate the Earth shattering nature of this image, so that is what we are going to explore.

### The classical experiment

Given there is some interaction between the atoms and the magnetic field, this leads to us assuming that the atom possesses a magnetic moment magnetic moment \boldsymbol{\mu}. The energy of the interaction is given by

$$
E = -\boldsymbol{\mu} \cdot \mathbf{B}
$$

where $\mathbf{B}$ is the magnetic field.

??? Question "Question 1.1.1: What is the force due to this interaction? Write an expression for the force in the $z$-direction"

    The force is the negative gradient of the energy, which in this case yields

    $$
    \mathbf{F} = \nabla \left(\boldsymbol{\mu} \cdot \mathbf{B}\right)
    $$

    and by the design of the experiment, we know the field is primarily in the $z$-direction and so

    \[
    \begin{align}
    F_z & = \frac{\partial}{\partial z}\left(\boldsymbol{\mu} \cdot \mathbf{B}\right) \\
    & \approx \mu_z \frac{\partial B_z}{\partial z}
    \end{align}
    \]

    Consequently, the force is largely _perpendicular_ to the direction of beam propagation, with the amount of deflection being proportional to the component of the magnetic moment in the direction of the field gradient.

The origin of a (classical) magnetic moment is either a separation of poles, or loops of current, and explicitly the magnitude of the magnetic moment $\mu$ is

$$
\mu = I \times A
$$

where $I$ is the current in the loop and $A$ is the area of the loop. In the early 1920s, atomic model _de jour_ was the Bohr model[^1], where atoms consist of charges in discrete energy shells, and so we can meaningfully talk about a charge $q$ moving at speed $v$ around the loop of a circle of radius $r$.

??? Question "Question 1.1.2: Show that the magnitude of the magnetic moment is given by $qrv/2$"
    This is plug and play from $\mu = I \times A$, requiring only that one the definition of current:

    \[
    \begin{align}
    \mu & = I \times A \\
    & = \frac{q}{2\pi r / v} \times \pi r^2 \\
    & = \frac{qrv}{2}
    \end{align}
    \]

From rotational mechanics, we know the orbital the angular momentum $L = mvr$, so we rewrite

$$
\mu = \frac{q}{2m} L.
$$

We also take further inspiration from rotational mechanics in the form of an orbiting body can itself rotate (e.g. the earth spinning whilst rotating around the sun), so we assume our charged particle has

* _Orbital_ angular momentum $\mathbf{L}$
* _Intrinsic_ angular momentum $\mathbf{S}$

both of which will contribute to the magnetic interaction. By analogy with the orbital angular momentum, we can propose a relation between the magnetic moment and the intrinsic angular momentum as

$$
\boldsymbol{\mu} = g\frac{q}{2m} \mathbf{S}
$$

where $g$ is the dimensionless $g-$factor which contains all of the juicy physics. Arriving at a theoretical value for this constant goes beyond the scope of this course[^2], but it turns out the value of $g$ is approximately -2, and the deviation from -2 is hailed as one of the grand successes of the theory of Quantum Electrodynamics: the predicted value of

$$
g_{\mathrm{theory}} = -2.002319304363286
$$

matches the experimental value of

$$
g_{\mathrm{exp}} = −2.00231930436256(35)
$$

 _very_ well.

### Long-shot silver

We must take a brief sojourn from physics fundamentals to look at the practicalities of the experiment, such that we can realistically model the system.

??? Question "Question 1.1.3: How many common isotopes of silver are there and how many neutrons are in each isotope? How does the existence of these isotopes alter our analysis?"

    The common isotopes of silver are $^{107}$Ag and $^{109}$Ag, having 60 and 62 neutrons respectively. Impressively, these isotopes occur with [near-similar abundances](https://en.wikipedia.org/wiki/Isotopes_of_silver) at $51.8%$ and $48.2%$ respectively.

    In all cases, the magnetic moment depends on the _inverse_ of the particle mass, so for both protons and neutrons which have a mass some thousands of times bigger, we can simply ignore[^3] thier contribution to the magnetic moment of the atom.

??? Question "Question 1.1.4: What is the electronic configuration of Silver? How many unpaired electrons are in the outer shell? What are the consequneces for our (the Stern-Gerlach) experiment? Write an expression of the magnetic moment of neutral silver."

    The electronic confiuration for silver is

    $$
    \mathrm{Ag} = 1\mathrm{s}^2 2\mathrm{s}^2 2\mathrm{p}^6 3\mathrm{s}^2 3\mathrm{p}^6 4\mathrm{s}^2 3\mathrm{d}^{10} 4\mathrm{p}^6 4\mathrm{d}^{10} 5\mathrm{s}^1
    $$

    or equivalently

    $$
    \mathrm{Ag} = [\mathrm{Kr}] 4\mathrm{d}^{10} 5\mathrm{s}^1
    $$

    meaning that there is only a single unpaired electron in the outer shell, and it is also in the ground state, which has an isotropic distribution and thus no orbital angular momentum, meaning only the intrinsic angular momentum of the electron will contribute to the interaction.

    The magnetic moment for the silver atom is then

    $$
    \boldsymbol{\mu} = -g\frac{e}{2 m_e} \mathbf{S}
    $$

    where $e$ is the magnitude of the electron charge and $m_e$ is the electronic mass.

!!! bug "Are we baking in the result for the classical analysis by using what amounts to quantum info?"

    Yes, but this needn't be the case; however, it really simplifies the discussion. The Stern-Gerlach experiment was done with neutral silver, so we seek to analyse this result; but we could look at the case of Hydrogen (which was done afterwards) or the plethora of other systems, but multielectron systems do require a bit of modern knowledge to make the classical analysis fit together. An interesting thought is [why don't we do the experiment or analysis with electrons themselves](#preliminary-provocations)?

The force in the the $z-$ direction for a silver atom is thus

$$
\begin{align}
F_z & \approx \mu_z \frac{\partial B_z}{\partial z} \\
& = - g \frac{e}{2 m_e} S_z \frac{\partial B_z}{\partial z}
\end{align}
$$

and directly, we have the deflection of the beam through the apparatus being a direct measurement of the $z$ component of the spin along the axis of the magnetic field gradient.

??? Question "Question 1.1.5: Make a prediction of the distribution of deflected silver atoms you would expect for a thermal source."

    A reasonable assumption one can make is that the intrinsic angular momentum for each $5\mathrm{s}$ electron has the same magnitude, and thus we can write the $z-$component as

    $$
    S_z = |\mathbf{S}|\cos\left(\theta\right)
    $$

    where $\theta$ is the angle between the $z-$axis and the spin vector $\mathbf{S}$. For a thermal beam, we would expect all values of $\theta$, with the explicit angular flux to be determined by the apparatus; however, the from of this being largely unimportant save for the fact we expect all values of $\theta$ to be present. We therefore would expect a continuous range of spin projections, ranging from $S_z \in [-|\mathbf{S}|, |\mathbf{S}|]$

### The results

??? abstract "Reprint: the experimental results of the original Stern-Gerlach experiment"
    <figure markdown>
      ![](Stern-gerlach.webp)
    </figure>

![Surprise](doakes.jpeg){ align=left width="200" }

We can now return to the results as recorded by Stern and Gerlach. If we look at the image without the magnetic field gradient, we see the silver beam form a line (which is due to the geometry of experiment) and when the gradient is switched on, only two projections along the field gradient are observed, which indicates only two values of the $z-$ component of the electron spin are possible. The magnitude of these deflections are consistent with the values of the spin component of

$$
S_z = \pm \frac{\hbar}{2}
$$

where the _reduced Planck constant_ is $\hbar = h/2\pi$ and Plank's constant is $h=6.62607015 \times 10^{-34}~\mathrm{J \cdot Hz^{-1}}$. The Stern-Gerlach experiment is evidence of the quantisation of the electron spin angular momentum along an axis.

!!! info "The quantisation axis"
    In our working here, we have chosen the $z-$axis to be the direction along which we measure the spin component, but we could have equally picked any other axis and observed the same result. It is a well-observed convention to define the axis of the magnetic field (gradient) to be along $z$, and we are not going to start rocking the boat.

## A general Stern-Gerlach experiment

We are going to regroup: with your socks (hopefully) having been blown off by the above result, we are going to move into a generalised framework to consider these kinds of experiments - and yes, should you need to take a minute to collect you socks, please do so now.

### Details in the bin

We are going to strip back the Stern-Gerlach experiment to the core features, which consists of the following:

* A beam of atoms
* A Stern-Gerlach device which analyses the component of spin along a given axis

A schematic of the system is shown below:

<figure markdown>
  ![](Stern-Gerlach simple.svg)
  <figcaption>A schematic of the simplified Stern-Gerlach system</figcaption>
</figure>

We are also going to label the output ports of our analyser: the up and down arrows ($\uparrow$ and $\downarrow$) indicate the possible measurement results for the analyser, which correspond to the measurements

$$
S_z = \pm \frac{\hbar}{2}
$$

and as there are only two results, we can refer to these as _spin up_ and _spin down_. The thing that we are measuring, the projection of $\mathbf{S}$ onto the $z-$axis ($S_z$) is the _observable_, i.e. the thing we are measuring.

### The quantum state

When we talk about the beams in our system, be it the input beam or the beams after the analyser, we are describing quantum states. In the first part of this course, you will have encountered quantum mechanical states in the context of wavefunctions, which are solutions to the Schrödinger equation. Here we adopt a more general representation of quantum states, which is not limited to the degrees of freedom chosen to represent the wavefunction (e.g. position/momentum space) but rather talk about a state as an object containing all of the information that we can know about the system. Mathematically, we represent states using  _Dirac notation_; in the case of our spin up and spin down states, we label these $|+\rangle$ and $|-\rangle$, where we have introduced a new symbol to demarcate a quantum state, the ket. We will delve deeper into these objects [later](../1-2-statevectors/), but for the moment it sufficient to know that a general state is mathematically described by the ket $|\psi\rangle$.

!!! info "Uniqueness of ket labels"
    A quantum state is described by a ket, but the label in the ket is **not** unique. For example, we might label the spin-up state as

    * $| + \rangle$
    * $| S_z = +\hbar/2 \rangle$
    * $| +\mathbf{\hat{z}} \rangle$
    * $| \uparrow \rangle$
    * $\ldots$

    where the label is not important; in all cases, we are talking about the state with a projection of $+\hbar/2$ through our Stern-Gerlach analyser.

!!! abstract "Postulate 1"
    The state of a quantum mechanical system - the entirety of information that you can know about it - is represented mathematically by a normalised ket $|\psi\rangle$

We now seek to perform a series of experiments which the systems will behave exactly as expected and no strange behaviour will take place.

!!! example "Experiment simulator"
    An [online simulation](https://physics.weber.edu/schroeder/software/Spins.html) is available to allow you to play along with the following experiments.  

### Experiment one

The following set of experiments are conducted by sending our beam through various analysers. An example of such an experiment from our simple setup above is shown below:

<figure markdown>
  ![](Stern-Gerlach simple_.svg){width="500"}
  <figcaption>The simplified Stern-Gerlach experiment with proportions of atoms detected from the output ports</figcaption>
</figure>

In our first example, we are going to stack two analysers aligned along the $z-$axis. The beam will be split by the first analyser, and we then take the spin up component of the beam and use this as the input to a second analyser, meaning the spin component is again analysed.

!!! example "Experiment time"

    === "Experimental setup"
        <figure markdown>
          ![](Stern-Gerlach Ex1.svg){width="500"}
          <figcaption>What will the proportion of particles detected at the output ports?</figcaption>
        </figure>

    === "Experimental results"
        <figure markdown>
          ![](Stern-Gerlach Ex1_.svg){width="500"}
        </figure>

        This result is perhaps unsurprising, as the first analyser measures an atom to have a $z-$component of spin $S_z = +\hbar/2$, and the 2nd analyser also measures $S_z = +\hbar/2$ for these atoms. It should be emphasised that in this scenario, the first analyser can be considered to be preparing the quantum state: if we have a mixture of spin up and spin down atoms before the analyser, atoms from a given output port will be either spin up or spin down.

### Experiment two

We are now going to preform the same experiment as [experiment one](#experiment-one) with the exception being that we are going to replace the second analyser with an analyser which is aligned to the $x-$axis, meaning that we now measure the $x$ component of the spin $S_x$ rather than $S_z$.

!!! example "Experiment time"

    === "Experimental setup"
        <figure markdown>
          ![](Stern-Gerlach Ex2.svg){width="500"}
          <figcaption>What will the proportion of particles detected at the output ports?</figcaption>
        </figure>

    === "Experimental results"
        <figure markdown>
          ![](Stern-Gerlach Ex2_.svg){width="500"}
        </figure>

        At the top port of the first analyser, we still have atoms in the spin up state $|+\rangle$ as per the previous example, but following the second analyser, we have atoms which have components $S_x = +\hbar/2$ and $S_x = -\hbar/2$, which we denote by $|+\rangle_x$ and $|-\rangle_x$ respectively. Points of note from this experiment are

        * Even though we have changed the orientation of the analyser, there are still only two possible values for the projection of the spin
        * Results for this experiment would be unchanged if we had taken the spin down output from the first analyser
        * Critically: for any given atom, we cannot predict the output of the second analyser. We know that there will be a $50\%$ probability of an atom exiting via a specific port, but nothing more

Quantum mechanics is inherently probabilistic: we cannot know the outcome of a given measurement without making said measurement. In the development of quantum mechanics, it was postulated that whilst measurements appeared to be probabilistic, there was actually some other variable which was underwriting the system, which if known would allow us to conclusively predict results. This so-called _hidden variable_ theory of quantum mechanics was shown to be incompatible with observed results[^4], something we shall discuss in detail later in the course.

### Experiment three

We shall now extend [experiment two](#experiment-two) with the addition of a third analyser, again aligned along the $z-$axis, meaning we are measuring the component of the spin along the $z$, $x$, and $z$ axes respectively.

!!! example "Experiment time"

    === "Experimental setup"
        <figure markdown>
          ![](Stern-Gerlach Ex3.svg){width="500"}
          <figcaption>What will the proportion of particles detected at the output ports?</figcaption>
        </figure>

    === "Experimental results"
        <figure markdown>
          ![](Stern-Gerlach Ex3_.svg){width="500"}
        </figure>

        ![Surprise](doakes.jpeg){ align=left width="100" }

        If this result does not cause a double take, then marinate in it a bit longer until that happens. We have measured $S_z = +\hbar/2$, then we have taken a measurement of $S_x$, and then immediately taken another measurement of $S_z$, but the result is now a mixture of $S_z = +\hbar/2$ and $S_z = -\hbar/2$. Somehow, by measuring $S_x$, we have erased knowledge of $S_z$.

A key feature of quantum mechanics is that making a measurement fundamentally alters the system. These experiments are designed to illustrate that there is a fundamental incompatibility between measurements of different spin components, or formally: that $S_x$ and $S_z$ are incompatible observables. This means that we cannot these values simultaneously.

!!! warning "Compatible versus incompatible observables"

    In this case we see that $S_z$ is incompatible with $S_x$ (and also $S_y$), but this does not mean that all pairs of observables are incompatible. It is an important aspect of quantum mechanics that we can make _certain_ measurements without altering other aspects of the system. We shall discuss this in detail later, but for now it is sufficient to say that there are both sets of compatible observables and incompatible observables.

### Experiment four

For our final experiment, we are going to repeat [experiment three](#experiment-three) but we are going to alter the beam as it comes out of analyser number 2: namely change what goes into analyser number three.

!!! example "Experiment time"

    === "Experimental setup"
        <figure markdown>
          ![](Stern-Gerlach Ex4.svg){width="800"}
          <figcaption>What will the proportion of particles detected at the output ports?</figcaption>
        </figure>

    === "Spin up only"
        <figure markdown>
          ![](Stern-Gerlach Ex4a.svg){width="800"}
        </figure>

        This is exactly the same as [experiment three](#experiment-three).

    === "Spin down only"
        <figure markdown>
          ![](Stern-Gerlach Ex4b.svg){width="800"}
        </figure>

        This is in effect, exactly the same as [experiment three](#experiment-three).

    === "Combined spin up and spin down"
        <figure markdown>
          ![](Stern-Gerlach Ex4c.svg){width="800"}
        </figure>

        ![Surprise](doakes.jpeg){ align=left width="100" }

        This result is perhaps the strangest of all: by recombining the outputs from the second analyser, we have somehow made the atoms recall their state from the output of analyser number one! Classical probability theory cannot explain this aspect of quantum mechanics.

Whilst these results may appear extremely foreign, you already have an intuition for what is going on: consider the canonical double-slit experiment. When light waves pass through slits, each slit produces a nearly uniform illumination of the screen, but when the two slits are allowed to combine, an interference pattern in observed. In order to describe this phenomenon, we consider the complex-valued electric fields from both sources, and ultimately calculate the intensity as the square of the field amplitude, and the nature of complex-valued fields permits interference effects. In this sense, quantum mechanical is no different to any other form of wave mechanics, but we must work to describe and calculate the amplitudes of the quantum mechanical waves.

---

## Conclusions


The Stern-Gerlach experiment demonstrates some foundational concepts of quantum mechanics:

1. Quantum mechanics is probabilistic
2. Spin measurements are quantised
3. Quantum measurements disturb the system

---

## Exercises

### Preliminary provocations
1. Why use an inhomogeneous magnetic field?
2. Why is the experiment done with silver atoms?

### Heavy hitters
1.
2.

---

!!! info "Image credits"

    Header image taken from the PhD thesis [Spinor Bose-Einstein condensates in magnetic field gradients](https://bridges.monash.edu/articles/thesis/Spinor_Bose-Einstein_condensates_in_magnetic_field_gradients/4697395/1)

[^1]: more accurately, at this time it was the Bohr-Sommerfeld model, which is an extension of the Bohr model to include elliptical orbits which fixed some problems. One will also see in [solid-state physics](https://ssp.utasphys.cloud.edu.au/) that Sommerfeld has a real talent for tweaking existing theories to make them run a bit better.
[^2]: A study of the the relativistic wave equation, known as the _Dirac equation_, is required to fully flesh out this result.
[^3]: In this case we can, but more generally, the magnetic moment of the nucleus cannot be ignored (see LINK ME! hyperfine splitting)
[^4]: The [2022 Nobel Prize in physics](https://www.nobelprize.org/prizes/physics/2022/summary/) was awarded for the pioneering work of making these measurements

--8<-- "includes/abbreviations.md"
