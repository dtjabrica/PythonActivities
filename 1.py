import tkinter as tk
from tkinter import messagebox, simpledialog
import random

class MathGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Game")
        self.root.configure(bg='lightblue')
        self.root.geometry('500x400')
        self.score = 50
        self.create_widgets()

    def generate_question(self):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        return num1, num2, num1 * num2

    def check_answer(self, answer, correct_answer, score_label):
        if answer is not None and str(answer).isdigit():
            answer = int(answer)
            if answer == correct_answer:
                messagebox.showinfo("Correct", "You are correct!")
                self.score += 5
            else:
                messagebox.showwarning("Incorrect", "Incorrect. Please try again.")
                self.score -= 5
            score_label.config(text=f"Score: {self.score}")
        else:
            messagebox.showwarning("Invalid Answer", "Please enter a valid numeric answer.")

    def play_game(self):
        if self.score > 0:
            num1, num2, correct_answer = self.generate_question()
            question_text = f"How much is {num1} times {num2}"

            dialog_window = tk.Toplevel(self.root)
            dialog_window.title("Math Game")
            dialog_window.geometry('500x400')
            dialog_window.configure(bg='lightblue')

            # Display the score in the dialog window
            score_label = tk.Label(dialog_window, text=f"Score: {self.score}", font=("Helvetica", 12))
            score_label.pack(pady=10)

            question_label = tk.Label(dialog_window, text=question_text, font=("Helvetica", 12))
            question_label.pack(pady=10)

            answer_entry = tk.Entry(dialog_window, font=("Helvetica", 12))
            answer_entry.pack(pady=10)

            answer = None

            def get_answer():
                nonlocal answer
                answer = answer_entry.get()
                self.check_answer(answer, correct_answer, score_label)
                dialog_window.destroy()

            # Enter Answer button to submit the answer
            enter_answer_button = tk.Button(dialog_window, text="Enter Answer", font=("Comic Sans MS", 12),
                                            command=get_answer)
            enter_answer_button.pack(pady=20)

            # Quit button to end the game
            quit_button = tk.Button(dialog_window, text="Quit", font=("Comic Sans MS", 12), command=dialog_window.destroy)
            quit_button.pack(pady=20)

            answer_entry.focus_set()
            dialog_window.wait_window(dialog_window)

            if answer is not None:
                self.play_game()
            else:
                self.end_game()

        else:
            messagebox.showinfo("Game Over", "Game over! Your final score is: {}".format(self.score))
            self.root.destroy()

    def end_game(self):
        user_confirm = messagebox.askyesno("Confirmation", "Are you sure you want to quit the game?")
        if user_confirm:
            messagebox.showinfo("Game Over", "Game over! Your final score is: {}".format(self.score))
            self.root.destroy()

    def create_widgets(self):
        # Create an empty Label for spacing
        space_label = tk.Label(self.root, text="", pady=10)
        space_label.pack()

        # Create a Label widget for the title
        title_label = tk.Label(self.root, text="MultiplyMania", font=("Comic Sans MS", 24), pady=10)
        title_label.pack()

        # Create a Button widget for the "Start Game" button
        start_button = tk.Button(self.root, text="Start Game", font=("Comic Sans MS", 15), command=self.play_game, width=10, height=2)
        start_button.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = MathGameGUI(root)
    root.mainloop()
