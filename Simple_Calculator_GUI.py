#Calculator Using GUI

from tkinter import*
exp=" "
def press(num):
	global exp
	exp=exp+str(num)
	equation.set(exp)

#fun to evaluate final expression
def equalpress():
	try:
	    gobal exp
	    total=str(eval(exp))
	    equation.set(total)
	    exp=" "
	except:
	     equation.set("error")
	     exp=" "

#function to clear contents
def clear():
	global exp
	exp=" "
	equation.set(" ")

#driver code

if _name_ =="__main__":
#create GUI window
	gui = Tk()
	gui.configure(background="light green”)
	gui.title("Simple Calculator")
	gui.geometry ("250x150")
	equation = StringVar()
	exp_field=Entry(gui, textvariable=equation)
	exp_field.grid(columnspan=4 , ipadx=70)
	button1 = Button(gui, text='1',fg='black' ,bg='yellow’ , command=lambda: 	press(1),height=button1. grid(row=2, column=0)
	button2 = Button(gui, text='2',fg='black',bg='yellow’ , command=lambda: 	press(2),height=button2.grid(row=2, column=1)
	button3 = Button(gui, text='3',fg='black' ,bg='yellow’ , command=lambda: 	press(3),height=button3.grid(row=2, column=2)
	button4 = Button(gui,text='4',fg='black',bg='yellow' , command=lambda: 	press(4) ,height=button4. grid(row=3, column=0)
	button5 = Button(gui, text='5',fg='black',bg='yellow' , command=lambda: 	press(5),height=button5.grid(row=3, column=1)
	button6 = Button(gui, text='6',fg='black',bg='yellow’ , command=lambda: 	press(6),height=button6. grid(row=3, column=2)
	button7 = Button(gui, text='7',fg='black',bg='yellow’ , command=lambda: 	press(7),height=button7.grid(row=4, column=0)
	button8 = Button(gui, text='8',fg='black' ,bg='yellow' , command=lambda: 	press(8) ,height=button8. grid(row=4, column=1)
	button9 = Button(gui, text='9',fg='black',bg='yellow' , command=Lambda: 	press(9), height=button9. grid(row=4, column=2)
	button0 = Button(gui, text='0', fg='black',bg='yellow’ , command=lambda: 	press(0),height=button0. grid(row=5, column=9)
	plus = Button(gui, text='+',fg='black',bg='yellow' , command=lambda: 	press("+"), height=plus.grid(row=2,column=3)
	minus = Button(gui,text="-',fg='black',bg='yellow' , command=lambda: 	press("-"),height=minus. grid(row=3, column=3)
	multiply = Button(gui,text='*',fg='black',bg="yellow' , command=lambda: 	press("*") , height=multiply. grid(row=4, column=3)
	divide = Button(gui,text='/',fg="black',bg='yellow' , command=lambda: 	press("/"), height=divide. grid(row=5, column=3)
	equal = Button(gui, text='=',fg="black' ,bg="yellow',command=equalpress, 	height=1, width=equal. grid(row=5, column=2)
	clear=Button(gui,text='clear',fg=‘black',bg="yellow' ,command=clear,heig	ht=1,width=clear. grid(row=5, column=1)
	decimal = Button(gui,text='.',fg='black' ,bg='yellow’ , command=lambda: 	press("."),height=decimal. grid(row=6, column=0)

#start GUI

gui.mainloop()
