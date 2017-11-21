from .dfa import DFA


def main():
    states = input('Enter the states in your DFA : ')
    states = states.split()
    alphabets = input('Enter the alphabets : ')
    alphabets = alphabets.split()
    init_state = input('Enter initial state : ')
    final_states = input('Enter the final states : ')
    final_states = final_states.split()
    transition_matrix = [list(map(str, input().split())) for _ in range(len(alphabets))]

    dfa = DFA(states, alphabets, init_state, final_states, transition_matrix)
    dfa.toregex()


if __name__ == '__main__':
    main()