from tkinter import *
import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk

#fonction global aux 2 modes
def image_joueur_pierre():                                                                              #change image joueur -> image pierre
    global render_joueur_pierre
    global load_joueur_pierre
    image_joueur_pierre = Label(zone_4, image=render_joueur_pierre,bg='#FFFFFF').grid(row=3,column=0,columnspan=1)


def image_joueur_feuille():                                                                              #change image joueur -> image feuille
    global render_joueur_feuille
    global load_joueur_feuille
    image_joueur_feuille = Label(zone_4, image=render_joueur_feuille,bg='#FFFFFF').grid(row=3,column=0,columnspan=1)


def image_joueur_ciseaux():                                                                              #change image joueur -> image ciseaux
    global render_joueur_ciseaux
    global load_joueur_ciseaux
    image_joueur_ciseaux = Label(zone_4, image=render_joueur_ciseaux,bg='#FFFFFF').grid(row=3,column=0,columnspan=1)

"""Début fonctions propre au mode libre"""
def valider():
    """donne le gagnant de chaque tour"""
    global zone_1
    global zone_2
    global zone_3
    global zone_4
    global zone_5
    global zone_6
    global zone_7
    global zone_8
    global zone_9
    global zone_10
    global zone_11
    global var
    from random import randint
    action_ordinateur = randint(1,3)
    action_joueur = var.get()
    global load_joueur_pierre
    global load_joueur_feuille
    global load_joueur_ciseaux
    global load_ordinateur_pierre
    global load_ordinateur_feuille
    global load_ordinateur_ciseaux
    global render_ordinateur_feuille
    global render_ordinateur_pierre
    global render_ordinateur_ciseaux
    global render_joueur_pierre
    global render_joueur_feuille
    global render_joueur_ciseaux
    global bou_valider
    bou_valider = Button(zone_9,text = 'VALIDER',font =('Arial 10 bold'),width=0,command = valider,state = DISABLED).grid(row=8,column=0,rowspan=2)    #grise le bouton valider
    global bou_rejouer
    bou_rejouer= Button(zone_9,text="REJOUER",font =('Arial 10 bold'),command=rejouer,state=NORMAL).grid(row=8,column=1,rowspan=2) #rend de nouveau accessible le bouton rejouer
    global border_color_joueur
    global border_color_ordinateur
    global compteur_ordinateur
    global compteur_joueur
    global pt_joueur
    global pt_ordinateur
    global zone_2
    if action_joueur == 1 and action_ordinateur == 2 : #victoire ordnateur
        border_color_ordinateur = Frame(zone_4, bg= '#1FFF00',height=60,width=60).grid(row=3,column=2,columnspan=1)             #couleur bordure gagnant/vert
        render_ordinateur_feuille = ImageTk.PhotoImage(load_ordinateur_feuille)
        image_ordinateur_feuille = Label(zone_4, image=render_ordinateur_feuille,bg='#FFFFFF').grid(row=3,column=2,columnspan=1)#image ordinateur
        border_color_joueur = Frame(zone_4, bg= '#FF0000',height=60,width=60).grid(row=3,column=0,columnspan=1)                 #couleur bordure perdant/rouge
        render_joueur_pierre = ImageTk.PhotoImage(load_joueur_pierre)
        image_joueur_pierre = Label(zone_4, image=render_joueur_pierre,bg='#FFFFFF').grid(row=3,column=0,columnspan=1)          #image joueur
        compteur_ordinateur+=1                                                                                                  #compteur ordinateur
        text_compteur_joueur = """Pt(s) JOUEUR :""",compteur_joueur
        pt_joueur =Label(zone_3, text= text_compteur_joueur,bg='#7DCEA0',fg='#FFFFFF',font =('Arial 8 bold')).grid(row=2,column=0,columnspan=1) #actualisation des compteurs afficher
        text_compteur_ordinateur = """Pt(s) ORDINATEUR :""",compteur_ordinateur
        pt_ordinateur=Label(zone_3, text= text_compteur_ordinateur,fg='#FFFFFF',bg='#7DCEA0',font =('Arial 8 bold')).grid(row=2,column=2,columnspan=1)
        Label(zone_2,text=" PERDU ",bg='#FFFFFF',font =('Arial 11 bold'),fg='#FF0000').grid(row=1,column=0,columnspan=3)

    elif action_ordinateur == 1 and action_joueur == 2 : #victoire joueur
        border_color_ordinateur = Frame(zone_4, bg= '#FF0000',height=60,width=60).grid(row=3,column=2,columnspan=1)
        render_ordinateur_pierre = ImageTk.PhotoImage(load_ordinateur_pierre)
        image_ordinateur_pierre = Label(zone_4, image=render_ordinateur_pierre,bg='#FFFFFF').grid(row=3,column=2,columnspan=1)
        border_color_joueur = Frame(zone_4, bg= '#1FFF00',height=60,width=60).grid(row=3,column=0,columnspan=1)
        render_joueur_feuille = ImageTk.PhotoImage(load_joueur_feuille)
        image_joueur_feuille = Label(zone_4, image=render_joueur_feuille,bg='#FFFFFF').grid(row=3,column=0,columnspan=1)
        compteur_joueur+=1
        text_compteur_joueur = """Pt(s) JOUEUR :""",compteur_joueur
        pt_joueur =Label(zone_3, text= text_compteur_joueur,bg='#7DCEA0',fg='#FFFFFF',font =('Arial 8 bold')).grid(row=2,column=0,columnspan=1)
        text_compteur_ordinateur = """Pt(s) ORDINATEUR :""",compteur_ordinateur
        pt_ordinateur=Label(zone_3, text= text_compteur_ordinateur,bg='#7DCEA0',fg='#FFFFFF',font =('Arial 8 bold')).grid(row=2,column=2,columnspan=1)
        Label(zone_2,text="GAGNER",bg='#FFFFFF',font =('Arial 11 bold'),fg='#1FFF00').grid(row=1,column=0,columnspan=3)

    elif action_joueur == 2 and action_ordinateur == 3 : #victoire ordnateur
        border_color_ordinateur = Frame(zone_4, bg= '#1FFF00',height=60,width=60).grid(row=3,column=2,columnspan=1)
        render_ordinateur_ciseaux = ImageTk.PhotoImage(load_ordinateur_ciseaux)
        image_ordinateur_ciseaux = Label(zone_4, image=render_ordinateur_ciseaux,bg='#FFFFFF').grid(row=3,column=2,columnspan=1)
        border_color_joueur = Frame(zone_4, bg= '#FF0000',height=60,width=60).grid(row=3,column=0,columnspan=1)
        render_joueur_feuille = ImageTk.PhotoImage(load_joueur_feuille)
        image_joueur_feuille = Label(zone_4, image=render_joueur_feuille,bg='#FFFFFF').grid(row=3,column=0,columnspan=1)
        compteur_ordinateur+=1
        text_compteur_joueur = """Pt(s) JOUEUR :""",compteur_joueur
        pt_joueur =Label(zone_3, text= text_compteur_joueur,bg='#7DCEA0',fg='#FFFFFF',font =('Arial 8 bold')).grid(row=2,column=0,columnspan=1)
        text_compteur_ordinateur = """Pt(s) ORDINATEUR :""",compteur_ordinateur
        pt_ordinateur=Label(zone_3, text= text_compteur_ordinateur,bg='#7DCEA0',fg='#FFFFFF',font =('Arial 8 bold')).grid(row=2,column=2,columnspan=1)
        Label(zone_2,text=" PERDU ",bg='#FFFFFF',font =('Arial 11 bold'),fg='#FF0000').grid(row=1,column=0,columnspan=3)

    elif action_ordinateur == 2 and action_joueur == 3 : #victoire joueur
        border_color_ordinateur = Frame(zone_4, bg= '#FF0000',height=60,width=60).grid(row=3,column=2,columnspan=1)
        render_ordinateur_feuille = ImageTk.PhotoImage(load_ordinateur_feuille)
        image_ordinateur_feuille = Label(zone_4, image=render_ordinateur_feuille,bg='#FFFFFF').grid(row=3,column=2,columnspan=1)
        border_color_joueur = Frame(zone_4, bg= '#1FFF00',height=60,width=60).grid(row=3,column=0,columnspan=1)
        render_joueur_ciseaux = ImageTk.PhotoImage(load_joueur_ciseaux)
        image_joueur_ciseaux = Label(zone_4, image=render_joueur_ciseaux,bg='#FFFFFF').grid(row=3,column=0,columnspan=1)
        compteur_joueur+=1
        text_compteur_joueur = """Pt(s) JOUEUR :""",compteur_joueur
        pt_joueur =Label(zone_3, text= text_compteur_joueur,bg='#7DCEA0',fg='#FFFFFF',font =('Arial 8 bold')).grid(row=2,column=0,columnspan=1)
        text_compteur_ordinateur = """Pt(s) ORDINATEUR :""",compteur_ordinateur
        pt_ordinateur=Label(zone_3, text= text_compteur_ordinateur,bg='#7DCEA0',fg='#FFFFFF',font =('Arial 8 bold')).grid(row=2,column=2,columnspan=1)
        Label(zone_2,text="GAGNER",bg='#FFFFFF',font =('Arial 11 bold'),fg='#1FFF00').grid(row=1,column=0,columnspan=3)

    elif action_joueur == 3 and action_ordinateur == 1 : #victoire ordnateur
        border_color_ordinateur = Frame(zone_4, bg= '#1FFF00',height=60,width=60).grid(row=3,column=2,columnspan=1)
        load_ordinateur_pierre = Image.open("C:/Users/Elève/Desktop/icones shifumi/icons8-poing-serré-50.png")
        render_ordinateur_pierre = ImageTk.PhotoImage(load_ordinateur_pierre)
        image_ordinateur_pierre = Label(zone_4, image=render_ordinateur_pierre,bg='#FFFFFF').grid(row=3,column=2,columnspan=1)
        border_color_joueur = Frame(zone_4, bg= '#FF0000',height=60,width=60).grid(row=3,column=0,columnspan=1)
        render_joueur_ciseaux = ImageTk.PhotoImage(load_joueur_ciseaux)
        image_joueur_ciseaux = Label(zone_4, image=render_joueur_ciseaux,bg='#FFFFFF').grid(row=3,column=0,columnspan=1)
        compteur_ordinateur+=1
        text_compteur_joueur = """Pt(s) JOUEUR :""",compteur_joueur
        pt_joueur =Label(zone_3, text= text_compteur_joueur,bg='#7DCEA0',fg='#FFFFFF',font =('Arial 8 bold')).grid(row=2,column=0,columnspan=1)
        text_compteur_ordinateur = """Pt(s) ORDINATEUR :""",compteur_ordinateur
        pt_ordinateur=Label(zone_3, text= text_compteur_ordinateur,bg='#7DCEA0',fg='#FFFFFF',font =('Arial 8 bold')).grid(row=2,column=2,columnspan=1)
        Label(zone_2,text=" PERDU ",bg='#FFFFFF',font =('Arial 11 bold'),fg='#FF0000').grid(row=1,column=0,columnspan=3)

    elif action_ordinateur == 3 and action_joueur == 1 : #victoire joueur
        border_color_ordinateur = Frame(zone_4, bg= '#FF0000',height=60,width=60).grid(row=3,column=2,columnspan=1)
        render_ordinateur_ciseaux = ImageTk.PhotoImage(load_ordinateur_ciseaux)
        image_ordinateur_ciseaux = Label(zone_4, image=render_ordinateur_ciseaux,bg='#FFFFFF').grid(row=3,column=2,columnspan=1)
        border_color_joueur = Frame(zone_4, bg= '#1FFF00',height=60,width=60).grid(row=3,column=0,columnspan=1)
        render_joueur_pierre = ImageTk.PhotoImage(load_joueur_pierre)
        image_joueur_pierre = Label(zone_4, image=render_joueur_pierre,bg='#FFFFFF').grid(row=3,column=0,columnspan=1)
        compteur_joueur+=1
        text_compteur_joueur = """Pt(s) JOUEUR :""",compteur_joueur
        pt_joueur =Label(zone_3, text= text_compteur_joueur,bg='#7DCEA0',fg='#FFFFFF',font =('Arial 8 bold')).grid(row=2,column=0,columnspan=1)
        text_compteur_ordinateur = """Pt(s) ORDINATEUR :""",compteur_ordinateur
        pt_ordinateur=Label(zone_3, text= text_compteur_ordinateur,bg='#7DCEA0',fg='#FFFFFF',font =('Arial 8 bold')).grid(row=2,column=2,columnspan=1)
        Label(zone_2,text="GAGNER",bg='#FFFFFF',font =('Arial 11 bold'),fg='#1FFF00').grid(row=1,column=0,columnspan=3)

    elif action_joueur == 1 and action_ordinateur == 1 : #egalite
        border_color_ordinateur = Frame(zone_4, bg= '#686968',height=60,width=60).grid(row=3,column=2,columnspan=1)
        render_ordinateur_pierre = ImageTk.PhotoImage(load_ordinateur_pierre)
        image_ordinateur_pierre = Label(zone_4, image=render_ordinateur_pierre,bg='#FFFFFF').grid(row=3,column=2,columnspan=1)
        border_color_joueur = Frame(zone_4, bg= '#686968',height=60,width=60).grid(row=3,column=0,columnspan=1)
        render_joueur_pierre = ImageTk.PhotoImage(load_joueur_pierre)
        image_joueur_pierre = Label(zone_4, image=render_joueur_pierre,bg='#FFFFFF').grid(row=3,column=0,columnspan=1)
        text_compteur_joueur = """Pt(s) JOUEUR :""",compteur_joueur
        pt_joueur =Label(zone_3, text=text_compteur_joueur,bg='#7DCEA0',fg='#FFFFFF',font =('Arial 8 bold')).grid(row=2,column=0,columnspan=1)
        text_compteur_ordinateur = """Pt(s) ORDINATEUR :""",compteur_ordinateur
        pt_ordinateur=Label(zone_3, text=text_compteur_ordinateur,bg='#7DCEA0',fg='#FFFFFF',font =('Arial 8 bold')).grid(row=2,column=2,columnspan=1)
        Label(zone_2,text="EGALITE",bg='#FFFFFF',font =('Arial 11 bold'),fg='#686968').grid(row=1,column=0,columnspan=3)

    elif action_joueur == 2 and action_ordinateur == 2 : #egalite
        border_color_ordinateur = Frame(zone_4, bg= '#686968',height=60,width=60).grid(row=3,column=2,columnspan=1)
        render_ordinateur_feuille = ImageTk.PhotoImage(load_ordinateur_feuille)
        image_ordinateur_feuille = Label(zone_4, image=render_ordinateur_feuille,bg='#FFFFFF').grid(row=3,column=2,columnspan=1)
        border_color_joueur = Frame(zone_4, bg= '#686968',height=60,width=60).grid(row=3,column=0,columnspan=1)
        render_joueur_feuille = ImageTk.PhotoImage(load_joueur_feuille)
        image_joueur_feuille = Label(zone_4, image=render_joueur_feuille,bg='#FFFFFF').grid(row=3,column=0,columnspan=1)
        text_compteur_joueur = """Pt(s) JOUEUR :""",compteur_joueur
        pt_joueur =Label(zone_3, text=text_compteur_joueur,bg='#7DCEA0',fg='#FFFFFF',font =('Arial 8 bold')).grid(row=2,column=0,columnspan=1)
        text_compteur_ordinateur = """Pt(s) ORDINATEUR :""",compteur_ordinateur
        pt_ordinateur=Label(zone_3, text= text_compteur_ordinateur,bg='#7DCEA0',fg='#FFFFFF',font =('Arial 8 bold')).grid(row=2,column=2,columnspan=1)
        Label(zone_2,text="EGALITE",bg='#FFFFFF',font =('Arial 11 bold'),fg='#686968').grid(row=1,column=0,columnspan=3)

    elif action_joueur == 3 and action_ordinateur == 3 : #egalite
        border_color_ordinateur = Frame(zone_4, bg= '#686968',height=60,width=60).grid(row=3,column=2,columnspan=1)
        render_ordinateur_ciseaux = ImageTk.PhotoImage(load_ordinateur_ciseaux)
        image_ordinateur_ciseaux = Label(zone_4, image=render_ordinateur_ciseaux,bg='#FFFFFF').grid(row=3,column=2,columnspan=1)
        border_color_joueur = Frame(zone_4, bg= '#686968',height=60,width=60).grid(row=3,column=0,columnspan=1)
        render_joueur_ciseaux = ImageTk.PhotoImage(load_joueur_ciseaux)
        image_joueur_ciseaux = Label(zone_4, image=render_joueur_ciseaux,bg='#FFFFFF').grid(row=3,column=0,columnspan=1)
        text_compteur_joueur = """Pt(s) JOUEUR :""",compteur_joueur
        pt_joueur =Label(zone_3, text=text_compteur_joueur,bg='#7DCEA0',fg='#FFFFFF',font =('Arial 8 bold')).grid(row=2,column=0,columnspan=1)
        text_compteur_ordinateur = """Pt(s) ORDINATEUR :""",compteur_ordinateur
        pt_ordinateur=Label(zone_3, text= text_compteur_ordinateur,bg='#7DCEA0',fg='#FFFFFF',font =('Arial 8 bold')).grid(row=2,column=2,columnspan=1)
        Label(zone_2,text="EGALITE",bg='#FFFFFF',font =('Arial 11 bold'),fg='#686968').grid(row=1,column=0,columnspan=3)


