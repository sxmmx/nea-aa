#importing required libraries
from tkinter import *
from tkinter import ttk
from tkinter import ttk, messagebox
import tkinter.font as tkFont
import quizQ
import sqlite3


#instance of root
root = Tk()


#global variable = current_question
current_question = 0
current_question1 = 0

global qs_label
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




# Function to display the current question and choices
def show_question2():
    # Get the current question from the quiz_data list
    question = quizQ.quiz_data1[current_question]
    qs_label1.config(text=question["question"])

    # Display the choices on the buttons
    choices = question["choices"]
    for i in range(3):
        choice_btns[i].config(text=choices[i], state="normal") # Reset button state

    # Clear the feedback label and disable the next button
    feedback_label.config(text="")
    next_btn.config(state="disabled")

def check_answer2(choice):
  # Get the current question from the quiz_data1 list
      question = quizQ.quiz_data1[current_question]
      selected_choice = choice_btns[choice].cget("text")

      # Check if the selected choice matches the correct answer
      if selected_choice == question["answer"]:
          # Update the score and display it
          global score
          score += 1
          score_label.config(text="Score: {}/{}".format(score, len(quizQ.quiz_data1)))
          feedback_label.config(text="Correct!", foreground="green")
      else:
          feedback_label.config(text="Incorrect!", foreground="red")

      # Disable all choice buttons and enable the next button
      for button in choice_btns:
          button.config(state="disabled")
          next_btn.config(state="normal")

  # Function to move to the next question
def next_question2():
      global current_question1
      current_question1 +=1

      if current_question1 < len(quizQ.quiz_data1):
          # If there are more questions, show the next question
          show_question2()
      else:
          # If all questions have been answered, display the final score and end the quiz
          messagebox.showinfo("Quiz Completed",
                              "Quiz Completed! Final score: {}/{}".format(score, len(quizQ.quiz_data1)))


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

# Create a function to execute SQL queries
def execute_query(query, params=()):
    try:
        c.execute(query, params)
        conn.commit()
        return True
    except Exception as e:
        conn.rollback()
        print("Error occurred!", e)
        return False


#conneting to database
conn = sqlite3.connect('Users.db')
c = conn.cursor()

#creating database
c.execute('''CREATE TABLE IF NOT EXISTS Users(
  UserID INTEGER PRIMARY KEY,
  User_name TEXT,
  User_password TEXT)''')

conn.commit()

#creating function checks if sign up detials are already in database
#if not, it will be inserted
def signup(User_name, User_password):
    try:
        conn = sqlite3.connect('Users.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM Users WHERE User_name = "%s"''' %(User_name,))
        if cursor.fetchone():
            messagebox.showerror("Error", "Username already exists, Choose a different username.")
            return
        cursor.execute("INSERT INTO Users (User_name, User_password) VALUES (?, ?)", (User_name, User_password))
        conn.commit()

          # Create a file for the user
        with open(f"{User_name}_file.txt", "w") as file:
            file.write("Welcome to the platform!")
        #telling user whether it was successful or not
        messagebox.showinfo("Success", "Signup successful!")
    except Exception as e:
        conn.rollback()
        print("Error occurred!", e)
    finally:
        conn.close()

#taking user details to pass throuth the logintodb function
#to see if details are in database. will return results on whether it was successful
def login(User_name, User_password):
        success = logintodb(User_name, User_password)
        if success:
            messagebox.showinfo("Success", "Login successful!")
        else:
            messagebox.showerror("Error", "Invalid username/password, try again.")

#function that checks if user details exist in database
def logintodb(User_name, User_password):
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Users WHERE User_name = ? AND User_password = ?", (User_name, User_password))
            result = cursor.fetchone()
            return result is not None
        except Exception as e:
            print("Error occurred!", e)
            return False



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
  sub_btn = Button(newWindow,text = 'Submit', font = ("century gothic" ,20,'normal'), bg='#5e32a8', command = submit1).grid(row=9, column=0)

#will take the details print in console, then send details 
#tologin function
def submit1():
   User_name = name_var.get()
   User_password = passw_var.get()
   print("The name is : " + User_name)
   print("The password is : " + User_password)
   login(User_name, User_password)
   name_var.set("")
   passw_var.set("")
  
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
  sub_btn = Button(newWindow,text = 'Submit', font = ("century gothic" ,20,'normal'), bg='#02ddf5', command=submit).grid(row=15,column=0)

#will print detail in console, then send details
#to signup function
def submit():
   User_name = name_var.get()
   User_password = passw_var.get()
   print("The name is : " + User_name)
   print("The password is : " + User_password)
   signup(User_name, User_password)
   name_var.set("")
   passw_var.set("")


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
  qs_label.grid(row=1, column=1)#placing it on screen
  
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
    state="disabled"# is abled when question is answered
  )
  
  next_btn.grid(row=10,column=1)

    # Initialize the current question index
  current_question = 0
  show_question()


  

