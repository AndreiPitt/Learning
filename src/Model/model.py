class Model:
    """
    Model class, abstracts the core data of the MVC pattern, model maintains updates data based on events/calls it
    receives from Controller. Dependency should be one-way, Controller - Model, in other words, Model functions should
    not actively call methods of Controller or View.
    """
    def __init__(self):
        pass