def rejouer():
    global render_joueur
    global render_ordinateur
    global bou_valider
    global load_ordinateur
    global load_joueur
    global render_ordinateur
    global render_joueur
    bou_valider = Button(zone_9,text = 'VALIDER',font =('Arial 10 bold'),width=0,command = valider,state = NORMAL).grid(row=8,column=0,rowspan=2) #rend de nouveau accessible le bouton valider
    global bou_rejouer
    bou_rejouer= Button(zone_9,text="REJOUER",font =('Arial 10 bold'),command=rejouer,state=DISABLED).grid(row=8,column=1,rowspan=2)#rend innacessible le bouton rejouer
    border_color_joueur = Frame(zone_4, bg= '#7DCEA0',height=60,width=60).grid(row=3,column=0,columnspan=1)        #renitialise border et image du joueru et de l'ordinateur
    image_joueur = Label(zone_4, image=render_joueur,bg='#FFFFFF').grid(row=3,column=0,columnspan=1)
    border_color_ordinateur = Frame(zone_4, bg= '#7DCEA0',height=60,width=60).grid(row=3,column=2,columnspan=1)
    image_ordinateur = Label(zone_4, image=render_ordinateur,bg='#FFFFFF').grid(row=3,column=2,columnspan=1)

def quitter():
    global fen1
    fen2 = Tk()  #création nouvelle fenêtre temporaire
    fen2.geometry("250x100")
    fen2.title("Quitter")
    fen2.configure(bg='#FFFFFF')
    Frame(fen2, bg='#FFFFFF',height=50,width=250).grid(row=0,column=0,columnspan=2,rowspan = 1)
    Label(fen2,text='Es-tu sûr de vouloir quitter ?',bg='#FFFFFF',font =('Arial 10 bold')).grid(row=0,column=0,columnspan=2)
    def two_funcs(*funcs):
        def two_funcs(*args, **kwargs):
            for f in funcs:
                f(*args, **kwargs)
        return two_funcs
    bou_quitter_oui = Button(fen2,text = 'oui',font =('Arial 10 bold'),command = two_funcs(fen2.destroy,fen1.destroy)).grid(row=1,column=0)
    bou_quitter_non = Button(fen2,text = 'non',font =('Arial 10 bold'),command = fen2.destroy).grid(row=1,column=1)
    fen2.mainloop()


