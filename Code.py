import tkinter as tk
import random

WORDS= [
    "array", "class", "while", "break", "input", "print", "debug", "scope", "stack",
    "queue", "token", "float", "tuple", "macro", "logic", "const",
    "error", "bytes", "fetch", "cache", "trace", "scope", "index", "event",
    "click", "linux", "graph", "loops", "mouse", "intel", "cloud", "write", "block"
]

class ColorWordle:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Game")
        self.root.geometry("400x550")
        self.root.resizable(False, False)

        self.create_widgets()
        self.start_new_game()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Guess the 5-letter word:", font=("Arial", 14))
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.root, font=("Arial", 14), justify='center')
        self.entry.pack(pady=5)
        self.entry.bind("<Return>", self.check_guess)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.history_frame = tk.Frame(self.root)
        self.history_frame.pack(pady=10)

        self.play_again_btn = tk.Button(self.root, text="Play Again", font=("Arial", 12),
                                        command=self.start_new_game, state="disabled")
        self.play_again_btn.pack(pady=10)

    def start_new_game(self):
        self.word = random.choice(WORDS)
        self.tries = 0
        self.entry.config(state="normal")
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.play_again_btn.config(state="disabled")

        # Clear previous history
        for widget in self.history_frame.winfo_children():
            widget.destroy()

    def check_guess(self, event=None):
        guess = self.entry.get().lower()
        if len(guess) != 5 or not guess.isalpha():
            self.result_label.config(text="Enter a valid 5-letter word.", fg="red")
            return

        self.tries += 1
        row_frame = tk.Frame(self.history_frame)
        row_frame.pack()

        for i in range(5):
            letter = guess[i].upper()
            color = "light gray"
            if guess[i] == self.word[i]:
                color = "green"
            elif guess[i] in self.word:
                color = "yellow"

            lbl = tk.Label(row_frame, text=letter, width=4, font=("Courier", 16), bg=color, relief="ridge")
            lbl.pack(side="left", padx=2, pady=2)

        if guess == self.word:
            self.result_label.config(text=f"Correct! You guessed it in {self.tries} tries!", fg="green")
            self.entry.config(state='disabled')
            self.play_again_btn.config(state="normal")
        elif self.tries == 6:
            self.result_label.config(text=f"Out of tries! The word was: {self.word}", fg="blue")
            self.entry.config(state='disabled')
            self.play_again_btn.config(state="normal")

        self.entry.delete(0, tk.END)

if __name__ == '__main__':
    root = tk.Tk()
    app = ColorWordle(root)
    root.mainloop()
