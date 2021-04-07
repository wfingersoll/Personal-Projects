import nqueens as nq
import random
import math

"""
Author: William Ingersoll
03/19/2021

A program to solve the n-queens problem with simulated annealing

"""

class local_search:

    #Schedul function for the simulated annealing algorithim
    def scheduling(self, T, decayRate):
        return (T*decayRate)

    #Simulated Annealing algorithim
    def simulatedAnnealing(self, current, decayRate, T_Threshold):
        
        #Set starting temp to 100 and get the initial h-cost
        T = 100.0
        h_cost = nq.numAttackingQueens(current)
        
        #Loop until temperature is low enough or we found a perfect solution
        while(T>T_Threshold and (h_cost > 0)):
            #Find current h-cost and lower the temperature
            h_cost = nq.numAttackingQueens(current)
            T = self.scheduling(T, decayRate)

            #Get a random succsessor state
            states = nq.getSuccessorStates(current)
            random_state = random.randrange(0, len(states))
            #If the succsessor state is objectively better we move there
            if(nq.numAttackingQueens(states[random_state])<h_cost):
                current=states[random_state]
            #If the succsessor state is not better we run an equation to randomly decide whether or not we move there
            else:
                delta_e = h_cost - nq.numAttackingQueens(states[random_state])
                threshold = math.pow(math.e, (delta_e/T))
                random_num = random.randrange(0, 1)
                if(random_num < threshold):
                    current=states[random_state]
           
        return current

#A function to run simulated annealing multiple times
def loop(experiments, b_size, ls):
    
    #Cycle through the three dictionary values
    for elem in experiments.values():
        #Init the final h-cost's
        final_h = []

        #setup a board to use
        current = nq.Board(b_size)
        current.rand()

        #Print decay rate, etc.
        print("###############################################\nDecay Rate is: " + str(elem[0]) + ", Threshold is: " + str(elem[1]) + "\n###############################################")

        #Run the experiment 10 times
        x=1
        while(x<=10):
            #Print run # and initial board
            print(" | Run " + str(x) + " |")
            print("Starting Board:")
            current.printBoard()
            #Print initial boards h-cost
            print("H-Value: " + str(nq.numAttackingQueens(current)))
            #run simulated annealing
            current = ls.simulatedAnnealing(current, elem[0], elem[1])
            x+=1
            #Print final board
            print("Final Board:")
            current.printBoard()
            #Print final h-cost
            print("H-Value: " + str(nq.numAttackingQueens(current)))
            #Add h-cost to final h's
            final_h.append(nq.numAttackingQueens(current))
    
        #Print avg final h-cost
        avg = 0
        for x in final_h:
            avg+=x
        print("Average final h-cost: " + str(avg/10))


def main():
    ls = local_search()
    #A dictionary to hold all the decay rate + threshold combos
    experiments = {
        "exp1": [0.9, 0.000001],
        "exp2": [0.75, 0.00000001],
        "exp3": [0.5, 0.00000001]
    }
    #call the loop function with three different board sizes
    loop(experiments, 4, ls)
    loop(experiments, 8, ls)
    loop(experiments, 16, ls)

if __name__=='__main__':
    main()