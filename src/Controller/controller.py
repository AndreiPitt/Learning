
class Controller:
    """
    Controller is the primary coordinator in the MVC pattern, it collects user input, initiates necessary changes to
    model (data) and refreshes View to reflect any changes that might have happened.
    """
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        self.view.start()
