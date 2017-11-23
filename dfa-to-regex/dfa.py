class DFA:

    def __init__(self, states, alphabets, init_state, final_states, transition_dict):
        self.states = states
        self.alphabets = alphabets
        self.init_state = init_state
        self.final_states = final_states
        self.transition_dict = transition_dict
        self.regex = ''
        self.ds = {}

    def get_intermediate_states(self):
        return [state for state in self.states if state not in ([self.init_state] + self.final_states)]

    def get_predecessors(self, state):
        #return [key for key, value in self.transition_dict.items() if state in value and state != key]
        return [key for key, value in self.ds.items() if state in value.keys() and value[state] != 'phi' and key != state]

    def get_successors(self, state):
        val = [value for key, value in self.transition_dict.items() if state in key]
        return [j for i in val for j in i if j != state]

    def get_if_loop(self, state):
        #t = self.transition_dict[state]
        #return [i for i, v in enumerate(t) if state == v]
        if self.ds[state][state] != 'phi':
            return self.ds[state][state]
        else:
            return ''

    def toregex(self):
        n = len(self.states)
        intermediate_states = self.get_intermediate_states()
        dict_states = {r: {c: 'phi' for c in self.states} for r in self.states}
        for i in self.states:
            for j in self.states:
                indices = [ii for ii, v in enumerate(self.transition_dict[i]) if v == j]    #get indices of states
                if len(indices) != 0:
                    dict_states[i][j] = '+'.join([str(self.alphabets[v]) for v in indices])

        self.ds = dict_states
        print(dict_states)
        temp_states = self.states

        for inter in intermediate_states:
            predecessors = self.get_predecessors(inter)
            successors = self.get_successors(inter)
            print('predecessor : ', predecessors)
            print('successor : ', successors)

            #dd = {r: {c: 'phi' for c in self.states if c != inter} for r in self.states if r != inter}
            dd = {r: {c: 'phi' for c in temp_states if c != inter} for r in temp_states if r != inter}
            for i in predecessors:
                for j in successors:
                    inter_loop = self.get_if_loop(inter)
                    print('i : ', i, ' j : ', j)
                    #dict_states[i][j] = '+'.join((dict_states[i][j], ''.join(('('+dict_states[i][inter]+')', '('+inter_loop+')' + '*', '('+dict_states[inter][j]+')'))))
                    dict_states[i][j] = '+'.join(('('+dict_states[i][j]+')', ''.join(('('+dict_states[i][inter]+')', '('+inter_loop+')' + '*', '('+dict_states[inter][j]+')'))))


            #temp_states =
        print(dict_states)
        #print(dd)
        init_loop = dict_states[self.init_state][self.init_state]
        init_to_final = dict_states[self.init_state][self.final_states[0]] + '(' + dict_states[self.final_states[0]][self.final_states[0]] + ')' + '*'
        final_to_init = dict_states[self.final_states[0]][self.init_state]
        re = '(' + '('+init_loop+')' + '+' + '('+init_to_final+')' + '('+final_to_init+')' + ')' + '*' + '('+init_to_final+')'
        print(re)


def main():
    states = input('Enter the states in your DFA : ')
    states = states.split()
    alphabets = input('Enter the alphabets : ')
    alphabets = alphabets.split()
    init_state = input('Enter initial state : ')
    final_states = input('Enter the final states : ')
    final_states = final_states.split()
    print('Define the transition function : ')
    transition_matrix = [list(map(str, input().split())) for _ in range(len(states))]
    transition_dict = dict(zip(states, transition_matrix))
    print('transition dict : ', transition_dict)
    dfa = DFA(states, alphabets, init_state, final_states, transition_dict)
    dfa.toregex()


if __name__ == '__main__':
    main()
