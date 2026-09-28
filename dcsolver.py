from dc import DC
from search import astar_search, uniform_cost_search
 
 
cases = [
    ("why", "ask"),
    ("bear", "duck")
]
 
 
#costs = ["steps", "scrabble", "frequency"]
costs = ["frequency"]
 
for initial, goal in cases:
        for cost in costs:
            print(f"\n{initial} -> {goal}, cost={cost}")
 
 
            ucs_problem = DC(initial, goal, cost)
            print("UCS:")
            ucs_result = uniform_cost_search(ucs_problem, display=True)
            print("Solution cost:", ucs_result.path_cost)
 
 
            astar_problem = DC(initial, goal, cost)
            print("A*:")
            astar_result = astar_search(astar_problem, display=True)
            print("Solution cost:", astar_result.path_cost)