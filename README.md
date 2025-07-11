# OptiRoute

OptiRoute is a Python project that provides an API for solving shortest path problems using Google OR-Tools. It uses FastAPI for the web API, Pydantic for data validation, and Uvicorn as the ASGI server.

## Features
- Solve shortest path problems via API
- Built with FastAPI and Google OR-Tools
- Data validation with Pydantic

## Getting Started

### Installation
Use [UV](https://github.com/astral-sh/uv) as the package manager:

```bash
uv pip install -r requirements.txt
```

### Running the API
Use [poe](https://github.com/nat-n/poethepoet) as the task runner:

```bash
poe start
```

## API Usage
Send a POST request to `/shortest-path` with a JSON payload:
```json
{
  "nodes": ["A", "B", "C", "D"],
  "edges": [
    {"from": "A", "to": "B", "weight": 1},
    {"from": "B", "to": "C", "weight": 2},
    {"from": "C", "to": "D", "weight": 1},
    {"from": "A", "to": "D", "weight": 5}
  ],
  "start": "A",
  "end": "D"
}
```

Response:
```json
{
  "path": ["A", "B", "C", "D"],
  "total_weight": 4
}
```

## License
See LICENSE file.
