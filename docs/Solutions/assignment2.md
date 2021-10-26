# Assignment 2: Bonding and harmonic chains

The second assignment can be found [here](../assignments/Assignment two.pdf).

## Exercise 1 - Bonding: not LCAO

1. In you own words, explain why ionic bonds occur, and what properties one would expect from and ionic solid.

    Ionic bonds occur as an electron is transferred from one atom to another, and the resulting ions attract each other. Typical properties are due to the nature of the bond being very strong, with materials having high melting temperatures, and usually being hard, brittle, and electrically insulating. They are also mostly soluble, but this is not of so much relevance here.

2. The (first) ionisation energy of sodium is roughly $5.14\mathrm{eV}$, and the electron affinity of chlorine is roughly $3.62$, and the bond length between the two atoms when a sodium chloride molecule is formed is roughly $0.236\mathrm{nm}$. Assuming that _all_ of the cohesive energy is due to the Coulomb interaction, calculate the bonding energy.

    The cohesive energy is related to the bond distance $d$ via

    $$
    E_{coh} = \frac{e^2}{4\pi\epsilon_0 d}.
    $$

    Using the value $d= 2.36 \unicode{x212B}$ one finds a cohesive enrgy of $6.10\mathrm{eV}$ and thus the total binding energy is

    $$
    E = -5.14 + 3.62 + 6.10 = 4.58 \mathrm{eV}
    $$

3. The measured value of the bonding energy of sodium chloride is $4.26\mathrm{eV}$. How does this compare to your value above? Justify your response.

    The calculated value above is slightly larger than the measured value with the reason for the discrepancy being there must be a repulsive fore between the ions (otherwise the would collapse into a singularity!) in addition to the Coulomb attraction, therefore reducing the size of the cohesive (binding) energy.

4. In our discussion of bonding, we did not explicitly discuss van der Waals bonding. Research what is the nature of the van der Waals bond, explicitly describing the origin of the attractive force formation and reason as to why the force is of the form $R^{-7}$

    Van der Waals forces are from correlated dipole fluctuations. If the electron is a given fixed position, there is a dipole moment $\mathbf{p} = e\mathbf{r}$ where $\mathbf{r}$ is the vector from the electron to the proton. With the electron "orbiting" (i.e, in an eigenstate), the average dipole moment is zero. However, if an electric field is applied to the atom, the atom will develop a polarisation (i.e., it will be more likely for the electron to be found on one side of the nucleus than on the other). We write

    $$
    \mathbf{p} = \chi \mathbf{E}
    $$

    with $\chi$ the polarisability. Now, let us suppose we have two such atoms, separated a distance $r$ in the $\hat{x}$ direction. Suppose one atom momentarily has a dipole moment $\mathbf{p}_1$ (for definiteness, suppose this dipole moment is in the $\hat{z}$ direction). Then the second atom will feel an electric field

    $$
    E = \frac{p_1}{4\pi\epsilon_0 r^3}
    $$

    in the negative $\hat{z}$ direction. The second atom then, due to its polarisability, develops a dipole moment $p_2 = \chi E$ which in turn is attracted to the first atom. The potential energy between these two dipoles is

    $$
    U=\frac{-\left|p_{1}\right|\left|p_{2}\right|}{4 \pi \epsilon_{0} r^{3}}=\frac{-p_{1} \chi E}{\left(4 \pi \epsilon_{0}\right) r^{3}}=\frac{-\left|p_{1}\right|^{2} \chi}{\left(4 \pi \epsilon_{0} r^{3}\right)^{2}}
    $$

    corresponding to a force which is attractive and proportional to $1/r7$. Note that while for a single isolated atom $\langle p \rangle = 0$ the result is proportional instead to $\langle |p|^2 \rangle \sim \langle |r|^2 \rangle$ with r the position of an electron, is nonzero.

## Exercise 2 - Bonding: LCAO

In our formulation of the LCAO formulation we assumed that orbitals were orthogonal, with the justification that the qualitative behaviour was still going to be fine.

Assume that we introduce a trial wavefunction:

\[
|\psi \rangle = \sum_{i=1}^{N} \phi_i |i\rangle
\]

however, we are not going to enforce that the state be orthogonal. Rather, we define an overlap matrix $\mathcal{S}$ with elements

\[
\mathcal{S}_{i,j} = \langle i | j \rangle
\]

