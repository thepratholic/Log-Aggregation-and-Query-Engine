# Log Aggregation & Query Engine

## Project Idea
This project is an in-memory log aggregation and query engine. Logs are indexed by:
- Level (ERROR, INFO, WARN)
- Service (auth-service, payment-service)
- Timestamp (sorted for fast range queries)

The engine supports:
- Fast queries by level and service
- Efficient time-range queries
- Top-K error message analytics

## Data Structures
- `dict + list` for level and service indexes
- `dict + sorted list` for timestamp index
- `Counter` and `heapq` for top-K errors

## Time Complexity
- add_log(): O(log n) for timestamp insertion  
- get_by_level/service(): O(1)  
- get_by_time_range(): O(log n + k)  
- top_k_errors(): O(n + k log k)

## Usage
1. Import `LogEntry` and `LogAggregationEngine`
2. Add logs via `add_log()`
3. Run queries like `get_by_level()`, `get_by_service()`, `get_by_time_range()`, `top_k_errors()`
