from tkinter import *
import tkinter.messagebox
click = True
def start():
    global root
    root = Tk()
    root.title("Tic Tac Toe")
    def play(button):
        global click, root
        if button["text"] == " " and click==True:
            button["text"] = "X"
            click = False
        elif button["text"] == " " and click==False:
            button['text'] = "O"
            click = True
        if (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
            button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
            button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
            button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
            button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
            button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X" or
            button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
            button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X"):
            answer = tkinter.messagebox.askquestion('X Player wins!!!', 'Do you want to play again')
            root.destroy()
            if answer == 'yes': start()
        elif (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
            button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
            button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
            button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
            button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
            button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O" or
            button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
            button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O"):
            answer = tkinter.messagebox.askquestion('O Player wins!!!', 'Do you want to play again')
            root.destroy()
            if answer == 'yes': start()
        elif (button1["text"]!=" " and button2["text"]!=" " and button3["text"]!=" " and button4["text"]!=" " and
              button5["text"] != " " and button6["text"]!=" " and button7["text"]!=" " and button8["text"]!=" " and
              button9["text"] != " "):
            answer = tkinter.messagebox.askquestion('Game Tied!!!', 'Do you want to play again')
            root.destroy()
            if answer=="yes": start()
    button1 = Button(root, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button1))
    button1.grid(row=1, column=0, sticky=S+N+E+W)
    button2 = Button(root, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button2))
    button2.grid(row=1, column=1, sticky=S+N+E+W)
    button3 = Button(root, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button3))
    button3.grid(row=1, column=2, sticky=S+N+E+W)
    button4 = Button(root, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button4))
    button4.grid(row=2, column=0, sticky=S+N+E+W)
    button5 = Button(root, text=" ", font=("Times 26 bold"), height=4, width=8, command=lambda:play(button5))
    button5.grid(row=2, column=1, sticky=S+N+E+W)
    button6 = Button(root, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button6))
    button6.grid(row=2, column=2, sticky=S+N+E+W)
    button7 = Button(root, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button7))
    button7.grid(row=3, column=0, sticky=S+N+E+W)
    button8 = Button(root, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button8))
    button8.grid(row=3, column=1, sticky=S+N+E+W)
    button9 = Button(root, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button9))
    button9.grid(row=3, column=2, sticky=S+N+E+W)
    root.mainloop()
start()