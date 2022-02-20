import string, random, time
from PokemonNames import words
from tkinter import *


canvas = Tk()
canvas.title("Hangman")
canvas.geometry("340x230")
frame = (canvas)
tch = string.ascii_uppercase
blarp = list(tch)


hello = 'Hello! Would you like to play a word guessing game?\nYou can guess a random pokemon name!'
lives = 7
meh = ("Sans Serif", 8, "bold")


guess2 = ''
guess = StringVar()
Guess = Entry(frame, textvariable = guess, justify = 'center', bg= "white", font = meh)
Guess.grid(column = 7, sticky = 'news', columnspan = 5, row = 8)
name= ' '
nameL=[]
lList=[]
score = 0
try1= 'Press any letter to guess\nor type a letter and hit submit'
Hello = Label(frame, text = hello,  wraplength=0)
Hello.grid(column = 5, columnspan = 10, row = 0, rowspan = 2)
Hello2 = Label(frame, text = try1, wraplength=0)
Hello2.grid(column = 5, columnspan = 10, row = 4, rowspan = 3)
Hello3 = Label(frame, text = lList)
Hello3.grid(column=5, columnspan=10, row = 7)

Lives = Label(frame, text = f'Lives: {lives}', bg = "light blue", width = 9)
Lives.grid(column=0, row = 9, columnspan = 8)

def Name():
    global name, nameL, lList
    name = random.choice(words).upper()
    nameL = set(name)
    lList = [letter if letter in guess2 else '*' for letter in name]
    lives = 7


def Submit(c):
    c = c.upper()
    global guess2, lives, name, nameL, lList,score
    if lives >0:
        if c in guess2:
            Hello.config(text= f'You have already guessed {c}.\nPlease select another letter.')
        if c not in guess2:
            guess2 += c
            Hello.config(text = f'You have guessed the letters\n')
            if c not in name:
                lives -= 1
    lList = [letter if letter in guess2 else '*' for letter in name]
    Hello2.config(text = f'{guess2}\n')
    Hello3.config(text = lList)
    Lives.config(text = f'Lives: {lives}')
    if set(lList) == nameL:
        Congrats()
    if lives <=0:
        Hello.config(text = f'You have run out of lives.\nThe Pokemon name was {name}.')
        Hello2.config(text='Press Continue to play again or Quit to exit.\n')


def Get():
    c = Guess.get()
    Submit(c)
    Guess.delete(0, END)

def Get2(event):
    c = Guess.get()
    Submit(c)
    Guess.delete(0, END)


def Cont():
    global name, nameL, lList, lives, guess2
    if '*' in lList and lives >0:
        Hello.config(text = 'Please finish guessing the current Pokemon.')
        Hello2.config(text = 'Or press Quit to exit')
    else:
        guess2 = ' '
        lives = 7
        Name()
        Hello.config(text = hello)
        Hello2.config(text = try1)
        Hello3.config(text = lList)
        Lives.config(text = f'Lives: {lives}')


def Congrats():
    Hello.config(text = f'Congratulations!\nYou guessed {name} with {lives} lives left.')
    Hello2.config(text ='Press Continue to play again or Quit to exit.')



i = 0
for a in range(3):
    for b in range(9):
        try:
            Button(canvas, text = blarp[i], command=lambda c=(blarp[i]): Submit(c), width = 4).grid(column=b+5, row = a+10)
            i+=1
        except:
            pass

Button(frame, text = "Quit", font = meh, anchor = 'center', command = lambda: quit(), width = 5, bg="#EE4B2B").grid(column=12, row = 9, columnspan = 10)
Button(frame, text = "Continue", font = meh, anchor = 'center', command = lambda: Cont(), width = 9, bg = "teal").grid(column=8, row = 9, columnspan = 10)
Button(frame, text = "Submit", bg = "green", font = meh, justify = 'center', command = lambda: Get()).grid(row =9, column = 6, columnspan=5)
canvas.bind('<Return>', Get2)


Name()
Hello3.config(text = lList)


canvas.mainloop()
