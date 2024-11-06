import datetime


class Project:
    """New class Project"""
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initializes a new Project instance."""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __lt__(self, other):
        """Compares two Project instances based on priority."""
        return self.priority < other.priority

    def __str__(self):
        """Returns a string representation of the Project instance."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate}, completion: {self.completion_percentage}%")

    def is_completed(self):
        """Checks if the project is completed."""
        return self.completion_percentage == 100

    def update_project(self, new_priority, new_completion_percentage):
        """Update completion and/or priority if provided (leaves as is if None)."""
        if new_completion_percentage != "":
            self.completion_percentage = new_completion_percentage
        if new_priority != "":
            self.priority = new_priority
