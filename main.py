#importing required libraries
from tkinter import *
from tkinter import ttk, messagebox
import tkinter.font as tkFont
import quizQ
import sqlite3
#instance of window and root
root = Tk()
win=Tk()

#global variable = current_question
current_question = 0
current_question1 = 0
#score initialise
score = 0

# Function to display the current question and choices
def show_question():
    # Get the current question from the quiz_data list
    question = quizQ.quiz_data[current_question]
    qs_label.config(text=question["question"])

    # Display the choices on the buttons
    choices = question["choices"]
    for i in range(3):
        choice_btns[i].config(text=choices[i], state="normal") # Reset button state

    # Clear the feedback label and disable the next button
    feedback_label.config(text="")
    next_btn.config(state="disabled")

def check_answer(choice):
  # Get the current question from the quiz_data list
      question = quizQ.quiz_data[current_question]
      selected_choice = choice_btns[choice].cget("text")

      # Check if the selected choice matches the correct answer
      if selected_choice == question["answer"]:
          # Update the score and display it
          global score
          score += 1
          score_label.config(text="Score: {}/{}".format(score, len(quizQ.quiz_data)))
          feedback_label.config(text="Correct!", foreground="green")
      else:
          feedback_label.config(text="Incorrect!", foreground="red")

      # Disable all choice buttons and enable the next button
      for button in choice_btns:
          button.config(state="disabled")
          next_btn.config(state="normal")

  # Function to move to the next question
def next_question():
      global current_question
      current_question +=1

      if current_question < len(quizQ.quiz_data):
          # If there are more questions, show the next question
          show_question()
      else:
          # If all questions have been answered, display the final score and end the quiz
          messagebox.showinfo("Quiz Completed",
                              "Quiz Completed! Final score: {}/{}".format(score, len(quizQ.quiz_data)))
          

  
#size of window
root.geometry("800x600")

#setting bg colour
root['background']= '#faf8bb'

#login/signup variables
name_var = StringVar()
passw_var = StringVar()

#connecting to a database
conn = sqlite3.connect('Users.db')
#making a cursor
c = conn.cursor()


# defining a function that will
# get the name and password and 
# print them on the screen
def submit():
  name=name_var.get()
  password=passw_var.get()

  print("The name is : " + name)
  print("The password is : " + password)

  loginintodb(name, password)

  name_var.set("")
  passw_var.set("")

def loginintodb(name, password):

  if password:
    db = sqlite3.connect('Users.db') 

    cursor = db.cursor()

      # A Table in the database
    savequery = "SELECT * FROM Users WHERE User_name = ? AND User_password = ?"
    
    try:
        cursor.execute(savequery, (name, password))
        myresult = cursor.fetchall()
       # Printing the result of the query
        for x in myresult:
           print(x)
        print("Query Executed successfully")
    except Exception as e:
       db.rollback()
       print("Error occurred: ", e)
    db.close()


#--login page
#function to make a new window when button is clicked and features of the page 
#(clr, btn, etc)
def openNewWindow1():
  newWindow = Toplevel(root)
  newWindow.title("login")
  newWindow.geometry("800x600")
  newWindow['background']= '#5e32a8'
  gobackButton = Button(newWindow,text="Go Back", font=("Century Gothic", 20), bg='#5e32a8',command=newWindow.destroy).grid(row=0,column=0)
  myLabel2 = Label(newWindow, text="Login", font=("century gothic", 28), bg='#5e32a8').grid(row=0,column=4)
  # creating a label for username
  name_label = Label(newWindow, text = 'Username', font=("Century Gothic",20, 'bold'), bg='#5e32a8').grid(row=6,column=2)

  # creating a entry for username
  name_entry = Entry(newWindow,textvariable = name_var, font=("century gothic" ,20,'normal')).grid(row=6,column=6)

  # creating a label for password
  passw_label = Label(newWindow, text = 'Password', font = ("century gothic",20,'bold'), bg='#5e32a8').grid(row=8,column=2)

  # creating a entry for password
  passw_entry = Entry(newWindow, textvariable = passw_var, font = ("century gothic",20,'normal'), show = '*').grid(row=8,column=6)

  # creating a submit button 
  sub_btn = Button(newWindow,text = 'Submit', font = ("century gothic" ,20,'normal'), bg='#5e32a8', command = submit).grid(row=9, column=0)
  
#--signup page
#function to make sign up window when button is clicked and features of the page 
#(clr, btn, etc)
def openNewWindow2():
  newWindow = Toplevel(root)
  newWindow.title("signup")
  newWindow.geometry("800x600")
  newWindow['background']= '#02ddf5'
  gobackButton = Button(newWindow,text="Go Back", font=("Century Gothic", 20), bg='#02ddf5', command=newWindow.destroy).grid(row=0,column=0)
  myLabel3 = Label(newWindow, text="Sign Up", font=("century gothic", 28), bg='#02ddf5').grid(row=0,column=4)
  # creating a label for username
  name_label = Label(newWindow, text = 'Username', font=("Century Gothic",20, 'bold'), bg='#02ddf5').grid(row=6,column=2)

  # creating a entry for username
  name_entry = Entry(newWindow,textvariable = name_var, font=("century gothic" ,20,'normal')).grid(row=6,column=6)

  # creating a label for password
  passw_label = Label(newWindow, text = 'Password', font = ("century gothic",20,'bold'), bg='#02ddf5').grid(row=8,column=2)

  # creating a entry for password
  passw_entry = Entry(newWindow, textvariable = passw_var, font = ("century gothic",20,'normal'), show = '*').grid(row=8,column=6)

  # creating a submit button 
  sub_btn = Button(newWindow,text = 'Submit', font = ("century gothic" ,20,'normal'), bg='#02ddf5', command=
submit).grid(row=15,column=0)

