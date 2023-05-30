import tkinter
from tkinter import *
from PIL import ImageTk,Image,ImageDraw
import os
import sys


def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("670x470+400+100")
    register_screen.minsize(670, 470)
    register_screen.maxsize(670, 470)
    reg_img = Image.open("C:\\Users\\riyam\\PycharmProjects\\MajorProject\\Login_register\\images\\bg17.jpg")
    render = ImageTk.PhotoImage(reg_img)
    img1 = Label(register_screen, image=render)
    img1.image = render
    img1.place(x=-30,y=-160)

    global username
    global password
    global emailid
    global username_entry
    global password_entry
    global emailid_entry
    username = StringVar()
    password = StringVar()
    emailid = StringVar()

    def Reg_btn_hover(e):
        Reg_btn["bg"] = "red"

    def Reg_btn_hover_leave(e):
        Reg_btn["bg"] = "Chartreuse"

    Label(register_screen, text="Please Enter Details Below", width=30, height=1, bg="black",fg="cyan",font=("Bodoni MT", 25, "bold","underline")).pack()
    #Label(register_screen, text="").pack()
    emailid_lable = Label(register_screen, text="Email id", width=15, height=1, bg="black", fg="white", font=("Imprint MT Shadow", 20, "bold"))
    emailid_lable.place(x=200, y=65)
    emailid_entry = Entry(register_screen, textvariable=emailid, highlightthicknes="2", width=30, highlightbackground="white",bg="turquoise")
    emailid_entry.place(x=250, y=100)
    username_lable = Label(register_screen, text="Username ", width=15, height=1, bg="black", fg="white",font=("Imprint MT Shadow", 20, "bold"))
    username_lable.place(x=205, y=150)
    username_entry = Entry(register_screen, textvariable=username, highlightthicknes="2",width=30, highlightbackground="white",bg="turquoise")
    username_entry.place(x=250, y=200)
    password_lable = Label(register_screen, text="Password", width=15, height=1, bg="black", fg="white", font=("Imprint MT Shadow", 20, "bold"))
    password_lable.place(x=205, y=235)
    password_entry = Entry(register_screen, textvariable=password, show='*', highlightthicknes="2",width=30,highlightbackground="white", bg="turquoise")
    password_entry.place(x=250, y=280)
    #Label(register_screen, text="").pack()
    Reg_btn = Button(register_screen, text="REGISTER", width=10, height=1, bg="Chartreuse", fg="black", font=("Orelega One", 20,"bold"),command=register_user)
    Reg_btn.place(x=250, y=330)
    Reg_btn.bind("<Enter>", Reg_btn_hover)
    Reg_btn.bind("<Leave>", Reg_btn_hover_leave)


def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("670x470+400+100")
    login_screen.minsize(670, 470)
    login_screen.maxsize(670, 470)
    log_img = Image.open("C:\\Users\\riyam\\PycharmProjects\\MajorProject\\Login_register\\images\\v915-wit-008_1_1.jpg")
    log_render = ImageTk.PhotoImage(log_img)
    img2 = Label(login_screen, image=log_render)
    img2.image = log_render
    img2.place(x=-5, y=0)

    t2 = Label(login_screen, text="Enter the details below", width=20, height=1, bg="white",fg="black",font=("Bodoni MT", 25,"bold","underline"))
    t2.place(x=150,y=20)
    #Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    usr_lbl = Label(login_screen, text="Username", bg="white",fg="red", font=("Imprint MT Shadow", 20, "bold"))
    usr_lbl.place(x=270, y=80)
    username_login_entry = Entry(login_screen, textvariable=username_verify, width="30",bg="MistyRose2", highlightthicknes="2",highlightbackground="black")
    username_login_entry.place(x=240,y=125)
    #Label(login_screen, text="").pack()
    pwd_lbl = Label(login_screen, text="Password",bg="white",fg="red", font=("Imprint MT Shadow", 20, "bold"))
    pwd_lbl.place(x=270, y=170)
    password_login_entry = Entry(login_screen, textvariable=password_verify,width="30", show='*', bg="MistyRose2",highlightthicknes="2", highlightbackground="black")
    password_login_entry.place(x=240,y=215)
    #Label(login_screen, text="").pack()
    login_btn = Button(login_screen, text="LOGIN", width=10, height=1, bg="sienna1", fg="white",highlightthicknes="3", font=("Orelega One", 17),command=login_verify)
    login_btn.place(x=265,y=265)

    def login_btn_hover(e):
        login_btn["bg"] = "red"

    def login_btn_hover_leave(e):
        login_btn["bg"] = "sienna1"

    login_btn.bind("<Enter>", login_btn_hover)
    login_btn.bind("<Leave>", login_btn_hover_leave)


def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)


    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()

# Designing popup for login success

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100+400+100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=openIda).pack()


def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100+400+100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100+400+100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

def openIda():
    os.system("C:\\Users\\riyam\\PycharmProjects\\MajorProject\\IDA\\ida.py")

# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("670x470+400+100")
    main_screen.minsize(670, 470)
    main_screen.maxsize(670, 470)

    img = ImageTk.PhotoImage(Image.open("C:\\Users\\riyam\\PycharmProjects\\MajorProject\\Login_register\\images\\bg8.jpg"))
    my_label = Label(main_screen, image=img)
    my_label.place(x=0, y=40, relwidth=1, relheight=1,width=700,height=700)
    my_label.pack()

    main_screen.title("Account Login")
    my_label1 = Label(main_screen,text="IDA", bg="black",fg="white", width="10", height="2", font=("Bauhaus 93", 45,))
    my_label1.place(x=40,y=10)
    my_label2 = Label(main_screen, text="Please select your choice", bg="black",fg="BlueViolet", width="20", height="1", font=("Monotype Corsiva", 20,"bold"))
    my_label2.place(x=60,y=110)
    btn1 = Button(text="Login", fore="black", bg="Chartreuse", height="1", width="20", font=("Orelega One", 20, "bold"), command=login)
    btn1.place(x=45, y=200)
    btn2 = Button(text="Register", fore="black", bg="Chartreuse", height="1", width="20",font=("Orelega One", 20, "bold"), command=register)
    btn2.place(x=45, y=300)

    def btn1_hover(e):
        btn1["bg"] = "red"

    def btn1_hover_leave(e):
        btn1["bg"] = "Chartreuse"

    def btn2_hover(e):
        btn2["bg"] = "red"

    def btn2_hover_leave(e):
        btn2["bg"] = "Chartreuse"

    btn1.bind("<Enter>", btn1_hover)
    btn1.bind("<Leave>", btn1_hover_leave)
    btn2.bind("<Enter>", btn2_hover)
    btn2.bind("<Leave>", btn2_hover_leave)

    main_screen.mainloop()


main_account_screen()