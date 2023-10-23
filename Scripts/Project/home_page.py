from tkinter import PhotoImage 
from tkinter import *

#Creating a window to show show UI of Desktop app
window = Tk()
window.title('FinTrack')
window.config(bg='#c5bfc7')
window.resizable(False,False)
window.geometry("1200x700+100+50")

# Create a Label Widget to display the text or Image
background_image = PhotoImage(file="Scripts\\Project\\1.png")
label = Label(window, image = background_image)
label.place(relx=0.5,rely=0.5,anchor="center")

#UI fonts
f = ('Times', 14)

# Frame to show stats
bottom_frame = Frame(window, width=1200, height=250, bg="green" ,relief="solid")
bottom_frame.place(rely=1,relx=0.5,anchor="s")

# Frame to  add expenses 
expense_frame = Frame(window, width=600, height=450, bg="red", bd=2)
expense_frame.place(relx=0,rely=0, anchor="nw")
    
Label(
    expense_frame, 
    text="Enter Item", 
    bg='#CCCCCC',
    font=f,
    width=600
    ).grid(row=0, column=0, pady=10)

Label(
    expense_frame, 
    text="Add Amount", 
    bg='#CCCCCC',
    font=f
    ).grid(row=1, column=0, pady=10)

register_Itme = Entry(
    expense_frame, 
    font=f
    )

register_Amount = Entry(
    expense_frame, 
    font=f
    )

register_btn = Button(
    expense_frame, 
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


left_frame= Frame(window, width=600, height=450, bg="blue")
left_frame.place(relx=1,rely=0, anchor="ne")

Label(
    left_frame, 
    text="", 
    bg='#CCCCCC',
    font=f
    ).grid(row=1, column=0, sticky=W, pady=10)

register_blank = Entry(
    left_frame, 
    font=f
    )
register_blank.grid(row=1, column=1, pady=10, padx=20) 



label3 = Label(bottom_frame, text="Frame 3 (Green)")
label3.place(x=700, y=50, anchor="sw")

# Create two Label widgets
label4 = Label(label3, text="Column 1")
label5 = Label(label3, text="Column 2")

# Place the Label widgets in the label3 frame
label4.grid(row=0, column=0)
label5.grid(row=0, column=1)



window.mainloop()