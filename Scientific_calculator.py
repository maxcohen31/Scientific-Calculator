# Scientific calculator 
# Author: Emanuele

from tkinter import *
import math

# Initializing the window
calc_wind = Tk()

# Title
calc_wind.title('Scientific calculator')

# character variable and entry_input variable
character = ''
entry_input = StringVar()
e = math.exp # Euler's number
log = math.log10
ln = math.log

# Buttons graphic
graphic = {'bd': 4,
    'fg': '#F0F8FF',
    'bg': 'gray12',
    'font': ('arial', 13),
    'width': 2,
    'height': 2,
    'relief': 'flat',
    'activebackground': 'gray12'}

# Function to get the input as a string
def get_input(n):
    global character
    character += str(n)
    entry_input.set(character)
    
# Delete all the input on the screen    
def delete_all_input():
    global character
    character = ''
    entry_input.set(character)    

# The equal function will allow us to get the result
# the eval() function is perfect for our purpose
def equal_to():
    global character
    getting_the_result = str(eval(character))
    character = getting_the_result
    entry_input.set(getting_the_result)

# AC function 
def ac_function():
    global character
    deleting = character[:-1]
    character = deleting
    entry_input.set(character)  
    
# Function to calculate the sine of an integer
def sin_function():
    global character
    calc_sin = str(math.sin(math.radians(int(character))))
    character = calc_sin
    entry_input.set(calc_sin)
    
# Function to calculate the cosine of an integer
def cos_function():
    global character
    calc_cos = str(math.cos(math.radians(int(character))))
    character = calc_cos
    entry_input.set(calc_cos)    

# Function to calculate the tanget of an integer
def tan_function():
    global character
    calc_tan = str(math.tan(math.radians(int(character))))
    character = calc_tan
    entry_input.set(calc_tan)
    
# Function to calculate the cotanget of an integer
def cotan_function():
    global character
    calc_cotan = str(1 / math.tan(math.radians(int(character))))
    character = calc_cotan
    entry_input.set(calc_cotan)

# Factorial function
def factorial_function():
    global character
    character = str(math.factorial(int(character)))
    entry_input.set(character)

# Square root of an integer
def square_function():
    global character
    if int(character) >= 0:
        square_root = str(eval(character + '**(1/2)'))
        character = square_root
    else:
        square_root = 'Math ERROR'     
    entry_input.set(character)  
   
# Third root function
def third_root_function():
    global character
    third_root_calc = str(eval(character + '**(1/3)'))
    character = third_root_calc
    entry_input.set(character) 

# Function to find the percentage of a function
def percentage_function():
    global character
    calc_percentage = str(eval(character + '0.01'))
    character = calc_percentage
    entry_input.set(character)
     
# Function to change the sign
def change_sign():
    global character
    if character[0] == '-':
        sign = character[:1]
    else:
        sign = '-' + character                
    character = sign
    entry_input.set(sign) 
    
# Showing the display
entry_display = Entry(calc_wind, font=('arial', 25), relief='flat', bg='#222222', fg='#FFFFFF', width=40, bd=4, justify='left', textvariable=entry_input)
entry_display.grid(columnspan=5, padx=10, pady=5)

# 0 button
zero_butt = Button(calc_wind, text='0', padx=15, pady=5, **graphic, command=lambda: get_input(0)).grid(row=9, column= 0, sticky='swen')

# period button
period_butt = Button(calc_wind, text='.', padx=15, pady=5, **graphic, command=lambda: get_input('.')).grid(row=9, column=1, sticky='swen')

# EXP button
exp_butt = Button(calc_wind, text='EXP', padx=15, pady=5, **graphic, command=lambda: get_input('e^')).grid(row=9, column=2, sticky='swen')

# Equal button
equal_butt = Button(calc_wind, text='=', padx = 40, pady=5, **graphic, command=lambda: equal_to()).grid(columnspan=2,row=9, column=3, sticky='swen')

# 1 button
button_1 = Button(calc_wind, text='1', padx=15, pady=5, **graphic, command=lambda: get_input(1)).grid(row=8, column=0, sticky='swen')

# 2 button
button_2 = Button(calc_wind, text='2', padx=15, pady=5, **graphic, command=lambda: get_input(2)).grid(row=8, column=1, sticky='swen')

# 3 button
button_3 = Button(calc_wind, text='3', padx=15, pady=5, **graphic, command=lambda: get_input(3)).grid(row=8, column=2, sticky='swen')

# Adding button
adding_button = Button(calc_wind, text='+', padx=15, pady=5, **graphic, command=lambda: get_input('+')).grid(row=8, column=3, sticky='swen')

# Subtract button
subtract_button = Button(calc_wind, text='-', padx=15, pady=5, **graphic, command=lambda: get_input('-')).grid(row=8, column=4, sticky='swen')

# 4 button
button_4 = Button(calc_wind, text='4', padx=15, pady=5, **graphic, command=lambda: get_input(4)).grid(row=7, column=0, sticky='swen')

# 5 button
button_5 = Button(calc_wind, text='5', padx=15, pady=5, **graphic, command=lambda: get_input(5)).grid(row=7, column=1, sticky='swen')

# 6 button
button_6 = Button(calc_wind, text='6', padx=15, pady=5, **graphic, command=lambda: get_input(6)).grid(row=7, column=2, sticky='swen')

# Multiply button
multiply_button = Button(calc_wind, text='*', padx=15, pady=5, **graphic, command=lambda: get_input('*')).grid(row=7, column=3, sticky='swen')

# Division button
division_button = Button(calc_wind, text='/', padx=15, pady=5, **graphic, command=lambda: get_input('/')).grid(row=7, column=4, sticky='swen')

