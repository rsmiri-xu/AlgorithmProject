from src.graph import SemanticGraph
from src.dijkstra import dijkstra_simple
from src.LLMhelper import get_semantic_similarity

def main():
    words = [w.strip() for w in input("کلمات (با کاما): ").split(",")]
    graph = SemanticGraph(words)
    
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            w1, w2 = words[i], words[j]
            weight = get_semantic_similarity(w1, w2)
            graph.add_edge(w1, w2, weight)
            print(f"{w1}-{w2}: {weight}")
    
    start = input("مبدأ: ").strip()
    end = input("مقصد: ").strip()
    
    result = dijkstra_simple(graph.graph, start, end)
    if result:
        path, cost = result
        print(f"مسیر: {' → '.join(path)}")
        print(f"هزینه: {cost}")
    else:
        print("مسیر وجود ندارد")

if __name__ == "__main__":
    main()