def shifumi_libre():
    global var
    global fen1
    global load_joueur
    global load_ordinateur
    global load_pierre
    global load_feuille
    global load_ciseaux
    global render_ordinateur
    global render_joueur
    global render_pierre
    global render_feuille
    global render_ciseaux
    for widget in fen1.winfo_children():
        widget.destroy()
    zone_1= Frame(fen1, bg='#7DCEA0',height=45,width=350).grid(row=0,column=0,columnspan=3)
    Label(zone_1,text='-SHIFUMI-',bg='#7DCEA0',font =('Arial 20 bold'),fg='#FFFFFF').grid(row=0,column=0,columnspan=3)
    zone_2= Frame(fen1, bg='#FFFFFF',height=25,width=350).grid(row=1,column=0,columnspan=3)
    zone_3= Frame(fen1, bg='#7DCEA0',height=25,width=350).grid(row=2,column=0,columnspan=3)
    pt_joueur =Label(zone_3, text="Pt(s) JOUEUR :",bg='#7DCEA0',fg='#FFFFFF',font =('Arial 8 bold')).grid(row=2,column=0,columnspan=1)       #emplacement pt joueur
    pt_ordinateur=Label(zone_3, text="Pt(s) ORDINATEUR :",bg='#7DCEA0',fg='#FFFFFF',font =('Arial 8 bold')).grid(row=2,column=2,columnspan=1)#enplacement pt ordinateur

    zone_4= Frame(fen1, bg='#FFFFFF',height=90,width=350).grid(row=3,column=0,columnspan=3)

    #JOUEUR
    border_color_joueur = Frame(zone_4, bg= '#7DCEA0',height=60,width=60).grid(row=3,column=0,columnspan=1) #defini la bordure du cardre joueur
    image_joueur = Label(zone_4, image=render_joueur,bg='#FFFFFF').grid(row=3,column=0,columnspan=1)        #affiche image d'acceuil du joueur

    #VS
    vs= Label(zone_4,text="VS",bg='#FFFFFF',font =('Arial 16 bold')).grid(row=3,column=1,columnspan=1)

    #ORDINATEUR
    border_color_ordinateur = Frame(zone_4, bg= '#7DCEA0',height=60,width=60).grid(row=3,column=2,columnspan=1) #defini la bordure du cadre ordinateur
    image_ordinateur = Label(zone_4, image=render_ordinateur,bg='#FFFFFF').grid(row=3,column=2,columnspan=1)    #affiche image d'acceuil de l'ordinateur

    zone_5= Frame(fen1, bg='#7DCEA0',height=35,width=350).grid(row=4,column=0,columnspan=3)
    Label(zone_5, text="CHOISIS TON ARME",bg='#7DCEA0',fg='#FFFFFF',font =('Arial 15 bold')).grid(row=4,column=0,columnspan=3)

    zone_6= Frame(fen1, bg='#FFFFFF',height=80,width=350).grid(row=5,column=0,columnspan=3)

    """definition radiobutton"""
    #PIERRE
    border_color_img_pierre = Frame(zone_6, bg= '#FFFFFF',height=65,width=85).grid(row=5,column=0,columnspan=1)
    image_pierre = Radiobutton(zone_6,variable=var, image=render_pierre,bg='#FFFFFF',activebackground='#7DCEA0',command = image_joueur_pierre,value=1).grid(row=5,column=0,columnspan=1)
    #FEUILLE
    border_color_img_feuille = Frame(zone_6, bg= '#FFFFFF',height=65,width=85).grid(row=5,column=2,columnspan=1)
    image_feuille = Radiobutton(zone_6,variable=var, image=render_feuille,bg='#FFFFFF',activebackground='#7DCEA0',command=image_joueur_feuille,value=2).grid(row=5,column=2,columnspan=1)

    zone_7= Frame(fen1, bg='#FFFFFF',height=80,width=350).grid(row=6,column=0,columnspan=3)

    #CISEAUX
    border_color_img_ciseaux = Frame(zone_7, bg= '#FFFFFF',height=65,width=85).grid(row=6,column=1,columnspan=1)
    image_ciseaux = Radiobutton(zone_7,variable=var, image=render_ciseaux,bg='#FFFFFF',activebackground='#7DCEA0',command= image_joueur_ciseaux,value=3).grid(row=6,column=1,columnspan=1)
    """"""

    zone_8= Frame(fen1, bg='#7DCEA0',height=25,width=350).grid(row=7,column=0,columnspan=3)

    zone_9= Frame(fen1, bg='#FFFFFF',height=40,width=350).grid(row=8,column=0,columnspan=3)

    bou_valider = Button(zone_9,text = 'VALIDER',font =('Arial 10 bold'),width=0,command = valider,state = NORMAL).grid(row=8,column=0,rowspan=2)  #bouton valider
    bou_rejouer= Button(zone_9,text="REJOUER",font =('Arial 10 bold'),command=rejouer,state=DISABLED).grid(row=8,column=1,rowspan=2)  #bouton rejouer

    bou_quitter = Button(zone_9,text = 'QUITTER',font =('Arial 10 bold'),width=0,command = quitter ).grid(row=8,column=2,rowspan=2) #bouton quitter


    #DECO
    zone_10= Frame(fen1, bg='#FFFFFF',height=20,width=350).grid(row=9,column=0,columnspan=3)
    zone_11= Frame(fen1, bg='#7DCEA0',height=20,width=350).grid(row=10,column=0,columnspan=3)

