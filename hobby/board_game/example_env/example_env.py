import gym.error as error
import pandas as pd
from gym import core as Gym
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from players.player import Player,creating_player
from players.oppenent import Oppenent,creating_oppenent


class Example_env(Gym.Env):
    metadata = {'render.modes': ['human']}
    reward_range = (-5, 5)
    action_space = ['first', 'left', 'right', 'top', 'down',
                    'left_down', 'right_down', 'left_up', 'right_up']
    observation_space = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    player_list = []
    oppenent_list = []

    def __init__(self):

        self.state = None
        self.nxt_state = None
        pass

    def get_reward(self):
        return 0
        if self.action == 'start':
            pass

    def _step(self, action):
        try:
            table = pd.read_csv('/home/vtd/Documents/test.csv')
        except IOError as e:
            raise error.DependencyNotInstalled(
                '{}. (HINT: you may need to install the Go dependencies.)'.format(e))

        if action == 'first':
            reward = get_reward(self)
            next_state = None
            Done = None
            pass
        else:
            a_num = {'left': 0, 'right': 1, 'top': 2, 'down': 3,
                     'left_down': 4, 'right_down': 5, 'left_up': 6, 'right_up': 7}
            nxt_state = table.ix[a_num[action], self.state]
            reward = get_reward(self)
        return (nxt_state, reward, done)
        pass

    def _reset(self):
        pass

    def _render(self, mode='human', close=False):
        fig1 = plt.figure()
        ax1 = fig1.add_subplot(111, aspect='equal')
        Board = patches.Rectangle((0, 0), 1, 1, fill=False)
        player1 = patches.Circle((0, 0), 0.05, facecolor="green")
        player2 = patches.Circle((0, 1), 0.05, facecolor="green")
        player3 = patches.Circle((0.5, 0.5), 0.05, facecolor="green")
        oppenent1 = patches.Circle((1, 0), 0.05, facecolor="red")
        oppenent2 = patches.Circle((1, 1), 0.05, facecolor="red")
        oppenent3 = patches.Circle((0.5, 1), 0.05, facecolor="red")

        ax1.add_patch(Board)
        plt.plot([0.5, 0.5], [0, 1])
        plt.plot([0, 1], [0, 1])
        plt.plot([0, 1], [1, 0])
        plt.plot([0, 1], [0.5, 0.5])

        ax1.add_patch(player1)
        ax1.add_patch(player2)

        player1.remove()
        plt.axis('off')
        plt.show()

        pass

    def _seed(self, seed=None):
        pass

    def _close(self):
        pass

    def action_per_state(self, state):
        if state in self.observation_space[:3]:
            if state == 'a':
                action_list = ['right', 'down', 'right_down']
                return action_list
            elif state == 'b':
                action_list = ['left', 'right', 'down']
                return action_list
            else:
                action_list = ['left', 'down', 'left_down']
                return action_list
        elif state in self.observation_space[3:6]:
            if state == 'd':
                action_list = ['right', 'top', 'down']
                return action_list
            elif state == 'e':
                action_list = self.action_space[1:]
                return action_list
            else:
                action_list = ['left', 'top', 'down']
                return action_list
        else:
            if state == 'g':
                action_list = ['right', 'top', 'right_up']
                return action_list
            elif state == 'h':
                action_list = ['left', 'right', 'top']
                return action_list
            else:
                action_list = ['left', 'top', 'left_up']
                return action_list




def check_state_free(self):
    for i in Example_env.player_list:
        if id(i) != id(self):
            if i.state == self.state:
                raise Exception('already this state is occupied by another player')
    for i in Example_env.oppenent_list:
        if id(i) != id(self):
            if i.state == self.state:
                raise Exception('already this state is occupied by another oppenent')


p1 = creating_player('a')
print id(p1.player_list[0])
print id(p1)
o1 = creating_oppenent('b')
print Oppenent._no_of_coin_oppenent, Player._no_of_coin_player
print id(o1.oppenent_list[0])
