# Slippery Walk Three: 
# stochastic environment (50% action success, 33.33% stays, 16.66% backwards)
# 3 non-terminal states, 2 terminal states
# only reward is still at the right-most cell in the walk
# episodic environment, the agent terminates at the left- or right-most cell
# agent starts in state 2 (middle of the walk) T-1-2-3-T
# actions left (0) or right (1)

import numpy as np

class SlipperyWalkFive:
    def __init__(self):
        self.P = {
        0: {
            0: [(1.0, 0, 0.0, True)],
            1: [(1.0, 0, 0.0, True)]
        },
        1: {
            0: [(0.5000000000000001, 0, 0.0, True),
                (0.3333333333333333, 1, 0.0, False),
                (0.16666666666666666, 2, 0.0, False)
            ],
            1: [(0.5000000000000001, 2, 0.0, False),
                (0.3333333333333333, 1, 0.0, False),
                (0.16666666666666666, 0, 0.0, True)
            ]
        },
        2: {
            0: [(0.5000000000000001, 1, 0.0, False),
                (0.3333333333333333, 2, 0.0, False),
                (0.16666666666666666, 3, 0.0, False)
            ],
            1: [(0.5000000000000001, 3, 0.0, False),
                (0.3333333333333333, 2, 0.0, False),
                (0.16666666666666666, 1, 0.0, False)
            ]
        },
        3: {
            0: [(0.5000000000000001, 2, 0.0, False),
                (0.3333333333333333, 3, 0.0, False),
                (0.16666666666666666, 4, 1.0, True)
            ],
            1: [(0.5000000000000001, 4, 1.0, True),
                (0.3333333333333333, 3, 0.0, False),
                (0.16666666666666666, 2, 0.0, False)
            ]
        },
        4: {
            0: [(1.0, 4, 0.0, True)],
            1: [(1.0, 4, 0.0, True)]
        }
    }
        self.nState = len(self.P)
        self.naction= 2
        self.startState = 2
        #print("State, Start State, Number of Action ",self.nState, self.startState, self.naction,"\n")

    def transitions(self, state, action):
       #Return list of (prob, next_state, reward, done)
            return self.P[state][action]


#objSlipperyWalkFive = SlipperyWalkFive()
#step = objSlipperyWalkFive.transitions(2,0)
#print(step)