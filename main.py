import logging


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
                path_y = np.linspace(start['Position Y'], destination['Position Y'], 100)
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

    def run_simulation(self):
        self.logger.info("Starting the simulation...")
        self.define_starting_points()
        self.define_destinations()
        self.simulate_paths()
        self.generate_heatmap()
        self.logger.info("Simulation completed.")


# Example usage
simulator = BuildingMovementSimulator(data=sample_data)
simulator.run_simulation()
