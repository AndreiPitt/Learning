from src.Controller.controller import Controller
from src.Model.model import Model
from src.View.view import View

if __name__ == "__main__":
    model = Model()
    view = View()
    controller = Controller(model, view)
    controller.run()
