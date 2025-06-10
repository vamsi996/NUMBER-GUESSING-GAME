# NUMBER-GUESSING-GAME

# DESCRIPTION:

This project is a fun and interactive Number Guessing Game with a GUI, built using Python and Tkinter. The user selects a difficulty level, guesses a randomly generated number, and earns points based on the number of attempts. The game also tracks results in a CSV file and displays a leaderboard for top scores.

**Setup and Imports:**

The program begins by importing the necessary Python libraries: tkinter for the GUI (Graphical User Interface). messagebox and ttk from tkinter for popups and table-style widgets. random to generate a secret number. csv to save game results. datetime and timedelta to get Indian date and time. os to check file existence (used for leaderboard logic).

**Defining Game Settings:**

A dictionary is created to store difficulty levels: Easy: Guess between 1 to 10 in 5 attempts. Medium: Guess between 1 to 50 in 7 attempts. Hard: Guess between 1 to 100 in 10 attempts. Each level changes the guessing range and maximum attempts.

**Indian Date and Time:**

A function is defined to convert the current time to Indian Standard Time (UTC+5:30), and returns it in: DD-MM-YYYY date format HH:MM:SS time format This will be used to timestamp the CSV records.

**Game Initialization:**

When the GUI opens: The window is titled appropriately. All important variables like secret number, attempts, score, etc., are initialized. GUI widgets (labels, buttons, input boxes) are created using Tkinter.

**Player Input:**

The player is prompted to: Enter their name (mandatory to start the game). Choose a difficulty level from a dropdown menu. Click Start Game to begin. If no name is entered, a warning popup appears.

**Game Logic (Guessing):**

Once the game starts: A secret number is generated based on difficulty. The player is asked to guess the number. Each guess is checked: If it's too low, a “Too low” message is shown. If it's too high, a “Too high” message is shown. If correct, a "Congratulations!" popup appears with the score. The score starts at 100 and is reduced by 10 for every incorrect attempt.

**Game Over Conditions:**

The player wins if they guess the number correctly before using all attempts. If the player fails within the given attempts: A message shows the correct number. Game ends and resets.

**Saving Results to CSV:**

After each game ends (win or lose): The player's data is saved in a CSV file with columns: Name, Date, Time, Difficulty, Secret Number, Attempts, Score, Result (Win/Lose) If the file is new, headers are added first.

**Leaderboard Feature:**

A "Show Leaderboard" button opens a new window showing the top 10 scores. The leaderboard: Loads all previous results from the CSV. Sorts them by score in descending order. Displays name, score, date, time, and result in a table. If no data exists, it shows a popup saying “No game data found.”

# OUTPUT:

