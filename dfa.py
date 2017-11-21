class DFA:

    def __init__(self, states, alphabets, init_state, final_states, transition_matrix):
        self.states = states
        self.alphabets = alphabets
        self.init_state = init_state
        self.final_states = final_states
        self.transition_matrix = transition_matrix

    def toregex(self):
        pass
