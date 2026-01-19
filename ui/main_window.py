import tkinter as tk
from ui.screens import (
    PlaceholderScreen,
    FactorialScreen,
    FibonacciScreen,
    SortsScreen,
    MergeSortScreen,
    ShuffleCardsScreen,
    StatsScreen,
    PalindromeScreen,
    PatternsDemoScreen,
    RSAScreen
)

class MainWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.algorithms = [
            "RSA Encrypt/Decrypt",
            "Fibonacci (DP)",
            "Selection/Bubble Sort",
            "Merge Sort (Divide & Conquer)",
            "Shuffle Deck (Randomised)",
            "Factorial (Recursion)",
            "Array Stats (Search)",
            "Palindrome Substrings (Memoization)",
            "Design Patterns Demo",
        ]

        left = tk.Frame(self, width=250)
        left.pack(side="left", fill="y")

        right = tk.Frame(self)
        right.pack(side="right", fill="both", expand=True)

        tk.Label(left, text="Choose Algorithm", font=("Arial", 12, "bold")).pack(padx=10, pady=(10, 0))

        self.listbox = tk.Listbox(left)
        for name in self.algorithms:
            self.listbox.insert(tk.END, name)
        self.listbox.pack(fill="both", expand=True, padx=10, pady=10)
        self.listbox.bind("<<ListboxSelect>>", self._on_select)

        self.screen_container = right
        self.current_screen = None

        self.listbox.selection_set(1)
        self._load_screen(self.algorithms[1])

    def _on_select(self, event):
        idxs = self.listbox.curselection()
        if not idxs:
            return
        name = self.listbox.get(idxs[0])
        self._load_screen(name)

    def _load_screen(self, name: str):
        if self.current_screen is not None:
            self.current_screen.destroy()

        if name == "Factorial (Recursion)":
            self.current_screen = FactorialScreen(self.screen_container)
        elif name == "Fibonacci (DP)":
            self.current_screen = FibonacciScreen(self.screen_container)
        elif name == "Selection/Bubble Sort":
            self.current_screen = SortsScreen(self.screen_container)
        elif name == "Merge Sort (Divide & Conquer)":
            self.current_screen = MergeSortScreen(self.screen_container)
        elif name == "Shuffle Deck (Randomised)":
            self.current_screen = ShuffleCardsScreen(self.screen_container)
        elif name == "Array Stats (Search)":
            self.current_screen = StatsScreen(self.screen_container)
        elif name == "Palindrome Substrings (Memoization)":
            self.current_screen = PalindromeScreen(self.screen_container)
        elif name == "Design Patterns Demo":
            self.current_screen = PatternsDemoScreen(self.screen_container)
        elif name == "RSA Encrypt/Decrypt":
            self.current_screen = RSAScreen(self.screen_container)
        else:
            self.current_screen = PlaceholderScreen(self.screen_container, name)

        self.current_screen.pack(fill="both", expand=True, padx=10, pady=10)