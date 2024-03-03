import tkinter
from tkinter import messagebox
window=tkinter.Tk()
window.title("Login Form By Ashmit ")
window.geometry("600x500")

def login():
    username="ashmitdubey"
    password="12345"
    if username_entry.get()==username and password_entry.get()==password:
      messagebox.showinfo(title="Login success",message="you successfully logged in.")

    else:
        messagebox.showinfo(title="Login Fail",message="ERROR")

frame=tkinter.Frame()


#creating widgets
login_label=tkinter.Label(frame,text="Login Form",fg="#00FFFF",font=("Times New Roman",30))
username_label=tkinter.Label(frame,text="Username",fg="#DAA520",font=("Times New Roman",15))
username_entry=tkinter.Entry(frame)
password_entry=tkinter.Entry(frame,show="*")
password_label=tkinter.Label(frame,text="Password",fg="#DC143C",font=("Times New Roman",15))
login_button=tkinter.Button(frame,text="Login",fg="#4B0082",font=("Arial",15),command=login)

#using pack,place or grid for placing
login_label.grid(row=0,column=0,columnspan=2, sticky="news",pady=40)
username_label.grid(row=1,column=0,pady=20,padx=5)
password_label.grid(row=2,column=0,pady=20,padx=5)
username_entry.grid(row=1,column=1)
password_entry.grid(row=2,column=1)
login_button.grid(row=3,column=0,columnspan=2,pady=30)


frame.pack()

window.mainloop()