# 7 button 
button_7 = Button(calc_wind, text='7', padx=15, pady=5, **graphic, command=lambda: get_input(7)).grid(row=6, column=0, sticky='swen')

# 8 button
button_8 = Button(calc_wind, text='8', padx=15, pady=5, **graphic, command=lambda: get_input(8)).grid(row=6, column=1, sticky='swen')

# 9 button
button_9 = Button(calc_wind, text='9', padx=15, pady=5, **graphic, command=lambda: get_input(9)).grid(row=6, column=2, sticky='swen')

# DEL button
del_button = Button(calc_wind, text='DEL', padx=15, pady=5,activebackground="#FB9F10", bg='#FB9F10', foreground='#FFFFFF', command=lambda: delete_all_input()).grid(row=6, column=3, sticky='swen')

# AC button
ac_button = Button(calc_wind, text='AC', padx=15, pady=5, activebackground="#FB9F10", bg='#FB9F10', foreground='#FFFFFF', command=lambda: ac_function()).grid(row=6, column=4, sticky='swen')

# Brackets buttons
bracket1 = Button(calc_wind, text='(', padx=15, pady=5, **graphic, command=lambda: get_input('(')).grid(row=5, column=0, sticky='swen')
bracket2 = Button(calc_wind, text=')', padx=15, pady=5, **graphic, command=lambda: get_input(')')).grid(row=5, column=1, sticky='swen')

# Change sign button
plus_min = Button(calc_wind, text='\u00B1', padx=15, pady=5, **graphic, command=lambda: change_sign()).grid(row=5, column=2, sticky='swen')

# Percentage button
percentage_button = Button(calc_wind, text='%', padx=15, pady=5, **graphic, command=lambda: percentage_function()).grid(row=5, column=3, sticky='swen')

# e^x button
ex_function = Button(calc_wind, text='e^x', padx=15, pady=5, **graphic, command=lambda: get_input('e(')).grid(row=5, column=4, sticky='swen')

# Square root button
square_root = Button(calc_wind, text='\u00B2\u221A', padx=15, pady=5, **graphic, command=lambda: square_function()).grid(row=4, column=0, sticky='swen')

# Third root button
third_root = Button(calc_wind, text='\u00B3\u221A', padx=15, pady=5, **graphic, command=lambda: third_root_function()).grid(row=4, column=1, sticky='swen')

# Nth root button
nth_root = Button(calc_wind, text='\u221A', padx=15, pady=5, **graphic, command=lambda: get_input('**(1/')).grid(row=4, column=2, sticky='swen')

# Logarithm with base 10 button
log_10 = Button(calc_wind, text='log\u2081\u2080', padx=15, pady=5, **graphic, command=lambda: get_input('log(')).grid(row=4, column=3, sticky='swen') 

# Natural logarithm(base e) button
ln = Button(calc_wind, text='ln', padx=15, pady=5, **graphic, command=lambda: get_input('ln(')).grid(row=4, column=4, sticky='swen') 

# X^2 button
pow_2 = Button(calc_wind, text='x\u00B2', padx=15, pady=5, **graphic, command=lambda: get_input('**2')).grid(row=3, column=0, sticky='swen')

# X^3 button
pow_3 = Button(calc_wind, text='x\u00B3', padx=15, pady=5, **graphic, command=lambda: get_input('**3')).grid(row=3, column=1, sticky='swen')

# x^n
nth_pow = Button(calc_wind, text='x^n', padx=15, pady=5, **graphic, command=lambda: get_input('**')).grid(row=3, column=2, sticky='swen') 

# Inverse of a number button
inverse_button = Button(calc_wind, text='x\u207b\xb9', padx=15, pady=5, **graphic, command=lambda: get_input('**-1')).grid(row=3, column=3, sticky='swen')

# 10^x button
pow_of_10_button = Button(calc_wind, text='10^x', padx=15, pady=5, **graphic, command=lambda: get_input('10**')).grid(row=3, column=4, sticky='swen') 

# Abs button (absolute value)
abs_button = Button(calc_wind, text='Abs', padx=15, pady=5, **graphic, command=lambda: get_input('abs(')).grid(row=2, column=0, sticky='swen')

# Euler's number button
euler_button = Button(calc_wind, text='e', padx=15, pady=5, **graphic, command=lambda: get_input(math.e)).grid(row=2, column=1, sticky='swen')

# Factorial button
factorial_button = Button(calc_wind, text='n!', padx=15, pady=5, **graphic, command=lambda:factorial_function()).grid(row=2, column=2, sticky='swen')

# Integer division quotient button
int_div_button = Button(calc_wind, text='div', padx=15, pady=5, **graphic, command=lambda: get_input('//')).grid(row=2, column=3, sticky='swen')

# Modulo button
modulo_button = Button(calc_wind, text='mod', padx=15, pady=5, **graphic, command=lambda: get_input('%')).grid(row=2, column=4, sticky='swen')

# Sin button
sin_button = Button(calc_wind, text='sin', padx=15, pady=5, **graphic, command=lambda: sin_function()).grid(row=1, column=0, sticky='swen')

# Cos button
cos_button = Button(calc_wind, text='cos', padx=15, pady=5, **graphic, command=lambda: cos_function()).grid(row=1, column=1, sticky='swen')

# Tan button
tan_button = Button(calc_wind, text='tan', padx=15, pady=5, **graphic, command=lambda: tan_function()).grid(row=1, column=2, sticky='swen')

# Cot button
cot_button = Button(calc_wind, text='cot', padx=15, pady=5, **graphic, command=lambda: cotan_function()).grid(row=1, column=3, sticky='swen')

# Pi button
pi_button = Button(calc_wind, text='π', padx=15, pady=5, **graphic, command=lambda: get_input(math.pi)).grid(row=1, column=4, sticky='swen')


# Calling the calculator window
calc_wind.mainloop()


