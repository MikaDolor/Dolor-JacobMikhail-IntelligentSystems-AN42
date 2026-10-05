import agentpy as ap
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# -------- Agent Definition -----------
class BiasedWalker(ap.Agent):
    def step(self):
        # 60% chance to move Right (1,0), 40% split among other directions
        weights = [0.6, 0.133, 0.133, 0.134]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        move = random.choices(directions, weights=weights)[0]

        pos = self.model.grid.positions[self]
        nx = max(0, min(self.p.grid_size[0] - 1, pos[0] + move[0]))
        ny = max(0, min(self.p.grid_size[1] - 1, pos[1] + move[1]))

        self.model.grid.move_to(self, (nx, ny))

# -------- Model Definition -----------
class BiasedWalkModel(ap.Model):
    def setup(self):
        self.grid = ap.Grid(self, self.p.grid_size, torus=False)
        self.agents = ap.AgentList(self, self.p.agents, BiasedWalker)
        self.grid.add_agents(self.agents, random=True)

    def step(self):
        self.agents.step()

# -------- Run Parameters -----------
parameters = {
    'agents': 10,
    'grid_size': (10, 10),
    'steps': 30
}

model = BiasedWalkModel(parameters)
model.setup()

# -------- Interactive Animation -----------
fig, ax = plt.subplots()
ax.set_xlim(-0.5, model.p.grid_size[0] - 0.5)
ax.set_ylim(-0.5, model.p.grid_size[1] - 0.5)
ax.set_xticks(range(model.p.grid_size[0]))
ax.set_yticks(range(model.p.grid_size[1]))
ax.grid(True)

scat = ax.scatter([], [], s=150, color='red')

def update(frame):
    model.step()
    positions = [model.grid.positions[agent] for agent in model.agents]
    scat.set_offsets(positions)
    return scat,

ani = animation.FuncAnimation(fig, update, frames=model.p.steps, blit=True, repeat=False)
plt.show()