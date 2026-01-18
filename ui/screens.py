import tkinter as tk

class PlaceholderScreen(tk.Frame):
    

    def __init__(self, master, title):
        super().__init__(master)

        tk.Label(
            self,
            text=title,
            font=("Arial", 16, "bold")
        ).pack(anchor="w", pady=(10, 5))

        tk.Label(
            self,
            text="This algorithm will be implemented in a later stage.",
            font=("Arial", 11)
        ).pack(anchor="w")


class FactorialScreen(tk.Frame):
    """
    Factorial screen (to be implemented).
    """

    def __init__(self, master):
        super().__init__(master)

        tk.Label(
            self,
            text="Factorial (Recursion)",
            font=("Arial", 16, "bold")
        ).pack(anchor="w")

        tk.Label(
            self,
            text="Implementation pending.",
            font=("Arial", 11)
        ).pack(anchor="w")