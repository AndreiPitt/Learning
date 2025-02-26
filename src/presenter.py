class Presenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.on_button_click = self.on_button_click
        self.update_view()

    def update_view(self):
        data = self.model.get_data()
        self.view.set_label_text(data)

    def on_button_click(self):
        # Aici poți adăuga logica ce trebuie executată la click-ul butonului
        self.update_view()