#--trancription quiz
def openNewWindow3():
  global qs_label, score_label, feedback_label, choice_btns, next_btn #defining global variables
  newWindow = Toplevel(root)
  newWindow.title("tcquiz")
  newWindow.geometry("800x600")
  newWindow['background']= '#42f56c'
  gobackButton = Button(newWindow,text="Go Back", font=("Century Gothic", 20), bg='#42f56c', command=newWindow.destroy).grid(row=0,column=0,sticky='nsew')
  titlelabel = Label(newWindow, text="Question Time!", font=("Century Gothic", 28), bg='#42f56c').grid(row=0,column=1)
  #question label
  qs_label = ttk.Label(
      newWindow,
      anchor="center",
      wraplength=500,
      background= '#42f56c'
    )
  qs_label.grid(row=1, column=1)
  
#choice buttons
  choice_btns = []
  for i in range(3):
    button = ttk.Button(
      newWindow,
      command=lambda i=i: check_answer(i)
    )
    button.grid(row=3, column=i)
   
    choice_btns.append(button)
#feedback label
  feedback_label = ttk.Label(
    newWindow,
    anchor="center",
    wraplength=500,
    background= '#42f56c'
  )
  feedback_label.grid(row=6,column=1)

#initialising score
  score=0
#score label
  score_label = Label(
    newWindow,
    text="Score: 0/{}".format(len(quizQ.quiz_data)),
    anchor="center",
    background= '#42f56c'
  )
  score_label.grid(row=8,column=1)

  
    # Create the next button
  next_btn = ttk.Button(
    newWindow,
    text="Next",
    command=next_question,
    state="disabled"
  )
  
  next_btn.grid(row=10,column=1)

    # Initialize the current question index
  current_question = 0
  show_question()


#--translation quiz
def openNewWindow4():
  global qs_label, score_label, feedback_label, choice_btns, next_btn #defining global variables
  newWindow = Toplevel(root)
  newWindow.title("signup")
  newWindow.geometry("800x600")
  newWindow['background']= '#f5b55d'
  gobackButton = Button(newWindow,text="Go Back", font=("Century Gothic", 20), bg='#f5b55d', command=newWindow.destroy).grid(row=0,column=0,sticky='nsew')
  titlelabel = Label(newWindow, text="Question Time!", font=("Century Gothic", 28), bg='#f5b55d').grid(row=0,column=1)
  qs_label1 = ttk.Label(
     newWindow,
     anchor="center",
     wraplength=500,
     background= '#f5b55d'
   )
  qs_label1.grid(row=1, column=1)

  #choice buttons
  choice_btns1 = []
  for i in range(3):
    button = ttk.Button(
      newWindow,
      command=lambda i=i: check_answer(i)
    )
    button.grid(row=3, column=i)

    choice_btns1.append(button)
  #feedback label
  feedback_label1 = ttk.Label(
    newWindow,
    anchor="center",
    wraplength=500,
    background= '#f5b55d'
  )
  feedback_label1.grid(row=6,column=1)

  #initialising score
  score=0
  #score label
  score_label1 = Label(
    newWindow,
    text="Score: 0/{}".format(len(quizQ.quiz_data1)),
    anchor="center",
    background= '#f5b55d'
  )
  score_label1.grid(row=8,column=1)


# Create the next button
  next_btn1 = ttk.Button(
    newWindow,
    text="Next",
    command=next_question,
    state="disabled"
  )

  next_btn1.grid(row=10,column=1)

  # Initialize the current question index
current_question1 = 0
show_question1()





#--start quiz
def openNewWindow5():
  newWindow = Toplevel(root)
  newWindow.title("signup")
  newWindow.geometry("800x600")
  newWindow['background']= '#faa5e5'
  gobackButton = Button(newWindow,text="Go Back", font=("Century Gothic", 20), bg='#faa5e5', command=newWindow.destroy).grid(row=0,column=0,sticky='nsew')
  myLabel4 = Label(newWindow, text="Where do you want to start?",font=("Century Gothic", 28), bg='#faa5e5').grid(row=0,column=2)
#sticky function centres button
  tcButton = Button(newWindow,text="Transcription",font=("Century Gothic", 20), bg='#faa5e5',command=openNewWindow3).grid(row=3,column=2)
  tlButton = Button(newWindow,text="Translation",font=("Century Gothic", 20), bg='#faa5e5',command=openNewWindow4).grid(row=4,column=2)


#--main page(root)

#creating label to put on screen,(font + size)
#.putting labels on screen and with position
myLabel1 = Label(root, text="Protein Synthesis Quiz", font=("Century Gothic", 28),bg='#faf8bb').grid(row=0,column=5)

#creating buttons to put on screen,(font + size),colour
#,command to go to a diff page
#.putting labels on screen with position
loginButton = Button(root,text="Login",font=("Century Gothic", 20),bg='#faf8bb',command=openNewWindow1).grid(row=0,column=80)

SignUpButton = Button(root,text="Sign Up",font=("Century Gothic", 20),bg='#faf8bb',command=openNewWindow2).grid(row=5,column=80)

startquizButton = Button(root,text="START",font=("Century Gothic", 20),bg='#faf8bb',command=openNewWindow5).grid(row=10,column=5)

  

root.mainloop()
