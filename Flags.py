class Flags:

    def __init__(self, flags):
        #### any info you want to store are here, for instance:
        self.final_state = (4,4)
        # Sort given flag positions into ordered-dictionary by flag value
        self.flagPos = flags
        self.flags = list({k: v for k, v in sorted(flags.items(), key=lambda item: item[1])}.keys())
        ## hint: self.flags indicate the position of each flag and the correct order it should be collected
        self.flagCounter = 0
        self.action_set = {(0,1),(0,-1),(-1,0),(1,0)}
    
    def initial_state(self):
    # return the initial state of this MDP ...
        return (0,0)

    def get_all_states(self):
    # return all the possible states in this MDP
        return [(x,y) for x in range(5) for y in range(5)]
    
    def is_terminal (self, state) :
    # this function should return a Boolean indicating whether or not state is a terminal state; in other 
    # words , does the game end at the specified state or does the robot keep playing ?
        if state == (4,4):
            return True
        else:
            return False    
    
    def transition(self, state , action) :
    # this function should simulate the intended behavior of the Flags domain
    # in particular ,t given the specified state and action, his function should return a tuple containing two things :
    # 1. the next state to which we are transitioning to in the next period
    # 2. the reward obtained according to your rewardfunction when transitioning to the next state
    ## don't need to return the whole transition matrix
    ## also, if the current state is the final state, we stop

    # Denote actions from set {(0,1),(0,-1),(-1,0),(1,0)} as {up,down,left,right}
        # Check if current state is already terminal
        if self.is_terminal(state):
            return state, 1
        # Generate next state
        next_state = self.computeNextState(state, action)
        # Check if next state is terminal
        if self.is_terminal(next_state):
            return next_state, 1
        # Check if flag is in remaining-flags-list
        if next_state in self.flags:
            # Check if it's the first flag
            if next_state == self.flags[0]:
                # Capture flag, update flags array
                self.flags = self.flags[1:]
                return next_state, 1
            # Not the first flag, penalize agent
            else:
                return next_state, -3
        # Normal move, continue
        else:
            return next_state, -1
    
    def computeNextState(self, state, action):
        # Assert action is valid
        try:
            assert action in self.action_set
        except:
            print("Illegal action given!")
        # Check if agent would go out-of-bounds
        if self.isOutOfBounds(state, action):
            return state
        else:
            return (state[0]+action[0],state[1]+action[1])

    def isOutOfBounds(self, state, action):
        if (state[0] == 0 and action == (-1,0)) or \
            (state[0] == 4 and action == (1,0)) or \
            (state[1] == 0 and action == (0,-1)) or \
            (state[1] == 4 and action == (0,1)):
            return True
        else:
            return False