class GymSession:
    def __init__(self, exercise, sets, reps):
        self.exercise = exercise
        self.sets = sets
        self.reps = reps

    def __str__(self):
        return f"{self.exercise}: {self.sets} sets of {self.reps} reps"


class ToDoTask:
    def __init__(self, task, category, deadline):
        self.task = task
        self.category = category
        self.deadline = deadline

    def __str__(self):
        return f"Task: {self.task}, Category: {self.category}, Deadline: {self.deadline}"
