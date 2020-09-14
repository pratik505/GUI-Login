from tkinter import Tk, Toplevel, Label, Button, Entry, mainloop, END, StringVar


def destroy_registersuccess_messagebox():
    register_done.destroy()
    screen_register.destroy()


def destroy_registerfail_messagebox():
    register_error.destroy()


def destroy_loginsuccess_messagebox():
    login_done.destroy()
    screen_login.destroy()


def destroy_loginerror_messagebox():
    login_error.destroy()


def register_fail():
    # Message box for failure of login.

    global register_error

    register_error = Toplevel(screen_register)
    register_error.title("ERROR")
    register_error.geometry("200x150")

    Label(register_error, text="").pack()
    Label(register_error, text="Username Already Exists").pack()
    Label(register_error, text="").pack()

    Button(register_error, text="OK", width=8, command=destroy_registerfail_messagebox).pack()


def register_success():
    # Message box for success in registering.

    global register_done

    register_done = Toplevel(screen_register)
    register_done.title("REGISTERED")
    register_done.geometry("200x150")

    Label(register_done, text="").pack()
    Label(register_done, text="Registration Success!!!").pack()
    Label(register_done, text="").pack()

    Button(register_done, text="OK", width=8, command=destroy_registersuccess_messagebox).pack()


def login_fail():
    # Message box for failure of login.

    global login_error

    login_error = Toplevel(screen_login)
    login_error.title("Error")
    login_error.geometry("200x150")

    Label(login_error, text="").pack()
    Label(login_error, text="Incorrect Password").pack()
    Label(login_error, text="Try Again").pack()
    Label(login_error, text="").pack()

    Button(login_error, text="OK", width=8, command=destroy_loginerror_messagebox).pack()


def login_success():
    # Message for success of login.

    global login_done

    login_done = Toplevel(screen_login)
    login_done.title("Login Success!!!")
    login_done.geometry("200x150")

    Label(login_done, text="").pack()
    Label(login_done, text="Success").pack()
    Label(login_done, text="").pack()

    Button(login_done, text="OK", width=8, command=destroy_loginsuccess_messagebox).pack()


def registering():
    # Functioning for registering.

    username_info = username.get()
    email_info = email.get()
    phone_no_info = phone_no.get()
    password_info = password.get()
    count1 = 0

    user_file = open("users.txt", "r")
    for line in user_file:
        userinfo_list = list(line.split())
        if (username == "" or email_info == "" or phone_no_info == "" or password_info == "") or (userinfo_list[0] == username_info):
            count1 += 1
    user_file.close

    if count1 == 0:
        user_file = open("users.txt", "a")
        user_file.write(username_info + "\t")
        user_file.write(email_info + "\t")
        user_file.write(phone_no_info + "\t")
        user_file.write(password_info)
        user_file.write("\n")
        user_file.close
        register_success()
    else:
        register_fail()
    

    username_entry.delete(0, END)
    email_entry.delete(0, END)
    phone_no_entry.delete(0, END)
    password_entry.delete(0, END)


def logging():
    # Functioning for logging.

    username_info = username.get()
    password_info = password.get()
    count2 = 0

    user_file = open("users.txt", "r")
    for line in user_file:
        contents_list = line.split()
        if ((username_info=="") or (password_info=="")):
            count2 += 1
        elif ((username_info != contents_list[0]) and (password_info != contents_list[3])):
            count2 += 1
        else:
            count2 = 0
    user_file.close()

    if count2 < 1:
        login_success()
    else:
        login_fail()


def for_register():
    # Creating the Register interface.

    global screen_register
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
    password_entry = Entry(screen_register, textvariable=password, width=20, show="*")
    password_entry.pack()

    Label(screen_register, text="").pack()
    Button(screen_register, text="Register", width=10, command=registering).pack()


def for_login():
    # Creating the Login interface.

    global screen_login
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
    password_entry = Entry(screen_login, textvariable=password, width=20, show="*")
    password_entry.pack()

    Label(screen_login, text="").pack()
    Button(screen_login, text="Login", width=10, command=logging).pack()


def main():
    # Creating the initial interface.

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
