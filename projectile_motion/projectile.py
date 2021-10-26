"""This program plots the trajectory of a ballistic projtile fired on Earth and the Moon.

This program calls a function named 'projectilemotion' with a number of arguments
passed in as variables such as initial displacement in 'x' and 'y' domain, initial
velocity, as well as the launch angle and acceleration due to gravity. Gravity
will be defined as either 9.81m/s**2 for Earth or 1.62m/s**2 for the Moon. This 
program will plot the flight path (trajecotry) of the projectile on a graph by
calculating the maxRange in x-direction (m), yPeak(m) and the x-position in
which it achieves yPeak(m).

    Typical usage examples:
    
    bla = blabla
    he = hehe
"""

import argparse
import logging
import math
import os
import sys
import tkinter as tk
from tkinter import filedialog, PhotoImage

import matplotlib.pylab as plot
import numpy as np

# GLOBAL DEFAULTS
ICON_FILE = 'projectile_logo.png'

def projectilemotion(x0, y0, v0, theta, g) -> plot[xPeak, yPeak, maxRange]:
    """projectlemotion requires 5 user input arguments which are as follows;

    Args:
        x0: Initial displacement in 'x' domain in [m].
        y0: Initial displacement in 'y' domain in [m].
        v0: Initial velocity of projectile in [m/s].
        theta: launch angle of projectile in [degrees]
        g: The acceleration due to gravity for either Earth or Moon in [m/s**2].

    Returns:
        A plotted trajectory of the projectile under the conditions defined by
          the args above, calculating the following outputs:
        
        xPeak: the value of x [m] at which the yPeak is achieved.
        yPeak: the maximum displacement in y-direction [m].
        maxRange: the maximum displacement in x-direction [m].
    
    Raises:
        Error: 
    """ 

    theta = 45 # launch angle in degrees
    launchAngle = (theta * (math.pi/180)) # Converts launch angle into radians
    maxRange = ((v0.**2)/g) * (np.sin(2*launchAngle)) # Calculates range in x-direction (using .^ vector   multiplication)
    xStep = (maxRange / 100) # Calculates step, using 100 values for plotting up to the range           
    x = x0:xStep:maxRange # x vector from initial x-value --> range. 100 values
    y = ((x * tan(launchAngle)) - g/(2*(v0.**2)*(np.cos(launchAngle)).**2)*x.**2) + y0 # displacement in y-direction
    
    for n = 1:length(x) 
        flightPath = plot(x(n),y(n),'b.') # trajectory of projectile with blue trace
        set(flightPath,'LineWidth',2) # trace width on plot
        title('Projectile Motion') # title for plot
        xlabel('distance (m)')
        ylabel('height (m)') # labelling axes
        hold on # this allows multiple plots on a single figure
        #  if (mod(n,3) == 0) - this could be used to perform a live plot. By increasing the
        #  integer, the plot will speed up by dividing every 3 values of x as opposed to
        #  every value of x if using a ‘pause’ operator at each plot.
        #  end

    end
    
    zoom on
    yPeak = max(y) # max height of plot
    maxPoint = find(y == max(y(:))) # Index of max point on plot
    xPeak = x(maxPoint) # value of x at peak height
    flightPath = plot(x(maxPoint),y(maxPoint),'r.') # denoting max point with red marker
    set(flightPath,'MarkerSize',20) # marker size to stand out on plot

    end

if __name__ == '__main__':
    main()
