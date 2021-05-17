import numpy as np
from vi_util import *

"""
Value Iteration Algorithim, ITCS 3153
William Ingersoll

I hate this, I hate who ever came up with row major order.
Why is it allowed to bounce off of wall? It seems completely illogical that the best route forward is to repeatedly 
bash its skull against an obstacle until it flings into the right direction.

I fixed the row major order in the util file, which was clearly written in respect to a typical cartesian system.
Up is x, across is y

Fun assignemt overall 9/10
"""


class State:

    def __init__(self, x_val, y_val):
        self.x = x_val
        self.y = y_val

def get_expected_utility(action, state, trans, U, states):
    result = 0.0

    #Finding the right index on the transition model given the action
    if(action == 'U'):
        action_table = 0
    elif(action == 'R'):
        action_table = 1
    elif(action == 'D'):
        action_table = 2
    else:
        action_table = 3

    #Summation through the transition model x the current utility for that position
    for state_prime, elem in enumerate(states):
        result += (trans[action_table, state, state_prime])*U[state_prime]

    return(result)



def value_iteration(states, actions, trans, rewards, discount):
    #Init two empty arrays, one for utilities and the otehr for updated utilities
    U = np.full(len(states), 0.0)
    U_prime = np.full(len(states), 0.0)
    
    #Set the threshold
    error = 0.00001
    threshold = 0.0
    if(discount < 1):
        threshold = (error*(1-discount))/discount
    else:
        threshold = 0.001

    #Start the main loop until delta is smaller than our threshold
    while(True):

        #Set U equal to U Prime
        U = np.copy(U_prime)
        #Set delta to 0 as a base
        delta = 0.0
        #Loop through each state
        for state, elem in enumerate(states):
            utilities = []
            for action in actions:
                utilities.append(get_expected_utility(action, state, trans, U, states))
   
            #Check to see if we're at our terminal indicies
            if((state == 6) or (state == 10)):
                U_prime[state] = rewards[state]
            #If not then we use the bellman equation for the utility
            else:
                U_prime[state] = rewards[state] + (discount*(max(utilities)))        
            #Update delta
            if(abs(U_prime[state] - U[state]) > delta):
                delta = abs(U_prime[state] - U[state])
        #End the loop if we're below the threshold
        if(delta < threshold):
            break
        
    return(U)

def main():
    #create an empty states array in row-major order
    states = []
    for i in range(1, 4):
        for j in range(1, 5):
            #exclude the point 2,2
            if(not ((i == 2) and (j == 2))):
                states.append(State(i, j))


    #Action list
    actions = ['U', 'R', 'D', 'L']
    
    #All pairs to test
    outputs = {
        "o1": [1.0, -0.04],
        "o2": [1.0, -0.25],
        "o3": [1.0, -0.01],
        "o4": [0.5, -0.04],
        "o5": [0.5, -0.25],
        "o6": [0.5, -0.01],
    }

    for output in outputs.values():

        #Initializing a rewards array
        rewards = np.array([])
        rewards = np.full(len(states), output[1])
        rewards[6] = -1.0
        rewards[10] = 1.0


        #Discount value
        discount = output[0]

        #Call the value iteration function
        U = value_iteration(states, actions, P, rewards, discount)


        #Getting policy
        policy = getPolicyForGrid(states, U, actions, P, [6, 10])

        #Printing Info
        print("---------------------------------------------\nDISCOUNT: " + str(discount) + " | REWARD: " + str(rewards[0]))
        print("---------------------------------------------\nUTILIES:")
        for u in U:
            print(str(u))
        print("---------------------------------------------\nPOLICY: " + str(policy))
        printPolicyForGrid(policy, 4, 3, [5])
        


if __name__ == "__main__":
    main()