import logging
from random import sample
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.filters import gaussian_filter
import pandas as pd
print(pd.__version__)


class BuildingMovementSimulator:
    def __init__(self, data):
        self.data = data
        self.starting_points = None
        self.destinations = None
        self.paths = []

        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def define_starting_points(self):
        try:
            # Attempt to use "ENTRY" as starting points, otherwise randomly select
            self.starting_points = self.data[self.data['Name'].str.contains("ENTRY", na=False)]
            if self.starting_points.empty:
                self.starting_points = self.data.sample(5)
            self.logger.info(f"Defined {len(self.starting_points)} starting points.")
        except Exception as e:
            self.logger.error(f"Error in defining starting points: {e}")

    def define_destinations(self, num_destinations=10):
        try:
            self.destinations = self.data.sample(num_destinations)
            self.logger.info(f"Defined {num_destinations} destinations.")
        except Exception as e:
            self.logger.error(f"Error in defining destinations: {e}")

    def simulate_paths(self):
        try:
            for _, start in self.starting_points.iterrows():
                destination = self.destinations.sample(1).iloc[0]
                path_x = np.linspace(start['Position X'], destination['Position X'], 100)
                print(path_x)
                path_y = np.linspace(start['Position Y'], destination['Position Y'], 100)
                print(path_y)
                self.paths.append((path_x, path_y))
            self.logger.info(f"Simulated {len(self.paths)} paths.")
        except Exception as e:
            self.logger.error(f"Error in simulating paths: {e}")
            
    def generate_heatmap(self):
        try:
            all_x = []
            all_y = []
            for path in self.paths:
                all_x.extend(path[0])
                all_y.extend(path[1])

            hist, xedges, yedges = np.histogram2d(all_x, all_y, bins=100)
            smoothed_hist = gaussian_filter(hist, sigma=2)

            plt.figure(figsize=(10, 10))
            plt.imshow(smoothed_hist.T, origin='lower', aspect='auto', 
                    extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]], 
                    cmap='hot')
            plt.colorbar(label='Frequency')
            plt.xlabel('Position X')
            plt.ylabel('Position Y')
            plt.title('Employee Movement Heatmap')
            plt.show()
            
            self.logger.info("Heatmap generated successfully.")
        except Exception as e:
            self.logger.error(f"Error in generating heatmap: {e}")

    def robust_generate_heatmap(self):
        try:
            all_x = []
            all_y = []
            for path in self.paths:
                all_x.extend(path[0])
                all_y.extend(path[1])

            # Removing NaN values
            all_x = [x for x, y in zip(all_x, all_y) if not (np.isnan(x) or np.isnan(y))]
            all_y = [y for x, y in zip(all_x, all_y) if not (np.isnan(x) or np.isnan(y))]

            if not all_x or not all_y:  # If after removing NaNs, there's no data left
                self.logger.warning("No valid data points left for heatmap after removing NaN values.")
                return

            hist, xedges, yedges = np.histogram2d(all_x, all_y, bins=100)
            smoothed_hist = gaussian_filter(hist, sigma=2)

            plt.figure(figsize=(10, 10))
            plt.imshow(smoothed_hist.T, origin='lower', aspect='auto',
                       extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]],
                       cmap='hot')
            plt.colorbar(label='Frequency')
            plt.xlabel('Position X')
            plt.ylabel('Position Y')
            plt.title('Employee Movement Heatmap')
            plt.show()

            self.logger.info("Heatmap generated successfully.")
        except Exception as e:
            self.logger.error(f"Error in generating heatmap: {e}")

    def run_simulation(self):
        self.logger.info("Starting the simulation...")
        self.define_starting_points()
        self.define_destinations()
        self.simulate_paths()
        self.robust_generate_heatmap()
        self.logger.info("Simulation completed.")


1+1
sample_data = pd.read_csv('auto_cad_data_extraction_test_230909.csv', on_bad_lines='skip')





filtered_data = sample_data.dropna(subset=['Position X', 'Position Y'])


plt.scatter(filtered_data['Position X'], filtered_data['Position Y'])
plt.scatter(sample_data['Position X'], sample_data['Position Y'])
plt.xlabel('Position X')
plt.ylabel('Position Y')
plt.title('Data Points')
plt.show()

sample_data['Start X'].unique()

sample_data['Position Y'].head()
sample_data['Position X'].head()
sample_data['Position Z'].unique()

building_movement_simulator = BuildingMovementSimulator(sample_data)
building_movement_simulator = BuildingMovementSimulator(filtered_data)

building_movement_simulator.define_starting_points()
building_movement_simulator.define_destinations(10)
building_movement_simulator.simulate_paths()
building_movement_simulator.generate_heatmap()
building_movement_simulator.robust_generate_heatmap()
building_movement_simulator.run_simulation()


import numpy as np

# Define starting points (entries)
starting_points = sample_data[sample_data['Name'].str.contains("ENTRY")]

# Randomly select potential destinations
num_destinations = 10
destinations = sample_data.sample(num_destinations)

starting_points, destinations

# Display the first few rows of the data
sample_data.head()

sample_data['Start X'].unique()


sample_data['Dateigröße'].unique()

sample_data.columns

test = pd.DataFrame(sample_data)

test.info()
for i in test.columns:
    print(i)

# Example usage
simulator = BuildingMovementSimulator(data=sample_data)
simulator.run_simulation()





