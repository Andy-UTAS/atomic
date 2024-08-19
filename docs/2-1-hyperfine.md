---
comments: true

jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.0'
      jupytext_version: 1.0.2
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

```python tags=["initialize"]

from matplotlib import pyplot
import numpy as np

from common import draw_classic_axes, configure_plotting

configure_plotting()

```

# State vectors

_Time to do the same experiment lots of times and get different results_

## Introduction

![](header.png){ title="Stern-Gerlach separation of a Bose-Einstein condensate of Rubdiuim-87" }


```python
# Data from Einstein's paper
T = [222.4, 262.4, 283.7, 306.4, 331.3, 358.5, 413.0, 479.2, 520.0, 879.7, 1079.7, 1258.0]
c = [0.384, 0.578, 0.683, 0.798, 0.928, 1.069, 1.343, 1.656, 1.833, 2.671, 2.720, 2.781]

fig, ax = pyplot.subplots()
ax.scatter(T, c)
ax.set_xlabel('$T [K]$')
ax.set_ylabel('$C/k_B$')
ax.set_ylim((0, 3))
ax.set_title('Heat capacity of diamond')
fig.show()
```

---

## Conclusions

---

## Exercises

### Preliminary provocations
1. What happens if you happen to choose your variational wavefunction perfectly? That is, you trail wavefunction is an eigenstate of the Hamiltonian?

$$
E_0 \le \langle \psi | \mathscr{H} | \psi \rangle = E_0 \langle \psi | \psi \rangle = E_0
$$
as you might expect

### Heavy hitters


---

!!! info "Image credits"

    Header image taken from the PhD thesis [Spinor Bose-Einstein condensates in magnetic field gradients](https://bridges.monash.edu/articles/thesis/Spinor_Bose-Einstein_condensates_in_magnetic_field_gradients/4697395/1)

[^1]: more accurately, at this time it was the Bohr-Sommerfeld model, which is an extension of the Bohr model to include elliptical orbits which fixed some problems. One will also see in [solid-state physics](https://ssp.utasphys.cloud.edu.au/) that Sommerfeld has a real talent for tweaking existing theories to make them run a bit better.
[^2]: A study of the the relativistic wave equation, known as the _Dirac equation_, is required to fully flesh out this result.
[^3]: In this case we can, but more generally, the magnetic moment of the nucleus cannot be ignored (see LINK ME! hyperfine splitting)

--8<-- "includes/abbreviations.md"
