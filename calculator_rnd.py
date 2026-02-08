import tkinter as tk
from tkinter import ttk, messagebox

# Główna klasa kalkulatora
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("600x300")
        
        # Tworzymy dwa kalkulatory obok siebie
        self.create_calc(root, 0, "LED")
        self.create_calc(root, 1, "BAT")
    
    # Funkcja tworząca jeden kalkulator
    def create_calc(self, root, index, name):
        # Rama dla kalkulatora
        frame = ttk.Frame(root, padding=10)
        frame.pack(side="left", fill="both", expand=True)
        
        # Tytuł kalkulatora
        ttk.Label(frame, text=name, font=("Arial", 12, "bold")).pack(pady=5)
        
        # Pole dla zmiennej a (Rp)
        ttk.Label(frame, text="Rp:").pack(pady=5)
        a_input = ttk.Entry(frame, width=20)
        a_input.pack(pady=2)
        
        # Pole dla zmiennej b (Opk)
        ttk.Label(frame, text="Opk:").pack(pady=5)
        b_input = ttk.Entry(frame, width=20)
        b_input.pack(pady=2)
        
        # Pole dla formuły
        ttk.Label(frame, text="Formula:").pack(pady=5)
        formula_input = ttk.Entry(frame, width=20)
        formula_input.pack(pady=2)
        formula_input.insert(0, "1/(a*b)")
        
        # Przycisk do obliczenia
        ttk.Button(frame, text="Calculate", command=lambda: self.calc(a_input, b_input, formula_input, result)).pack(pady=10)
        
        # Label na wynik
        result = ttk.Label(frame, text="", font=("Arial", 12, "bold"), foreground="blue")
        result.pack(pady=10)
        
        # Enter uruchamia obliczenie
        frame.bind("<Return>", lambda e: self.calc(a_input, b_input, formula_input, result))
    
    # Funkcja obliczająca wynik
    def calc(self, a_input, b_input, formula_input, result):
        try:
            # Pobieramy wartości z pól i zamieniamy przecinek na kropkę
            a = float(a_input.get().replace(",", "."))
            b = float(b_input.get().replace(",", "."))
            formula = formula_input.get()
            
            # Obliczamy wynik
            res = eval(formula, {"__builtins__": {}}, {"a": a, "b": b})
            result.config(text=f"Result: {res}", foreground="green")
        
        # Obsługa błędów
        except Exception as e:
            messagebox.showerror("Error", str(e))
            result.config(text="Error!", foreground="red")

# Uruchomienie aplikacji
if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
