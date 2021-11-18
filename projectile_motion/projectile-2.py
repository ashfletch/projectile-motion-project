import matplotlib.pylab as plt
import numpy as np

def trajectory(x0: int, y0: int, v0: int, theta: int, g: float) -> tuple:
    launch_angle = (theta * (np.pi / 180)) # Converts launch angle into radians
    max_range = int(((v0**2) / g) * (np.sin(2 * launch_angle))) # Calculates range in x-direction (using vector multiplication)
    x_step = int(max_range / 100) # Calculates step, using 100 values for plotting up to the range
    x_values = []
    for value in range(x0, max_range, x_step):
        x_values.append(value)
    
    y_values = []
    for x in x_values:
        y_values.append(((x * np.tan(launch_angle)) - g / (2 * (v0**2) *
         (np.cos(launch_angle))**2) * x**2) + y0)
    return (x_values, y_values)


def projectilemotion(x0: int, y0: int, v0: int, theta: int, g: float):
    pass
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

def plot(x_values, y_values):
    plt.plot(x_values, y_values)

    #plt.axis([0, max_range, 0, max(y_values)]) 
    #Commented because max_range is nowhere defined
    
    plt.xlabel('Range [m]')
    plt.ylabel('Height [m]')
    plt.show()


if __name__ == '__main__':
    x_values, y_values= trajectory(0, 0, 940, 45, 1.62)
    # because trajectory returns 2 vectors...

    # and you forgot to call plot
    plot(x_values,y_values)