"""Fin fonctions propre au mode libre"""

"""Début fonctions propre au mode challenge"""
def val():
    global var_2
    if var_2.get() == 4:
        a = 5
    elif var_2.get() == 5:
        a =10
    elif var_2.get()==6:
        a=15
    return a

def result():
    a= int(val())
    global compteur_joueur
    global compteur_ordinateur
    if compteur_joueur == a and compteur_ordinateur < a:
        fen3 = Tk()
        fen3.geometry("250x100")
        fen3.title("GAGNER")
        fen3.configure(bg='#FFFFFF')
        Frame(fen3, bg='#FFFFFF',height=50,width=250).grid(row=0,column=0,columnspan=2,rowspan = 1)
        Label(fen3,text='BRAVO ! Tu as GAGNE',bg='#FFFFFF',font =('Arial 10 bold')).grid(row=0,column=0,columnspan=2)
        def two_funcs(*funcs):
            def two_funcs(*args, **kwargs):
                for f in funcs:
                    f(*args, **kwargs)
            return two_funcs
        bou_quitter_bye = Button(fen3,text = 'EN REVOIR',font =('Arial 10 bold'),command = two_funcs(fen3.destroy,fen1.destroy)).grid(row=1,column=0,columnspan =2)
        fen3.mainloop()
    elif compteur_joueur < a and compteur_ordinateur == a:
        fen3 = Tk()
        fen3.geometry("250x100")
        fen3.title("PERDU")
        fen3.configure(bg='#FFFFFF')
        Frame(fen3, bg='#FFFFFF',height=50,width=250).grid(row=0,column=0,columnspan=2,rowspan = 1)
        Label(fen3,text='Tu as perdu...dommage',bg='#FFFFFF',font =('Arial 10 bold')).grid(row=0,column=0,columnspan=2)
        def two_funcs(*funcs):
            def two_funcs(*args, **kwargs):
                for f in funcs:
                    f(*args, **kwargs)
            return two_funcs
        bou_quitter_bye = Button(fen3,text = 'EN REVOIR',font =('Arial 10 bold'),command = two_funcs(fen3.destroy,fen1.destroy)).grid(row=1,column=0,columnspan =2)
        fen3.mainloop()


