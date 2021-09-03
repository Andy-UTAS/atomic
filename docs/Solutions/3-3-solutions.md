# Solutions to exercises

## Solutions for _The specific heat of solids I_ exercises

# Solutions for lecture 7 exercises

## Warm up exercises
1. Check by yourself
2.
$$
[m^*] = \frac{[p^2]}{[E]} = kg
$$
3.
$$
m^* = m_e,
$$
where $m_e$ is the free electron mass. This is expected because the free elctrons are not subject to a potential
4. If the dispersion relation is parabolic, so in the free electron model.

## Exercise 1: Next-nearest neighbours chain

1.

The Schrödinger equation is given by: $|\Psi\rangle = \sum_n \phi_n |n\rangle$ such that we find $$ E\phi_n = E_0\phi_n - t\phi_{n-1} - t\phi_{n+1} - t'\phi_{n-2} - t'\phi_{n+2}$$

2.

Solving the Schrödinger equation yields dispersion: $$E(k) = E_0 -2t\cos(ka) -2t'\cos(2ka)$$

3.

$$m^* = \frac{\hbar^2}{2a^2}\frac{1}{t\cos(ka)+4t'\cos(2ka)}$$

Plot for t=t':

```python
k1 = np.linspace(-pi, -pi/2-0.01, 300);
k2 = np.linspace(-pi/2+0.01, pi/2-0.01, 300);
k3 = np.linspace(pi/2+0.01, pi, 300);

pyplot.plot(k1, 1/(5*np.cos(k1)),'b');
pyplot.plot(k2, 1/(5*np.cos(k2)),'b');
pyplot.plot(k3, 1/(5*np.cos(k3)),'b');
pyplot.xlabel(r'$k$'); pyplot.ylabel('$m_{eff}(k)$');
pyplot.xticks([-pi,0,pi],[r'$-\pi/a$',0,r'$\pi/a$']);
pyplot.yticks([],[]);
pyplot.tight_layout();
```

4.

Plots for 2t'=t, 4t'=t and 10t'=t:

```python
def m(k,t):
    return 1/(np.cos(k)+4*t*np.cos(2*k))

k1 = np.linspace(-1.6, -0.83, 300);
k2 = np.linspace(-0.826, 0.826, 300);
k3 = np.linspace(0.83, 1.6, 300);

pyplot.plot(k1, m(k1,2),'b');
pyplot.plot(k2, m(k2,2),'b');
pyplot.plot(k3, m(k3,2),'b',label='t=2t\'');
pyplot.xlabel('$k$'); pyplot.ylabel('$m_{eff}(k)$');
pyplot.xticks([-1.6,0,1.6],[r'$-\pi/a$',0,r'$\pi/a$']);
pyplot.yticks([0],[]);
pyplot.tight_layout();

k1 = np.linspace(-1.58, -0.81, 300);
k2 = np.linspace(-0.804, 0.804, 300);
k3 = np.linspace(0.81, 1.58, 300);

pyplot.plot(k1, m(k1,4),'r');
pyplot.plot(k2, m(k2,4),'r');
pyplot.plot(k3, m(k3,4),'r',label='t=4t\'');

k1 = np.linspace(-1.575, -0.798, 300);
k2 = np.linspace(-0.790, 0.790, 300);
k3 = np.linspace(0.798, 1.575, 300);

pyplot.plot(k1, m(k1,10),'k');
pyplot.plot(k2, m(k2,10),'k');
pyplot.plot(k3, m(k3,10),'k',label='t=10t\'');

pyplot.legend();
```
