# Solutions to exercises

## Solutions for _The specific heat of solids I_ exercises

### Preliminary provocations

  1. $C = 2k_B$.
  2. ![](/images/01_Ex_0_2.svg)

### Exercise 1: Total heat capacity of a diatomic material
  1. Use the formula $\omega = \sqrt{\frac{k}{m}}$.

  2. Energy per atom is given by

  $$
  E = \frac{N_{^6Li}}{N}\hbar\omega_{^6Li}(2 + 1/2) + \frac{N_{^7Li}}{N}\hbar\omega_{^7Li}(4 + 1/2).
  $$

  3. Energy per atom is given by

  $$
  E = \frac{N_{^6Li}}{N}\hbar\omega_{^6Li}\left(n_B(\beta\hbar\omega_{^6Li}) + \frac{1}{2}\right) + \frac{N_{^7Li}}{N}\hbar\omega_{^7Li}\left(n_B(\beta\hbar\omega_{^7Li}) + \frac{1}{2}\right).
  $$

  4. Heat capacity per atom is given by

  $$
  C = \frac{N_{^6Li}}{N}C_{^6Li} + \frac{N_{^7Li}}{N}C_{^7Li},
  $$

## Solutions for _The specific heat of solids II_ exercises

### Preliminary provocations
  1. The polarization is related to the direction of the amplitudes of the waves with respect to the direction of the wave.
  In 3D, there are only 3 different amplitude directions possible.
  2.
  $$
  \int k_x k_y \rightarrow \int_{0}^{2\pi} \mathrm{d} \theta \int_{0}^{\infty} k \mathrm{d} k = 2\pi \int_{0}^{\infty} k \mathrm{d} k
  $$
  3. The Debye frequency $\omega_D$.
  4. The wavelength is of the order of the interatomic spacing:
  $$
  \lambda = (\frac{4}{3}\pi)^{1/3} a.
  $$


### Exercise 1: Debye model: concepts.

  1. $k = \frac{4\pi}{L}$ and $k = -\frac{4\pi}{L}$.  
  2.
  3. The number of states per $k$ or per frequency.
  4.
  $$
  g(\omega) = \frac{dN}{d\omega} = \frac{dN}{dk}\frac{dk}{d\omega} = \frac{1}{v}\frac{dN}{dk}.
  $$
  We assume that in $d$ dimensions there are $d$ polarizations.

  For 1D we have that $N = \frac{L}{2\pi}\int_{-k}^{k} dk$, hence $g(\omega) = \frac{L}{\pi v}$.

  For 2D we have that $N = 2\left(\frac{L}{2\pi}\right)^2\int d^2k = 2\left(\frac{L}{2\pi}\right)^2\int 2\pi kdk$, hence $g(\omega) = \frac{L^2\omega}{\pi v^2}$.

  For 3D we have that $N = 3\left(\frac{L}{2\pi}\right)^3\int d^3k = 3\left(\frac{L}{2\pi}\right)^3\int 4\pi k^2dk$, hence $g(\omega) = \frac{3L^3\omega^2}{2\pi^2v^3}$.

###  Exercise 2: Debye model in 2D.

  1. See lecture notes.
  2. $$
  \begin{align}
  E &= \int_{0}^{\omega_D}g(\omega)\hbar\omega\left(\frac{1}{e^{\beta\hbar\omega} - 1} + \frac{1}{2}\right)d\omega \\
  &= \frac{L^2}{\pi v^2\hbar^2\beta^3}\int_{0}^{\beta\hbar\omega_D}\frac{x^2}{e^{x} - 1}dx + C.
  \end{align}
  $$
  3. High temperature implies $\beta \rightarrow 0$, hence $E = \frac{L^2}{\pi v^2\hbar^2\beta^3}\frac{(\beta\hbar\omega_D)^2}{2} + C$, and then $C = \frac{k_BL^2\omega^2_D}{2\pi v^2} = 2Nk_B$. We've used the value for $\omega_D$ calculated from $2N = \int_{0}^{\omega_D}g(\omega)d\omega$.
  4. In the low temperature limit we have that $\beta \rightarrow \infty$, hence $E \approx \frac{L^2}{\pi v^2\hbar^2\beta^3}\int_{0}^{\infty}\frac{x^2}{e^{x} - 1}dx + C = \frac{2\zeta(3)L^2}{\pi v^2\hbar^2\beta^3} + C$. Finally $C = \frac{6\zeta(3)k^3_BL^2}{\pi v^2\hbar^2}T^2$. We used the fact that $\int_{0}^{\infty}\frac{x^2}{e^{x} - 1}dx = 2\zeta(3)$ where $\zeta$ is the Riemann zeta function.

