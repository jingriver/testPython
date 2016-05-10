import numpy as np
import matplotlib.pyplot as plt

# Data to fit a polynomial to.
x = np.array([4,8,16,32,64])*10**3
y = np.array([0.1,0.3,1.3,5.1,20.5])
print x
print y
poly_params = np.polyfit(x, y, 3)    # Fit the data with a 3rd degree polynomial
poly_3 = np.poly1d(poly_params)      # Construct the polynomial

xPoly = np.linspace(0, max(x), 100)  # Generate 100 x-coordinates from 0 to max(x)
yPoly = poly_3(xPoly)             # Use the polynomial to calculate the y-coordinates
print xPoly
print yPoly
# Plot the results
plt.plot(x, y, 'o', xPoly, yPoly, '-g')
plt.show()