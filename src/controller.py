from src.model import GymSession, ToDoTask


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_gym_session(self, exercise, sets, reps):
        new_session = GymSession(exercise, sets, reps)
        self.model["gym_sessions"].append(new_session)

    def add_task(self, task, category, deadline):
        new_task = ToDoTask(task, category, deadline)
        self.model["tasks"].append(new_task)

    def display_data(self):
        self.view.display_gym_sessions(self.model["gym_sessions"])
        self.view.display_tasks(self.model["tasks"])
