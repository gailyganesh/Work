
# a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
# b = ['left', 'right', 'top', 'down',
#      'left_down', 'right_down', 'left_up', 'right_up']
# c = ['left', 'right', 'up', 'down']
# if 'd' in a[:4]:
#     print('correct')
# b = b[1:]
# b.remove('top')
# b = b[:4]
#
# print (b)
# import pandas as pd
#
#
# def summa(action, state):
#     db = pd.read_csv('/home/vtd/Documents/test.csz')
#     print (db)
#     a_num = {'left': 0, 'right': 1, 'top': 2, 'down': 3,
#              'left_down': 4, 'right_down': 5, 'left_up': 6, 'right_up': 7}
#     nxt_state = db.ix[a_num[action], state]
#     print(nxt_state)
#
#
# summa('left', 'e')


# class hi(object):
#     a = 1
#
#
# class h(hi):
#     b = 3
#
#
# x, y, z = h(), h(), h()
# print x
# from gym.utils import seeding
# import numpy as np
#
#
# def _seed(seed=None):
#     np_random, seed = seeding.np_random(seed)
#     return [seed], np_random
#
#
# np_random = _seed(0)
# print (dir(np_random))
# print _seed(12)
# _seed(11)
# np.random.seed(0)
import matplotlib.pyplot as plt
import matplotlib.patches as patches
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
# plt.plot([0, 0], [0, 1])
# plt.plot([0, 1], [0, 0])
# plt.plot([1, 1], [0, 1])
# plt.plot([1, 0], [1, 1])

plt.axis('off')
plt.show()
