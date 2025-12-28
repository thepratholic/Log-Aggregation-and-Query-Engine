from log_entry import LogEntry
from log_engine import LogAggregationEngine

# Engine create karo
engine = LogAggregationEngine()

# Sample logs add karo
logs = [
    LogEntry(100, "INFO", "auth-service", "User logged in"),
    LogEntry(105, "ERROR", "auth-service", "Invalid password"),
    LogEntry(110, "INFO", "payment-service", "Payment successful"),
    LogEntry(120, "ERROR", "payment-service", "Payment failed"),
    LogEntry(125, "WARN", "auth-service", "Password attempt limit nearing")
]

for log in logs:
    engine.add_log(log)


# Query by level
error_logs = engine.get_by_level("ERROR")
print("ERROR logs:")
for log in error_logs:
    print(log)

# Query by service
auth_logs = engine.get_by_service("auth-service")
print("\nAuth-service logs:")
for log in auth_logs:
    print(log)

# Query by time range
time_logs = engine.get_by_time_range(105, 120)
print("\nLogs from time 105 to 120:")
for log in time_logs:
    print(log)

top_errors = engine.top_k_errors(2)
print("\nTop 2 ERROR messages:")
for msg, freq in top_errors:
    print(f"{msg} -> {freq} times")
