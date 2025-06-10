import tkinter as tk
from tkinter import messagebox, ttk
import random
import csv
from datetime import datetime, timedelta
import os

CSV_FILE = "game_results.csv"

difficulty_levels = {
    "Easy": (1, 10, 5),
    "Medium": (1, 50, 7),
    "Hard": (1, 100, 10)
}

def get_indian_datetime():
    now = datetime.utcnow() + timedelta(hours=5, minutes=30)
    return now.strftime("%d-%m-%Y"), now.strftime("%H:%M:%S")

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.secret_number = None
        self.attempts = 0
        self.max_attempts = 0
        self.score = 0
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text=" Number Guessing Game", font=("Arial", 16, "bold")).pack(pady=10)

        tk.Label(self.root, text="Enter Your Name:").pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack(pady=5)

        self.diff_var = tk.StringVar(value="Easy")
        tk.Label(self.root, text="Select Difficulty:").pack()
        tk.OptionMenu(self.root, self.diff_var, *difficulty_levels.keys()).pack(pady=5)

        tk.Button(self.root, text="Start Game", command=self.start_game).pack(pady=10)

        self.input_label = tk.Label(self.root, text="")
        self.input_label.pack()
        self.entry = tk.Entry(self.root)
        self.submit_button = tk.Button(self.root, text="Submit Guess", command=self.check_guess)
        self.result_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.result_label.pack(pady=5)

        tk.Button(self.root, text="Show Leaderboard", command=self.show_leaderboard).pack(pady=5)

    def start_game(self):
        player_name = self.name_entry.get().strip()
        if not player_name:
            messagebox.showwarning("Missing Name", "Please enter your name to play.")
            return

        diff = self.diff_var.get()
        low, high, self.max_attempts = difficulty_levels[diff]
        self.secret_number = random.randint(low, high)
        self.attempts = 0
        self.score = 0

        self.input_label.config(text=f"Guess a number between {low} and {high} (Attempts: {self.max_attempts})")
        self.entry.delete(0, tk.END)
        self.entry.pack()
        self.submit_button.pack()
        self.result_label.config(text="")

    def check_guess(self):
        guess = self.entry.get()
        if not guess.isdigit():
            messagebox.showwarning("Invalid Input", "Please enter a valid number.")
            return

        guess = int(guess)
        self.attempts += 1

        if guess < self.secret_number:
            self.result_label.config(text="📉 Too low!")
        elif guess > self.secret_number:
            self.result_label.config(text="📈 Too high!")
        else:
            self.score = 100 - (self.attempts - 1) * 10
            self.result_label.config(text=f" Correct! Score: {self.score}")
            messagebox.showinfo("Congratulations!", f"You guessed it right!\nScore: {self.score}")
            self.save_result("Win")
            self.reset_game()
            return

        if self.attempts >= self.max_attempts:
            self.result_label.config(text=f" Out of attempts! The number was {self.secret_number}.")
            self.save_result("Lose")
            self.reset_game()

    def reset_game(self):
        self.entry.pack_forget()
        self.submit_button.pack_forget()

    def save_result(self, result):
        name = self.name_entry.get().strip()
        date, time = get_indian_datetime()
        with open(CSV_FILE, mode="a", newline="") as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(["Name", "Date", "Time", "Difficulty", "Secret Number", "Attempts", "Score", "Result"])
            writer.writerow([name, date, time, self.diff_var.get(), self.secret_number, self.attempts, self.score, result])

    def show_leaderboard(self):
        if not os.path.exists(CSV_FILE):
            messagebox.showinfo("Leaderboard", "No game data found.")
            return

        leaderboard = tk.Toplevel(self.root)
        leaderboard.title("Leaderboard")
        tree = ttk.Treeview(leaderboard, columns=("Name", "Score", "Date", "Time", "Result"), show="headings")
        for col in ("Name", "Score", "Date", "Time", "Result"):
            tree.heading(col, text=col)
            tree.column(col, width=100)
        tree.pack(fill="both", expand=True)

        with open(CSV_FILE, newline="") as file:
            reader = csv.DictReader(file)
            sorted_data = sorted(reader, key=lambda x: int(x["Score"]), reverse=True)
            for row in sorted_data[:10]:
                tree.insert("", "end", values=(row["Name"], row["Score"], row["Date"], row["Time"], row["Result"]))

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
