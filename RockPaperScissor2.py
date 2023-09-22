import tkinter as tk
import random

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or (player_choice == "Paper" and computer_choice == "Rock")
        or (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        player_score_var.set(player_score_var.get() + 1)
        return "You win!"
    else:
        computer_score_var.set(computer_score_var.get() + 1)
        return "Computer wins!"

# Function to handle player's choice
def player_choice(choice):
    computer_choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(computer_choices)
    
    result = determine_winner(choice, computer_choice)
    
    player_label.config(text=f"Player: {choice}")
    computer_label.config(text=f"Computer: {computer_choice}")
    result_label.config(text=result)

# Function to reset the game
def reset_game():
    player_label.config(text="Player: ")
    computer_label.config(text="Computer: ")
    result_label.config(text="")
    player_score_var.set(0)
    computer_score_var.set(0)

# Create the main window
window = tk.Tk()
window.title("Rock, Paper, Scissors Game")
window.geometry("500x500")
window.configure(bg="#EEEEEE")

# Create labels with a cohesive design
title_label = tk.Label(window, text="Rock, Paper, Scissors", font=("Helvetica", 24), bg="#EEEEEE")
title_label.pack(pady=20)

player_label = tk.Label(window, text="Player: ", font=("Helvetica", 14), bg="#EEEEEE")
player_label.pack()

computer_label = tk.Label(window, text="Computer: ", font=("Helvetica", 14), bg="#EEEEEE")
computer_label.pack()

result_label = tk.Label(window, text="", font=("Helvetica", 18), bg="#EEEEEE", fg="#333333")
result_label.pack(pady=30)

# Create labels for scorekeeping
player_score_var = tk.IntVar()
computer_score_var = tk.IntVar()

player_score_label = tk.Label(window, text="Player Score:", font=("Helvetica", 14), bg="#EEEEEE")
player_score_label.pack()
player_score_display = tk.Label(window, textvariable=player_score_var, font=("Helvetica", 14), bg="#EEEEEE")
player_score_display.pack()

computer_score_label = tk.Label(window, text="Computer Score:", font=("Helvetica", 14), bg="#EEEEEE")
computer_score_label.pack()
computer_score_display = tk.Label(window, textvariable=computer_score_var, font=("Helvetica", 14), bg="#EEEEEE")
computer_score_display.pack()

# Create buttons for player choices with proper alignment
choice_frame = tk.Frame(window, bg="#EEEEEE")
choice_frame.pack()

rock_button = tk.Button(choice_frame, text="Rock", font=("Helvetica", 14), bg="#3066A3", fg="#EEEEEE", width=10, height=2, command=lambda: player_choice("Rock"))
paper_button = tk.Button(choice_frame, text="Paper", font=("Helvetica", 14), bg="#3066A3", fg="#EEEEEE", width=10, height=2, command=lambda: player_choice("Paper"))
scissors_button = tk.Button(choice_frame, text="Scissors", font=("Helvetica", 14), bg="#3066A3", fg="#EEEEEE", width=10, height=2, command=lambda: player_choice("Scissors"))

rock_button.pack(side=tk.LEFT, padx=10)
paper_button.pack(side=tk.LEFT, padx=10)
scissors_button.pack(side=tk.LEFT, padx=10)

# Create a button to reset the game
reset_button = tk.Button(window, text="Reset", font=("Helvetica", 14), bg="#5EA9EA", fg="#EEEEEE", width=10, height=2, command=reset_game)
reset_button.pack(pady=20)

# Start the GUI main loop
window.mainloop()
