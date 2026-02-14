from src.dijkstra import dijkstra_simple

graph = {
    "A": {"B": 0.2, "C": 0.5},
    "B": {"A": 0.2, "C": 0.3, "D": 0.4},
    "C": {"A": 0.5, "B": 0.3, "D": 0.1},
    "D": {"B": 0.4, "C": 0.1}
}

result = dijkstra_simple(graph, "A", "D")
print("A به D:", result)
