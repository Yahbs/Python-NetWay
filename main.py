# -*- coding: utf-8 -*-

from tkinter import *
import socket
import threading
import time
import datetime
import hashlib
import mysql.connector
from mysql.connector import Error

def getWindow():

    # Fenêtre
    window = Tk()
    window.title("NetWay Management")
    window.geometry(("1080x600"))
    window.minsize(1080,600)
    window.iconbitmap("./Pictures/netway_icon.ico")
    window.config(background="#cce6aa")

    # Les frames
    frameLog = Frame(window, bg="#cce6aa")
    frameLogged = Frame(window, bg="black")

    # Titre
    label_title = Label(frameLog, text="Netway Management", font=("Calibri", 40), bg="#cce6aa", fg="white")
    label_title.pack(expand=YES, side=TOP)

    # Images
    width = 300
    height = 300
    img = PhotoImage(file="./Pictures/netway_img.png")
    canvas = Canvas(frameLog, width=width, height=height, bg="#cce6aa", bd=0, highlightthickness=0)
    canvas.create_image(width/2, height/2, image=img)
    canvas.pack(expand=YES, side=BOTTOM)

    # Champs login
    login_entry = Entry(frameLog, font=("Calibri", 25), bg="white", fg="#9bb07f")
    login_entry.insert(0, "Baptiste")
    login_entry.pack()
    
    # Champs Mot de passe
    passwd_entry = Entry(frameLog, font=("Calibri", 25), bg="white", fg="#9bb07f")
    passwd_entry.insert(0, "ESGIProjet123!")
    passwd_entry.config(show="*")
    passwd_entry.pack()

    def logSession(login_entry, passwd_entry):
    
        # Récuperation des entrées utilisateurs
        login_value = login_entry.get()
        passwd_value = passwd_entry.get()
        
        # credential du serveur de connexion
        ip = "192.168.1.53"
        db = "NetWay_Management"
        
        # Connexion à la base de donnée
        try :
            connexion = mysql.connector.connect(host=ip, database=db, user=login_value, password=passwd_value)
            
            if connexion.is_connected():
                logged_title = Label(frameLogged, text="Bienvenue" + login_value + "!", font=("Calibri", 40), bg="black", fg="white")
                logged_title.pack()
                
        
        except Error as e:
            print(e)
            
        finally:
             if connexion is not None and connexion.is_connected():
              connexion.close()
                
        

    # Bouton Connexion
    log_button = Button(frameLog, text="Se connecter", font=("Calibri", 25), bg="white", fg="#9bb07f", command = logSession(login_entry, passwd_entry))
    log_button.pack(pady=25, fill=X)


    # Ajout de la frameLog
    frameLog.pack(expand=YES)

    # Afficher la fenêtre
    window.mainloop()

  
    

getWindow()




    