1. Show that with the above conditions, one arrives at an _effective_ Schrödinger equation

    \[
    \mathcal{H} \phi = E\mathcal{S}\phi
    \]

    where

    \[
    \mathcal{H}_{i,j} = \langle i | \hat{H} | j \rangle
    \]

    and $\phi$ is the vector of the coefficients for the $\phi_i$.

    This is the variational method 101. It is necessary to compute $E$ through

    $$
    E=\frac{\langle\psi|H| \psi\rangle}{\langle\psi \mid \psi\rangle}=\frac{\sum_{n, m} \phi_{n}^{*} \mathcal{H}_{n m} \phi_{m}}{\sum_{n, m} \phi_{n}^{*} S_{n m} \phi_{m}}
    $$

    which must then be minimised with respect to the $\phi_n$. This is most simply done by differentiating with respect to $\phi_n^*$ and solving for the root(s):

    $$
    \begin{aligned}
    0 =\frac{\partial E}{\partial \phi_{n}^{*}} & =\frac{\sum_{m} \mathcal{H}_{n m} \phi_{m}}{\sum_{n, m} \phi_{n}^{*} S_{n m} \phi_{m}}-\left(\frac{\sum_{n, m} \phi_{n}^{*} \mathcal{H}_{n m} \phi_{m}}{\sum_{n, m} \phi_{n}^{*} S_{n m} \phi_{m}}\right) \frac{\sum_{n, m} S_{n m} \phi_{m}}{\sum_{n, m} \phi_{n}^{*} S_{n m} \phi_{m}} \\
    & =\sum_{m} \mathcal{H}_{n m} \phi_{m}-E \sum_{m} S_{n m} \phi_{m}
    \end{aligned}
    $$

    where we have used the definition of $E$ above to simplify the 2nd term in the top line. This is exactly the result required.

2. Consider the case where N=2 (i.e. the diatomic case) and the orbitals are $s$ ($l=0$) orbitals. Use the above equation to solve for the energy eigenvalues of the system.

    Firstly, the reason we consider $s$ states is because an $s$ orbital can be taken to be manifestly positive everywhere (it has no nodes), so overlaps $S_{ij}$ must be real and positive, making life a little easier.

    In order to solve the equation

    \[
    \mathcal{H} \phi = E\mathcal{S}\phi
    \]

    it is simplest to solve the eigenvalue problem

    \[
    \mathcal{S}^{-1}\mathcal{H} \phi = E\phi.
    \]

    As we normally do, we write the Hamiltonian $\mathcal{H}$ as

    $$
    \mathcal{H}=\left(\begin{array}{cc}
    \epsilon & t \\
    t^{*} & \epsilon
    \end{array}\right)
    $$

    with $t$ the hopping and $\epsilon = \epsilon_0 + V_{\mathrm{cross}}$, and the overlap matrix is just

    $$
    \mathcal{S}=\left(\begin{array}{cc}
    1 & S \\
    S & 1
    \end{array}\right)
    $$

    where we have defined the only non-trivial element $\mathcal{S}_{12} = S$. We then need to diagonalise

    $$
    \mathcal{S}^{-1} \mathcal{H}=\frac{1}{1-S^{2}}\left(\begin{array}{cc}
    \epsilon-S t & t-\epsilon S \\
    t-\epsilon S & \epsilon-S t
    \end{array}\right)
    $$

    which has eigenvalues

    \begin{equation}
    E_{\pm} = \frac{1}{1-S^2}\left( |\epsilon - S t| \pm |t - \epsilon S| \right).
    \end{equation}

## Exercise 3 - Quantum thermal expansion

In a _content unpacking_ session, we discussed thermal expansion arising from the anharmonic term in the interatomic potential. Assume masses $m_1$ and $m_2$ for the interacting particles and let's consider an anharmonic perturbation $\delta V$

\[
\delta V = -\frac{\kappa_3}{6}(x-x_0)^3
\]

to the one-dimensional quantum harmonic oscillator $H_0$:

\[
H_0 = \frac{p^2}{2m}+\frac{\kappa}{2}(x-x_0)^2.
\]

To first order in $\kappa_3$, it can be shown that

\[
\langle n | x | n \rangle = x_0 + \frac{E_n \kappa_3}{2\kappa^2}
\]

where $|n\rangle$ is the eigenstate of the harmonic oscillator with

\[
E_n = \hbar\omega \left(n+\frac{1}{2}\right)
\]

