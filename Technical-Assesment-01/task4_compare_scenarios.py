import agentpy as ap
import random
import matplotlib.pyplot as plt

class DynamicWalker(ap.Agent):
    def step(self):
        pos = self.model.grid.positions[self]
        
        # Scenario 1: Standard isotropic random walk
        if self.model.p.bias == 'none':
            move = random.choice([(1,0), (-1,0), (0,1), (0,-1)])
        # Scenario 2: Strong bias towards top-right corner
        else:
            move = random.choices([(1,0), (-1,0), (0,1), (0,-1)], weights=[0.4, 0.1, 0.4, 0.1])[0]
            
        nx = max(0, min(self.p.grid_size[0] - 1, pos[0] + move[0]))
        ny = max(0, min(self.p.grid_size[1] - 1, pos[1] + move[1]))
        self.model.grid.move_to(self, (nx, ny))

class ComparisonModel(ap.Model):
    def setup(self):
        self.grid = ap.Grid(self, self.p.grid_size, torus=False)
        self.agents = ap.AgentList(self, self.p.agents, DynamicWalker)
        self.grid.add_agents(self.agents, random=True)

    def step(self):
        self.agents.step()

# Execute Scenario A (Unbiased)
params_a = {'agents': 40, 'grid_size': (20, 20), 'steps': 50, 'bias': 'none'}
model_a = ComparisonModel(params_a)
model_a.run()

# Execute Scenario B (Biased toward Top-Right)
params_b = {'agents': 40, 'grid_size': (20, 20), 'steps': 50, 'bias': 'top_right'}
model_b = ComparisonModel(params_b)
model_b.run()

# Plot Comparison
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Scenario A Plot
pos_a = [model_a.grid.positions[a] for a in model_a.agents]
ax1.scatter([p[0] for p in pos_a], [p[1] for p in pos_a], color='blue')
ax1.set_title("Scenario A: Unbiased Random Walk")
ax1.set_xlim(0, 20); ax1.set_ylim(0, 20); ax1.grid(True)

# Scenario B Plot
pos_b = [model_b.grid.positions[a] for a in model_b.agents]
ax2.scatter([p[0] for p in pos_b], [p[1] for p in pos_b], color='red')
ax2.set_title("Scenario B: Biased Walk (Top-Right)")
ax2.set_xlim(0, 20); ax2.set_ylim(0, 20); ax2.grid(True)

plt.show()