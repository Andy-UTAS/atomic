#!/usr/bin/python

"""
Atomic.py: a program to deliver required content for jupyter notebooks to compliment the atomic physics course
"""

######### Make default plot style #########
import matplotlib

# Define the default plot style through rcParams
def setplotstyle():
    matplotlib.rcParams['text.usetex'] = False
    matplotlib.rcParams['figure.figsize'] = (10, 7)
    matplotlib.rcParams['font.size'] = 16
    matplotlib.rcParams['axes.linewidth'] = 2.5
    for p in ['xtick', 'ytick']:
        matplotlib.rcParams[p+'.major.size'] = 10
        matplotlib.rcParams[p+'.minor.size'] = 5
        matplotlib.rcParams[p+'.major.width'] = 2.5
        matplotlib.rcParams[p+'.minor.width'] = 1.5

def draw_classic_axes(ax, x=0, y=0, xlabeloffset=.1, ylabeloffset=.07):
    ax.set_axis_off()
    x0, x1 = ax.get_xlim()
    y0, y1 = ax.get_ylim()
    ax.annotate(
        ax.get_xlabel(), xytext=(x1, y), xy=(x0, y),
        arrowprops=dict(arrowstyle="<-"), va='center'
    )
    ax.annotate(
        ax.get_ylabel(), xytext=(x, y1), xy=(x, y0),
        arrowprops=dict(arrowstyle="<-"), ha='center'
    )
    for pos, label in zip(ax.get_xticks(), ax.get_xticklabels()):
        ax.text(pos, y - xlabeloffset, label.get_text(),
                ha='center', va='bottom')
    for pos, label in zip(ax.get_yticks(), ax.get_yticklabels()):
        ax.text(x - ylabeloffset, pos, label.get_text(),
                ha='right', va='center')

def wavelength_to_rgb(wavelength, gamma=0.8):
    ''' taken from http://www.noah.org/wiki/Wavelength_to_RGB_in_Python
    This converts a given wavelength of light to an 
    approximate RGB color value. The wavelength must be given
    in nanometers in the range from 380 nm through 750 nm
    (789 THz through 400 THz).

    Based on code by Dan Bruton
    http://www.physics.sfasu.edu/astro/color/spectra.html
    Additionally alpha value set to 0.5 outside range
    '''
    wavelength = float(wavelength)
    if wavelength >= 380 and wavelength <= 750:
        A = 1.
    else:
        A=0.5
    if wavelength < 380:
        wavelength = 380.
    if wavelength >750:
        wavelength = 750.
    if wavelength >= 380 and wavelength <= 440:
        attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
        R = ((-(wavelength - 440) / (440 - 380)) * attenuation) ** gamma
        G = 0.0
        B = (1.0 * attenuation) ** gamma
    elif wavelength >= 440 and wavelength <= 490:
        R = 0.0
        G = ((wavelength - 440) / (490 - 440)) ** gamma
        B = 1.0
    elif wavelength >= 490 and wavelength <= 510:
        R = 0.0
        G = 1.0
        B = (-(wavelength - 510) / (510 - 490)) ** gamma
    elif wavelength >= 510 and wavelength <= 580:
        R = ((wavelength - 510) / (580 - 510)) ** gamma
        G = 1.0
        B = 0.0
    elif wavelength >= 580 and wavelength <= 645:
        R = 1.0
        G = (-(wavelength - 645) / (645 - 580)) ** gamma
        B = 0.0
    elif wavelength >= 645 and wavelength <= 750:
        attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
        R = (1.0 * attenuation) ** gamma
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0
    return (R,G,B,A)
        
######### Import packages #########
import math # math for basic mathematical operations
import pandas as pd # panads for data manipulation
import numpy as np # numpy for all things mathematical/numerical
import matplotlib.pyplot as plt # matplotlib.pyplot for plotting
from matplotlib.animation import FuncAnimation # matplotlib.animation for making animations
from matplotlib import cm, colors, colormaps # cm for colour maps
from mpl_toolkits.mplot3d import Axes3D  # Axes 3D for 3D plots, where Axes3D import has side effects: it enables using projection='3d' in add_subplot
from mpl_toolkits.axes_grid1.inset_locator import inset_axes # insert_axes for tweaking/aesthetics, notably colourbar placement
import plotly.offline as py
import plotly.graph_objs as go
from IPython.display import HTML 
# import wikitables
import scipy.constants as const # scipy.constants for physical constants
import scipy.special as sp # scipy.special for special functions
from scipy.optimize import curve_fit # scipy.optimize for curve fitting
import scipy.integrate as integrate #scipy.integrate for numerical integration
# from scipy.signal import find_peaks # scipy.signal for peak finding
from scipy.stats import norm, maxwell # scpipy.stats for normal distribution
import qutip # qutip for quantum calculations

######### "Global variables" (not actually gloabl variables in the python sense) #########
a0 = const.physical_constants['Bohr radius'][0] # Bohr radius
c = const.c # Speed of light
e = const.e # Elementary charge
epsilon_0 = const.epsilon_0 # Vacuum permittivity
mu_0 = const.mu_0 # Vacuum magnetic permeability
h = const.h # Planck constant
hbar = const.hbar # Reduced Planck constant
kb = const.k # Boltzmann's constant
m_e = const.m_e # Mass of the electron 
R = const.R # Molar gas constant
R_infty = const.physical_constants['Rydberg constant times hc in eV'][0] # Rydberg constant in eV
mu_B = const.physical_constants['Bohr magneton in eV/T'][0] # Bohr magneton in units of eV/T
amu = const.physical_constants['atomic mass constant'][0] # Atomic mass unit kg
pi = np.pi # Pi

setplotstyle() # Set the plot style
savefigflag = True # Set the savefig flag to True, meaning produced figures will be saved. By default, this should be False and it is just here to help streamline content production

print('Atomic.py - the package for atomic physics content for use in KYA323 has been loaded. \n\nCore package versions are as follows:')
print('Matplotlib', matplotlib.__version__)
print('NumPy', np.__version__)