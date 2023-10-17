# -*- coding: utf-8 -*-

import string
from random import randint, choice
from tkinter import *


def generate_password():
    password_min = 6
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    

#Settings
window = Tk()
window.title("Generateur password")
window.geometry("720x480")
window.minsize(480, 360)
window.iconbitmap("logo.ico")
window.config(background='#d1a1ff')


#Frame 1
frame= Frame(window, bg="#d1a1ff")


#Image
width = 300
height=300
image= PhotoImage(file="mot-de-passe.png").zoom(35).subsample(32)
canvas=Canvas(frame, width=width, height=height, bg="#d1a1ff", bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)


#Sous-boite
right_frame = Frame(frame, bg="#d1a1ff")


#Titre
label_title = Label(right_frame, text="Mot de passe", font=("Helvetica", 20), bg='#d1a1ff', fg="white")
label_title.pack()


#Champs/entrée/input
password_entry = Entry(right_frame, font=("Helvetica", 20), bg='#d1a1ff', fg="white")
password_entry.pack()


#Boutton
generate_password_button = Button(right_frame, text="Generer", font=("Helvetica", 20), bg='#d1a1ff', fg="white", command=generate_password)
generate_password_button.pack(fill=X)


#Sous-boite a droite
right_frame.grid(row=0, column=1, sticky=W)


#Afficher
frame.pack(expand=YES)

#Menu
menu_bar = Menu(window)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

window.config(menu=menu_bar)


window.mainloop()