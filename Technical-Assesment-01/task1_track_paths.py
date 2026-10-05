import agentpy as ap
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class PathTrackingWalker(ap.Agent):
    def setup(self):
        # Store path history for each agent
        self.path = []

    def step(self):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        move = random.choice(directions)
        
        pos = self.model.grid.positions[self]
        new_x = max(0, min(self.p.grid_size[0] - 1, pos[0] + move[0]))
        new_y = max(0, min(self.p.grid_size[1] - 1, pos[1] + move[1]))
        
        self.model.grid.move_to(self, (new_x, new_y))
        # Record updated position
        self.path.append((new_x, new_y))

class PathModel(ap.Model):
    def setup(self):
        self.grid = ap.Grid(self, self.p.grid_size, torus=False)
        self.agents = ap.AgentList(self, self.p.agents, PathTrackingWalker)
        self.grid.add_agents(self.agents, random=True)
        
        # Log initial positions
        for agent in self.agents:
            agent.path.append(self.grid.positions[agent])

    def step(self):
        self.agents.step()

# Parameters
parameters = {'agents': 5, 'grid_size': (10, 10), 'steps': 20}
model = PathModel(parameters)
model.setup()

# Setup Visualization
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-0.5, model.p.grid_size[0] - 0.5)
ax.set_ylim(-0.5, model.p.grid_size[1] - 0.5)
ax.grid(True)

scat = ax.scatter([], [], s=150, zorder=3)
# Create a line plot for each agent's trail
lines = [ax.plot([], [], alpha=0.6, linewidth=2)[0] for _ in model.agents]

def update(frame):
    model.step()
    
    # Update agent dots
    positions = [model.grid.positions[a] for a in model.agents]
    scat.set_offsets(positions)
    
    # Update trail lines
    for line, agent in zip(lines, model.agents):
        px, py = zip(*agent.path)
        line.set_data(px, py)
        
    return [scat] + lines

ani = animation.FuncAnimation(fig, update, frames=model.p.steps, blit=True, repeat=False)
plt.show()