###  Exercise 3: Different phonon modes.

  1. $$
  g(\omega) = \sum_{\text{polarizations}}\frac{dN}{dk}\frac{dk}{d\omega} = \left(\frac{L}{2\pi}\right)^3\sum_{\text{polarizations}}4\pi k^2\frac{dk}{d\omega} = \frac{L^3}{2\pi^2}\left(\frac{2}{v_\perp^3} + \frac{1}{v_\parallel^3}\right)\omega^2
  $$
  $$
  E = \int_{0}^{\omega_D}g(\omega)\hbar\omega\left(\frac{1}{e^{\beta\hbar\omega} - 1} + \frac{1}{2}\right)d\omega = \frac{L^3}{2\pi^2\hbar^3\beta^4}\left(\frac{2}{v_\perp^3} + \frac{1}{v_\parallel^3}\right)\int_{0}^{\beta\hbar\omega_D}\frac{x^3}{e^{x} - 1}dx + C.
  $$

  2. Note that we can get $\omega_D$ from $3N = \int_{0}^{\omega_D}g(\omega)$ so everything cancels as usual and we are left with the Dulong-Petit law $C = 3Nk_B$.
  3. In the low temperature limit we have that $C \sim \frac{2\pi^2k_B^4L^3}{15\hbar^3}\left(\frac{2}{v_\perp^3} + \frac{1}{v_\parallel^3}\right)T^3$. We used that $\int_{0}^{\infty}\frac{x^3}{e^{x} - 1}dx = \frac{\pi^4}{15}$.

### Exercise 4: Anisotropic sound velocities.

  $$
  E = 3\left(\frac{L}{2\pi}\right)^3\int d^3k\hbar\omega(\mathbf{k})\left(n_B(\beta\hbar\omega(\mathbf{k})) + \frac{1}{2}\right) = 3\left(\frac{L}{2\pi}\right)^3\frac{1}{v_xv_yv_z}\int d^3\kappa\frac{\hbar\kappa}{e^{\beta\hbar\kappa} - 1} + C,
  $$

  where we used the substitutions $\kappa_x = k_xv_x,\kappa_y = k_yv_y, \kappa_z = k_zv_z$. Finally

  $$
  E = \frac{3\hbar L^3}{2\pi^2}\frac{1}{v_xv_yv_z}\int_0^{\kappa_D} d\kappa\frac{\kappa^3}{e^{\beta\hbar\kappa} - 1} + C = \frac{3L^3}{2\pi^2\hbar^3\beta^4}\frac{1}{v_xv_yv_z}\int_0^{\beta\hbar\kappa_D} dx\frac{x^3}{e^{x} - 1} + C,
  $$

  hence $C = \frac{\partial E}{\partial T} = \frac{6k_B^4L^3T^3}{\pi^2\hbar^3}\frac{1}{v_xv_yv_z}\int_0^{\beta\hbar\kappa_D} dx\frac{x^3}{e^{x} - 1}$. We see that the result is similar to the one with the linear dispersion, the only difference is the factor $1/v_xv_yv_z$ instead of $1/v^3$.

## Solutions for _Electrons in metals I_ exercises

### Exercise 1: Extracting quantities from basic Hall measurements

  1. Hall voltage is measured across the sample width. Hence,

    $$
    V_H = -\int_{0}^{W} E_ydy
    $$

    where $E_y = -v_xB$.

    $R_{xy}$ = $-\frac{B}{ne}$, so it does not depend on the sample geometry.


  2. If hall resistance and magnetic field are known, the charge density is calculated from $R_{xy} = -\frac{B}{ne}$. As $V_x = -\frac{I_x}{ne}B$, a stronger field makes Hall voltages easier to measure.

  3.
  $$
  R_{xx} = \frac{\rho_{xx}L}{W}
  $$

  where $ \rho_{xx} = \frac{m_e}{ne^2\tau}$. Therefore, scattering time ($\tau$) is known and $R_{xx}$ depend upon the sample geometry.

