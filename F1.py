#DEVELOPED BY ANAND
from tkinter import *
import math

#Calculator variables
expression= ""
ans1 = 0
rec = 0
sqr = 0
sqrt = 0
log = 0

#Press
def press(num):
	global expression
	expression = expression + str(num)
	equation.set(expression)

#Press_equal
def press_equal():
	try:
		global expression
		global ans1
		total = str(eval(expression))
		equation.set(total)
		ans1 = total
		expression = ""
#Error
	except:
		equation.set(" error ")
		expression = ""

#Reciprocal
def reciprcl():
	try:
		global expression
		global rec
		if expression != "":
			rec= expression
		else:
			rec = ans1
		expression=""
		expression = expression + str(1/int(rec))
		equation.set(expression)

	except:
		equation.set(" error ")
		expression = ""

#Square
def sqr():
	try:
		global expression
		global sqr
		if expression != "":
			sqr= expression
		else:
			sqr = ans1
		expression=""
		expression = expression + str(math.pow(float(sqr),2))
		equation.set(expression)

	except:
		equation.set(" error ")
		expression = ""

#Log
def log():
	try:
		global expression
		global log
		if expression != "":
			log= expression
		else:
			log = ans1
		expression=""
		expression = expression + str(math.log10(float(log)))
		equation.set(expression)

	except:
		equation.set(" error ")
		expression = ""

#Square_root
def sqrt():
	try:
		global expression
		global sqrt
		if expression != "":
			sqrt= expression
		else:
			sqrt = ans1
		expression=""
		expression = expression + str(math.sqrt(float(sqrt)))
		equation.set(expression)

	except:
		equation.set(" error ")
		expression = ""

#Clearing calculator screen
def clear():
	global expression
	expression = ""
	equation.set("")

#Erase
def erase():
	global expression
	expression = expression[:-1]
	equation.set(expression)

#Answer
def answ():
	try:
		global expression
		global ans1
		expression += ans1
		equation.set(expression)

	except:
		equation.set(" error ")
		expression = ""

# Calculator window
if __name__ == "__main__":
	gui = Tk()
	gui.configure(background= "black")
	gui.title("GUI based Calculator")
	gui.geometry("320x330")

	equation = StringVar()

#Text entry box
	expression_field = Entry(gui, textvariable=equation, width= 40)

#Forming Grid
	expression_field.grid(columnspan=4, ipadx= 20,ipady= 10)

#Creating buttons of calculator
	button1 = Button(gui, text=' 1 ', fg='black', bg='grey', command=lambda: press(1), height=2, width=10)
	button1.grid(row=5, column=0)

	button2 = Button(gui, text=' 2 ', fg='black', bg='grey', command=lambda: press(2), height=2, width=10)
	button2.grid(row=5, column=1)

	button3 = Button(gui, text=' 3 ', fg='black', bg='grey', command=lambda: press(3), height=2, width=10)
	button3.grid(row=5, column=2)

	button4 = Button(gui, text=' 4 ', fg='black', bg='grey', command=lambda: press(4), height=2, width=10)
	button4.grid(row=4, column=0)

	button5 = Button(gui, text=' 5 ', fg='black', bg='grey', command=lambda: press(5), height=2, width=10)
	button5.grid(row=4, column=1)

	button6 = Button(gui, text=' 6 ', fg='black', bg='grey', command=lambda: press(6), height=2, width=10)
	button6.grid(row=4, column=2)

	button7 = Button(gui, text=' 7 ', fg='black', bg='grey', command=lambda: press(7), height=2, width=10)
	button7.grid(row=3, column=0)

	button8 = Button(gui, text=' 8 ', fg='black', bg='grey', command=lambda: press(8), height=2, width=10)
	button8.grid(row=3, column=1)

	button9 = Button(gui, text=' 9 ', fg='black', bg='grey', command=lambda: press(9), height=2, width=10)
	button9.grid(row=3, column=2)

	button0 = Button(gui, text=' 0 ', fg='black', bg="grey", command=lambda: press(0), height=2, width=10)
	button0.grid(row=6, column=0)

	plus = Button(gui, text=' + ', fg='black', bg='grey', command=lambda: press("+"), height=2, width=10)
	plus.grid(row=6, column=3)

	minus = Button(gui, text=' - ', fg='black', bg='grey', command=lambda: press("-"), height=2, width=10)
	minus.grid(row=5, column=3)

	multiply = Button(gui, text=' * ', fg='black', bg='grey', command=lambda: press("*"), height=2, width=10)
	multiply.grid(row=4, column=3)

	divide = Button(gui, text=' / ', fg='black', bg='grey', command=lambda: press("/"), height=2, width=10)
	divide.grid(row=3, column=3)

	equal = Button(gui, text=' = ', fg='black', bg='grey', command=press_equal, height=2, width=10)
	equal.grid(row=6, column=2)

	clear_entry = Button(gui, text=' CE ', fg='black', bg='grey', command=lambda: erase(), height=2, width=10)
	clear_entry.grid(row=2, column=2)

	Decimal= Button(gui, text='.', fg='black', bg='grey', command=lambda: press('.'), height=2, width=10)
	Decimal.grid(row=6, column=1)

	Percentage = Button(gui, text=' % ', fg='black', bg='grey', command=lambda: press('/100'), height=2, width=10)
	Percentage.grid(row=1, column=0)

	Clear_whole = Button(gui, text=' C ', fg='black', bg='grey', command=clear, height=2, width=10)
	Clear_whole.grid(row=7, column=0)

	Reciprocal = Button(gui, text=' 1/x ', fg='black', bg='grey', command=reciprcl, height=2, width=10)
	Reciprocal.grid(row=1, column=3)

	Square = Button(gui, text=' x^2 ', fg='black', bg='grey', command=sqr, height=2, width=10)
	Square.grid(row=1, column=2)

	Log = Button(gui, text=' log ', fg='black', bg='grey', command=log, height=2, width=10)
	Log.grid(row=2, column=3)

	Square_root = Button(gui, text=' x^0.5 ', fg='black', bg='grey', command=sqrt, height=2, width=10)
	Square_root.grid(row=1, column=1)

	Answer = Button(gui, text=' Ans ', fg='black', bg='grey', command=answ, height=2, width=10)
	Answer.grid(row=7, column=3)

	Par1 = Button(gui, text=' ( ', fg='black', bg='grey', command=lambda: press('('), height=2, width=10)
	Par1.grid(row=2, column=0)

	Par2 = Button(gui, text=' ) ', fg='black', bg='grey', command=lambda: press(')'), height=2, width=10)
	Par2.grid(row=2, column=1)

	e = Button(gui, text=' e ', fg='black', bg='grey', command=lambda: press(str(math.e)), height=2, width=10)
	e.grid(row=7, column=1)

	pi = Button(gui, text=' π ', fg='black', bg='grey', command=lambda: press(str(math.pi)), height=2, width=10)
	pi.grid(row=7, column=2)

	gui.mainloop()
