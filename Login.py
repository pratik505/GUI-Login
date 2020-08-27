from tkinter import *


def registering():
    username_info = username.get()
    email_info = email.get()
    phone_no_info = phone_no.get()
    password_info = password.get()

    user_file = open("users.txt", "a")
    user_file.write(username_info + "\n")
    user_file.write(email_info + "\n")
    user_file.write(phone_no_info + "\n")
    user_file.write(password_info + "\n")
    user_file.close()

    username_entry.delete(0, END)
    email_entry.delete(0, END)
    phone_no_entry.delete(0, END)
    password_entry.delete(0, END)


def logging():
    username_info = username.get()
    password_info = password.get()

    user_file = open("users.txt", "r")

    file_contents = user_file.read()
    contents_list = [x for x in file_contents.split("\n")]

    if (username_info in contents_list) and (password_info in contents_list) and username_info!="" and password_info!="":
        print("Login Success.")
    else:
        error = Tk()
        error.title("Error")
        error.geometry("200x150")

        Label(error, text="").pack()
        Label(error, text="Incorrect Password").pack()
        Label(error, text="Try Again").pack()
        Label(error, text="").pack()

        Button(error, text="OK", width=8, command=quit).pack()

    user_file.close()


def for_register():
    global username
    global email
    global phone_no
    global password
    global username_entry
    global email_entry
    global phone_no_entry
    global password_entry

    screen_register = Toplevel(root)
    screen_register.title("Register")
    screen_register.geometry("400x300")

    username = StringVar()
    email = StringVar()
    phone_no = StringVar()
    password = StringVar()

    Label(screen_register, text="").pack()
    Label(screen_register, text="Please Enter the Details Below:-").pack()
    Label(screen_register, text="").pack()

    Label(screen_register, text="Username").pack()
    username_entry = Entry(screen_register, textvariable=username, width=20)
    username_entry.pack()

    Label(screen_register, text="E-mail").pack()
    email_entry = Entry(screen_register, textvariable=email, width=20)
    email_entry.pack()

    Label(screen_register, text="Phone no.").pack()
    phone_no_entry = Entry(screen_register, textvariable=phone_no, width=20)
    phone_no_entry.pack()

    Label(screen_register, text="Password").pack()
    password_entry = Entry(screen_register, textvariable=password, width=20)
    password_entry.pack()

    Label(screen_register, text="").pack()
    Button(screen_register, text="Register", width=10, command=registering).pack()


def for_login():
    global username
    global password

    username = StringVar()
    password = StringVar()

    screen_login = Toplevel(root)
    screen_login.title("Login")
    screen_login.geometry("400x200")

    Label(screen_login, text="").pack()

    Label(screen_login, text="Username/E-mail").pack()
    username_entry = Entry(screen_login, textvariable=username, width=20)
    username_entry.pack()

    Label(screen_login, text="Password").pack()
    password_entry = Entry(screen_login, textvariable=password, width=20)
    password_entry.pack()

    Label(screen_login, text="").pack()
    Button(screen_login, text="Login", width=10, command=logging).pack()


def main():
    global root
    root = Tk()
    root.title("Student Management System")
    root.geometry("400x200")

    Label(root, text="").pack()
    Label(root, text="").pack()

    login = Button(root, text="Login", width="20", height="2", command=for_login)
    login.pack()

    Label(root, text="").pack()

    register = Button(root, text="Register", width="20", height="2", command=for_register)
    register.pack()

    root.mainloop()


main()
