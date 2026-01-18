import tkinter as tk
from ui.main_window import MainWindow

def main():
    root = tk.Tk()
    root.title("Algorithms Assignment GUI")
    root.geometry("900x600")
    MainWindow(root).pack(fill="both", expand=True)
    root.mainloop()

if __name__ == "__main__":
    main()