def valider_challenge():
    global zone_1
    global zone_2
    global zone_3
    global zone_4
    global zone_5
    global zone_6
    global zone_7
    global zone_8
    global zone_9
    global zone_10
    global zone_11
    global var
    from random import randint
    action_ordinateur = randint(1,3)
    action_joueur = var.get()
    """donne le gagnant de chaque tour"""
    global load_joueur_pierre
    global load_joueur_feuille
    global load_joueur_ciseaux
    global load_ordinateur_pierre
    global load_ordinateur_feuille
    global load_ordinateur_ciseaux
    global render_ordinateur_feuille
    global render_ordinateur_pierre
    global render_ordinateur_ciseaux
    global render_joueur_pierre
    global render_joueur_feuille
    global render_joueur_ciseaux
    global bou_valider
    bou_valider = Button(zone_9,text = 'VALIDER',font =('Arial 10 bold'),width=0,command = valider,state = DISABLED).grid(row=8,column=0,rowspan=2)    #grise le bouton valider
    global bou_rejouer
    bou_rejouer= Button(zone_9,text="REJOUER",font =('Arial 10 bold'),command=rejouer,state=NORMAL).grid(row=8,column=1,rowspan=2) #rend de nouveau accessible le bouton rejouer
    global border_color_joueur
    global border_color_ordinateur
    global compteur_ordinateur
    global compteur_joueur
    global pt_joueur
    global pt_ordinateur
    a = val()
    while compteur_joueur < a and compteur_ordinateur < a:
        if action_joueur == 1 and action_ordinateur == 2 :
            border_color_ordinateur = Frame(zone_4, bg= '#1FFF00',height=60,width=60).grid(row=3,column=2,columnspan=1)             #couleur bordure gagnant/vert
            render_ordinateur_feuille = ImageTk.PhotoImage(load_ordinateur_feuille)
            image_ordinateur_feuille = Label(zone_4, image=render_ordinateur_feuille,bg='#FFFFFF').grid(row=3,column=2,columnspan=1)#image ordinateur
            border_color_joueur = Frame(zone_4, bg= '#FF0000',height=60,width=60).grid(row=3,column=0,columnspan=1)                 #couleur bordure perdant/rouge
            render_joueur_pierre = ImageTk.PhotoImage(load_joueur_pierre)
            image_joueur_pierre = Label(zone_4, image=render_joueur_pierre,bg='#FFFFFF').grid(row=3,column=0,columnspan=1)          #image joueur
            compteur_ordinateur+=1                                                                                                  #compteur ordinateur
            text_compteur_joueur = """Pt(s) JOUEUR :""",compteur_joueur,"/",a
            pt_joueur =Label(zone_3, text= text_compteur_joueur,bg='#7DCEA0',fg='#FFFFFF',font =('Arial 8 bold')).grid(row=2,column=0,columnspan=1) #actualisation des compteurs afficher
            text_compteur_ordinateur = """Pt(s) ORDINATEUR :""",compteur_ordinateur,"/",a
            pt_ordinateur=Label(zone_3, text= text_compteur_ordinateur,fg='#FFFFFF',bg='#7DCEA0',font =('Arial 8 bold')).grid(row=2,column=2,columnspan=1)
            Label(zone_2,text=" PERDU ",bg='#FFFFFF',font =('Arial 11 bold'),fg='#FF0000').grid(row=1,column=0,columnspan=3)
        elif action_ordinateur == 1 and action_joueur == 2 :
            border_color_ordinateur = Frame(zone_4, bg= '#FF0000',height=60,width=60).grid(row=3,column=2,columnspan=1)
            render_ordinateur_pierre = ImageTk.PhotoImage(load_ordinateur_pierre)
            image_ordinateur_pierre = Label(zone_4, image=render_ordinateur_pierre,bg='#FFFFFF').grid(row=3,column=2,columnspan=1)
            border_color_joueur = Frame(zone_4, bg= '#1FFF00',height=60,width=60).grid(row=3,column=0,columnspan=1)
            render_joueur_feuille = ImageTk.PhotoImage(load_joueur_feuille)
            image_joueur_feuille = Label(zone_4, image=render_joueur_feuille,bg='#FFFFFF').grid(row=3,column=0,columnspan=1)
            compteur_joueur+=1
            text_compteur_joueur = """Pt(s) JOUEUR :""",compteur_joueur,"/",a
            pt_joueur =Label(zone_3, text= text_compteur_joueur,bg='#7DCEA0',fg='#FFFFFF',font =('Arial 8 bold')).grid(row=2,column=0,columnspan=1)
            text_compteur_ordinateur = """Pt(s) ORDINATEUR :""",compteur_ordinateur,"/",a
            pt_ordinateur=Label(zone_3, text= text_compteur_ordinateur,bg='#7DCEA0',fg='#FFFFFF',font =('Arial 8 bold')).grid(row=2,column=2,columnspan=1)
            Label(zone_2,text="GAGNER",bg='#FFFFFF',font =('Arial 11 bold'),fg='#1FFF00').grid(row=1,column=0,columnspan=3)
        elif action_joueur == 2 and action_ordinateur == 3 :
            border_color_ordinateur = Frame(zone_4, bg= '#1FFF00',height=60,width=60).grid(row=3,column=2,columnspan=1)
            render_ordinateur_ciseaux = ImageTk.PhotoImage(load_ordinateur_ciseaux)
            image_ordinateur_ciseaux = Label(zone_4, image=render_ordinateur_ciseaux,bg='#FFFFFF').grid(row=3,column=2,columnspan=1)
            border_color_joueur = Frame(zone_4, bg= '#FF0000',height=60,width=60).grid(row=3,column=0,columnspan=1)
            render_joueur_feuille = ImageTk.PhotoImage(load_joueur_feuille)
            image_joueur_feuille = Label(zone_4, image=render_joueur_feuille,bg='#FFFFFF').grid(row=3,column=0,columnspan=1)
            compteur_ordinateur+=1
            text_compteur_joueur = """Pt(s) JOUEUR :""",compteur_joueur,"/",a
            pt_joueur =Label(zone_3, text= text_compteur_joueur,bg='#7DCEA0',fg='#FFFFFF',font =('Arial 8 bold')).grid(row=2,column=0,columnspan=1)
            text_compteur_ordinateur = """Pt(s) ORDINATEUR :""",compteur_ordinateur,"/",a
            pt_ordinateur=Label(zone_3, text= text_compteur_ordinateur,bg='#7DCEA0',fg='#FFFFFF',font =('Arial 8 bold')).grid(row=2,column=2,columnspan=1)
            Label(zone_2,text=" PERDU ",bg='#FFFFFF',font =('Arial 11 bold'),fg='#FF0000').grid(row=1,column=0,columnspan=3)
        elif action_ordinateur == 2 and action_joueur == 3 :
            border_color_ordinateur = Frame(zone_4, bg= '#FF0000',height=60,width=60).grid(row=3,column=2,columnspan=1)
            render_ordinateur_feuille = ImageTk.PhotoImage(load_ordinateur_feuille)
            image_ordinateur_feuille = Label(zone_4, image=render_ordinateur_feuille,bg='#FFFFFF').grid(row=3,column=2,columnspan=1)
            border_color_joueur = Frame(zone_4, bg= '#1FFF00',height=60,width=60).grid(row=3,column=0,columnspan=1)
            render_joueur_ciseaux = ImageTk.PhotoImage(load_joueur_ciseaux)
            image_joueur_ciseaux = Label(zone_4, image=render_joueur_ciseaux,bg='#FFFFFF').grid(row=3,column=0,columnspan=1)
            compteur_joueur+=1
            text_compteur_joueur = """Pt(s) JOUEUR :""",compteur_joueur,"/",a
            pt_joueur =Label(zone_3, text= text_compteur_joueur,bg='#7DCEA0',fg='#FFFFFF',font =('Arial 8 bold')).grid(row=2,column=0,columnspan=1)
            text_compteur_ordinateur = """Pt(s) ORDINATEUR :""",compteur_ordinateur,"/",a
            pt_ordinateur=Label(zone_3, text= text_compteur_ordinateur,bg='#7DCEA0',fg='#FFFFFF',font =('Arial 8 bold')).grid(row=2,column=2,columnspan=1)
            Label(zone_2,text="GAGNER",bg='#FFFFFF',font =('Arial 11 bold'),fg='#1FFF00').grid(row=1,column=0,columnspan=3)
        elif action_joueur == 3 and action_ordinateur == 1 :
            border_color_ordinateur = Frame(zone_4, bg= '#1FFF00',height=60,width=60).grid(row=3,column=2,columnspan=1)
            load_ordinateur_pierre = Image.open("icons8-poing-serré-50.png")
            render_ordinateur_pierre = ImageTk.PhotoImage(load_ordinateur_pierre)
            image_ordinateur_pierre = Label(zone_4, image=render_ordinateur_pierre,bg='#FFFFFF').grid(row=3,column=2,columnspan=1)
            border_color_joueur = Frame(zone_4, bg= '#FF0000',height=60,width=60).grid(row=3,column=0,columnspan=1)
            render_joueur_ciseaux = ImageTk.PhotoImage(load_joueur_ciseaux)
            image_joueur_ciseaux = Label(zone_4, image=render_joueur_ciseaux,bg='#FFFFFF').grid(row=3,column=0,columnspan=1)
            compteur_ordinateur+=1
            text_compteur_joueur = """Pt(s) JOUEUR :""",compteur_joueur,"/",a
            pt_joueur =Label(zone_3, text= text_compteur_joueur,bg='#7DCEA0',fg='#FFFFFF',font =('Arial 8 bold')).grid(row=2,column=0,columnspan=1)
            text_compteur_ordinateur = """Pt(s) ORDINATEUR :""",compteur_ordinateur,"/",a
            pt_ordinateur=Label(zone_3, text= text_compteur_ordinateur,bg='#7DCEA0',fg='#FFFFFF',font =('Arial 8 bold')).grid(row=2,column=2,columnspan=1)
            Label(zone_2,text=" PERDU ",bg='#FFFFFF',font =('Arial 11 bold'),fg='#FF0000').grid(row=1,column=0,columnspan=3)
        elif action_ordinateur == 3 and action_joueur == 1 :
            border_color_ordinateur = Frame(zone_4, bg= '#FF0000',height=60,width=60).grid(row=3,column=2,columnspan=1)
            render_ordinateur_ciseaux = ImageTk.PhotoImage(load_ordinateur_ciseaux)
            image_ordinateur_ciseaux = Label(zone_4, image=render_ordinateur_ciseaux,bg='#FFFFFF').grid(row=3,column=2,columnspan=1)
            border_color_joueur = Frame(zone_4, bg= '#1FFF00',height=60,width=60).grid(row=3,column=0,columnspan=1)
            render_joueur_pierre = ImageTk.PhotoImage(load_joueur_pierre)
            image_joueur_pierre = Label(zone_4, image=render_joueur_pierre,bg='#FFFFFF').grid(row=3,column=0,columnspan=1)
            compteur_joueur+=1
            text_compteur_joueur = """Pt(s) JOUEUR :""",compteur_joueur,"/",a
            pt_joueur =Label(zone_3, text= text_compteur_joueur,bg='#7DCEA0',fg='#FFFFFF',font =('Arial 8 bold')).grid(row=2,column=0,columnspan=1)
            text_compteur_ordinateur = """Pt(s) ORDINATEUR :""",compteur_ordinateur,"/",a
            pt_ordinateur=Label(zone_3, text= text_compteur_ordinateur,bg='#7DCEA0',fg='#FFFFFF',font =('Arial 8 bold')).grid(row=2,column=2,columnspan=1)
            Label(zone_2,text="GAGNER",bg='#FFFFFF',font =('Arial 11 bold'),fg='#1FFF00').grid(row=1,column=0,columnspan=3)
        elif action_joueur == 1 and action_ordinateur == 1 :
            border_color_ordinateur = Frame(zone_4, bg= '#686968',height=60,width=60).grid(row=3,column=2,columnspan=1)
            render_ordinateur_pierre = ImageTk.PhotoImage(load_ordinateur_pierre)
            image_ordinateur_pierre = Label(zone_4, image=render_ordinateur_pierre,bg='#FFFFFF').grid(row=3,column=2,columnspan=1)
            border_color_joueur = Frame(zone_4, bg= '#686968',height=60,width=60).grid(row=3,column=0,columnspan=1)
            render_joueur_pierre = ImageTk.PhotoImage(load_joueur_pierre)
            image_joueur_pierre = Label(zone_4, image=render_joueur_pierre,bg='#FFFFFF').grid(row=3,column=0,columnspan=1)
            text_compteur_joueur = """Pt(s) JOUEUR :""",compteur_joueur,"/",a
            pt_joueur =Label(zone_3, text=text_compteur_joueur,bg='#7DCEA0',fg='#FFFFFF',font =('Arial 8 bold')).grid(row=2,column=0,columnspan=1)
            text_compteur_ordinateur = """Pt(s) ORDINATEUR :""",compteur_ordinateur,"/",a
            pt_ordinateur=Label(zone_3, text=text_compteur_ordinateur,bg='#7DCEA0',fg='#FFFFFF',font =('Arial 8 bold')).grid(row=2,column=2,columnspan=1)
            Label(zone_2,text="EGALITE",bg='#FFFFFF',font =('Arial 11 bold'),fg='#686968').grid(row=1,column=0,columnspan=3)
        elif action_joueur == 2 and action_ordinateur == 2 :
            border_color_ordinateur = Frame(zone_4, bg= '#686968',height=60,width=60).grid(row=3,column=2,columnspan=1)
            render_ordinateur_feuille = ImageTk.PhotoImage(load_ordinateur_feuille)
            image_ordinateur_feuille = Label(zone_4, image=render_ordinateur_feuille,bg='#FFFFFF').grid(row=3,column=2,columnspan=1)
            border_color_joueur = Frame(zone_4, bg= '#686968',height=60,width=60).grid(row=3,column=0,columnspan=1)
            render_joueur_feuille = ImageTk.PhotoImage(load_joueur_feuille)
            image_joueur_feuille = Label(zone_4, image=render_joueur_feuille,bg='#FFFFFF').grid(row=3,column=0,columnspan=1)
            text_compteur_joueur = """Pt(s) JOUEUR :""",compteur_joueur,"/",a
            pt_joueur =Label(zone_3, text=text_compteur_joueur,bg='#7DCEA0',fg='#FFFFFF',font =('Arial 8 bold')).grid(row=2,column=0,columnspan=1)
            text_compteur_ordinateur = """Pt(s) ORDINATEUR :""",compteur_ordinateur,"/",a
            pt_ordinateur=Label(zone_3, text= text_compteur_ordinateur,bg='#7DCEA0',fg='#FFFFFF',font =('Arial 8 bold')).grid(row=2,column=2,columnspan=1)
            Label(zone_2,text="EGALITE",bg='#FFFFFF',font =('Arial 11 bold'),fg='#686968').grid(row=1,column=0,columnspan=3)
        elif action_joueur == 3 and action_ordinateur == 3 :
            border_color_ordinateur = Frame(zone_4, bg= '#686968',height=60,width=60).grid(row=3,column=2,columnspan=1)
            render_ordinateur_ciseaux = ImageTk.PhotoImage(load_ordinateur_ciseaux)
            image_ordinateur_ciseaux = Label(zone_4, image=render_ordinateur_ciseaux,bg='#FFFFFF').grid(row=3,column=2,columnspan=1)
            border_color_joueur = Frame(zone_4, bg= '#686968',height=60,width=60).grid(row=3,column=0,columnspan=1)
            render_joueur_ciseaux = ImageTk.PhotoImage(load_joueur_ciseaux)
            image_joueur_ciseaux = Label(zone_4, image=render_joueur_ciseaux,bg='#FFFFFF').grid(row=3,column=0,columnspan=1)
            text_compteur_joueur = """Pt(s) JOUEUR :""",compteur_joueur,"/",a
            pt_joueur =Label(zone_3, text=text_compteur_joueur,bg='#7DCEA0',fg='#FFFFFF',font =('Arial 8 bold')).grid(row=2,column=0,columnspan=1)
            text_compteur_ordinateur = """Pt(s) ORDINATEUR :""",compteur_ordinateur,"/",a
            pt_ordinateur=Label(zone_3, text= text_compteur_ordinateur,bg='#7DCEA0',fg='#FFFFFF',font =('Arial 8 bold')).grid(row=2,column=2,columnspan=1)
            Label(zone_2,text="EGALITE",bg='#FFFFFF',font =('Arial 11 bold'),fg='#686968').grid(row=1,column=0,columnspan=3)
        result()



