import string, random, time, sys
from PokemonNames import words
from tkinter import *


#work on Guess

canvas = Tk()
canvas.title("Hangman: Pokemon Edition")
canvas.configure()
canvas.geometry("450x330")
canvas.resizable(width = False, height = False)
chat_frame1 = Frame(canvas, bg= "#22AC22", width = 450, height = 55)
chat_frame1.place(x = 0, y = 0)
chat_frame2 = Frame(canvas, bg= "#7CFC00", width = 450, height = 55)
chat_frame2.place(x = 0, y = 55)
chat_frame3 = Frame(canvas, bg= "light green", width = 450, height = 35)
chat_frame3.place(x = 0, y = 110)
entry_frame = Frame(canvas, bg= "#7AD75D", width = 450, height = 40)
entry_frame.place(x = 0, y = 145)
button_menu = Frame(canvas, bg = "light blue", width = 450, height = 45)
button_menu.place(x = 0, y = 180)
keyboard_frame = Frame(canvas, width = 450, height = 170, bg = "blue")
keyboard_frame.place(relwidth = 1, relheight = 1, x = 0, rely = .67)

tch = string.ascii_uppercase
blarp = list(tch)

hello = 'Hello! Would you like to play a word guessing game?\nYou can guess a random pokemon name!'
lives = 7
meh = ("Sans Serif", 12, "bold")

Lives = Label(button_menu, text = f'Lives = {lives}', bg = "light blue", font = meh)
Lives.place(rely = .2, relx = .05)

guess2 = ''
guess3= ''
guess = StringVar()
Guess = Entry(entry_frame, textvariable = guess, justify = 'center', font = meh)
Guess.place(rely = .5, relx = .5, anchor= "center")
name= ' '
nameL=[]
lList=[]
score = 0
try1= 'Press any letter to guess\nor type a letter and hit submit'
Hello = Label(chat_frame1, text = hello,  wraplength= 500, bg = '#22AC22', font = meh)
Hello.place(relx = .5, rely = .5, anchor = 'center')
Hello2 = Label(chat_frame2, text = try1, wraplength= 500, font = meh, bg= "#7CFC00")
Hello2.place(relx = .5, rely = .5, anchor = 'center')
Hello3 = Label(chat_frame3, text = lList, font = meh, bg= "light green")
Hello3.place(relx = .5, rely = .5, anchor = 'center')



def Name():
    global name, nameL, lList
    name = random.choice(words).upper()
    nameL = set(name)
    lList = [letter if letter in guess2 else '*' for letter in name]
    lives = 7



def Submit(c):
    global guess2, guess3, lives, name, nameL, lList,score
    if lives >0:
        c = c.upper()
        if c in guess2:
            Hello.config(text= f'You have already guessed {c}.\n{guess2}')
        if c not in guess2:
            if len(c) >=2:
                guess3 = c
            if len(c) == 1:
                guess2 += c
            Hello.config(text = f'You have guessed\n{guess2}')
            if c not in name:
                lives -= 1
        if set(lList) == nameL:
            Congrats()
        if c.upper() == name.upper():
            lList = set(c.upper())
            Hello3.config(text = c.upper())
            Congrats()
    if lives <=0:
        Hello.config(text = f'You have run out of lives.\nThe Pokemon name was {name}.')
        Hello2.config(text='Press Continue to play again or Quit to exit.\n')
    lList = [letter if letter in guess2 else '*' for letter in name]
    Hello2.config(text = f'Guess the Pokemon Name\n{guess3}', wraplength=0)
    Hello3.config(text = lList)
    Lives.config(text = f'Lives: {lives}')
    if set(lList) == nameL:
        Congrats()
    if c.upper() == name.upper():
        lList = set(c.upper())
        Hello3.config(text = c.upper())
        Congrats()


def Get():
    c = Guess.get()
    Submit(c)
    Guess.delete(0, END)

def Get2(event):
    c = Guess.get()
    Submit(c)
    Guess.delete(0, END)


def Cont():
    global name, nameL, lList, lives, guess2, guess3
    if '*' in lList and lives >0:
        Hello.config(text = 'Please finish guessing the current Pokemon.')
        Hello2.config(text = 'Or press Quit to exit')
    else:
        guess2 = ''
        guess3 = ''
        name = ''
        nameL.clear()
        lList.clear()
        lives = 7
        Name()
        Hello.config(text = hello)
        Hello2.config(text = try1)
        Hello3.config(text = ' ')
        Lives.config(text = f'Lives: {lives}')


def Congrats():
    Hello.config(text = f'Congratulations!\nYou guessed {name} with {lives} lives left.')
    Hello2.config(text ='Press Continue to play again or Quit to exit.\n')



i = 0
for a in range(3):
    for b in range(9):
        try:
            Button(keyboard_frame, text = blarp[i], command=lambda c=(blarp[i]): Submit(c), width = 4).grid(padx = 5, pady = 5, column=b+5, row = a+10)
            i+=1
        except:
            pass

Button(button_menu, text = "Quit", font = meh, anchor = 'center', command = lambda: quit(), width = 5, bg="#EE4B2B").place(relx = .75, rely = .1)
Button(button_menu, text = "Continue", font = meh, anchor = 'center', command = lambda: Cont(), width = 9, bg = "teal").place(relx = .49, rely = .1)
Button(button_menu, text = "Submit", bg = "green", font = meh, justify = 'center', command = lambda: Get()).place(relx = .3, rely = .1)
canvas.bind('<Return>', Get2)


Name()
Hello3.config(text = lList)



canvas.mainloop()
