from ale_py import ALEInterface
from ale_py.roms import Breakout
import gym

ale = ALEInterface()
ale.loadROM(Breakout)

env = gym.make('Breakout-v0')
env.reset()
for _ in range(100000):
    env.render()
    env.step(env.action_space.sample()) # take a random action
env.close()