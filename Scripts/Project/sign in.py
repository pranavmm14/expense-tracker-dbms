
from tkinter import PhotoImage 
from tkinter import *



window = Tk()
window.title('Expense Tracker')
window.config(bg='#c5bfc7')
window.resizable(False,False)
window.geometry("1200x700+100+50")



f = ('Times', 14)
var = StringVar()
var.set('male')

background_image = PhotoImage(file="Scripts\\Project\\1.png")


# Create a Label Widget to display the text or Image
label = Label(window, image = background_image)
label.pack()


right_frame = Frame(
    window, 
    bd=2, 
    bg='#ffffff',
    relief=SOLID, 
    padx=10, 
    pady=10
    )


Label(
    right_frame, 
    text="First Name", 
    bg='#fff',
    font=f,
    foreground='#063808'
    ).grid(row=0, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Last Name", 
    bg='#fff',
    font=f,
    foreground='#063808'
    ).grid(row=1, column=0, sticky=W, pady=10)


Label(
    right_frame, 
    text="Enter Email", 
    bg='#fff',
    font=f,
    foreground='#063808'
    ).grid(row=2, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Contact Number", 
    bg='#fff',
    font=f,
    foreground='#063808'
    
    ).grid(row=3, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Select Gender", 
    bg='#fff',
    font=f,
    foreground='#063808'
    ).grid(row=4, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Enter Password", 
    bg='#fff',
    font=f,
    foreground='#063808'
    ).grid(row=5, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Re-Enter Password", 
    bg='#fff',
    font=f,
    foreground='#063808'
    ).grid(row=6, column=0, sticky=W, pady=10)

gender_frame = LabelFrame(
    right_frame,
    bg='#fff',
    bd=2, 
    padx=10, 
    pady=10,
    foreground='#063808',
    )


register_firstname = Entry(
    right_frame, 
    font=f,
    bd=5, 
    foreground='#063808',
    )

register_lastname = Entry(
    right_frame, 
    font=f,
    bd=5, 
    foreground='#063808',
    )

register_email = Entry(
    right_frame, 
    font=f,
    bd=5, 
    foreground='#063808',
    )

register_mobile = Entry(
    right_frame, 
    font=f,
    bd=5, 
    foreground='#063808',
    )


male_rb = Radiobutton(
    gender_frame, 
    text='Male',
    bg='#CCCCCC',
    variable=var,
    value='male',
    foreground='#063808',
    font=('Times', 10),
    
)

female_rb = Radiobutton(
    gender_frame,
    text='Female',
    bg='#CCCCCC',
    variable=var,
    value='female',
    foreground='#063808',
    font=('Times', 10),
  
)

others_rb = Radiobutton(
    gender_frame,
    text='Others',
    bg='#CCCCCC',
    variable=var,
    value='others',
    foreground='#063808',
    font=('Times', 10)
   
)

register_pwd = Entry(
    right_frame, 
    font=f,
    bd=5, 
    foreground='#063808',
    show='*'
)
pwd_again = Entry(
    right_frame, 
    font=f,
    bd=5, 
    foreground='#063808',
    show='*'
)

register_btn = Button(
    right_frame, 
    width=15, 
    text='Register', 
    font=f, 
    background='#fff',
    relief=SOLID,
    cursor='hand2',
    command=None
)


register_firstname.grid(row=0, column=1, pady=10, padx=20)
register_lastname.grid(row=1, column=1, pady=10, padx=20)
register_email.grid(row=2, column=1, pady=10, padx=20) 
register_mobile.grid(row=3, column=1, pady=10, padx=20)
gender_frame.grid(row=4, column=1, pady=10, padx=20)
register_pwd.grid(row=5, column=1, pady=10, padx=20)
pwd_again.grid(row=6 , column=1, pady=10, padx=20)
register_btn.grid(row=7, column=1, pady=10, padx=20)
right_frame.place(x=700,y=50,anchor="nw")

male_rb.pack(expand=True, side=LEFT)
female_rb.pack(expand=True, side=LEFT)
others_rb.pack(expand=True, side=LEFT)


left_frame = Frame(
    window, 
    bd=2, 
    bg='#b1a5cc',   
    relief=SOLID, 
    padx=10,
    pady=10
    )

Label(
    left_frame, 
    text="UserName", 
    bg='#b1a5cc',
    font=f,
    foreground='#250073'
    ).grid(row=0, column=0, sticky=W, pady=10)

Label(
    left_frame, 
    text="Password", 
    bg='#b1a5cc',
    font=f,
    foreground='#250073'
    ).grid(row=1, column=0, pady=10)

email_tf = Entry(
    left_frame, 
    font=f,
    bd=5,
    foreground='#250073',
    background='#ddd9de',
    )
pwd_tf = Entry(
    left_frame, 
    font=f,
    bd=5,
    foreground='#250073',
    background='#ddd9de',
    show='*'
    )
login_btn = Button(
    left_frame, 
    width=15, 
    text='Login', 
    font=f, 
    foreground='#250073',
    relief=SOLID,
    cursor='hand2',
    command=None,
    bg='#b1a5cc'
    )

email_tf.grid(row=0, column=1, pady=10, padx=20)
pwd_tf.grid(row=1, column=1, pady=10, padx=20)
login_btn.grid(row=2, column=1, pady=10, padx=20)
left_frame.place(x=100,y=50,anchor="nw")


window.mainloop()