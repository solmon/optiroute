from fastapi import FastAPI
from .services import ShortestPathSolver, ShortestPathRequest, ShortestPathResponse

app = FastAPI()

# Initialize the solver
shortest_path_solver = ShortestPathSolver()

@app.post("/shortest-path", response_model=ShortestPathResponse)
def shortest_path(data: ShortestPathRequest):
    """Endpoint for solving shortest path problems."""
    return shortest_path_solver.solve(data)