1. What is the value of $\omega$ in terms of $m_1$ and $m_2$?

    The relationship between frequency and mass for a harmonic oscillator is

    $$
    \omega = \sqrt{\frac{\kappa}{m}}
    $$

    and given our system is comprised of two masses $m_1$ and $m_2$, we should use the _reduced_ mass $\mu$:

    $$
    \mu = \frac{m_1 m_2}{m_1 + m_2}
    $$

2. What is the interpretation of the $|0\rangle$ state?

    The $|0\rangle$ state is the ground state of the harmonic oscillator, which has some notable features, but most relevant is that the energy is not equal to the minimum of the potential, but rather $\hbar\omega/2$ above the minimum, and therefore the will be fluctuations in both the position and momentum of the trapped particle around the minimum which is what gives rise to the average separation of atoms.


3. The expectation value of $x$ as a function of temperature is written as

    \[
    \langle x \rangle_{\beta} = \frac{\sum_n \langle n | x | n \rangle e^{-\beta E_n}}{\sum_n e^{-\beta E_n}}
    \]

    1. Find the coefficient of thermal expansion

        Just crank the handle:

        $$
        \begin{aligned}
        \langle x\rangle_{\beta} &=\frac{\sum_{n}\langle n|x| n\rangle e^{-\beta E_{n}}}{\sum_{n} e^{-\beta E_{n}}}=\frac{\sum_{n} \left(x_{0}+E_{n} \kappa_{3} /\left(2 \kappa^{2}\right) \right) e^{-\beta E_{n}}}{\sum_{n} e^{-\beta E_{n}}} \\
        &=x_{0}+\frac{\langle E\rangle_{\beta} \kappa_{3}}{2 \kappa^{2}}
        \end{aligned}
        $$

        where $\langle E \rangle_\beta$ is the energy expectation of a harmonic oscillator of frequency $\omega$ at temperature $\beta = 1/(k_{\mathrm{B}} T)$. It is fine to use the result that  $\langle E \rangle_\beta$ directly:

        $$
        \begin{aligned}
        \langle E\rangle_\beta &=-(1 / Z) \partial Z / \partial \beta=(\hbar \omega / 2) \operatorname{coth}(\beta \hbar \omega / 2) \\
        &=\hbar \omega\left(n_{B}(\beta \hbar \omega)+\frac{1}{2}\right)
        \end{aligned}
        $$

        but this can be derived easily enough from the partition function:

        $$
        \begin{aligned}
        Z_{1 d} &=\sum_{n \geq 0} e^{-\beta \hbar \omega(n+1 / 2)} \\
        &=e^{-\beta \hbar \omega / 2} 1 /\left(1-e^{-\beta \hbar \omega}\right) \\
        &=1 /[2 \sinh (\beta \hbar \omega / 2)]
        \end{aligned}
        $$

        Combining the above equations one arrives at

        $$
        \langle x\rangle_{\beta}=x_{0}+\left(\kappa_{3} \hbar \omega /\left(4 \kappa^{2}\right)\right) \operatorname{coth}(\beta \hbar \omega / 2)
        $$

        and then the coefficient of thermal expansion is then

        $$
        \alpha=\frac{1}{x_{0}} \frac{d\langle x\rangle_{\beta}}{d T}=\frac{\kappa_{3}}{2 x_{0} \kappa^{2}} \frac{d\langle E\rangle}{d T}
        $$

        The term $\frac{d\langle E\rangle}{d T}$ is identified as the specific heat $C$, and the specific heat of the a harmonic oscillator was covered when discussing the Einstein model of a solid, but can be calculated directly from the equation for $\langle E \rangle_\beta$ to yield

        \begin{equation}
        \alpha=\frac{\kappa_{3} C}{2 x_{0} \kappa^{2}}=\frac{\kappa_{3}}{2 x_{0} \kappa^{2}} k_{b}(\beta \hbar \omega)^{2} \frac{e^{\beta \hbar \omega}}{\left(e^{\beta \hbar  \omega}-1\right)^{2}}
        \end{equation}


    2. What is the behaviour of the coefficient at both high and low temperature, and comment on the physical significance of these results.

    In the low-temperature limit, the modes "freeze" out, entirely analogous to the specific heat dropping out at low temperature (there needs to be a minimum energy put into the system to enact change because of the quantised states of the harmonic oscillator).

    In the high-temperature limit, $C \rightarrow k_{\mathrm{B}}$ so one obtains

    $$
    \alpha = \frac{\kappa_3 k_{\mathrm{B}}}{2 x_0 \kappa^2}
    $$

    in agreement with the classical result, and this result is valid when $k_{\mathrm{B}} T \gg \hbar \omega.$

