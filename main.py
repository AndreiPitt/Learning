from src.model import Model
from src.presenter import Presenter
from src.view import View

if __name__ == "__main__":
    model = Model()
    view = View()
    presenter = Presenter(model, view)
    view.mainloop()
