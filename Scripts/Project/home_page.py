from tkinter import PhotoImage 
from tkinter import *

# Create the main window
window = Tk()
window.title('Expense Tracker')
window.config(bg='#0B5A81')
window.resizable(False,False)
window.geometry("1200x700+100+50")
# background_image = PhotoImage(file="Scripts\\Project\\1.png")
# label6 = Label(window, image = background_image)
# label6.pack()


f = ('Times', 14)
var = StringVar()
var.set('male')




# Create a bottom frame below the top frames
bottom_frame = Frame(window, width=900, height=100, bg="green")
bottom_frame.grid(row=10, column=10, columnspan=2, padx=10, pady=10)

# Add widgets to the frames
right_frame = Frame(window, width=300, height=600, bg="red")
right_frame.grid(row=3, column=10, padx=1, pady=1)
window, 
bd=2, 
bg='#CCCCCC',
relief=SOLID, 
padx=10, 
pady=10
    
Label(
    right_frame, 
    text="Enter Item", 
    bg='#CCCCCC',
    font=f
    ).grid(row=1, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Add Amount", 
    bg='#CCCCCC',
    font=f
    ).grid(row=2, column=0, sticky=W, pady=10)

register_Itme = Entry(
    right_frame, 
    font=f
    )

register_Amount = Entry(
    right_frame, 
    font=f
    )

register_btn = Button(
    right_frame, 
    width=15, 
    text='Add', 
    font=f, 
    relief=SOLID,
    cursor='hand2',
    command=None
)

register_Itme.grid(row=1, column=1, pady=10, padx=20) 
register_Amount.grid(row=2, column=1, pady=10, padx=20)
register_btn.grid(row=7, column=1, pady=10, padx=20)


left_frame= Frame(window, width=300, height=600, bg="blue")
left_frame.grid(row=3, column=20, padx=1, pady=1)
window, 
bd=2, 
bg='#CCCCCC',
relief=SOLID, 
padx=10, 
pady=10
    
Label(
    left_frame, 
    text="", 
    bg='#CCCCCC',
    font=f
    ).grid(row=1, column=0, sticky=W, pady=10)

register_blanck = Entry(
    left_frame, 
    font=f
    )
register_blanck.grid(row=1, column=1, pady=10, padx=20) 



label3 = Label(bottom_frame, text="Frame 3 (Green)")
label3.place(x=700, y=50, anchor="sw")

# Create two Label widgets
label4 = Label(label3, text="Column 1")
label5 = Label(label3, text="Column 2")

# Place the Label widgets in the label3 frame
label4.grid(row=0, column=0)
label5.grid(row=0, column=1)



window.mainloop()