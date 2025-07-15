from pydantic import BaseModel, Field
from typing import List
from ortools.graph.python import min_cost_flow


class Edge(BaseModel):
    from_: str = Field(..., alias="from")
    to: str
    weight: int


class ShortestPathRequest(BaseModel):
    nodes: List[str]
    edges: List[Edge]
    start: str
    end: str


class ShortestPathResponse(BaseModel):
    path: List[str]
    total_weight: int


class ShortestPathSolver:
    """Solver for shortest path problems using Google OR-Tools."""
    
    def solve(self, data: ShortestPathRequest) -> ShortestPathResponse:
        """
        Solve the shortest path problem using min-cost flow algorithm.
        
        Args:
            data: Request containing nodes, edges, start and end points
            
        Returns:
            Response containing the shortest path and total weight
        """
        node_indices = {name: idx for idx, name in enumerate(data.nodes)}
        start_idx = node_indices[data.start]
        end_idx = node_indices[data.end]
        
        solver = min_cost_flow.SimpleMinCostFlow()
        
        # Add edges to the graph
        for edge in data.edges:
            solver.add_arc_with_capacity_and_unit_cost(
                node_indices[edge.from_], node_indices[edge.to], 1, edge.weight
            )
        
        # Set supply/demand: source has supply 1, sink has demand 1, others are balanced
        for idx in node_indices.values():
            solver.set_node_supply(idx, 0)
        solver.set_node_supply(start_idx, 1)
        solver.set_node_supply(end_idx, -1)
        
        # Solve the problem
        if solver.solve() != solver.OPTIMAL:
            return ShortestPathResponse(path=[], total_weight=-1)
        
        # Reconstruct the path
        arcs = solver.num_arcs()
        path = [data.start]
        current = start_idx
        
        while current != end_idx:
            for i in range(arcs):
                if solver.flow(i) > 0 and solver.tail(i) == current:
                    next_idx = solver.head(i)
                    path.append(data.nodes[next_idx])
                    current = next_idx
                    break
            else:
                break
        
        total_weight = solver.optimal_cost()
        return ShortestPathResponse(path=path, total_weight=total_weight)
