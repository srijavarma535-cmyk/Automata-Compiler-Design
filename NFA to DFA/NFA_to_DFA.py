# NFA to DFA Conversion
# NFA accepts strings containing "101"

from collections import deque

# --------------------------------------------------
# NFA Definition
# --------------------------------------------------

nfa = {
    'q0': {
        '0': {'q0'},
        '1': {'q0', 'q1'}
    },

    'q1': {
        '0': {'q2'},
        '1': set()
    },

    'q2': {
        '0': set(),
        '1': {'q3'}
    },

    'q3': {
        '0': {'q3'},
        '1': {'q3'}
    }
}

# Start state
nfa_start = {'q0'}

# Final state
nfa_final = {'q3'}

# Input symbols
symbols = ['0', '1']


# --------------------------------------------------
# NFA to DFA Conversion
# --------------------------------------------------

# DFA states are sets of NFA states
start_dfa_state = frozenset(nfa_start)

# Store DFA transitions
dfa = {}

# Queue for unprocessed DFA states
queue = deque([start_dfa_state])

# Keep track of visited states
visited = set()


while queue:

    current = queue.popleft()

    if current in visited:
        continue

    visited.add(current)

    dfa[current] = {}

    # Check transition for 0 and 1
    for symbol in symbols:

        next_state = set()

        # Find transitions from every NFA state
        # inside the current DFA state
        for state in current:
            next_state.update(
                nfa[state][symbol]
            )

        next_state = frozenset(next_state)

        dfa[current][symbol] = next_state

        # Add new DFA state to queue
        if next_state not in visited:
            queue.append(next_state)


# --------------------------------------------------
# Find DFA Final States
# --------------------------------------------------

dfa_final = set()

for state in dfa:

    # If DFA state contains q3,
    # it is a final state
    if nfa_final.intersection(state):
        dfa_final.add(state)


# --------------------------------------------------
# Display DFA States
# --------------------------------------------------

print("DFA STATES")
print("----------")

for state in dfa:
    print(state)


# --------------------------------------------------
# Display DFA Transition Table
# --------------------------------------------------

print("\nDFA TRANSITION TABLE")
print("--------------------")

for state, transitions in dfa.items():

    print(
        state,
        "--0-->",
        transitions['0']
    )

    print(
        state,
        "--1-->",
        transitions['1']
    )


# --------------------------------------------------
# Display Final States
# --------------------------------------------------

print("\nDFA FINAL STATES")
print("----------------")

for state in dfa_final:
    print(state)


# --------------------------------------------------
# Test a String
# --------------------------------------------------

string = input("\nEnter a binary string: ")

current = start_dfa_state

print("\nSTATE TRACE")
print("-----------")

print("Start:", current)

for symbol in string:

    current = dfa[current][symbol]

    print(
        "Input:",
        symbol,
        "->",
        current
    )


# --------------------------------------------------
# Check whether string is accepted
# --------------------------------------------------

if current in dfa_final:

    print("\nString Accepted")

else:

    print("\nString Rejected")