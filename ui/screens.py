import tkinter as tk
from tkinter import messagebox

from algorithms.factorial import factorial
from algorithms.fibonacci import fib_dp
from algorithms.sorts import selection_sort, bubble_sort
from algorithms.mergesort import merge_sort
from algorithms.cards import create_deck, fisher_yates_shuffle
from algorithms.stats_search import stats_summary
from algorithms.palindromes import count_pal_substrings
from algorithms.rsa import generate_keypair, encrypt_text, decrypt_to_text
from patterns.observer import Subject, TextBoxObserver
from patterns.factory import TransformFactory
from patterns.decorator import timed


def parse_int_array(text: str):
    raw = text.replace(",", " ").split()
    if not raw:
        raise ValueError("Array cannot be empty.")
    return [int(x) for x in raw]


class PlaceholderScreen(tk.Frame):
    def __init__(self, master, title: str):
        super().__init__(master)
        tk.Label(self, text=title, font=("Arial", 16, "bold")).pack(anchor="w")
        tk.Label(self, text="Not implemented yet.", font=("Arial", 11)).pack(anchor="w", pady=(8, 0))


class FactorialScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="Factorial (Recursion)", font=("Arial", 16, "bold")).pack(anchor="w")

        form = tk.Frame(self)
        form.pack(anchor="w", pady=(12, 8), fill="x")

        tk.Label(form, text="Enter n (integer >= 0):").grid(row=0, column=0, sticky="w")
        self.n_entry = tk.Entry(form, width=20)
        self.n_entry.grid(row=0, column=1, sticky="w", padx=(8, 0))
        self.n_entry.insert(0, "6")

        tk.Button(form, text="Run", command=self._run).grid(row=0, column=2, padx=(12, 0))

        self.output = tk.Text(self, height=8)
        self.output.pack(fill="both", expand=False)

    def _run(self):
        try:
            n = int(self.n_entry.get().strip())
            res = factorial(n)
            self.output.delete("1.0", tk.END)
            self.output.insert(tk.END, f"{n}! = {res}\n")
        except ValueError as e:
            messagebox.showerror("Invalid input", str(e))


class FibonacciScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="Fibonacci (Dynamic Programming)", font=("Arial", 16, "bold")).pack(anchor="w")

        form = tk.Frame(self)
        form.pack(anchor="w", pady=(12, 8), fill="x")

        tk.Label(form, text="Enter n (integer >= 0):").grid(row=0, column=0, sticky="w")
        self.n_entry = tk.Entry(form, width=20)
        self.n_entry.grid(row=0, column=1, sticky="w", padx=(8, 0))
        self.n_entry.insert(0, "10")

        tk.Button(form, text="Run", command=self._run).grid(row=0, column=2, padx=(12, 0))

        self.output = tk.Text(self, height=8)
        self.output.pack(fill="both", expand=False)

    def _run(self):
        try:
            n = int(self.n_entry.get().strip())
            res = fib_dp(n)
            self.output.delete("1.0", tk.END)
            self.output.insert(tk.END, f"fib({n}) = {res}\n")
        except ValueError as e:
            messagebox.showerror("Invalid input", str(e))


class SortsScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="Selection & Bubble Sort", font=("Arial", 16, "bold")).pack(anchor="w")

        form = tk.Frame(self)
        form.pack(anchor="w", pady=(12, 8), fill="x")

        tk.Label(form, text="Enter array:").grid(row=0, column=0, sticky="w")
        self.array_entry = tk.Entry(form, width=45)
        self.array_entry.grid(row=0, column=1, columnspan=3, sticky="w", padx=(8, 0))
        self.array_entry.insert(0, "5, 3, 1, 4")

        tk.Label(form, text="Order:").grid(row=1, column=0, sticky="w", pady=(8, 0))
        self.order_var = tk.StringVar(value="Ascending")
        tk.OptionMenu(form, self.order_var, "Ascending", "Descending").grid(row=1, column=1, sticky="w")

        tk.Label(form, text="Algorithm:").grid(row=1, column=2, sticky="w")
        self.alg_var = tk.StringVar(value="Selection Sort")
        tk.OptionMenu(form, self.alg_var, "Selection Sort", "Bubble Sort").grid(row=1, column=3, sticky="w")

        tk.Button(self, text="Run", command=self._run).pack(anchor="w", pady=(10, 0))

        self.output = tk.Text(self, height=9)
        self.output.pack(fill="both", expand=False)

    def _run(self):
        try:
            arr = parse_int_array(self.array_entry.get())
            ascending = self.order_var.get() == "Ascending"

            if self.alg_var.get() == "Selection Sort":
                res = selection_sort(arr, ascending)
            else:
                res = bubble_sort(arr, ascending)

            self.output.delete("1.0", tk.END)
            self.output.insert(tk.END, f"Original: {arr}\nSorted:   {res}\n")
        except ValueError as e:
            messagebox.showerror("Invalid input", str(e))


class MergeSortScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="Merge Sort (Divide & Conquer)", font=("Arial", 16, "bold")).pack(anchor="w")

        form = tk.Frame(self)
        form.pack(anchor="w", pady=(12, 8), fill="x")

        tk.Label(form, text="Enter array:").grid(row=0, column=0, sticky="w")
        self.array_entry = tk.Entry(form, width=45)
        self.array_entry.grid(row=0, column=1, sticky="w", padx=(8, 0))
        self.array_entry.insert(0, "9, 2, 7, 1, 5")

        tk.Label(form, text="Order:").grid(row=1, column=0, sticky="w", pady=(8, 0))
        self.order_var = tk.StringVar(value="Ascending")
        tk.OptionMenu(form, self.order_var, "Ascending", "Descending").grid(row=1, column=1, sticky="w")

        tk.Button(self, text="Run", command=self._run).pack(anchor="w", pady=(10, 0))

        self.output = tk.Text(self, height=9)
        self.output.pack(fill="both", expand=False)

    def _run(self):
        try:
            arr = parse_int_array(self.array_entry.get())
            ascending = self.order_var.get() == "Ascending"
            res = merge_sort(arr, ascending)

            self.output.delete("1.0", tk.END)
            self.output.insert(tk.END, f"Original: {arr}\nSorted:   {res}\n")
        except ValueError as e:
            messagebox.showerror("Invalid input", str(e))


class ShuffleCardsScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="Shuffle Deck (Randomised)", font=("Arial", 16, "bold")).pack(anchor="w")
        tk.Button(self, text="Shuffle Deck", command=self._run).pack(anchor="w", pady=(12, 8))

        self.output = tk.Text(self, height=18)
        self.output.pack(fill="both", expand=False)

    def _run(self):
        deck = create_deck()
        shuffled = fisher_yates_shuffle(deck)

        self.output.delete("1.0", tk.END)
        for i, card in enumerate(shuffled, start=1):
            self.output.insert(tk.END, f"{i:02d}. {card}\n")


class StatsScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="Array Stats (Search)", font=("Arial", 16, "bold")).pack(anchor="w")

        form = tk.Frame(self)
        form.pack(anchor="w", pady=(12, 8), fill="x")

        tk.Label(form, text="Enter array:").grid(row=0, column=0, sticky="w")
        self.array_entry = tk.Entry(form, width=45)
        self.array_entry.grid(row=0, column=1, sticky="w", padx=(8, 0))
        self.array_entry.insert(0, "1, 2, 2, 3, 4, 9")

        tk.Button(self, text="Analyse", command=self._run).pack(anchor="w", pady=(10, 0))

        self.output = tk.Text(self, height=12)
        self.output.pack(fill="both", expand=False)

    def _run(self):
        try:
            arr = parse_int_array(self.array_entry.get())
            summary = stats_summary(arr)

            self.output.delete("1.0", tk.END)
            self.output.insert(tk.END, f"Smallest: {summary['smallest']}\n")
            self.output.insert(tk.END, f"Largest:  {summary['largest']}\n")
            self.output.insert(tk.END, f"Mode:     {summary['mode']}\n")
            self.output.insert(tk.END, f"Median:   {summary['median']}\n")
            self.output.insert(tk.END, f"Q1:       {summary['q1']}\n")
            self.output.insert(tk.END, f"Q3:       {summary['q3']}\n")
            self.output.insert(tk.END, f"Sorted:   {summary['sorted']}\n")
        except ValueError as e:
            messagebox.showerror("Invalid input", str(e))


class PalindromeScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="Palindrome Substrings (Memoization)", font=("Arial", 16, "bold")).pack(anchor="w")

        form = tk.Frame(self)
        form.pack(anchor="w", pady=(12, 8), fill="x")

        tk.Label(form, text="Enter string:").grid(row=0, column=0, sticky="w")
        self.s_entry = tk.Entry(form, width=45)
        self.s_entry.grid(row=0, column=1, sticky="w", padx=(8, 0))
        self.s_entry.insert(0, "ababa")

        tk.Button(self, text="Count", command=self._run).pack(anchor="w", pady=(10, 0))

        self.output = tk.Text(self, height=8)
        self.output.pack(fill="both", expand=False)

    def _run(self):
        s = self.s_entry.get()
        count = count_pal_substrings(s)
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, f"Total palindromic substrings: {count}\n")


class PatternsDemoScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="Design Patterns Demo", font=("Arial", 16, "bold")).pack(anchor="w")

        # Behavioral: Observer
        tk.Label(self, text="Behavioral Pattern: Observer", font=("Arial", 12, "bold")).pack(anchor="w", pady=(10, 0))
        self.log = tk.Text(self, height=7)
        self.log.pack(fill="x", pady=(4, 6))

        self.subject = Subject()
        self.subject.attach(TextBoxObserver(self.log))
        tk.Button(self, text="Notify observers", command=self._notify).pack(anchor="w")

        # Creational: Factory Method
        tk.Label(self, text="Creational Pattern: Factory Method", font=("Arial", 12, "bold")).pack(anchor="w", pady=(14, 0))
        f = tk.Frame(self); f.pack(anchor="w", pady=(4, 0))
        self.factory_var = tk.StringVar(value="Reverse")
        tk.OptionMenu(f, self.factory_var, "Reverse", "Uppercase").grid(row=0, column=0, sticky="w")
        self.factory_input = tk.Entry(f, width=30)
        self.factory_input.grid(row=0, column=1, padx=(8, 0))
        self.factory_input.insert(0, "Hello World")
        tk.Button(f, text="Run", command=self._factory_run).grid(row=0, column=2, padx=(8, 0))

        self.factory_out = tk.Label(self, text="")
        self.factory_out.pack(anchor="w", pady=(4, 0))

        # Structural: Decorator
        tk.Label(self, text="Structural Pattern: Decorator", font=("Arial", 12, "bold")).pack(anchor="w", pady=(14, 0))
        tk.Button(self, text="Time fib(30)", command=self._decorator_run).pack(anchor="w", pady=(4, 0))
        self.decorator_out = tk.Label(self, text="")
        self.decorator_out.pack(anchor="w", pady=(4, 0))

    def _notify(self):
        self.subject.notify("Observer event fired from GUI!")

    def _factory_run(self):
        try:
            transform = TransformFactory.create(self.factory_var.get())
            result = transform.run(self.factory_input.get())
            self.factory_out.config(text=f"Result: {result}")
        except ValueError as e:
            messagebox.showerror("Factory error", str(e))

    def _decorator_run(self):
        @timed
        def compute():
            return fib_dp(30)

        result, elapsed = compute()
        self.decorator_out.config(text=f"fib(30) = {result} | time: {elapsed:.6f}s")

class RSAScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="RSA Encrypt / Decrypt", font=("Arial", 16, "bold")).pack(anchor="w")

        # Mode
        mode_frame = tk.Frame(self)
        mode_frame.pack(anchor="w", pady=(10, 0))

        tk.Label(mode_frame, text="Mode:").grid(row=0, column=0, sticky="w")
        self.mode_var = tk.StringVar(value="Encrypt")
        tk.OptionMenu(mode_frame, self.mode_var, "Encrypt", "Decrypt").grid(row=0, column=1, sticky="w", padx=(8, 0))

        # Message / Ciphertext
        msg_frame = tk.Frame(self)
        msg_frame.pack(anchor="w", pady=(10, 0), fill="x")

        tk.Label(msg_frame, text="Input (Encrypt: text | Decrypt: integer ciphertext):").pack(anchor="w")
        self.input_box = tk.Text(msg_frame, height=4)
        self.input_box.pack(fill="x")

        # Keys
        key_frame = tk.Frame(self)
        key_frame.pack(anchor="w", pady=(10, 0), fill="x")

        tk.Label(key_frame, text="Keys (optional). If blank, auto-generate keys:").grid(row=0, column=0, columnspan=6, sticky="w")

        tk.Label(key_frame, text="n:").grid(row=1, column=0, sticky="w")
        self.n_entry = tk.Entry(key_frame, width=18)
        self.n_entry.grid(row=1, column=1, sticky="w", padx=(6, 12))

        tk.Label(key_frame, text="e:").grid(row=1, column=2, sticky="w")
        self.e_entry = tk.Entry(key_frame, width=10)
        self.e_entry.grid(row=1, column=3, sticky="w", padx=(6, 12))

        tk.Label(key_frame, text="d:").grid(row=1, column=4, sticky="w")
        self.d_entry = tk.Entry(key_frame, width=18)
        self.d_entry.grid(row=1, column=5, sticky="w", padx=(6, 0))

        # Optional p,q for user-supplied primes
        pq_frame = tk.Frame(self)
        pq_frame.pack(anchor="w", pady=(6, 0))

        tk.Label(pq_frame, text="(Optional) p:").grid(row=0, column=0, sticky="w")
        self.p_entry = tk.Entry(pq_frame, width=10)
        self.p_entry.grid(row=0, column=1, sticky="w", padx=(6, 12))

        tk.Label(pq_frame, text="q:").grid(row=0, column=2, sticky="w")
        self.q_entry = tk.Entry(pq_frame, width=10)
        self.q_entry.grid(row=0, column=3, sticky="w", padx=(6, 12))

        tk.Label(pq_frame, text="(Leave p/q empty for auto primes)").grid(row=0, column=4, sticky="w")

        # Buttons
        btn_frame = tk.Frame(self)
        btn_frame.pack(anchor="w", pady=(10, 0))

        tk.Button(btn_frame, text="Run", command=self._run).grid(row=0, column=0, padx=(0, 8))
        tk.Button(btn_frame, text="Generate Keys", command=self._gen_keys).grid(row=0, column=1)

        # Output
        tk.Label(self, text="Output:").pack(anchor="w", pady=(10, 0))
        self.output = tk.Text(self, height=10)
        self.output.pack(fill="both", expand=False)

        # Defaults
        self.input_box.insert("1.0", "Hello")

    def _gen_keys(self):
        try:
            p = self._try_int(self.p_entry.get())
            q = self._try_int(self.q_entry.get())
            n, e, d, p_used, q_used = generate_keypair(p=p, q=q)

            self.n_entry.delete(0, tk.END)
            self.e_entry.delete(0, tk.END)
            self.d_entry.delete(0, tk.END)

            self.n_entry.insert(0, str(n))
            self.e_entry.insert(0, str(e))
            self.d_entry.insert(0, str(d))

            self.output.delete("1.0", tk.END)
            self.output.insert(tk.END, "Generated RSA keys:\n")
            self.output.insert(tk.END, f"p = {p_used}\nq = {q_used}\n")
            self.output.insert(tk.END, f"n = {n}\ne = {e}\nd = {d}\n")
        except Exception as ex:
            messagebox.showerror("RSA key generation error", str(ex))

    def _run(self):
        try:
            mode = self.mode_var.get()

            # If user provided n/e/d, use them. Otherwise generate keys.
            n = self._try_int(self.n_entry.get())
            e = self._try_int(self.e_entry.get())
            d = self._try_int(self.d_entry.get())

            if n is None or (e is None and mode == "Encrypt") or (d is None and mode == "Decrypt"):
                # Try p/q if provided; else auto-generate
                p = self._try_int(self.p_entry.get())
                q = self._try_int(self.q_entry.get())
                n, e, d, p_used, q_used = generate_keypair(p=p, q=q)

            user_input = self.input_box.get("1.0", tk.END).strip()

            self.output.delete("1.0", tk.END)

            if mode == "Encrypt":
                ciphertext = encrypt_text(user_input, n, e)
                self.output.insert(tk.END, "ENCRYPT RESULT\n")
                self.output.insert(tk.END, f"ciphertext (int) = {ciphertext}\n\n")
                self.output.insert(tk.END, "KEYS USED\n")
                self.output.insert(tk.END, f"n = {n}\n")
                self.output.insert(tk.END, f"e = {e}\n")
                self.output.insert(tk.END, f"d = {d}\n")
            else:
                ciphertext = int(user_input)
                plaintext = decrypt_to_text(ciphertext, n, d)
                self.output.insert(tk.END, "DECRYPT RESULT\n")
                self.output.insert(tk.END, f"plaintext = {plaintext}\n\n")
                self.output.insert(tk.END, "KEYS USED\n")
                self.output.insert(tk.END, f"n = {n}\n")
                self.output.insert(tk.END, f"e = {e}\n")
                self.output.insert(tk.END, f"d = {d}\n")

        except ValueError as ex:
            messagebox.showerror("RSA input error", str(ex))
        except Exception as ex:
            messagebox.showerror("RSA error", str(ex))

    @staticmethod
    def _try_int(text: str):
        t = text.strip()
        if t == "":
            return None
        return int(t)