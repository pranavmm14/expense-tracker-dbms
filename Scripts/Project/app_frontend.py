import tkinter as tk

class RegisterFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="Enter Name", font=("Times", 14)).grid(row=0, column=0, pady=10)
        tk.Label(self, text="Enter Email", font=("Times", 14)).grid(row=1, column=0, pady=10)
        tk.Label(self, text="Contact Number", font=("Times", 14)).grid(row=2, column=0, pady=10)
        tk.Label(self, text="Select Gender", font=("Times", 14)).grid(row=3, column=0, pady=10)
        tk.Label(self, text="Enter Password", font=("Times", 14)).grid(row=4, column=0, pady=10)
        tk.Label(self, text="Re-Enter Password", font=("Times", 14)).grid(row=7, column=0, pady=10)

        self.register_name = tk.Entry(self, font=("Times", 14))
        self.register_email = tk.Entry(self, font=("Times", 14))
        self.register_mobile = tk.Entry(self, font=("Times", 14))
        self.register_pwd = tk.Entry(self, font=("Times", 14), show="*")
        self.pwd_again = tk.Entry(self, font=("Times", 14), show="*")
        self.register_btn = tk.Button(self, text="Register", font=("Times", 14), width=15, command=None)

        self.register_name.grid(row=0, column=1, pady=10, padx=20)
        self.register_email.grid(row=1, column=1, pady=10, padx=20)
        self.register_mobile.grid(row=2, column=1, pady=10, padx=20)
        self.register_pwd.grid(row=4, column=1, pady=10, padx=20)
        self.pwd_again.grid(row=7, column=1, pady=10, padx=20)
        self.register_btn.grid(row=8, column=1, pady=10, padx=20)

class LoginFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="Enter Email", font=("Times", 14)).grid(row=0, column=0, pady=10)
        tk.Label(self, text="Enter Password", font=("Times", 14)).grid(row=1, column=0, pady=10)

        self.email_tf = tk.Entry(self, font=("Times", 14))
        self.pwd_tf = tk.Entry(self, font=("Times", 14), show="*")
        self.login_btn = tk.Button(self, text="Login", font=("Times", 14), width=15, command=None)

        self.email_tf.grid(row=0, column=1, pady=10, padx=20)
        self.pwd_tf.grid(row=1, column=1, pady=10, padx=20)
        self.login_btn.grid(row=2, column=1, pady=10, padx=20)

class ExpenseTracker(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Expense Tracker")
        self.config(bg="#0B5A81")
        self.resizable(False, False)
        self.geometry("1200x700+100+50")

        self.register_frame = RegisterFrame(self)
        self.login_frame = LoginFrame(self)

        self.register_frame.place(x=700, y=50, anchor="nw")
        self.login_frame.place(x=100, y=50, anchor="nw")


