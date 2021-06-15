from scipy.interpolate import interp1d
import numpy as np
x = np.hstack((2.5, np.arange(3,12)))
y = [0, 1.5, 6, 13, 22, 35, 50, 70, 88, 100]
p_interp = interp1d(x, y, kind='quadratic')
def gen_power(v):
    return (v >= 2.5)*p_interp(np.clip(v, 2.5, 11))