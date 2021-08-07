# The specific heat of solids

## Introduction

We embark on our journey by starting at the nexus of the known and unknown, namely around the turn of the nineteenth and twentieth centuries, where the development of "modern" physics was being applied to systems which had hitherto be poorly understood. Now this is not to say that nothing was known about the systems, on the contrary: empirical laws had been used to great effect to describe the observable world, but with the increasing sophistication of experimental technique and apparatus, the cracks in certain rules started to appear.

## The Dulong–Petit law

Consider the heat capacity of a solid.

??? Question "Explain the concept of heat capacity to someone _without_ a science background. Said someone can be imaginary if required"

    The heat capacity is the a measure of how much heat, or how much energy transfer, is required to change the temperature of a material.

By measuring the heat capacity per weight, that is the _mass-specific heat capacity_, of a range of different elements, the two chemists Pierre Dulong and Alexis Petit observed the value was approximately constant when multiplied by the atomic weight of the element, stating that:

$$
c \times M = constant
$$

where $c$ is the specific heat capacity and $M$ is the molar mass of the material. More commonly, one will see the law expressed in terms of the heat capacity $C$ and number of moles $n$:

$$
C/n=\frac{\partial Q}{\partial T} = 3R
$$

where $R \approx 8.314~\mathrm{J K^{-1} mol^{-1}}$ is the ideal gas constant[^1]. In the physics context, it is much more common do talk about the number of atoms $N$, which transforms the above equation into the _Dulong-Peteit Law_:

$$
C/N= 3 k_\mathrm{B}
$$

But is this an accurate description? Let's have a look. Shown below is a plot of the heat capacity $C$[^2] (in units of $R$) as a function of atomic number:

<figure>
  <img src="../images/01_Dulong-Petit.svg">
  <figcaption> Heat capacity of the elements as sourced from the <a href='https://hbcp.chemnetbase.com/faces/contents/ContentsResults.xhtml'>CRC handbook of chemistry of physics</a></figcaption>
</figure>

which is pretty incredible. But a natural question arises: why is this the case?

### Equipartition

For a *gas* in thermal equilibrium, you will have seen that

$$
C_V/N = f/2 k_\mathrm{B}
$$

where $f$ is the number of thermodynamic degrees of freedom. We can see that the Dulong–Petit law is of this form, but suggests that the number of DoF is twice that of an ideal monatomic gas.

??? Question "What is the difference between the heat capacities $C_V$ and $C_P$? What is the relationship between the two quantities, and what is the implication for the heat capacity of solids?"

    As the heat capacity of an object is defined through $\frac{\partial Q}{\partial T}$, one must consider the different thermodynamic processes (e.g. isochoric versus isobraic) as the heat supplied to the system will be different (e.g. $dQ = dU$ versus $dQ = dU + PdV$). It then follows that we define the _heat capacity at constant volume_ $C_V$ and the _heat capacity at constant pressure_ $C_P$.

    Linking the two quantities is Mayer's relation, which states that for an ideal gas:

    $$
    C_P - C_V = nR
    $$

    and more generally

    $$
    C_P - C_V = \frac{VT\alpha^2}{\beta}
    $$

    where $\alpha$ is the thermal expansion coefficient and $\beta$ is the isothermal compressibility. This should immediately point to the implication for solids: solids tend to be rather incompressible, which manifests in small values of $\alpha$ and $\beta$, and especially small values of $\alpha^2$, and a negligible difference between $C_P$ and $C_V$. Hence the usage of $C$!

    <figure>
      <img src="../images/01_alpha.svg">
      <figcaption> The thermal expansion coefficients of various elements, noting that $\beta$ is of order $10^{-6} \mathrm{m}^2 \mathrm{N}^{-1}$ for squishy things (e.g. soft clay) down to $10^{-10} \mathrm{m}^2 \mathrm{N}^{-1}$ for things that a not squishy (e.g. rocks)</figcaption>
    </figure>

Depending on one's German language fluency, the [original article](https://onlinelibrary.wiley.com/doi/10.1002/andp.200590013)

=== "Plot"

    <figure>
      <img src="../images/Einstein_daimond_plot.png">
      <figcaption> Plot.</figcaption>
    </figure>

=== "Data"

    <figure>
      <img src="../images/Einstein_daimond_table.png">
      <figcaption> Plot.</figcaption>
    </figure> -->

[^1]: The exact value can be found on the [NIST database](https://physics.nist.gov/cgi-bin/cuu/Value?r)
[^2]: Data is collated in the _Heat Capacity of the Elements at 25 $^{\circ}$C_ as published in the [CRC handbook of chemistry of physics](https://hbcp.chemnetbase.com), but was sourced from [wikipedia](https://en.wikipedia.org/wiki/Heat_capacities_of_the_elements_(data_page))

--8<-- "includes/abbreviations.md"