def shifumi_challenge():
    global fen1
    global var
    global load_joueur
    global load_ordinateur
    global load_pierre
    global load_feuille
    global load_ciseaux
    global render_ordinateur
    global render_joueur
    global render_pierre
    global render_feuille
    global render_ciseaux
    for widget in fen1.winfo_children():
        widget.destroy()
    a = val()
    zone_1= Frame(fen1, bg='#7DCEA0',height=45,width=350).grid(row=0,column=0,columnspan=3)
    Label(zone_1,text='-SHIFUMI-',bg='#7DCEA0',font =('Arial 20 bold'),fg='#FFFFFF').grid(row=0,column=0,columnspan=3)
    zone_2= Frame(fen1, bg='#FFFFFF',height=25,width=350).grid(row=1,column=0,columnspan=3)
    zone_3= Frame(fen1, bg='#7DCEA0',height=25,width=350).grid(row=2,column=0,columnspan=3)
    text_pt_joueur = "Pt(s) JOUEUR :0","/",a
    pt_joueur =Label(zone_3, text=text_pt_joueur,bg='#7DCEA0',fg='#FFFFFF',font =('Arial 8 bold')).grid(row=2,column=0,columnspan=1)       #emplacement pt joueur
    text_pt_ordinateur="Pt(s) ORDINATEUR :0","/",a
    pt_ordinateur=Label(zone_3, text=text_pt_ordinateur,bg='#7DCEA0',fg='#FFFFFF',font =('Arial 8 bold')).grid(row=2,column=2,columnspan=1)#enplacement pt ordinateur

    zone_4= Frame(fen1, bg='#FFFFFF',height=90,width=350).grid(row=3,column=0,columnspan=3)
    #JOUEUR
    border_color_joueur = Frame(zone_4, bg= '#7DCEA0',height=60,width=60).grid(row=3,column=0,columnspan=1) #defini la bordure du cardre joueur
    image_joueur = Label(zone_4, image=render_joueur,bg='#FFFFFF').grid(row=3,column=0,columnspan=1)        #affiche image d'acceuil du joueur

    #VS
    vs= Label(zone_4,text="VS",bg='#FFFFFF',font =('Arial 16 bold')).grid(row=3,column=1,columnspan=1)

    #ORDINATEUR
    border_color_ordinateur = Frame(zone_4, bg= '#7DCEA0',height=60,width=60).grid(row=3,column=2,columnspan=1) #defini la bordure du cadre ordinateur
    image_ordinateur = Label(zone_4, image=render_ordinateur,bg='#FFFFFF').grid(row=3,column=2,columnspan=1)    #affiche image d'acceuil de l'ordinateur

    zone_5= Frame(fen1, bg='#7DCEA0',height=35,width=350).grid(row=4,column=0,columnspan=3)
    Label(zone_5, text="CHOISIS TON ARME",bg='#7DCEA0',fg='#FFFFFF',font =('Arial 15 bold')).grid(row=4,column=0,columnspan=3)

    zone_6= Frame(fen1, bg='#FFFFFF',height=80,width=350).grid(row=5,column=0,columnspan=3)
    #PIERRE
    border_color_img_pierre = Frame(zone_6, bg= '#FFFFFF',height=65,width=85).grid(row=5,column=0,columnspan=1)
    image_pierre = Radiobutton(zone_6,variable=var, image=render_pierre,bg='#FFFFFF',activebackground='#7DCEA0',command = image_joueur_pierre,value=1).grid(row=5,column=0,columnspan=1)
    #FEUILLE
    border_color_img_feuille = Frame(zone_6, bg= '#FFFFFF',height=65,width=85).grid(row=5,column=2,columnspan=1)
    image_feuille = Radiobutton(zone_6,variable=var, image=render_feuille,bg='#FFFFFF',activebackground='#7DCEA0',command=image_joueur_feuille,value=2).grid(row=5,column=2,columnspan=1)

    zone_7= Frame(fen1, bg='#FFFFFF',height=80,width=350).grid(row=6,column=0,columnspan=3)

    #CISEAUX
    border_color_img_ciseaux = Frame(zone_7, bg= '#FFFFFF',height=65,width=85).grid(row=6,column=1,columnspan=1)
    image_ciseaux = Radiobutton(zone_7,variable=var, image=render_ciseaux,bg='#FFFFFF',activebackground='#7DCEA0',command= image_joueur_ciseaux,value=3).grid(row=6,column=1,columnspan=1)

    zone_8= Frame(fen1, bg='#7DCEA0',height=25,width=350).grid(row=7,column=0,columnspan=3)

    zone_9= Frame(fen1, bg='#FFFFFF',height=40,width=350).grid(row=8,column=0,columnspan=3)

    bou_valider = Button(zone_9,text = 'VALIDER',font =('Arial 10 bold'),width=0,command = lambda: valider_challenge(),state = NORMAL).grid(row=8,column=0,rowspan=2)  #bouton valider

    bou_rejouer= Button(zone_9,text="REJOUER",font =('Arial 10 bold'),command=rejouer,state=DISABLED).grid(row=8,column=1,rowspan=2)  #bouton rejouer

    bou_quitter = Button(zone_9,text = 'QUITTER',font =('Arial 10 bold'),width=0,command = quitter ).grid(row=8,column=2,rowspan=2) #bouton quitter

    #DECO
    zone_10= Frame(fen1, bg='#FFFFFF',height=20,width=350).grid(row=9,column=0,columnspan=3)
    zone_11= Frame(fen1, bg='#7DCEA0',height=20,width=350).grid(row=10,column=0,columnspan=3)


