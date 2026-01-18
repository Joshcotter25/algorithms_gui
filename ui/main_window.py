import tkinter as tk
from ui.screens import PlaceholderScreen

class MainWindow(tk.Frame):
  

    def __init__(self, master):
        super().__init__(master)

        self.current_screen = None

        self.algorithms = [
            "Factorial (Recursion)",
            "Fibonacci (DP)",
            "Sorting Algorithms",
        ]

        self._build_layout()

    def _build_layout(self):
        sidebar = tk.Frame(self, width=200)
        sidebar.pack(side="left", fill="y")

        self.screen_container = tk.Frame(self)
        self.screen_container.pack(side="right", fill="both", expand=True)

        self.listbox = tk.Listbox(sidebar)
        self.listbox.pack(fill="y", expand=True)

        for algo in self.algorithms:
            self.listbox.insert(tk.END, algo)

        self.listbox.bind("<<ListboxSelect>>", self._on_select)

    def _on_select(self, event):
        selection = self.listbox.curselection()
        if not selection:
            return

        name = self.listbox.get(selection[0])
        self._load_screen(name)

    def _load_screen(self, name):
        if self.current_screen:
            self.current_screen.destroy()

        
        self.current_screen = PlaceholderScreen(self.screen_container, name)
        self.current_screen.pack(fill="both", expand=True)