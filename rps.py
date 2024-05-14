import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        
        self.user_score = 0
        self.computer_score = 0
        
        self.create_widgets()
        
    def create_widgets(self):
        self.label = tk.Label(self.root, text="Choose Rock, Paper, or Scissors:")
        self.label.pack(pady=10)
        
        self.rock_button = tk.Button(self.root, text="Rock", command=lambda: self.play_game("rock"))
        self.rock_button.pack(pady=5)
        
        self.paper_button = tk.Button(self.root, text="Paper", command=lambda: self.play_game("paper"))
        self.paper_button.pack(pady=5)
        
        self.scissors_button = tk.Button(self.root, text="Scissors", command=lambda: self.play_game("scissors"))
        self.scissors_button.pack(pady=5)
        
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=10)
        
        self.score_label = tk.Label(self.root, text="Score: You - 0, Computer - 0", font=("Helvetica", 12))
        self.score_label.pack(pady=10)
        
        #self.continue_button = tk.Button(self.root, text="Continue", command=self.continue_game)
        #self.continue_button.pack(pady=5)
        
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_game)
        self.stop_button.pack(pady=5)
        
    def get_computer_choice(self):
        choices = ["rock", "paper", "scissors"]
        return random.choice(choices)
        
    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "tie"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            return "user"
        else:
            return "computer"
        
    def play_game(self, user_choice):
        computer_choice = self.get_computer_choice()
        winner = self.determine_winner(user_choice, computer_choice)
        
        result_text = f"You chose: {user_choice}\nComputer chose: {computer_choice}\n"
        if winner == "tie":
            result_text += "It's a tie!"
        elif winner == "user":
            result_text += "You win!"
            self.user_score += 1
        else:
            result_text += "You lose!"
            self.computer_score += 1
        
        self.result_label.config(text=result_text)
        self.score_label.config(text=f"Score: You - {self.user_score}, Computer - {self.computer_score}")
        
    def continue_game(self):
        self.label.config(text="Choose Rock, Paper, or Scissors:")
        self.result_label.config(text="")
        
    def stop_game(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
