import datetime


class Project:
    def __init__(self, name=str, start_date=datetime, priority=int, cost_estimate=float, completion_percentage=int):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime("%d/%m/%Y")}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate}, completion: {self.completion_percentage} %")

    def is_completed(self):
        return self.completion_percentage == 100

    def update_project(self, new_priority, new_completion_percentage):
        """Update completion and/or priority if provided (leaves as is if None)."""
        if new_completion_percentage != "":
            self.completion_percentage = new_completion_percentage
        if new_priority != "":
            self.priority = new_priority
