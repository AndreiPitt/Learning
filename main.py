from src.controller import Controller
from src.view import View

if __name__ == "__main__":
    import tkinter as tk

    # Initial model data
    model = {
        "gym_sessions": [],
        "tasks": []
    }

    # Create the main Tkinter window
    root = tk.Tk()

    # Create the view
    view = View(root)

    # Create the controller
    controller = Controller(model, view)

    # Add some sample data
    controller.add_gym_session("Bench Press", 3, 10)
    controller.add_gym_session("Squats", 4, 12)
    controller.add_task("Finish project report", "Work", "2025-03-01")
    controller.add_task("Buy groceries", "Personal", "2025-02-27")

    # Display data
    controller.display_data()

    # Start the Tkinter main loop
    root.mainloop()
