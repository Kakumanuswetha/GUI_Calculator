from tkinter import *

window = Tk()
window.geometry("350x500")
window.title("Calculator")
window.configure(bg="#3399ff")
window.iconbitmap("calculator_icon.ico")
#button types ridge,raised,sunken,flat,solid,groove
#pady refers to how many pixels to pad the widget vertically outside the widget's border.
#So it increases the vertical space between this widget and other widget
#padx for horizontal space
#ipady and ipadx they refer to how many pixels to add horizontally and vertically inside the widgets border.
#They basically increased the widget ,the widget's size.

#StringVar is a class in Tkinter used to monitor changes in the string variable

# fill determines if the widgets keeps the minimal space needed or takes up any extra space allocated to it.
#We can assign to it X or Y or both 

#1st method to customize layout is pack():-pack places the widget or items in the middle
# 2nd method to customize layout of the widgets  :-  grid() function
# GRid:- Slices up the window into a table of rows and coloumns and places widgets accordingly.
#cannot use geometry manager grid inside which already has slaves managed by pack.
#to overcome grid error we need to create frames
# When the widget is a smaller than the cell sticky is used to indicate which slides and corners of the cell the widget sticks to.
# The direction is defined by the compass directions like north,east,south and so on, and we can use a string concatenation with it as follows.
#3rd method to customize layout is function place()
#place():-  It slices up the window into a coordinate system of the X and Y with the origin or the 00 position is the top left corner of our window.
#As we move to the right ,the x-position increases until the maximum value,which is the width.
#AS we move downwards the y position is increases until the maximum value,which is the height.
#1st method to customize layout is pack():-pack places the widget or items in the middle
#3rd method to customize layout is function place()
#place():-  It slices up the window into a coordinate system of the X and Y with the origin or the 00 position is the top left corner of our window.
#As we move to the right ,the x-position increases until the maximum value,which is the width.
#AS we move downwards the y position is increases until the maximum value,which is the height.

#test function is created to add functionality to button

#Retrieves the digits and operators pressed by the user using the lambda function and append them to a string variable, and then set the text variable of the entry box to the expression stored in our string variable.

expression=''

def press(n):
	global expression 
	expression = expression + str(n)
	equation.set(expression)

def equal():
	try:
		global expression 
		total = str(eval(expression))
		equation.set(total)
		expression=total
	except:
		equation.set('Error')
		expression=''
def clear():
	global expression
	expression=''
	equation.set('0')

def backspace():
	global expression 
	if(expression==''):
		print('Nothing to clear already empty')
		equation.set('0')
	else:
		expression = expression.rstrip(expression[-1])
		equation.set(expression)
expression_frame = Frame(window, bg="#3399ff")

buttons_frame = Frame(window, bg="#3399ff")
expression_frame.pack()
buttons_frame.pack()

font_entry = ('ariel',20,'bold')
font_button = ('new times roman',12)
equation = StringVar()
equation.set('0')
equation_field = Entry(expression_frame,textvariable=equation,font=font_entry,justify='right')
equation_field.pack(ipadx=10,ipady=10,pady=20)
button1 = Button(buttons_frame, text='1', font=font_button,relief='ridge',bg="#80bfff", borderwidth=1 , width=8 , height=3, command=lambda:press(1))
button2 = Button(buttons_frame, text='2', font=font_button,relief='ridge',bg="#80bfff", borderwidth=1 , width=8 , height=3,command=lambda:press(2))
button3 = Button(buttons_frame, text='3', font=font_button,relief='ridge',bg="#80bfff", borderwidth=1 , width=8 , height=3,command=lambda:press(3))
plus = Button(buttons_frame, text='+', font=font_button,relief='ridge',bg="#80bfff", borderwidth=1 , width=8 , height=3,command=lambda:press('+'))
button4 = Button(buttons_frame, text='4', font=font_button,relief='ridge',bg="#80bfff", borderwidth=1 , width=8 , height=3,command=lambda:press(4))
button5 = Button(buttons_frame, text='5', font=font_button,relief='ridge',bg="#80bfff", borderwidth=1 , width=8 , height=3,command=lambda:press(5))
button6 = Button(buttons_frame, text='6', font=font_button,relief='ridge',bg="#80bfff", borderwidth=1 , width=8 , height=3,command=lambda:press(6))
minus = Button(buttons_frame, text='-', font=font_button,relief='ridge',bg="#80bfff", borderwidth=1 , width=8 , height=3,command=lambda:press('-'))
button7 = Button(buttons_frame, text='7', font=font_button,relief='ridge',bg="#80bfff", borderwidth=1 , width=8 , height=3,command=lambda:press(7))
button8 = Button(buttons_frame, text='8', font=font_button,relief='ridge',bg="#80bfff", borderwidth=1 , width=8 , height=3,command=lambda:press(8))
button9 = Button(buttons_frame, text='9', font=font_button,relief='ridge',bg="#80bfff", borderwidth=1 , width=8 , height=3,command=lambda:press(9))
multiply = Button(buttons_frame, text='*', font=font_button,relief='ridge',bg="#80bfff", borderwidth=1 , width=8 , height=3,command=lambda:press('*'))
button0= Button(buttons_frame, text='0', font=font_button,relief='ridge',bg="#80bfff", borderwidth=1 , width=8 , height=3,command=lambda:press(0))
decimal= Button(buttons_frame, text='.', font=font_button,relief='ridge',bg="#80bfff", borderwidth=1 , width=8 , height=3,command=lambda:press('.'))
clear= Button(buttons_frame, text='C', font=font_button,relief='ridge',bg="#80bfff", borderwidth=1 , width=8 , height=3,command=clear)
divide= Button(buttons_frame, text='/', font=font_button,relief='ridge',bg="#80bfff", borderwidth=1 , width=8 , height=3,command=lambda:press('/'))
equal = Button(buttons_frame, text='=', font=font_button,relief='ridge',bg="#80bfff", borderwidth=1 , width=8 , height=3,command=equal)
backspace = Button(buttons_frame, text='<<', font=font_button,relief='ridge',bg="#80bfff", borderwidth=1 , width=8 , height=3,command=backspace)
#button19= Button(buttons_frame, text='1', font=font_button,relief='ridge',bg="#80bfff", borderwidth=1 , width=8 , height=3)

button1.grid(row=0 , column=0)
button2.grid(row=0 , column=1)
button3.grid(row=0 , column=2)
plus.grid(row=0 , column=3)

button4.grid(row=1 , column=0)
button5.grid(row=1 , column=1)
button6.grid(row=1 , column=2)
minus.grid(row=1 , column=3)

button7.grid(row=2 , column=0)
button8.grid(row=2 , column=1)
button9.grid(row=2 , column=2)
multiply.grid(row=2 , column=3)

button0.grid(row=3 , column=0)
decimal.grid(row=3 , column=1)
clear.grid(row=3 , column=2)
divide.grid(row=3 , column=3)

equal.grid(row=4 , column=0,columnspan=3,sticky='nsew')
backspace.grid(row=4 , column=3)

#To create functionality use command argument in the button function



window.mainloop()

