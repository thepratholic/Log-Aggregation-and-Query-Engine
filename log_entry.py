from dataclasses import dataclass

@dataclass
class LogEntry:
    timestamp: int
    level: str
    service: str
    message: str
