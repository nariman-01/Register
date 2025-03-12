from tkinter import *
from tkinter import messagebox
import back

win = Tk()
win.geometry("350x250")
win.resizable(0, 0)
win.title("Login Form")
win.configure(bg="#2c3e50")


oj1 = back.Exam("C:/lesson/data.db")
oj1.create_table()
def clear_entries():
    ent_fname.delete(0, END)
    ent_lname.delete(0, END)
    ent_email.delete(0, END)
    ent_pass.delete(0, END)

def insert():
    oj1.insert(ent_fname.get(), ent_lname.get(), ent_email.get(), ent_pass.get())


def sign_up():
    if not ent_email.get() or not ent_pass.get():
        messagebox.showerror("Error", "Please fill in the required fields!")
        return
    
    s = oj1.read()
    for i in s:
        if ent_email.get() == i[3]:
            messagebox.showerror("Error", "This email is already registered!")
            return
    
    insert()
    
 
    messagebox.showinfo("Success", f"Registration successful! Welcome {ent_fname.get()}!")
    

    clear_entries()

def sign_in():
    if not ent_email.get() or not ent_pass.get():
        messagebox.showerror("Error", "Please fill in the required fields!")
        return
    
    s = oj1.read()
    for i in s:
        if ent_email.get() == i[3] and ent_pass.get() == i[4]:
            messagebox.showinfo("Success", f"Welcome {i[1]}!")
            return
    
    messagebox.showerror("Error", "Account not found!")


frame = Frame(win, bg="#34495e", padx=20, pady=20)
frame.pack(pady=20)

Label(frame, text="First Name", bg="#34495e", fg="white", font=("Tahoma", 12)).grid(row=0, column=0, pady=5, sticky=W)
Label(frame, text="Last Name", bg="#34495e", fg="white", font=("Tahoma", 12)).grid(row=1, column=0, pady=5, sticky=W)
Label(frame, text="Email *", bg="#34495e", fg="white", font=("Tahoma", 12)).grid(row=2, column=0, pady=5, sticky=W)
Label(frame, text="Password *", bg="#34495e", fg="white", font=("Tahoma", 12)).grid(row=3, column=0, pady=5, sticky=W)

ent_fname = Entry(frame, font=("Tahoma", 12))
ent_fname.grid(row=0, column=1, pady=5, padx=10)
ent_lname = Entry(frame, font=("Tahoma", 12))
ent_lname.grid(row=1, column=1, pady=5, padx=10)
ent_email = Entry(frame, font=("Tahoma", 12))
ent_email.grid(row=2, column=1, pady=5, padx=10)
ent_pass = Entry(frame, font=("Tahoma", 12), show="*")
ent_pass.grid(row=3, column=1, pady=5, padx=10)


btn_up = Button(win, text="Sign Up", command=sign_up, font=("Tahoma", 12), bg="#27ae60", fg="white", width=12)
btn_up.place(x=200 , y= 210)
btn_in = Button(win, text="Sign In", command=sign_in, font=("Tahoma", 12), bg="#2980b9", fg="white", width=12)
btn_in.place(x=70 , y= 210)

win.mainloop()
