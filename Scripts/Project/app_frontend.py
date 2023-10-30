import tkinter as tk
from tkinter import PhotoImage

class RegisterFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bd=2, relief="solid", bg='#ffffff')
        self.register_firstname = tk.Entry(self, font=("Oxygen 14"),foreground='#250073')
        self.register_lastname = tk.Entry(self, font=("Oxygen 14"),foreground='#250073')
        self.register_email = tk.Entry(self, font=("Oxygen 14"),foreground='#250073')
        self.register_mobile = tk.Entry(self, font=("Oxygen 14"),foreground='#250073')
        self.register_pwd = tk.Entry(self, font=("Oxygen 14"),foreground='#250073', show="*")
        self.pwd_again = tk.Entry(self, font=("Oxygen 14"),foreground='#250073', show="*")
        self.register_btn = tk.Button(self, text="Register", font=("Oxygen 14"), width=15, command=None,background='#fff',relief="solid",cursor='hand2')

        self.register_firstname.grid(row=0, column=1, pady=10, padx=20)
        self.register_lastname.grid(row=1, column=1, pady=10, padx=20)
        self.register_email.grid(row=2, column=1, pady=10, padx=20)
        self.register_mobile.grid(row=3, column=1, pady=10, padx=20)
        self.register_pwd.grid(row=5, column=1, pady=10, padx=20)
        self.pwd_again.grid(row=6, column=1, pady=10, padx=20)
        self.register_btn.grid(row=7, column=1, pady=10, padx=20)

        tk.Label(self, text="First Name", bg='#fff', font=("Oxygen 14"), foreground='#250073').grid(row=0, column=0, pady=10)
        tk.Label(self, text="Last Name", bg='#fff', font=("Oxygen 14"), foreground='#250073').grid(row=1, column=0, pady=10)
        tk.Label(self, text="Enter username", bg='#fff', font=("Oxygen 14"), foreground='#250073').grid(row=2, column=0, pady=10)
        tk.Label(self, text="Contact Number", bg='#fff', font=("Oxygen 14"), foreground='#250073').grid(row=3, column=0, pady=10)
        tk.Label(self, text="Select Gender", bg='#fff', font=("Oxygen 14"), foreground='#250073').grid(row=4, column=0, pady=10)
        tk.Label(self, text="Enter Password", bg='#fff', font=("Oxygen 14"), foreground='#250073').grid(row=5, column=0, pady=10)
        tk.Label(self, text="Re-Enter Password", bg='#fff', font=("Oxygen 14"), foreground='#250073').grid(row=6, column=0, pady=10)


class LoginFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bd=2, relief="solid", bg='#b1a5cc')

        self.email_tf = tk.Entry(self, font=("Oxygen 14"), bg='#ddd9de',bd=2,foreground='#250073')
        self.pwd_tf = tk.Entry(self, font=("Oxygen 14"), show="*", bg='#ddd9de',bd=2,foreground='#250073')
        self.login_btn = tk.Button(self, text="Login", font=("Oxygen 14"), width=15, command=None,bg='#b1a5cc', relief="solid" ,cursor='hand2')

        self.email_tf.grid(row=0, column=1, pady=10, padx=20)
        self.pwd_tf.grid(row=1, column=1, pady=10, padx=20)
        self.login_btn.grid(row=2, column=1, pady=10, padx=20)

        tk.Label(self, text="UserName", bg='#b1a5cc', font=("Oxygen 14"), foreground='#250073').grid(row=0, column=0, pady=10)
        tk.Label(self, text="Password", bg='#b1a5cc', font=("Oxygen 14"), foreground='#250073').grid(row=1, column=0, pady=10)

class FinTrack(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("FinTrack")
        self.config(bg="#c5bfc7")
        # self.resizable(False, False)
        self.geometry("1200x700+100+50")

        self.background_image = PhotoImage(file="Scripts\\Project\\1.png")
        self.label = tk.Label(self, image=self.background_image)
        self.label.place(relx=0.5, rely=0.5, anchor="center")

        self.app_name_font = ('Oxygen 30 bold')
        self.app_name = tk.Label(self, text="FinTrack", font=self.app_name_font, bg="#fcb603", fg="#250073")

        self.name_frame = tk.Frame(self, bd=0, bg='#250073',relief='SOLID', padx=2, pady=2 )
        self.app_name.pack()

        self.register_frame = RegisterFrame(self)
        self.login_frame = LoginFrame(self)

        self.name_frame.place(relx=0.5,y=30,anchor="n")
        self.register_frame.place(x=700,y=150,anchor="nw")
        self.login_frame.place(x=100,y=150,anchor="nw")

if __name__ == "__main__":
    app = FinTrack()
    app.mainloop()
