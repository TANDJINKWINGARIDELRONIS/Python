from tkinter import *
from tkinter import messagebox

windows=Tk()
windows.title("MORPION")
windows.geometry("500x300")
windows.config(bg="gray30")


#declaration des variables globales

joueur="X" #indique que le joueur X commence

plateau =[["" for _ in range(5)] for _ in range(5)] #cree une matrice 5x5  
boutons=[] #liste qui contient les widgets BUTTON pour chaque case
historiques=[] #pile vide qui contient l'historique des coups
partie_termine=False
#fonction clic 
def clic(i,j):
    global joueur

    if plateau[i][j]=="" and not victoire() :#verifie si la case est vide et que le jeux est pas fini 

        plateau[i][j]=joueur #recupere le symbole du joueur
        boutons[i][j].config(text=joueur,state="disabled") #evite de cliquer deux fois sur le meme bouton
        historiques.append((i,j,joueur)) #empile les coups joués

        if victoire() :
            messagebox.showinfo("Partie Terminée",f"le joeur {joueur} gagne la partie")
            fin()
        elif match_nul() :
                messagebox.showinfo("Partie Terminée",f"La partie se termine sur un match nul BRAVO a tous")
        else :
                joueur="O"  if joueur== "X"  else  "X" #modifie le joueur si la partie continue

#fonction de retour en arriere
def unclic() :
    global joueur,partie_termine
    if  partie_termine :
        messagebox.showinfo("Partie Terminée","Impossible d'annuler car la partie est deja terminée")
        return
    if not historiques :
        messagebox.showinfo("Annuler","Aucun coup n'a encore été joué")
        return
    i,j,dernier_joueur=historiques.pop() #depile les coups joués
    plateau[i][j]=""
    boutons[i][j].config(text="",state="normal")
    joueur=dernier_joueur

#fonction de verification de la victoire 
def victoire() :
    for i in range(5) :
        #comparaison des lignes horizontales
        if plateau[i][0]==plateau[i][1]==plateau[i][2]==plateau[i][3]==plateau[i][4] !="" :
            return True
        #comparaison des lignes verticales
        if  plateau[0][i]==plateau[1][i]==plateau[2][i]==plateau[3][i]==plateau[4][i] !="" :
            return True
    #test de la premiere diagonale (De haut en bas)
    if  plateau[0][0]==plateau[1][1]==plateau[2][2]==plateau[3][3]==plateau[4][4] !="" :
            return True
    #test de la deuxieme diagonale (De bas en haut)
    if  plateau[0][4]==plateau[1][3]==plateau[2][2]==plateau[3][1]==plateau[4][0] !="" :
            return True
    return False

#fonction de match_nul
def match_nul() :
    global partie_termine
    #parcours toutes les cases (si au moins une est vide le match est pas nul) sinon match nul
    for i in range(5) :
        for j in range(5) :
            if  plateau[i][j]=="" :
                return False
    partie_termine=True
    return True


#fonction fin (qui desactive toutes les cases du jeu)
def fin() :
    global partie_termine
    partie_termine=True
    for ligne in boutons :
        for n in ligne :
            n.config(state="disabled")

#fontion pour lancer une nouvelle partie
def reset() : 
    global joueur,plateau,historique,partie_termine
    joueur="X"
    historiques.clear()
    partie_termine=False
    plateau =[["" for _ in range(5)] for _ in range(5)]
    for i in range(5) :
        for j in range(5) :
            boutons[i][j].config(text="",state="normal")

#fonction pour quitter le jeu
def quitter() :
    if messagebox.askyesno("Quitter","Voulez vous vraiment quitter le jeu?") :
        windows.quit()

#fontion d'aide
def aide() :
    messagebox.showinfo(
        "REGLES DU JEUX ",
        "Deux joueurs s'affrontent sur des grilles 5X5 "
        "Le premier à alligner 5 symboles identiques gagne!\n"
        "Important: Les symboles peuvent etre alligné horizontalement,verticalement ou sur la diagonale"
        "\nBonne partie a tous !"
    )

#fonction des information
def infos() :
    messagebox.showinfo(
        "A PROPOS",
        "Jeux de morpion\n"
        "Language=PYTHON"
        "\nversion=1.0"
    )
#creation de la barre de menu
menubar=Menu(windows)

#creation des sous menus
#--Menu fichier--
menu_fichier=Menu(menubar,tearoff=0)
menu_fichier.add_cascade(label="New Game",command=reset)
menu_fichier.add_separator()
menu_fichier.add_cascade(label="Exit",command=quitter)
menubar.add_cascade(label="Fichier",menu=menu_fichier)

#--Menu Option--
menu_option=Menu(menubar,tearoff=0)
menu_option.add_cascade(label="Undo",command=unclic)
menu_option.add_separator()
menu_option.add_cascade(label="aide",command=aide)
menu_option.add_separator()
menu_option.add_cascade(label="A propos",command=infos)
menubar.add_cascade(label="Option",menu=menu_option)



windows.config(menu=menubar)

#message de bienvenue
Label(windows,text="BIENVENUE DANS CE JEU",font=("Helvetica",18,"bold"),bg="gray30").pack(pady=10)

#construction du plateau
cadre=Frame(windows,bg="blue")
cadre.pack()

for i in range(5):
    ligne=[]
    for j in range(5) :
        bout=Button(cadre,text="",font=("Helvetica",14,"bold"),width=5,height=3,command=lambda i=i, j=j:clic(i,j))
        bout.grid(row=i, column=j,padx=5,pady=5)
        ligne.append(bout)
    boutons.append(ligne)


windows.mainloop()