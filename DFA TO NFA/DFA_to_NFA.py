import matplotlib.pyplot as plt
import networkx as nx

# DFA definition
dfa = {
    "q0": {"0": "q0", "1": "q1"},
    "q1": {"0": "q0", "1": "q1"}
}

start_state = "q0"
final_states = {"q1"}

# DFA to NFA conversion
nfa = {}

for state in dfa:
    nfa[state] = {}

    for symbol in dfa[state]:
        destination = dfa[state][symbol]

        # NFA stores destinations as sets
        nfa[state][symbol] = {destination}

print("DFA:")
for state, transitions in dfa.items():
    print(state, transitions)

print("\nNFA:")
for state, transitions in nfa.items():
    print(state, transitions)

print("\nState Mapping:")
for state in dfa:
    print(state, "->", state)


# Draw NFA diagram
G = nx.MultiDiGraph()

G.add_edge("q0", "q0", label="0")
G.add_edge("q0", "q1", label="1")
G.add_edge("q1", "q0", label="0")
G.add_edge("q1", "q1", label="1")

pos = {
    "q0": (0, 0),
    "q1": (2, 0)
}

plt.figure(figsize=(8, 5))

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=2500,
    node_color="lightblue",
    font_size=14,
    arrows=True
)

labels = nx.get_edge_attributes(G, "label")

nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=labels,
    font_size=12
)

plt.title("DFA to NFA Conversion")
plt.axis("off")
plt.show()