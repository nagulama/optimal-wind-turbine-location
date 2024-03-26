#import two libraries 
#numpy provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions.
#matplotlib.pyplot  provides an interface for creating visualizations like plots.
import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic wind speed and direction data
np.random.seed(0)#ensure reproducibility of the results
num_points = 500 #defines the number of data points to generate
wind_speed = np.random.uniform(3, 8, num_points)  # Wind speed in m/s, random wind speed between 3 and 10 m/s
wind_direction = np.random.uniform(0, 360, num_points)  # Wind direction in degrees, random wind direction btn 0 and 360

# Define a simple objective function to maximize energy production
def objective_function(x, y):
    # Placeholder function - in a real scenario, this would involve more complex calculations
    return -np.sqrt(x**2 + y**2)  # Negative distance to maximize calculated from the origin to the x,y points
#The negative distance is used as the objective function because the goal is to maximize energy production, and a larger distance from the origin corresponds to a higher energy production potential.

# Define turbine location constraints
min_distance = 100 # Minimum distance between turbines in meters, for a 500kW

# Optimization algorithm 
def optimize_turbine_locations():
    best_location = None
    best_score = -np.inf
    
    # Generate random turbine locations inorder to evaluate objective function
    for _ in range(10000):
        x = np.random.uniform(0, 100)  # X-coordinate of turbine
        y = np.random.uniform(0, 1000)  # Y-coordinate of turbine
        
        # Check distance constraint
        if best_location is not None and np.linalg.norm([x - best_location[0], y - best_location[1]]) < min_distance:
            continue
        
        # Evaluate objective function
        score = objective_function(x, y)
        
        # Update best location if best score got
        if score > best_score:
            best_location = [x, y]
            best_score = score
    
    return best_location

# plot wind data and optimal turbine location
plt.figure(figsize=(6, 6))
plt.scatter(wind_direction, wind_speed, color='blue', label='Wind Data')
plt.xlabel('Wind Direction in degrees')
plt.ylabel('Wind Speed (m/s)')
plt.title('optimal turbine spacing for kumi district')
plt.grid(True)

# Optimize turbine location
optimal_location = optimize_turbine_locations()
plt.scatter(optimal_location[0], optimal_location[1], color='red', label='Optimal Turbine Location')
plt.legend()
plt.show()
