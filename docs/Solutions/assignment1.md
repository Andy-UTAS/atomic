# Assignment 1: Debye, Drude, Sommerfeld, and chemistry

The first assignment can be found [here](../assignments/Assignment one.pdf)

## Exercise 1 - Debye

1. What are the assumptions of the Debye model?

    The Debye model considers only sound waves in a material (i.e. one assumes a linear dispersion $\omega = v k$) which oscillate up to a maximum frequency $\omega_{\mathrm{cutoff}} = \omega_d$, the Debye frequency, which exists to ensure that the total number of vibrational modes in the system is correct (equal to the number of degrees of freedom in the system).

2. Write an expression for the number of modes in a two-dimensional system, and thus determine the _Debye wavenumber_ (the wavenumber which corresponds to the Debye frequency).

    In two dimensions, there should be $2N$ modes (we implicitly assume that the different sound polarisations propagate with the same velocity, and thus

    $$
    2N = 2 \frac{A}{2\pi^2} \int_0^{|k| = k_d} \mathrm{d}^2 k
    $$

    where $A$ is the area of our periodic system ($L \times L$). The integral is simply the area of a circle with a radius $k_d$, so it evaluates to

    $$
    2N = \frac{2A}{(2\pi)^2}(\pi k_d^2)
    $$

    and ultimately obtains

    $$
    k_d = \sqrt{4\pi n}
    $$

    with $n = N/A$ (the two-dimensional density).

3. Provide a brief discussion of which elements you would expect to have a high Debye temperature, and which elements you would expect to have a low Debye temperature.

    The Debye temperature $T_d$ is defined through

    $$
    E_d = \hbar \omega_{d} = k_{\mathrm{B}} T_d
    $$

    and as was [shown in class](https://andy-utas.github.io/1-intoduction/1-2-specificheatII/#the-density-of-states), the Debye frequency is

    $$
    \omega_d^3 = 6\pi^2 n v_s^3
    $$

    where $v_s$ is the speed of sound in the material. Therefore, one would expect the materials with large $v_s$ to have the highest $T_d$. Consequently, a good guess for the highest $T_d$ would be diamond (and indeed, it is the highest). For low $T_d$, low speed of sound materials will be compressible - a small spring constant in the Einstein/Debye models - so the nobel gasses or soft metals (e.g. group I) would be good candidates.

## Exercise 2 - Drude: mixed ion-electron conductors (MIECs)

1. Calculate the electrical resistivity $\rho$

    Assuming that both species respond to the electric field independently - we assume that there are no interactions - the total conductivity is the sum of the two independent conductivities

    $$
    \sigma = \sigma_e + \sigma_i = e^2 \left(\frac{n_e \tau_e}{m_e} + \frac{n_i \tau_i}{m_i}\right)
    $$

    and therefore the resistivity $\rho = 1/\sigma$

    $$
    \rho  \frac{1}{e^2 \left(\frac{n_e \tau_e}{m_e} + \frac{n_i \tau_i}{m_i}\right)}
    $$

2. Calculate the thermal conductivity $\kappa$

    The thermal conductivity is calculated in the same way as the resistivity, in that we add the two pieces:

    $$
    \kappa = \kappa_e + \kappa_i = \frac{4k_{\textrm{B}}^2 T}{\pi} \left( \frac{n_e \tau_e}{m_e} + \frac{n_i \tau_i}{m_i} \right)
    $$

3. What is the Wiedemann-Franz law? Does it hold in this situation?

    The Wiedemann-Franz law states that the ratio (also known as the Lorenz number)

    $$
    L = \frac{\kappa}{T\sigma} = \frac{3}{2} \left(\frac{k_{\textrm{B}}}{e}\right)
    $$

    is roughly constant for metals, and it indeed holds for MIECs

4. If we consider a magnetic field applied in the $+z$ direction, we need only consider the conductivity in $x$ and $y$ and can write

    $$
    \rho =
    \begin{pmatrix}
    \frac{m}{nq^2\tau} & \frac{Bq}{n} \\
    -\frac{Bq}{n} & \frac{m}{nq^2\tau}
    \end{pmatrix}
    $$

    which is true for both charge carrier species. Use this result to calculate the resistivity matrix in the case of a MIEC.

    To make life simpler, one can write

    $$
    \rho =
    \begin{pmatrix}
    r & B R \\
    -B R & r
    \end{pmatrix}
    $$

    where $r = m/(n q^2 \tau)$ and $R=q/n$. We can then define $\rho_e$ and $\rho_i$ for the two species. The conductivities are then $\sigma_j=\rho_j^{-1}$ for $j = e, i$, and then the total conductivity $\sigma_t = \sigma_e + \sigma_i$. The total resistivity is then $\rho = \sigma_t^{-1}$ \mrk{1}. The process is pretty algebra heavy, but the results are

    \begin{align}
    \rho_{xx} & = \frac{B^2 (r_e R_i^2 + r_i R_e^2) + r_i r_e (r_e + r_i)}{B^2 (R_e + R_i)^2 + (r_e + r_i)^2} \\
    \rho_{xy} & = \frac{B (B^2 R_e R_i (R_e + R_i) + R_i r_e^2 + R_e r_i^2 }{B^2 (R_e + R_i)^2 + (r_e + r_i)^2}
    \end{align}

    Note that using software to do this kind of grunt work is absolutely fine (encouraged even)

## Exercise 3 - Sommerfeld

1. In your own words, explain what is the Fermi energy, Fermi temperature and the Fermi surface

    The Fermi energy is the chemical potential at $T=0$, the Fermi temperature is the associated temperature $T_F = E_F/k_{\textrm{B}}$, and is the temperature at which thermal energy would dictate the properties of a material to the same degree as the fact they are fermions. The Fermi surface is the surface in momentum space which separates the filled and unfilled states _at zero temperature__.

2. Write an expression for the number of states for a gas of free electrons in three dimension and use this to calculate the Fermi wavenumber and Fermi Energy

    $$
    N = \frac{2V}{(2\pi)^3} \int_{k<k_F} \mathrm{d}\mathbf{k}
    $$

    The factor of two is _very_ important. The integral is just the volume of a sphere of radius $k_F$, this is, $4\pi k_F^3/3$ which then yields

    $$
    k_F = (3\pi^2 N/V)^{1/3}
    $$

    and thus the Fermi energy is

    $$
    E_F = \frac{\hbar^2(3\pi^2 N/V)^{2/3}}{2m}
    $$

3. Using the previous result, estimate the value of the Fermi energy for Caesium

    Caesium has a density of $1.93\textrm{g/cm^3}$ and a mass of approximately $133 \textrm{amu}$  (132.9055) and thus the density of atoms is

    $$
    N/V = (1.93 \textrm{g/cm^3}) \times (10^2 \textrm{cm/m})^3 \times (\frac{1}{133}\textrm{mol/g}) \times (N_A \textrm{atoms/mol}) = 8.7 \textrm{atoms/m^3}
    $$

    and with one valence electron, $N/V$ for electrons is identical and we can plug it into the expression for $E_F$ from part (ii) which returns $E_F = 2.48 \times 10^{-19} \textrm {J} = 1.6 \textrm{eV}$

4. Obtain an expression for the density of states at the Fermi surface of a \textbf{two-dimensional} free-electron gas.

    For a two-dimensional gas

    $$
    N = 2A \int_{k<k_F} \frac{\mathrm{d}\mathbf{k}}{(2\pi)^2} = \frac{2A}{(2\pi)^2}\pi k_F^2
    $$

    where (again) $A$ is the area and the integral is over a circle with radius $k_F$ (c.f. exercise 1 (ii), only a factor of two different due to polarisation). Therefore

    $$
    k_F = (2\pi N/A)^{1/2}
    $$

    and the Fermi energy is

    $$
    E_F = \frac{\hbar^2 (2\pi N/A)}{2m} = \frac{\hbar^2\pi N/A}{m}
    $$

    The density of states is then independent of energy and is given by

    $$
    \frac{\mathrm{d}N}{\mathrm{d}E} = \frac{Am}{\hbar^2\pi} = N/E_F
    $$

5. Using the above result, show that for a two-dimensional free-electron gas that the chemical potential $\mu$ is independent of temperature when $T \ll \mu$

    From above, we have the density of states which we note to be temperature independent. Thus, for a fixed density of electrons, the chemical potential is fixed by

    $$
    n = \int_0^{\infty} \mathrm{d}E~g(E)~\frac{1}{\exp\left(\beta(E-\mu)\right)+1}.
    $$

    The connection one must make is that except for corrections exponentially small in $\beta\mu$, the value of the integral is independent of $\beta$ and thus one can assume that the dependence of $n$ on $\mu$ is temperature independent.

    If one wants to do the maths, we write the density of states as a constant $g$ (see above) and then the integral above can be recast

    $$
    n = g \int_{-\mu}^{\infty} \mathrm{d}x~\frac{1}{\exp(\beta x)+1} = g \int_{-\mu}^{\infty} \mathrm{d}x \frac{\exp(-\beta x)}{\exp(-\beta x)+1} = \frac{g}{\beta} \log(\exp(\beta \mu)+1)
    $$

    And for large $\beta\mu$ (small) we can expand to have

    $$
    n/g = \mu + \mathcal{O}\left(\exp(-\beta\mu)\right)
    $$

    which means that provided $T \ll \mu$, there is no dependence on the temperature.

## Exercise 4 - chemistry

1. Explain using the simplest language you can muster why is there periodic table important?

    Ability to predict properties of elements, ability to predict properties of compounds, ability to group/classify elements with similar characteristics, displays trends

2. Choose a naturally occurring element with a high atomic number and use Madelung's Rule to deduce the shell filling configuration.

    The configuration for uranium is shown below, and all shell filling will be in this order:

    U: 1s$^2$2s$^2$2p$^6$3s$^2$3p$^6$4s$^2$3d$^{10}$4p$^6$5s$^2$4d$^{10}$5p$^6$6s$^2$4e$^{14}$5d$^{10}$6p$^6$7s$^2$5f$^4$

    which can be written in shorthand as [Rn]7s$^2$5f$^4$.

3. Using any tools at your disposal (i.e. use a computer) produce a plot of the energy eigenstate described by $|5, 2, 0 \rangle$. You must include your code and you will be partially assessed on presentation: producing content that is digestible and visually pleasing is an important part of modern science!

    I made a mistake here, I should have the angular dependence or something, as plotting the wavefunction in 3D is hard.

    The electronic states of hydrogen can be found in many places (e.g. [Wikipedia](https://en.wikipedia.org/wiki/Hydrogen_atom)) and are given by

    $$
    \psi _{n\ell m}(r,\theta ,\varphi )={\sqrt {{\left({\frac {2}{na_{0}^{*}}}\right)}^{3}{\frac {(n-\ell -1)!}{2n(n+\ell )!}}}}e^{-\rho /2}\rho ^{\ell }L_{n-\ell -1}^{2\ell +1}(\rho )Y_{\ell }^{m}(\theta ,\varphi )
    $$

    where $\rho = 2r/n a_0^*$, $a_0^*=4\pi\epsilon_0\hbar^2/\mu e^2$ is the reduced Bohr radius, $\mu = m_e M/(m_e + M)$ is the reduced mass, $L_{n-\ell -1}^{2\ell +1}(\rho )$ is the generalised Laguerre polynomial and $Y_{\ell }^{m}(\theta ,\varphi )$ is the spherical harmonic function.