## Exercise 4 - One-dimensional oscillations

1. Explain what is meant by a _normal mode_ and a _phonon_

    A _normal mode_ is a periodic collective motion where all particles move at the same frequency. A _phonon_ is a quantum of vibration.

    People tend to be confused by phonons, so to explicitly connect the two and explain why phonons are bosons: each classical normal mode of vibration corresponds to a quantum mode of vibration which can be excited multiple times. A single mode may be occupied by a single phonon, or it may be occupied with multiple phonons corresponding to a larger amplitude oscillation. The fact that the same state may be multiply occupied by phonons means that phonons must be bosons.

2. Derive the dispersion relation for longitudinal oscillations of an infinite one-dimensional chain of identical atoms, assuming mass $m$, spring constant $\kappa$, and lattice spacing $a$

    The equation of motion of the $n^{\textrm{th}}$ particle along the chain is given by

    $$
    m \ddot{x}_{n}=\kappa\left(x_{n+1}-x_{n}\right)+\kappa\left(x_{n-1}-x_{n}\right)=\kappa\left(x_{n+1}+x_{n-1}-2 x_{n}\right)
    $$

    where $na$ is the equilibrium position of the $n^{\textrm{th}}$ particle. Looking for solutions of the form

    $$
    x_n = A e^{i\omega t - i k n a}
    $$

    one obtains

    $$
    \begin{aligned}
    -\omega^{2} m e^{i \omega t-i k n a} &=\kappa e^{i \omega t}\left(e^{i k(n+1) a}+e^{i k(n-1) a}-2 e^{i k n}\right) \\
    \omega^{2} m &=2 \kappa(\cos (k a)-1)
    \end{aligned}
    $$

    which can be recast as

    $$
    \omega = \sqrt{\frac{2\kappa}{m}\left(\cos(ka)-1\right)} = 2\sqrt{\frac{\kappa}{m}}\left|\sin\left(\frac{ka}{2}\right)\right|
    $$

3. Show that a the mode with wavevector $k$ is equivalent to the mode $k + 2\pi/a$

    $$
    e^{-i(k+2\pi/a)na} = e^{-i k n a} e^{-i 2\pi n} = e^{-i k n a}
    $$

4. Assuming periodic boundary conditions, how many different modes are there?

    If one assumes periodic boundary conditions, then $k = 2 \pi m/L$, but $k$ is identified with $k + 2 \pi /a$ so that there are therefore exactly $N = L/a$ different normal modes.

5. Find expressions for and plot both the group and phase velocities

    The phase velocity is calculated via

    $$
    v_p = \omega/k = \frac{2\sqrt{\frac{\kappa}{m}}\left|\sin\left( \frac{ka}{2} \right)\right|}{k}
    $$

    and the group velocity is

    $$
    v_g = \frac{d\omega}{dk} = a\sqrt{\frac{\kappa}{m}} \cos\left(\frac{|k|a}{2}\right) = \frac{a \omega_0}{2}\sqrt{1-\frac{\omega^2}{\omega_0^2}}
    $$

    where $\omega_0 = 2\sqrt{\kappa/m}$.

    To plot this, code such as that below

    ``` python
    kappa = 1
    m = 1
    a = 1

    def omega(k):
       return 2 * np.sqrt(kappa/m) * abs(np.sin(k * a / 2))

    def v_p(k):
       return omega(k)/k

    def v_g(k):
       omega_0 = 2 * np.sqrt(kappa/m)
       return omega_0 * (a/2) * np.sqrt(1 - (omega(k)/omega_0) ** 2)

    fig, ax = plt.subplots()
    k = np.linspace(-np.pi+0.01, np.pi-0.01, 300)

    ax.plot(k[0:149], v_p(k[0:149]), color = 'C0', label = 'Phase velocity');
    ax.plot(k[150:300], v_p(k[150:300]), color = 'C0');
    ax.plot(k[0:149], -v_g(k[0:149]), color = 'C1', label = 'Group velocity');
    ax.plot(k[150:300], v_g(k[150:300]), color = 'C1');
    ax.set_title('Velocities')
    ax.set_xlabel(r'$k$');
    ax.set_ylabel('$v(k)$');
    plt.xticks([-np.pi, 0, np.pi], [r'$-\pi/a$', 0, r'$\pi/a$']);
    plt.yticks([-1, 0, 1], [r'$-2\sqrt{\frac{\kappa}{m}}$', 0, r'$2\sqrt{\frac{\kappa}{m}}$']);
    plt.legend();
    plt.tight_layout();

    plt.savefig('A2-4-v.pdf', facecolor='white', transparent=False)

    plt.show()
    ```

    will yield this plot:

    ![](../images/A2-4-v.svg)

