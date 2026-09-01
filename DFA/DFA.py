import matplotlib.pyplot as plt
import networkx as nx

# --------------------------------------------------
# DFA: Strings containing "101" as a substring
# --------------------------------------------------

# q0 = No part of "101" matched
# q1 = "1" matched
# q2 = "10" matched
# q3 = "101" matched (FINAL STATE)

dfa = {
    'q0': {
        '0': 'q0',
        '1': 'q1'
    },

    'q1': {
        '0': 'q2',
        '1': 'q1'
    },

    'q2': {
        '0': 'q0',
        '1': 'q3'
    },

    'q3': {
        '0': 'q3',
        '1': 'q3'
    }
}

start_state = 'q0'
final_states = {'q3'}


# --------------------------------------------------
# Display each state's transitions
# --------------------------------------------------

print("DFA TRANSITIONS")
print("----------------")

print("q0:")
print("  On input 0 -> q0")
print("  On input 1 -> q1")

print("\nq1:")
print("  On input 0 -> q2")
print("  On input 1 -> q1")

print("\nq2:")
print("  On input 0 -> q0")
print("  On input 1 -> q3")

print("\nq3 (FINAL STATE):")
print("  On input 0 -> q3")
print("  On input 1 -> q3")


# --------------------------------------------------
# Display transition table
# --------------------------------------------------

print("\n\nTRANSITION TABLE")
print("----------------")
print("State\t0\t1")
print("q0\tq0\tq1")
print("q1\tq2\tq1")
print("q2\tq0\tq3")
print("q3\tq3\tq3")


# --------------------------------------------------
# Test a string
# --------------------------------------------------

string = input("\nEnter a binary string: ")

current_state = start_state

print("\nSTATE TRACING")
print("-------------")
print("Start State:", current_state)

for symbol in string:

    next_state = dfa[current_state][symbol]

    print(
        current_state,
        "--", symbol,
        "-->",
        next_state
    )

    current_state = next_state


# --------------------------------------------------
# Check acceptance
# --------------------------------------------------

if current_state in final_states:
    print("\nResult: ACCEPTED")
    print("The string contains '101'.")
else:
    print("\nResult: REJECTED")
    print("The string does not contain '101'.")


# --------------------------------------------------
# Draw DFA Diagram
# --------------------------------------------------

G = nx.DiGraph()

# Add states
G.add_nodes_from(['q0', 'q1', 'q2', 'q3'])

# Add transitions
G.add_edge('q0', 'q0', label='0')
G.add_edge('q0', 'q1', label='1')

G.add_edge('q1', 'q2', label='0')
G.add_edge('q1', 'q1', label='1')

G.add_edge('q2', 'q0', label='0')
G.add_edge('q2', 'q3', label='1')

G.add_edge('q3', 'q3', label='0, 1')


# Position of states
pos = {
    'q0': (0, 0),
    'q1': (2, 0),
    'q2': (4, 0),
    'q3': (6, 0)
}


# Draw states
nx.draw_networkx_nodes(
    G,
    pos,
    node_size=2500,
    node_color='lightblue'
)

# Draw state labels
nx.draw_networkx_labels(
    G,
    pos,
    font_size=14,
    font_weight='bold'
)

# Draw transitions
nx.draw_networkx_edges(
    G,
    pos,
    arrows=True,
    arrowsize=20,
    connectionstyle='arc3,rad=0.1'
)

# Draw transition labels
edge_labels = nx.get_edge_attributes(G, 'label')

nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels,
    font_size=12
)


# Mark final state q3 with double circle
nx.draw_networkx_nodes(
    G,
    pos,
    nodelist=['q3'],
    node_size=3000,
    node_color='none',
    edgecolors='black',
    linewidths=2
)

# Start arrow
plt.annotate(
    '',
    xy=pos['q0'],
    xytext=(-1.2, 0),
    arrowprops=dict(arrowstyle='->')
)

plt.text(
    -1.2,
    0.3,
    'Start',
    fontsize=11
)

plt.title(
    "DFA for Strings Containing '101' as a Substring",
    fontsize=15
)

plt.axis('off')
plt.show()