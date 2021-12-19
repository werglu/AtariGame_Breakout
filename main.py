from ale_py import ALEInterface
from ale_py.roms import Breakout
import gym
import time

ale = ALEInterface()
ale.loadROM(Breakout)

# env = gym.make('Breakout-v0')
# env = gym.make('BreakoutDeterministic-v4')
env = gym.make('BreakoutNoFrameskip-v4')
env.reset()
for _ in range(10000):
    env.render()
    time.sleep(0.01) # good for readability
    env.step(env.action_space.sample()) # take a random action
env.close()