6. Find an expression for the density of states $g(\omega)$ and plot $g(\omega)$

    The density of states is uniform in $k$: if there are $N$ sites in the system, there are $N$ modes total and the density of states is therefore $dN/dk = Na/(2\pi) = L/(2\pi)$ where $L$ is the length of the system. We then have

    $$
    \begin{aligned}
    g(\omega) &=d N / d \omega=(d N / d k)(d k / d \omega)=\frac{N a}{2 \pi v_{\text {group }}} \\
    &=\frac{N}{2 \pi \sqrt{\kappa / m} \cos (|k| a / 2)} \\
    &=\frac{2 N}{2 \pi \sqrt{(\kappa / m)-(\omega(k) / 2)^{2}}}
    \end{aligned}
    $$

    where we have used

    $$
    \left(\frac{\omega}{2}\right)^2 + \left(\frac{v_g}{a}\right)^2 = \frac{\kappa}{m}
    $$

    where in turn we have used the equation for the group velocity (previous question) to obtain the above identity.

    Note that the additional factor of 2 that appears in the numerator is to account for the fact that for each value of $\omega > 0$ there are actually two values of $k$ with that $\omega$, to ensure that if you integrate over frequency you correctly get back $N$ degrees of freedom.

    ![](../images/A2-4-dos.svg)

    The above plot was produced using the code below

    ``` python
    N = 1
    fig, ax = plt.subplots()
    w = np.linspace(0, np.pi/a - 1.15, 300);
    g = (2*N)/(2 * np.pi * np.sqrt((kappa/m)-(w/2)**2));
    ax.plot(w, g, 'C0');
    ax.set_xlabel(r'$\omega$');
    ax.set_ylabel('$g(\omega) [N/(\pi \sqrt{k/m})]$');
    ax.set_title('Density of states')
    plt.yticks([N/(np.pi * np.sqrt(kappa/m)), 2, 3], [1, 2, 3]);
    ax.set_ylim(0,3)
    plt.tight_layout();
    plt.savefig('A2-4-dos.pdf', facecolor='white', transparent=False)
    plt.show()
    ```  

7. Using $g(\omega)$, find an expression for the heat capacity and use any tools at your disposal to plot the heat capacity versus temperature

    The energy stored in the chain is given by

    $$
    U = \int d\omega~g(\omega)~\hbar \omega \left(n_{\textrm{B}}(\omega)+1/2\right)
    $$

    and so the heat capacity is $\partial U/\partial T$. The factor of 1/2 can be ignored as it is a temperature independent constant and thus will vanish upon differentiation.

    Plotting this requires numerical integration of the above equation, and one should get a plot similar to that as shown below, with the values on the $x$ axis changing with the parameters $\kappa$, $m$, and $a$.

    Code to perform the numerical integration appears below, with the highlighted lines actually performing the integration

    ``` python hl_lines="9-16"
    a = 1e-10

    def integrand(w):
      b = 1/T
      nb = 1/(np.exp(b * w) - 1)
      g = (2*N)/(2 * np.pi * np.sqrt((kappa/m)-(w/2)**2))
      return g * w * nb

    temp = np.linspace(0.01, 5, 150)
    U = []

    for T in temp:
      U.append(integrate.quad(integrand, 0, 2*np.sqrt(kappa/m))[0])

    dt = temp[1]-temp[0]
    dudt = np.gradient(U, dt)

    fig, ax = plt.subplots()
    ax.plot(temp, dudt)
    ax.set_xlabel('$T$ [K]')
    ax.set_ylabel('$C/k_\mathrm{B}$')
    ax.set_title('Specific heat')
    plt.savefig('A2-4-c.pdf', facecolor='white', transparent=False)
    plt.show()
    ```

    the output of which is shown here:

    ![](../images/A2-4-c.svg)
