from tkinter import *

root = Tk()
root.title("Calculator")
root.configure(background="#DDDDDD")

enter = Entry(root, width=22, font=('Bookman Old Style', 16), borderwidth=6)
enter.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    current = enter.get()
    enter.delete(0, END)
    enter.insert(0, str(current) + str(number))


def button_clear():
    enter.delete(0, END)


def button_plus():
    first_number = enter.get()
    global f_num
    global math
    f_num = int(first_number)
    math = "plus"
    enter.insert(END, "+")

def button_multiply():
    first_number = enter.get()
    global f_num
    global math
    f_num = int(first_number)
    math = "multiply"
    enter.insert(END, "×")

def button_minus():
    first_number = enter.get()
    global f_num
    global math
    f_num = int(first_number)
    math = "minus"
    enter.insert(END, "-")

def button_division():
    first_number = enter.get()
    global f_num
    global math
    f_num = int(first_number)
    math = "division"
    enter.insert(END, "÷")

def button_equal():
    second_number = enter.get()
    enter.delete(0, END)
    if math == "minus":
        find = second_number.find('-')
        enter.insert(0, f_num - int(second_number[find+1:]))
    elif math == "plus":
        find = second_number.find('+')
        enter.insert(0, f_num + int(second_number[find+1:]))
    elif math == "multiply":
        find = second_number.find('×')
        enter.insert(0, f_num * int(second_number[find+1:]))
    else:
        find = second_number.find('÷')
        if int(second_number[find + 1:]) != 0:
            enter.insert(0, f_num / int(second_number[find + 1:]))
        else:
            enter.insert(0, "Error: division by zero!")


button_1 = Button(root, text="1", font=('Bookman Old Style', 16), background="#CCDDFF", command=lambda: button_click(1))
button_2 = Button(root, text="2", font=('Bookman Old Style', 16), background="#CCDDFF", command=lambda: button_click(2))
button_3 = Button(root, text="3", font=('Bookman Old Style', 16), background="#CCDDFF", command=lambda: button_click(3))
button_4 = Button(root, text="4", font=('Bookman Old Style', 16), background="#CCDDFF", command=lambda: button_click(4))
button_5 = Button(root, text="5", font=('Bookman Old Style', 16), background="#CCDDFF", command=lambda: button_click(5))
button_6 = Button(root, text="6", font=('Bookman Old Style', 16), background="#CCDDFF", command=lambda: button_click(6))
button_7 = Button(root, text="7", font=('Bookman Old Style', 16), background="#CCDDFF", command=lambda: button_click(7))
button_8 = Button(root, text="8", font=('Bookman Old Style', 16), background="#CCDDFF", command=lambda: button_click(8))
button_9 = Button(root, text="9", font=('Bookman Old Style', 16), background="#CCDDFF", command=lambda: button_click(9))
button_0 = Button(root, text="0", font=('Bookman Old Style', 16), background="#CCDDFF", command=lambda: button_click(0))
button_plus = Button(root, text="+", font=('Bookman Old Style', 16), background="#CCCCFF", command=button_plus)
button_multiply = Button(root, text="×", font=('Bookman Old Style', 16), background="#CCCCFF", command=button_multiply)
button_minus = Button(root, text="−", font=('Bookman Old Style', 16), background="#CCCCFF", command=button_minus)
button_division = Button(root, text="÷", font=('Bookman Old Style', 16), background="#CCCCFF", command=button_division)
button_equal = Button(root, text="=", font=('Bookman Old Style', 16), background="#99BBFF", command=button_equal)
button_clear = Button(root, text="CLEAR", font=('Bookman Old Style', 16), background="#9999BF", command=button_clear)

button_1.grid(row=2, column=0, ipady=3, padx=[20, 0], pady=2, sticky="NSEW")
button_2.grid(row=2, column=1, ipady=3, padx=[10, 10], pady=2, sticky="NSEW")
button_3.grid(row=2, column=2, ipady=3, padx=[0, 20], pady=2, sticky="NSEW")

button_4.grid(row=3, column=0, ipady=3, padx=[20, 0], pady=2, sticky="NSEW")
button_5.grid(row=3, column=1, ipady=3, padx=[10, 10], pady=2, sticky="NSEW")
button_6.grid(row=3, column=2, ipady=3, padx=[0, 20], pady=2, sticky="NSEW")

button_7.grid(row=4, column=0, ipady=3, padx=[20, 0], pady=2, sticky="NSEW")
button_8.grid(row=4, column=1, ipady=3, padx=[10, 10], pady=2, sticky="NSEW")
button_9.grid(row=4, column=2, ipady=3, padx=[0, 20], pady=2, sticky="NSEW")

button_0.grid(row=5, column=0, ipady=3, padx=[20, 0], pady=2, sticky="NSEW")
button_equal.grid(row=5, column=1, columnspan=2, ipady=3, padx=[10, 20], pady=2, sticky="NSEW")

button_plus.grid(row=6, column=0, ipady=3, padx=[20, 0], pady=2, sticky="NSEW")
button_minus.grid(row=6, column=1, ipady=3, padx=[10, 10], pady=2, sticky="NSEW")
button_multiply.grid(row=6, column=2, ipady=3, padx=[0, 20], pady=2, sticky="NSEW")

button_division.grid(row=7, column=0, ipady=3, padx=[20, 0], pady=[2, 20], sticky="NSEW")
button_clear.grid(row=7, column=1, columnspan=2, ipady=3, padx=[10, 20], pady=[2, 20], sticky="NSEW")

root.mainloop()