#--translation quiz
def openNewWindow4():
  newWindow = Toplevel(root)
  newWindow.title("translation quiz")
  newWindow.geometry("800x600")
  newWindow['background']= '#f5b55d'
  gobackButton = Button(newWindow,text="Go Back", font=("Century Gothic", 20), bg='#f5b55d', command=newWindow.destroy).grid(row=0,column=0,sticky='nsew')
  titlelabel = Label(newWindow, text="Question Time!", font=("Century Gothic", 28), bg='#f5b55d').grid(row=0,column=1)

  #question label
  qs_label1 = ttk.Label(
    newWindow,
    anchor="center",
    wraplength=500,
    background= '#f5b55d'
  )
  qs_label1.grid(row=1, column=1)

  
  # choice buttons
  choice_btns = [] 
  for i in range(3):
    button = ttk.Button(
      newWindow, 
      command=lambda i=i: check_answer2(i)
    )
    button.grid(row=3, column=i)
    
    choice_btns.append(button)
    
    
  # feedback label
  feedback_label = ttk.Label(
    newWindow,
    anchor="center",
    wraplength=500,
    background= '#f5b55d'
  )
  feedback_label.grid(row=6,column=1)

  # initialising score
  score=0
  # score label
  score_label = Label(
    newWindow,
    text="Score: 0/{}".format(len(quizQ.quiz_data1)),
    anchor="center",
    background= '#f5b55d'
  )
  score_label.grid(row=8,column=1)

  # Create the next button
  next_btn = ttk.Button(
    newWindow,
    text="Next",
    command=next_question2,
    state="disabled"
  )

  next_btn.grid(row=10,column=1)
 
  # Initialize the current question index
  current_question1 = 0
  show_question2()


  


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

#to make summary page
def openNewWindow6():
  newWindow = Toplevel(root)
  newWindow.title("summary")
  newWindow.geometry("1500x1500")
  newWindow['background']= '#4287f5'
  gobackButton = Button(newWindow,text="Go Back", font=("Century Gothic", 20), bg='#4287f5', command=newWindow.destroy).grid(row=0,column=0,sticky='nsew')
  myLabel5 = Label(newWindow, text="What is protein synthesis?",font=("Century Gothic", 28), bg='#4287f5').grid(row=0,column=2)
  myLabel6 = Label(newWindow, text="Summary",font=("Century Gothic", 25), bg='#4287f5').grid(row=1,column=2)
#adding text
  summary_text = """Protein synthesis is the creation of protein using DNA. This is done by RNA Polymerase (an enzyme) breaking hydrogen bonds between the 
  complementary bases( A, T, C, and G), 
  causing the DNA to break into the sense strand and antisense strand 
  (this references the direction the strand on nucleotides are facing). 
  The antisense strand will be used as a template strand and free nucleotides (basic structural unit of nucleic acids like DNA) 
  will line up against complementary base pairs and join together
  by phosphodiester bonds(between nucleotides-), catalysed by RNA polymerase. 
  This forms messenger RNA, known as mRNA. This moves out of the nuclear pore into the cytoplasm, thus ending transcription.
When the mRNA is attached to a ribosome in the cytoplasm, translation starts. Transfer RNA (tRNA) is a molecule that binds amino acids
(the molecule that makes protein when combined) together based on anticodons (three complementary bases to mRNA bases ).
Anticodons on tRNA bind to codons on mRNA and are held together by hydrogen bonds. Amino acids in the cytoplasm attach to 
tRNA and ribosomes attach to amino acids on two tRNA molecules using peptide bonds before tRNA detaches from amino acids. 
This process repeats until a stop codon is reached. The amino acids can fold into a secondary or tertiary structure, with the 
primary structure is the amino acids not changing shape after being synthesised. Secondary and tertiary structures are proteins
in complex 3D form. This is so the proteins can carry out specific functions, like releasing hormones.
"""
  #seetings for text and putting it on screen
  summary_label = Label(newWindow, text=summary_text, font=("Century Gothic", 10), bg='#4287f5', wraplength=600)
  summary_label.grid(row=2, column=2)
  myLabel7 = Label(newWindow, text="Keywords",font=("Century Gothic", 25), bg='#4287f5').grid(row=3,column=2)
  #repeat
  keywords_text = """
  Amino acid: The monomers containing an amino group (NH2 ), a carboxyl group (COOH) and a variable R group that make up proteins.
  Polypeptide: Molecules formed by the condensation of many amino acids.  
  Antisense strand: DNA strand facing 3’ to 5’ direction, and is used as a template for mRNA.
  Sense strand: DNA strand facing the 5’ to 3’ direction.
  Secondary structure: The local interactions of the amino acids in the polypeptide chain. 
  Tertiary structure: The way that the whole protein folds to make a three dimensional structure.
  """
  keywords_label = Label(newWindow, text=keywords_text, font=("Century Gothic", 10), bg='#4287f5', wraplength=600)
  keywords_label.grid(row=4, column=2)


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

summaryButton = Button(root,text="Summary",font=("Century Gothic", 20),bg='#faf8bb',command=openNewWindow6).grid(row=15,column=5)

root.mainloop()
