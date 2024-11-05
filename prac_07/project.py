import datetime


class Project:
    def __init__(self, name=str, start_data=datetime, priority=int, cost_estimate=float, completion_percentage=int):
        self.name = name
        self.start_data = start_data
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return (f"{self.name}, start: {self.start_data}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate}, completion: {self.completion_percentage} %")

    def is_completed(self):
        return self.completion_percentage == 100
