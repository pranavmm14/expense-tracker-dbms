from tkinter import PhotoImage
from tkinter import *

# Create the main window
window = Tk()
window.title('Expense Tracker')
window.config(bg='#0B5A81')
window.resizable(False, False)
window.geometry("1200x700+100+50")

f = ('Times', 14)
var = StringVar()
var.set('male')

# Create a bottom frame at the bottom of the main window
bottom_frame = Frame(window, width=1200, height=100, bg="#fff")
bottom_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='s')

label3 = Label(bottom_frame)
label3.place(x=600, y=50, anchor="center")

label4 = Label(label3, text="Total Amount")
label5 = Label(label3, text="Current Amount")

register_TotalAmount = Entry(
    label4,
    font=f
)

register_CurrentAmount = Entry(
    label5,
    font=f
)

label4.grid(row=0, column=0, pady=10, padx=20)
label5.grid(row=0, column=1, pady=10, padx=20)

# Create a right frame on the right side
right_frame = Frame(window, width=300, height=600, bg="#fff")
right_frame.grid(row=0, column=2, padx=10, pady=10, sticky='ne')

Label(
    right_frame, 
    text="", 
    bg='#CCCCCC',
    font=f
).grid(row=0, column=0, sticky=W, pady=10)

register_blank = Entry(
    right_frame, 
    font=f
)
register_blank.grid(row=0, column=1, pady=10, padx=20) 

# Create a left frame on the left side
left_frame = Frame(window, width=400, height=600, bg="#fff")
left_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nw')
Label(
    left_frame, 
    text="Enter Item", 
    bg='#fff',
    font=f,
    background='#fff',
).grid(row=0, column=0, sticky=W, pady=10)

Label(
    left_frame, 
    text="Add Amount", 
    bg='#CCCCCC',
    font=f,
    background='#fff',
).grid(row=1, column=0, sticky=W, pady=10)

register_Item = Entry(
    left_frame, 
    font=f
)

register_Amount = Entry(
    left_frame, 
    font=f
)

register_btn = Button(
    left_frame, 
    width=15, 
    text='Add', 
    font=f, 
    relief=SOLID,
    cursor='hand2',
    command=None,
)

register_Item.grid(row=0, column=1, pady=10, padx=20) 
register_Amount.grid(row=1, column=1, pady=10, padx=20)
register_btn.grid(row=2, column=0, columnspan=2, pady=10)


window.mainloop()