def shifumi_challenge_choix():
    global fen1
    for widget in fen1.winfo_children():
        widget.destroy()
    zone_1= Frame(fen1, bg='#7DCEA0',height=45,width=350).grid(row=0,column=0,columnspan=3)
    Label(zone_1,text='-SHIFUMI-',bg='#7DCEA0',font =('Arial 20 bold'),fg='#FFFFFF').grid(row=0,column=0,columnspan=3)

    zone_2= Frame(fen1, bg='#FFFFFF',height=25,width=350).grid(row=1,column=0,columnspan=3)

    zone_3= Frame(fen1, bg='#7DCEA0',height=25,width=350).grid(row=2,column=0,columnspan=3)
    Label(zone_3,text='MODE CHALLENGE',bg='#7DCEA0',font =('Arial 10 bold'),fg='#FFFFFF').grid(row=2,column=0,columnspan=3)

    zone_4= Frame(fen1, bg='#7DCEA0',height=90,width=350).grid(row=3,column=0,columnspan=3)
    txt="""Le mode 'CHALLENGE' détermine un nombre
    de manches à gagner par le vainqueur"""
    Label(zone_4,text=txt,bg='#7DCEA0',font =('Arial 10 bold'),fg='#FFFFFF').grid(row=3,column=0,columnspan=3)

    zone_5= Frame(fen1, bg='#7DCEA0',height=35,width=350).grid(row=4,column=0,columnspan=3)
    Label(zone_5,text='sur combien de manche souhaites-tu réaliser ce challenge ?',bg='#7DCEA0',font =('Arial 8 italic'),fg='#FFFFFF').grid(row=4,column=0,columnspan=3)

    zone_6= Frame(fen1, bg='#FFFFFF',height=80,width=350).grid(row=5,column=0,columnspan=3)
    texte_6 = """→ Choisis ci-dessous le nombre
    de manches souhaitées : """
    Label(zone_6,text= texte_6 ,bg='#FFFFFF',font =('Arial 10 bold')).grid(row=5,column=0,columnspan=3)

    zone_7= Frame(fen1, bg='#FFFFFF',height=80,width=350).grid(row=6,column=0,columnspan=3)
    Radiobutton(zone_7, text ='5',variable=var_2,bg='#FFFFFF',activebackground='#7DCEA0',value=4,font =('Arial 11 bold')).grid(row=6,column=0)
    Radiobutton(zone_7, text ='10',variable=var_2,bg='#FFFFFF',activebackground='#7DCEA0',value=5,font =('Arial 11 bold')).grid(row=6,column=1)
    Radiobutton(zone_7, text ='15',variable=var_2,bg='#FFFFFF',activebackground='#7DCEA0',value=6,font =('Arial 11 bold')).grid(row=6,column=2)

    zone_8= Frame(fen1, bg='#7DCEA0',height=25,width=350).grid(row=7,column=0,columnspan=3)
    zone_9= Frame(fen1, bg='#FFFFFF',height=40,width=350).grid(row=8,column=0,columnspan=3)
    bou_valider_challenge = Button(zone_9,text = 'VALIDER',font =('Arial 10 bold'),width=0,state = NORMAL,command =shifumi_challenge).grid(row=8,column=0,rowspan=2)  #bouton valider
    bou_quitter_challenge_choix = Button(zone_9,text = 'QUITTER',font =('Arial 10 bold'),width=0,command = quitter_acceuil ).grid(row=8,column=2,rowspan=2) #bouton quitter
    zone_10= Frame(fen1, bg='#FFFFFF',height=20,width=350).grid(row=9,column=0,columnspan=3)
    zone_11= Frame(fen1, bg='#7DCEA0',height=20,width=350).grid(row=10,column=0,columnspan=3)


"""Fin fonctions propre au mode challenge"""

