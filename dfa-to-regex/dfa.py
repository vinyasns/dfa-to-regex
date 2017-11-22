class DFA:

    def __init__(self, states, alphabets, init_state, final_states, transition_dict):
        self.states = states
        self.alphabets = alphabets
        self.init_state = init_state
        self.final_states = final_states
        self.transition_dict = transition_dict
        self.regex = ''

    def get_intermediate_states(self):
        return [state for state in self.states if state not in ([self.init_state] + self.final_states)]

    def get_predecessors(self, state):
        return [key for key, value in self.transition_dict.items() if state in value]

    def get_successors(self, state):
        return [value for key, value in self.transition_dict.items() if state in key]

    def get_if_loop(self, state):
        t = self.transition_dict[state]
        return [i for i, v in enumerate(t) if state == v]

    def toregex(self):
        n = len(self.states)
        intermediate_states = self.get_intermediate_states()
        dict_states = {r: {c: 'phi' for c in self.states} for  r in self.states}
        for i in self.states:
            for j in self.states:
                indices = [ii for ii, v in enumerate(self.transition_dict[i]) if v == j]
                if len(indices) != 0:
                    dict_states[i][j] = '+'.join([str(self.alphabets[v]) for v in indices])


        print(dict_states)
        for inter in intermediate_states:
            predecessors = self.get_predecessors(inter)
            successors = self.get_successors(inter)
            #for i in predecessors:
             #   print(inter, " : ", i)
            #print('sucess : ')
            #for i in successors:
             #   print(inter, " : ", i)
            for i in predecessors:
                for j in successors:
                    inter_loop = self.get_if_loop(inter)
                    #temp_dict[i]


def main():
    states = input('Enter the states in your DFA : ')
    states = states.split()
    alphabets = input('Enter the alphabets : ')
    alphabets = alphabets.split()
    init_state = input('Enter initial state : ')
    final_states = input('Enter the final states : ')
    final_states = final_states.split()
    transition_matrix = [list(map(str, input().split())) for _ in range(len(states))]
    transition_dict = dict(zip(states, transition_matrix))
    print(transition_dict)
    dfa = DFA(states, alphabets, init_state, final_states, transition_dict)
    dfa.toregex()


if __name__ == '__main__':
    main()
