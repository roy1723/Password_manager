from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_number = [random.choice(letters) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list = password_letters + password_number + password_symbols
    random.shuffle(password_list)
    pass1= "".join(password_list)
    password_entry.insert(0, pass1)
    pyperclip.copy(pass1)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    a= web_entry.get()
    b= email_entry.get()
    c= password_entry.get()
    if len(c) == 0 or len(a) == 0 or len(b) == 0:
        messagebox.showerror(title="ERROR", message="You cannot leave the fields empty!")
    else:
        value= messagebox.askokcancel(title= "CONFIRM!", message= "Are you sure, you want to proceed with this data?")
        if value:
            with open("save.txt", "a") as file:
                file.write(f"{a}, {b}, {c}\n")
            web_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("Password Manager")
windows.config(padx= 20, pady= 20)
canvas = Canvas(height=200, width=200,highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0 , column=1)

#label
web_label = Label(text="Website:")
email_label = Label(text="E-mail:")
password_label = Label(text="Password:")
web_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

#entry
web_entry = Entry(width=35)
email_entry = Entry(width=35)
password_entry = Entry(width=21,show= "*")
web_entry.grid(column= 1, row=1, columnspan=2, sticky="EW")
web_entry.focus()
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, string="XyXy@gmail.com")
password_entry.grid(column=1, row=3, sticky= "EW")

#buttons
generate_button = Button(text="Generate Password", command=generate)
generate_button.grid(column=2, row=3, sticky="EW")
add_button = Button(text="Add", width=36, command= save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")
















windows.mainloop()