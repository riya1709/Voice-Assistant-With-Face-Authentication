import os
import subprocess

from Detector import main_app
from create_classifier import train_classifer
from create_dataset import start_capture
from tkinter import *
import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox,PhotoImage
#from PIL import ImageTk, Image
#from gender_prediction import emotion,ageAndgender
names = set()


class MainUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        global names
        with open("C:\\Users\\riyam\\PycharmProjects\\MajorProject\\FaceRecognition\\nameslist.txt", "r") as f:
            x = f.read()
            z = x.rstrip().split(" ")
            for i in z:
                names.add(i)
        self.title_font = tkfont.Font(family='Orelega One', size=20, weight="bold")
        self.button_font = tkfont.Font(family='Texturina 24pt Black',size=13,weight="bold")
        self.title("Face Recognizer")
        self.resizable(False, False)
        self.geometry("550x280+450+150")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.active_name = None
        container = tk.Frame(self)
        container.grid(sticky="nsew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
            frame = self.frames[page_name]
            frame.tkraise()

    def on_closing(self):

        if messagebox.askokcancel("Quit", "Are you sure?"):
            global names
            f =  open("C:\\Users\\riyam\\PycharmProjects\\MajorProject\\FaceRecognition\\nameslist.txt", "a+")
            for i in names:
                    f.write(i+" ")
            self.destroy()


class StartPage(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            #load = Image.open("homepagepic.png")
            #load = load.resize((250, 250), Image.ANTIALIAS)

            render = PhotoImage(file='C:\\Users\\riyam\\PycharmProjects\\MajorProject\\FaceRecognition\\homepagepic.png')
            img = tk.Label(self, image=render)
            img.image = render
            img.grid(row=0, column=1, rowspan=4, sticky="nsew")
            label = tk.Label(self, text="        Home Page        ", font=self.controller.title_font,fg="cyan4")
            label.grid(row=0, sticky="ew")
            button1 = tk.Button(self, text="   Add a User  ", fg="black", bg="PaleGreen3", font=self.controller.button_font,command=lambda: self.controller.show_frame("PageOne"))
            button2 = tk.Button(self, text="   Check a User  ", fg="black", bg="PaleGreen3",font=self.controller.button_font,command=lambda: self.controller.show_frame("PageTwo"))
            button3 = tk.Button(self, text="Quit", fg="black", bg="tomato3",font=self.controller.button_font, command=self.on_closing)
            button1.grid(row=1, column=0, ipady=3, ipadx=7)
            button2.grid(row=2, column=0, ipady=3, ipadx=2)
            button3.grid(row=3, column=0, ipady=3, ipadx=32)

            def button1_hover(e):
                button1["bg"] = "chartreuse2"

            def button1_hover_leave(e):
                button1["bg"] = "PaleGreen3"

            def button2_hover(e):
                button2["bg"] = "chartreuse2"

            def button2_hover_leave(e):
                button2["bg"] = "PaleGreen3"

            def button3_hover(e):
                button3["bg"] = "Red"

            def button3_hover_leave(e):
                button3["bg"] = "tomato3"

            button1.bind("<Enter>", button1_hover)
            button1.bind("<Leave>", button1_hover_leave)
            button2.bind("<Enter>", button2_hover)
            button2.bind("<Leave>", button2_hover_leave)
            button3.bind("<Enter>", button3_hover)
            button3.bind("<Leave>", button3_hover_leave)


        def on_closing(self):
            if messagebox.askokcancel("Quit", "Are you sure?"):
                global names
                with open("C:\\Users\\riyam\\PycharmProjects\\MajorProject\\FaceRecognition\\nameslist.txt", "w") as f:
                    for i in names:
                        f.write(i + " ")
                self.controller.destroy()


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        tk.Label(self, text="Enter the name", fg="#263942", font='Cambria 14 bold').grid(row=0, column=0, pady=10, padx=5)
        self.user_name = tk.Entry(self, borderwidth=3, bg="LightSkyBlue1", font='Perpetua')
        self.user_name.grid(row=0, column=1, pady=10, padx=10)
        self.buttoncanc = tk.Button(self, text="Cancel", bg="tomato3", fg="#263942", font=self.controller.button_font,command=lambda: controller.show_frame("StartPage"))
        self.buttonext = tk.Button(self, text="Next", fg="#ffffff", bg="PaleGreen3", font=self.controller.button_font,command=self.start_training)
        self.buttoncanc.grid(row=1, column=0, pady=10, ipadx=5, ipady=4)
        self.buttonext.grid(row=1, column=1, pady=10, ipadx=5, ipady=4)

        def buttoncanc_hover(e):
            self.buttoncanc["bg"] = "red"

        def buttoncanc_hover_leave(e):
            self.buttoncanc["bg"] = "tomato3"

        def buttonext_hover(e):
            self.buttonext["bg"] = "chartreuse2"

        def buttonext_hover_leave(e):
            self.buttonext["bg"] = "PaleGreen3"

        self.buttoncanc.bind("<Enter>", buttoncanc_hover)
        self.buttoncanc.bind("<Leave>", buttoncanc_hover_leave)
        self.buttonext.bind("<Enter>", buttonext_hover)
        self.buttonext.bind("<Leave>", buttonext_hover_leave)

    def start_training(self):
        global names
        if self.user_name.get() == "None":
            messagebox.showerror("Error", "Name cannot be 'None'")
            return
        elif self.user_name.get() in names:
            messagebox.showerror("Error", "User already exists!")
            return
        elif len(self.user_name.get()) == 0:
            messagebox.showerror("Error", "Name cannot be empty!")
            return
        name = self.user_name.get()
        names.add(name)
        self.controller.active_name = name
        self.controller.frames["PageTwo"].refresh_names()
        self.controller.show_frame("PageThree")


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global names
        self.controller = controller
        tk.Label(self, text="Select user", fg="#263942", font='Cambria 14 bold').grid(row=0, column=0, padx=10, pady=10)
        self.buttoncanc = tk.Button(self, text="Cancel",font=self.controller.button_font, command=lambda: controller.show_frame("StartPage"), bg="tomato3", fg="#263942")
        self.menuvar = tk.StringVar(self)
        self.dropdown = tk.OptionMenu(self, self.menuvar, *names)
        self.dropdown.config(bg="LightSkyBlue1")
        self.dropdown["menu"].config(bg="LightSkyBlue1")
        self.buttonext = tk.Button(self, text="Next",font=self.controller.button_font, command=self.nextfoo, fg="#ffffff", bg="PaleGreen3")
        self.dropdown.grid(row=0, column=1, ipadx=8, padx=10, pady=10)
        self.buttoncanc.grid(row=1, ipadx=5, ipady=4, column=0, pady=10)
        self.buttonext.grid(row=1, ipadx=5, ipady=4, column=1, pady=10)

        def buttoncanc_hover(e):
            self.buttoncanc["bg"] = "red"

        def buttoncanc_hover_leave(e):
            self.buttoncanc["bg"] = "tomato3"

        def buttonext_hover(e):
            self.buttonext["bg"] = "chartreuse2"

        def buttonext_hover_leave(e):
            self.buttonext["bg"] = "PaleGreen3"

        self.buttoncanc.bind("<Enter>", buttoncanc_hover)
        self.buttoncanc.bind("<Leave>", buttoncanc_hover_leave)
        self.buttonext.bind("<Enter>", buttonext_hover)
        self.buttonext.bind("<Leave>", buttonext_hover_leave)

    def nextfoo(self):
        if self.menuvar.get() == "None":
            messagebox.showerror("ERROR", "Name cannot be 'None'")
            return
        self.controller.active_name = self.menuvar.get()
        self.controller.show_frame("PageFour")

    def refresh_names(self):
        global names
        self.menuvar.set('')
        self.dropdown['menu'].delete(0, 'end')
        for name in names:
            self.dropdown['menu'].add_command(label=name, command=tk._setit(self.menuvar, name))

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.numimglabel = tk.Label(self, text="Number of images captured = 0", font='Cambria 14 bold', fg="SlateBlue4")
        self.numimglabel.grid(row=0, column=0, columnspan=2, sticky="ew", pady=10)
        self.capturebutton = tk.Button(self, text="Capture Data Set",font=self.controller.button_font, fg="#ffffff", bg="medium turquoise", command=self.capimg)
        self.trainbutton = tk.Button(self, text="Train The Model",font=self.controller.button_font, fg="#ffffff", bg="medium turquoise",command=self.trainmodel)
        self.capturebutton.grid(row=1, column=0, ipadx=5, ipady=4, padx=10, pady=20)
        self.trainbutton.grid(row=1, column=1, ipadx=5, ipady=4, padx=10, pady=20)

        def capturebutton_hover(e):
            self.capturebutton["bg"] = "dodger blue"

        def capturebutton_hover_leave(e):
            self.capturebutton["bg"] = "medium turquoise"

        def trainbutton_hover(e):
            self.trainbutton["bg"] = "dodger blue"

        def trainbutton_hover_leave(e):
            self.trainbutton["bg"] = "medium turquoise"

        self.capturebutton.bind("<Enter>", capturebutton_hover)
        self.capturebutton.bind("<Leave>", capturebutton_hover_leave)
        self.trainbutton.bind("<Enter>", trainbutton_hover)
        self.trainbutton.bind("<Leave>", trainbutton_hover_leave)

    def capimg(self):
        self.numimglabel.config(text=str("Captured Images = 0 "))
        messagebox.showinfo("INSTRUCTIONS", "We will Capture 300 pic of your Face.")
        x = start_capture(self.controller.active_name)
        self.controller.num_of_images = x
        self.numimglabel.config(text=str("Number of images captured = "+str(x)))

    def trainmodel(self):
        if self.controller.num_of_images < 300:
            messagebox.showerror("ERROR", "No enough Data, Capture at least 300 images!")
            return
        train_classifer(self.controller.active_name)
        messagebox.showinfo("SUCCESS", "The modele has been successfully trained!")
        self.controller.show_frame("PageFour")


class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Face Recognition", font=self.controller.title_font,fg="cyan4")
        label.grid(row=0,column=0, sticky="ew")
        button1 = tk.Button(self, text="Face Recognition", command=self.openwebcam, font=self.controller.button_font,fg="#ffffff", bg="dodger blue")
        button4 = tk.Button(self, text="Go to Home Page", font=self.controller.button_font,command=lambda: self.controller.show_frame("StartPage"), bg="white", fg="#263942")
        button1.grid(row=1,column=0, sticky="ew", ipadx=5, ipady=4, padx=10, pady=10)
        button4.grid(row=1,column=1, sticky="ew", ipadx=5, ipady=4, padx=10, pady=10)

        def button1_hover(e):
            button1["bg"] = "blue violet"

        def button1_hover_leave(e):
            button1["bg"] = "dodger blue"

        def button4_hover(e):
            button4["bg"] = "red"

        def button4_hover_leave(e):
            button4["bg"] = "white"

        button1.bind("<Enter>", button1_hover)
        button1.bind("<Leave>", button1_hover_leave)
        button4.bind("<Enter>", button4_hover)
        button4.bind("<Leave>", button4_hover_leave)

    def openwebcam(self):
        main_app(self.controller.active_name)
    #def gender_age_pred(self):
     #  ageAndgender()
    #def emot(self):
     #   emotion()



app = MainUI()
app.iconphoto(False, tk.PhotoImage(file='C:\\Users\\riyam\\PycharmProjects\\MajorProject\\FaceRecognition\\icon.ico'))
app.mainloop()
#subprocess.call(" python C:\\Users\\riyam\\PycharmProjects\\MajorProject\\IDA\\ida.py", shell=True)
#os.system("C:\\Users\\riyam\\PycharmProjects\\MajorProject\\IDA\\ida.py")