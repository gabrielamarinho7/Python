#Importando o Tkinter
from cgitb import text
from re import A
from tkinter import *
from tkinter import ttk
from tkinter import font
from turtle import bgcolor, width

#Cores

cor1 = "#0d0d0d" #preta
cor2 = "#ffffff" #branco
cor3 = "#160854" #azul
cor4 = "#92939c" #cinza
cor5 = "#f5ad3b" #laranja


janela =Tk ()
janela.title("Calculadora")
janela.geometry("300x310")
janela.config(bg=cor1)

#Criando Frames
frame_tela = Frame(janela, width=300, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=300, height=268)
frame_corpo.grid(row=1, column=0)


app_label = Label(frame_tela, text="123456789", width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font="Ivy 18", bg=cor3, fg=cor2)
app_label.place(x=0, y=0)


#Criando botões - primeira coluna

b_1 = Button(frame_corpo, text="C", width=14, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)

b_2 = Button(frame_corpo, text="%", width=7, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=150, y=0)

b_3 = Button(frame_corpo, text="/", width=7, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=230, y=0)

#Segunda coluna de botões

b_4 = Button(frame_corpo, text="7", width=7, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)

b_5 = Button(frame_corpo, text="8", width=7, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=75, y=52)

b_6 = Button(frame_corpo, text="9", width=7, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=150, y=52)

b_7 = Button(frame_corpo, text="*", width=7, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=230, y=52)

#Terceira coluna de botões

b_8 = Button(frame_corpo, text="4", width=7, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)

b_9 = Button(frame_corpo, text="5", width=7, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=75, y=104)

b_10 = Button(frame_corpo, text="6", width=7, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=150, y=104)

b_11 = Button(frame_corpo, text="-", width=7, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=230, y=104)

#Quarta coluna de botões

b_12 = Button(frame_corpo, text="1", width=7, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=155)

b_13 = Button(frame_corpo, text="2", width=7, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=75, y=155)

b_14 = Button(frame_corpo, text="3", width=7, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=150, y=155)

b_15 = Button(frame_corpo, text="+", width=7, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=230, y=155)

#Quinta coluna


b_16 = Button(frame_corpo, text="0", width=14, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)

b_17 = Button(frame_corpo, text=".", width=7, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=150, y=208)

b_18 = Button(frame_corpo, text="=", width=7, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=230, y=208)


janela.mainloop()
    
