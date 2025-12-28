from collections import defaultdict, Counter
import bisect, heapq

class LogAggregationEngine:
    def __init__(self):
        self.all_logs = []

        self.level_index = defaultdict(list)
        self.service_index = defaultdict(list)
        self.time_index = defaultdict(list)

        self.timestamps = []


    def add_log(self, log):
        self.all_logs.append(log)

        self.level_index[log.level].append(log)

        self.service_index[log.service].append(log)

        self.time_index[log.timestamp].append(log)

        bisect.insort(self.timestamps, log.timestamp)


    def get_by_level(self, level):
        return self.level_index.get(level, [])


    def get_by_service(self, service):
        return self.service_index.get(service, [])


    def get_by_time_range(self, start, end):
        result = []

        left = bisect.bisect_left(self.timestamps, start)
        right = bisect.bisect_right(self.timestamps, end)

        for ts in self.timestamps[left:right]:
            result.extend(self.time_index[ts])

        return result


    def top_k_errors(self, k):
        error_logs = self.get_by_level("ERROR")
        
        counter = Counter(log.message for log in error_logs)
        
        top_k = heapq.nlargest(k, counter.items(), key=lambda x: x[1])
        
        return top_k