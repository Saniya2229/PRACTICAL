import numpy as np
if not hasattr(np, "bool8"):   # Patch fix
    np.bool8 = np.bool_

import gym
import random

env = gym.make("Taxi-v3", render_mode="ansi")

state, _ = env.reset()
done = False
steps = 0

while not done and steps < 50:
    action = random.choice(range(env.action_space.n))  # random move
    state, reward, done, _, _ = env.step(action)
    steps += 1
    print(env.render())
