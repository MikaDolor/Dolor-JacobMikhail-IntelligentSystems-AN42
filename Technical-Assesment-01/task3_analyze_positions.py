import numpy as np
import matplotlib.pyplot as plt
import agentpy as ap
import random

# Model Setup
class SimpleModel(ap.Model):
    def setup(self):
        self.grid = ap.Grid(self, self.p.grid_size, torus=False)
        self.agents = ap.AgentList(self, self.p.agents, ap.Agent)
        self.grid.add_agents(self.agents, random=True)

    def step(self):
        for agent in self.agents:
            pos = self.grid.positions[agent]
            move = random.choice([(1,0), (-1,0), (0,1), (0,-1)])
            nx = max(0, min(self.p.grid_size[0] - 1, pos[0] + move[0]))
            ny = max(0, min(self.p.grid_size[1] - 1, pos[1] + move[1]))
            self.grid.move_to(agent, (nx, ny))

params = {'agents': 50, 'grid_size': (15, 15), 'steps': 100}
model = SimpleModel(params)
results = model.run()

# Extract final coordinates
final_positions = [model.grid.positions[a] for a in model.agents]
x_coords, y_coords = zip(*final_positions)

# Display Numerical Distribution Summary
print("--- Final Positions Summary ---")
print(f"Mean Position (X, Y): ({np.mean(x_coords):.2f}, {np.mean(y_coords):.2f})")
print(f"Standard Deviation: ({np.std(x_coords):.2f}, {np.std(y_coords):.2f})")

# Plot Heatmap of Agent Distribution
plt.figure(figsize=(6, 5))
plt.hist2d(x_coords, y_coords, bins=params['grid_size'][0], range=[[0, 15], [0, 15]], cmap='Blues')
plt.colorbar(label='Agent Count')
plt.title("Final Agent Density Distribution")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.show()