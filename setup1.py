#importing required libraries
from tkinter import *
from tkinter import ttk, messagebox
import tkinter.font as tkFont
import quizQ

# Global variables
current_question = 0
score = 0
choice_btns1 = []

# Function to display the current question and choices
def show_question1():
    # Get the current question from the quiz_data1 list
    question = quizQ.quiz_data1[current_question1]
    qs_label1.config(text=question["question"])

    # Display the choices on the buttons
    choices = question["choices"]
    for i in range(3):
        choice_btns1[i].config(text=choices[i], state="normal") # Reset button state

    # Clear the feedback label and disable the next button
    feedback_label1.config(text="")
    next_btn1.config(state="disabled")

def check_answer1(choice):
      global current_question, score
  # Get the current question from the quiz_data1 list
      question = quizQ.quiz_data1[current_question]
      selected_choice = choice_btns1[choice].cget("text")

      # Check if the selected choice matches the correct answer
      if selected_choice == question["answer"]:
          global score
          # Update the score and display it
          score += 1
          score_label.config(text="Score: {}/{}".format(score, len(quizQ.quiz_data1)))
          feedback_label1.config(text="Correct!", foreground="green")
      else:
          feedback_label1.config(text="Incorrect!", foreground="red")

      # Disable all choice buttons and enable the next button
      for button in choice_btns1:
          button.config(state="disabled")
      next_btn1.config(state="normal")

  # Function to move to the next question
def next_question1():
      global current_question

  
      current_question1 +=1

      if current_question1 < len(quizQ.quiz_data1):
          # If there are more questions, show the next question
          show_question1()
      else:
          # If all questions have been answered, display the final score and end the quiz
          messagebox.showinfo("Quiz Completed",
                              "Quiz Completed! Final score: {}/{}".format(score, len(quizQ.quiz_data1)))