"""Début fonctions propre à la configuration de l'accceuil"""
def quitter_acceuil():
        global fen1
        fen2_acceuil = Tk()
        fen2_acceuil.geometry("250x100")
        fen2_acceuil.title("Quitter")
        fen2_acceuil.configure(bg='#FFFFFF')
        Frame(fen2_acceuil, bg='#FFFFFF',height=50,width=250).grid(row=0,column=0,columnspan=2,rowspan = 1)
        Label(fen2_acceuil,text='Es-tu sûr de vouloir quitter ?',bg='#FFFFFF',font =('Arial 10 bold')).grid(row=0,column=0,columnspan=2)
        def two_funcs(*funcs):
            def two_funcs(*args, **kwargs):
                for f in funcs:
                    f(*args, **kwargs)
            return two_funcs
        bou_quitter_oui_acceuil = Button(fen2_acceuil,text = 'oui',font =('Arial 10 bold'),command = two_funcs(fen2_acceuil.destroy,fen1.destroy)).grid(row=1,column=0)
        bou_quitter_non_acceuil = Button(fen2_acceuil,text = 'non',font =('Arial 10 bold'),command = fen2_acceuil.destroy).grid(row=1,column=1)
        fen2_acceuil.mainloop()

def acceuil_shifumi():
    global fen1
    zone_1= Frame(fen1, bg='#7DCEA0',height=45,width=350).grid(row=0,column=0,columnspan=3)
    Label(zone_1,text='-CHOISIS TON MODE DE JEU-',bg='#7DCEA0',font =('Arial 17 bold'),fg='#FFFFFF').grid(row=0,column=0,columnspan=3)
    zone_2= Frame(fen1, bg='#FFFFFF',height=25,width=350).grid(row=1,column=0,columnspan=3)

    zone_3= Frame(fen1, bg='#7DCEA0',height=25,width=350).grid(row=2,column=0,columnspan=3)
    Label(zone_3,text = '•LIBRE',bg='#7DCEA0',font =('Arial 10 bold'),fg='#FFFFFF').grid(row=2,column=0)
    Label(zone_3,text = '•CHALLENGE',bg='#7DCEA0',font =('Arial 10 bold'),fg='#FFFFFF').grid(row=2,column=2)

    zone_4= Frame(fen1, bg='#7DCEA0',height=90,width=350).grid(row=3,column=0,columnspan=3)
    texte_libre = """Le jeu continu
    jusqu'à ce
    que l'on quitte"""
    Label(zone_4,text = texte_libre,bg='#7DCEA0',font =('Arial 10 bold'),fg='#FFFFFF').grid(row=3,column=0)
    texte_challenge = """Détermine un nombre
    de manches à gagner
    par le vainqueur"""
    Label(zone_4,text = texte_challenge,bg='#7DCEA0',font =('Arial 10 bold'),fg='#FFFFFF').grid(row=3,column=2)

    zone_5= Frame(fen1, bg='#7DCEA0',height=35,width=350).grid(row=4,column=0,columnspan=3)

    zone_6= Frame(fen1, bg='#FFFFFF',height=80,width=350).grid(row=5,column=0,columnspan=3)

    zone_7= Frame(fen1, bg='#FFFFFF',height=80,width=350).grid(row=6,column=0,columnspan=3)
    Button(zone_7,text = 'LIBRE',bg='#FFFFFF',font =('Arial 13 bold'),activebackground='#7DCEA0',command = shifumi_libre).grid(row=5,column=0,rowspan=2 )
    Button(zone_7,text = 'CHALLENGE',bg='#FFFFFF',font =('Arial 13 bold'),activebackground='#7DCEA0',command= shifumi_challenge_choix).grid(row=5,column=2,rowspan=2 )

    zone_8= Frame(fen1, bg='#7DCEA0',height=25,width=350).grid(row=7,column=0,columnspan=3)
    zone_9= Frame(fen1, bg='#FFFFFF',height=40,width=350).grid(row=8,column=0,columnspan=3)
    bou_quitter_acceuil = Button(zone_9,text = 'QUITTER',font =('Arial 10 bold'),width=0,command = quitter_acceuil ).grid(row=8,column=2,rowspan=2) #bouton quitter
    zone_10= Frame(fen1, bg='#FFFFFF',height=20,width=350).grid(row=9,column=0,columnspan=3)
    zone_11= Frame(fen1, bg='#7DCEA0',height=20,width=350).grid(row=10,column=0,columnspan=3)

"""Début fonctions propre à la configuration de l'accceuil"""

#fenêtre principal
fen1= Tk()
fen1.geometry("350x480")
fen1.title("ShiFuMi")
fen1.configure(bg='#FFFFFF')

#LOAD IMAGES
load_joueur = Image.open("icons8-utilisateur-50.png")
load_ordinateur = Image.open("icons8-moniteur-50.png")
load_pierre = Image.open("icons8-poing-serré-50.png")
load_feuille = Image.open("icons8-toute-la-main-50.png")
load_ciseaux = Image.open("icons8-main-ciseaux-50.png")

load_ordinateur_pierre = Image.open("icons8-poing-serré-50.png")
load_ordinateur_feuille = Image.open("icons8-toute-la-main-50.png")
load_ordinateur_ciseaux = Image.open("icons8-main-ciseaux-50.png")
load_joueur_pierre = Image.open("icons8-poing-serré-50.png")
load_joueur_feuille = Image.open("icons8-toute-la-main-50.png")
load_joueur_ciseaux = Image.open("icons8-main-ciseaux-50.png")

#render
render_joueur = ImageTk.PhotoImage(load_joueur)
render_ordinateur = ImageTk.PhotoImage(load_ordinateur)
render_joueur_pierre = ImageTk.PhotoImage(load_joueur_pierre)
render_joueur_feuille = ImageTk.PhotoImage(load_joueur_feuille)
render_joueur_ciseaux = ImageTk.PhotoImage(load_joueur_ciseaux)
render_pierre = ImageTk.PhotoImage(load_pierre)
render_feuille = ImageTk.PhotoImage(load_feuille)
render_ciseaux = ImageTk.PhotoImage(load_ciseaux)

#valeur radiobutton
var = IntVar()
var_2 = IntVar()

#compteur
compteur_joueur=0
compteur_ordinateur=0

#définition des zones
zone_1= Frame(fen1, bg='#7DCEA0',height=45,width=350).grid(row=0,column=0,columnspan=3)
zone_2= Frame(fen1, bg='#FFFFFF',height=25,width=350).grid(row=1,column=0,columnspan=3)
zone_3= Frame(fen1, bg='#7DCEA0',height=25,width=350).grid(row=2,column=0,columnspan=3)
zone_4= Frame(fen1, bg='#FFFFFF',height=90,width=350).grid(row=3,column=0,columnspan=3)
zone_5= Frame(fen1, bg='#7DCEA0',height=35,width=350).grid(row=4,column=0,columnspan=3)
zone_6= Frame(fen1, bg='#FFFFFF',height=80,width=350).grid(row=5,column=0,columnspan=3)
zone_7= Frame(fen1, bg='#FFFFFF',height=80,width=350).grid(row=6,column=0,columnspan=3)
zone_8= Frame(fen1, bg='#7DCEA0',height=25,width=350).grid(row=7,column=0,columnspan=3)
zone_9= Frame(fen1, bg='#FFFFFF',height=40,width=350).grid(row=8,column=0,columnspan=3)
zone_10= Frame(fen1, bg='#FFFFFF',height=20,width=350).grid(row=9,column=0,columnspan=3)
zone_11= Frame(fen1, bg='#7DCEA0',height=20,width=350).grid(row=10,column=0,columnspan=3)


acceuil_shifumi() # lancement acceuil

fen1.mainloop()