### Exercise 2: Motion of an electron in a magnetic and an electric field

  1.

  $$
  m\frac{d\bf v}{dt} = -e(\bf v \times \bf B)
  $$

  Magnetic field affects only the velocities along x and y, i.e., $v_x(t)$ and $v_y(t)$ as they are perpendicular to it. Therefore, the equations of motion for the electron are

  $$
  \frac{dv_x}{dt} = -\frac{e v_y B_z}{m}
  $$

  $$
  \frac{dv_y}{dt} = \frac{e v_x B_z}{m}
  $$

  2. We can compute $v_x(t)$ and $v_y(t)$ by solving the differential equations in 1.

  From

  $$
  v_x'' = -\frac{e^2B_z^2}{m^2}v_x
  $$

  and the initial conditions, we find $v_x(t) = v_0 \cos(\omega_c t)$ with $\omega_c=eB_z/m$. From this we can derive $v_y(t)=v_0\sin(\omega_c t)$.

  We now calculate the particle position using $x(t)=x(0) + \int_0^t v_x(t')dt'$ (and similar for $y(t)$). From this we can find a relation between the $x$- and $y$-coordinates of the particle

  $$
  (x(t) - x_0)^2 + (y(t) - y_0)^2 = \frac{v_0^2}{\omega_c^2}.
  $$

  This equation describes a circular motion around the point $x_0=x(0), y_0=y(0)+v_0/\omega$, where the characteristic frequency $\omega_c$ is called the *cyclotron* frequency. Intuition: $\frac{mv^2}{r} = evB$ (centripetal force = Lorentz force due to magnetic field).

  3. Due to the applied electric field $\bf E$ in the $x$-direction, the equations of motion acquire an extra term:

  $$
  m v_x' = -e(E_x + v_yB_z).
  $$

  Differentiating w.r.t. time leads to the same 2nd-order D.E. for $v_x$ as above. However, for $v_y$ we get

  $$
  v_y'' = -\omega_c^2(v_d+v_y),
  $$

  where we defined $v_d=\frac{E_x}{B_z}$. The general solutions are

  $$
  v_y(t) = c_1\sin(\omega_c t)+ c_2\cos(\omega_c t) -v_d \\
  v_x(t) = c_3\sin(\omega_c t)+ c_4\cos(\omega_c t).
  $$

  Using the initial conditions $v_x(0)=v_0$ and $v_y(0)=0$ and the 1st order D.E. above, we can show

  $$
  v_y(t) = v_0\sin(\omega_c t)+ v_d\cos(\omega_c t) -v_d \\
  v_x(t) = v_d\sin(\omega_c t)+ v_0\cos(\omega_c t).
  $$

  By integrating the expressions for the velocity we find:

  $$
  (x(t)-x_0)^2 + (y(t) - y_0 + v_d t))^2 = \frac{v_0^2}{\omega_c^2}.
  $$

  This represents a [cycloid](https://en.wikipedia.org/wiki/Cycloid#/media/File:Cycloid_f.gif): a circular motion around a point that moves in the $y$-direction with velocity $v_d=\frac{E_x}{B_z}$.

  <!---
  4.
  See 3_drude_model.md

  $$
  m\left(\frac{d\bf v}{dt} + \frac{\bf v}{\tau}\right) = -e(\bf E + \bf v \times \bf B)
  $$
  -->

### Exercise 3: Temperature dependence of resistance in the Drude model

  1. Find electron density from

  $$
  n_e = \frac{Z n N_A}{W}
  $$

  where *Z* is valence of copper atom, *n* is density, $N_A$ is Avogadro constant and *W* is atomic weight. Use $\rho = 1/\sigma$ from the lecture notes to calculate scattering time.

  $$
  \sigma = \frac{n e^2 \tau}{m}
  $$

  2. $\lambda = \langle v \rangle\tau$

  3. Scattering time $\tau \propto \frac{1}{\sqrt{T}}$; $\rho \propto \sqrt{T}$

  4. In general, $\rho \propto T$ as the phonons in the system scales linearly with T (remember high temperature limit of Bose-Einstein factor becomes $\frac{kT}{\hbar\omega}$ leading to $\rho \propto T$). Inability to explain this linear dependence is a failure of the Drude model.

### Exercise 4: The Hall conductivity matrix and the Hall coefficient

1. $\rho_{xx}$ is independent of B and

$\rho_{xy} \propto B$

2.
$$
\sigma_{xx} = \frac{\rho_{xx}}{\rho_{xx}^2 + \rho_{xy}^2}
$$

$$
\sigma_{xy} = \frac{-\rho_{yx}}{\rho_{xx}^2 + \rho_{xy}^2}
$$

This describes a [Lorentzian](https://en.wikipedia.org/wiki/Spectral_line_shape#Lorentzian).

## Solutions for exercises lecture 4: Sommerfeld model

### Warm-up questions
  1.
  $$
  E = \int \limits_0^{\infty} g(\varepsilon) n_{F}(\beta (\varepsilon - \mu)) \varepsilon \mathrm{d} \varepsilon
  $$

  2. The electronic heat capacity $C_e$ approaches $3N k_B$.

  3. Thermal smearing is too significant and we can not accurately approximate the fraction of the excited electron with triangles anymore. Thus the Sommerfeld expansion breaks down.

  4. Electrons.

### Exercise 1: potassium

1. Alkali metals mostly have a spherical Fermi surface. Their energy depends only on the magnitude of the Fermi wavevector.

2. Refer to the lecture notes.

3. Electrons are fermions and obey the Pauli exclusion principle. As electrons cannot occupy the same state, they are forced to occupy higher energy states resulting in high Fermi energy and high Fermi temperature.

4.
$$
n = \frac{N}{V} = \frac{1}{3 \pi^{2} \hbar^{3}}\left(2 m \varepsilon_{F}\right)^{3 / 2}
$$

5.
$$
n = \frac{\rho N_A Z}{M},
$$
where $\rho$ is the density, $N_A$ is the Avogadro's constant, $M$ is molar mass and $Z$ is the valence of potassium atom.
Comparing total and free electron density, only few electrons are available for conduction which is roughly 1 free electron per potassium atom.


### Exercise 3: a hypothetical material

1.
$$
E = \int_{0}^{\infty}\varepsilon g(\varepsilon) n_{F}(\beta (\varepsilon - \mu)) \textrm{d} \varepsilon = 2.10^{10}eV^{-\frac{3}{2}}  \int_{0}^{\infty}\frac{\varepsilon^{\frac{3}{2}}}{e^\frac{\varepsilon-5.2}{k_BT}+1} \textrm{d} \varepsilon
$$

2.
$$
E = \frac{4}{5} (5.2)^{\frac{5}{2}} 10^{10} eV
$$

3.
$$
\begin{align}
E(T)-E(T=0) &= \frac{\pi^2}{6}(k_B T)^2\frac{\partial}{\partial \varepsilon}\left(\varepsilon g(\varepsilon)\right)\bigg|_{\varepsilon=\varepsilon _F}\\
&\approx 8.356 10^8 eV
\end{align}
$$

5.

$C_v = 1.6713.10^6 eV/K$

4, 6.

```python
mu = 5.2
kB = 8.617343e-5
T = 1000 #kelvin

import numpy as np
from scipy import integrate

np.seterr(over='ignore')

# Fermi-Dirac distribution
def f(E, T):
    return 1 / (np.exp((E - mu)/(kB*T)) + 1)

# Density of states
def g(E):
    return 2e10 * np.sqrt(E)

#integration function
def integral(E, T):
    return f(E, T)*g(E)*E

## Solve integral numerically using scipy's integrate
dE = integrate.quad(integral, 0, 1e1, args=(T))[0] - 0.8e10 * 5.2**(5./2)

dT = 0.001
dEplus = integrate.quad(integral, 0, 1e1, args=(T+dT))[0] - 0.8e10 * 5.2**(5./2)
dEmin = integrate.quad(integral, 0, 1e1, args=(T-dT))[0] - 0.8e10 * 5.2**(5./2)

CV = (dEplus - dEmin) / (2*dT);

print(f'dE = {dE:.4e} eV')
print(f'Cv = {CV:.4e} eV/K')
```
Check the source code written in python for solving integral using midpoint rule.

### Exercise 3: graphene

1.

```python
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-1, 1, 100)
fig, ax = plt.subplots(figsize=(7, 5))
ax.plot(x, x, 'b')
ax.plot(x,-x, 'b')

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position(('data', 0.0))

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.set_xticks([])
ax.set_yticks([])

ax.set_xlabel(r'$\mid \vec k \mid$', fontsize=14)
ax.set_ylabel(r'$\varepsilon$', fontsize=18, rotation='horizontal')
ax.yaxis.set_label_coords(0.5,1)
ax.xaxis.set_label_coords(1.0, 0.49)
```

2.The DOS for the positive energies is given by
$$
g(\varepsilon) = 2_s 2_v 2 \pi \left(\frac{L}{2 \pi}\right)^2 \frac{\varepsilon}{c^2},
$$
where $2_s$ is the spin degeneracy and $2_v$ is the valley degeneracy.
If we account for the negative energies as well, we obtain
$$
g(\varepsilon) = 2_s 2_v 2 \pi \left(\frac{L}{2 \pi}\right)^2 \frac{|\varepsilon|}{c^2}.
$$

3.$g(\varepsilon)$ vs $\varepsilon$ is a linear plot. Here, the region marked by $-k_B T$ is a triangle whose area gives the number of electrons that can be excited:
$$
\begin{align}
n_{ex} &= \frac{1}{2} g(-k_B T) k_B T\\
&= \frac{L^2 k_B^2T^2}{\pi c^2}.
\end{align}
$$
From this it follows that the energy difference is given by
$$
E(T) - E_0 = \frac{L^2 k_B^3T^3}{\pi c^2}.
$$

4.
$$
C_v(T) = \frac{\partial E}{\partial T} = \frac{3L^2k_B^3T^2}{\pi c^2}
$$
