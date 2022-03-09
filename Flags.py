import numpy as np
np.random.seed(0)

class Flags:

    def __init__(self):
        #### any info you want to store are here, for instance:
        self.final_state = 
        self.flags = 
        ## hint: self.flags indicate the position of each flag and the correct order it should be collected
    
    
    def initial_state(self):
    # return the initial state of this MDP ...

        
    def get_all_states(self):
    # return all the possible states in this MDP

    
    def is_terminal (self, state) :
    # this function should return a Boolean indicating whether or not state is a terminal state; in other 
    # words , does the game end at the specified state or does the robot keep playing ?

    
    
    
    
    def transition(self, state , action) :
    # this function should simulate the intended behavior of the Flags domain
    # in particular , given the specified state and action, this function should return a tuple containing two things :
    # 1. the next state to which we are transitioning to in the next period
    # 2. the reward obtained according to your rewardfunction when transitioning to the next state
    ## don't need to return the whole transition matrix
    ## also, if the current state is the final state, we stop



        return next_state, reward
    
    
    #### you can include any other helper functions you want
    ## for instance: a helper function to see if the collection happens or not (if a collection satisify the collection order...)
    
    
   