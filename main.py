from tkinter import *
import random

main_window=Tk()
main_window.geometry('400x400')
main_window.title('Rock Paper Scissor')
main_window.resizable(0,0)
main_window.config(bg ='#000fff000')

Label(main_window,text='Rock Paper scissor',font=('arial', 22, 'bold'),bg='red').pack()
                                                      
#user input
user_take = StringVar()
Label(main_window, text = 'choose any one: Rock, Paper ,Scissors' , font='arial 15 bold', bg = 'seashell2').place(x=20,y=70)
Entry(main_window, font = 'arial 15', textvariable = user_take , bg = 'antiquewhite2').place(x=90 , y = 130)

comp_pick = random.randint(1,3)
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick ==2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissors'


Result = StringVar()
def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('tie,you both select same')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('you loose,computer select paper')
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set('you win,computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('you loose,computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('you win,computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('you loose,computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set('you win ,computer select paper')
    else:
        Result.set('invalid: choose any one -- rock, paper, scissors')

def Reset():
    Result.set("") 
    user_take.set("")

def Exit():
    main_window.destroy()

Entry(main_window, font = 'arial 10 bold', textvariable = Result, bg ='antiquewhite2',width = 50,).place(x=25, y = 250)
Button(main_window, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='blue' ,command = play).place(x=150,y=190)
Button(main_window, font = 'arial 13 bold', text = 'RESET'  ,padx =5,bg ='blue' ,command = Reset).place(x=70,y=310)
Button(main_window, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='blue' ,command = Exit).place(x=230,y=310)

