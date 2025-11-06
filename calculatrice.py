from tkinter import *
from tkinter import messagebox
import math



windows=Tk()
windows.title("Scientific calculator")
windows.config(bg="powder blue")
windows.resizable(width=False,height=False)
windows.geometry("900x600")

calculator=Frame(windows,bg="black")
calculator.grid()

#fonction pour quitter le jeu
def quitter() :
    if messagebox.askyesno("Scientific calculator","Voulez vous vraiment quitter?") :
        windows.quit()

#modifier la largeur de la calculatrice
def scientifique() :
    windows.resizable(width=False,height=False)
    windows.geometry("1700x600")

def standard() :
    windows.resizable(width=False,height=False)
    windows.geometry("900x600") 
   
#ecran d'affichage de la calculatrice
ecran=Entry(calculator,font=("arial",20,"bold"),bg="powder blue",bd=30,width=28,justify=RIGHT)
ecran.grid(row=0,column=0,columnspan=4,pady=1)
ecran.insert(0, "0")


#-----------------------------------partie logique(programmation orientée objet)---------------------------------------------

#creation d'une classe calculator
class Calculator:
    def __init__(self):
        self.total=0
        self.current=''
        self.input_value=True
        self.check_sum=False
        self.oper=''
        self.result=False
   
#---------------------fonction qui recupere les nombres saisis--------------------
    def input_number(self,num) :
        self.result=False
        num1=ecran.get() 
        num2=str(num)
        if self.input_value :
            self.current=num2
            self.input_value=False
        else :
            if num2=='.' :
                if num2 in num1 :
                    return    
            self.current=num1+num2
        self.display(self.current)
#--------------------fonction de calcul de la somme------------------------
    def sum_of_total(self) :
        self.result=True
        self.current=float(self.current)
        if self.check_sum==True :
            self.valid_function()
        else :
            self.total =float(ecran.get())

#-----------f--onction qui defini les operation --------------
    def valid_function(self) :
        if self.oper=="add" :
            self.total +=self.current
        if self.oper=="subb" :
            self.total -=self.current
        if self.oper=="mul" :
            self.total *=self.current
        if self.oper=="div" :
            self.total /=self.current
        if self.oper=="mod" :
            self.total //=self.current
        if self.oper=="pui" :
            self.total **=self.current
        self.input_value=True
        self.check_sum=False
        self.display(self.total)

#--------------fonction qui sert a recuperer l'operateur (+,-,*,%)------------        
    def operator(self,oper):
        self.current=float(self.current)
        if self.check_sum :
            self.valid_function()
        elif not self.result :
            self.total=self.current
            self.input_value=True
        self.check_sum=True
        self.oper=oper
        self.result=False

#----------------------fonction d'affichage------------------------    
    def display(self,value) :
        ecran.delete(0, END)
        ecran.insert(0, value)

    #-----------------------fonction effacer et effacer tout ----------------------------
    def clear(self):
        self.result=False
        value=ecran.get()
        if len(value)>1:
            new_value=value[:-1]
        else :
            new_value="0"
            self.input_value=True

        self.current=new_value
        self.display(new_value)
            
    def clear_all(self) :
        self.display("0")
        self.input_value=True

#----------------------------fonction plus ou moins -----------------------
    def pm(self) :
        self.result=False
        self.current=-(float(ecran.get()))
        self.display(self.current)

#--------------------------fonction racine carre--------------------
    def square(self) :
        self.result=False
        self.current=math.sqrt(float(ecran.get()))
        self.display(self.current)

#-------------------fonction pi ----------------------
    def pi(self) :
        self.result=False
        self.current=math.pi
        self.display(self.current)

#---------------------fonction 2pi -------------------
    def deux_pi(self) :
        self.result=False
        self.current=math.tau
        self.display(self.current)

#------------------------------fonction exponentielle---------------------------
    def e(self) :
        self.result=False
        self.current=math.e
        self.display(self.current)

#----------------------------fonction log --------------------------
    def log(self) :
        self.result=False
        a =float(ecran.get())
        if a<0 :
            self.display("Syntax Error")
        elif a==0 :
            self.display("Syntax Error")
        else :
            self.current=math.log(float(ecran.get()))
            self.display(self.current) 

#-------------------------fonction log de 2 -------------------
    def log2(self) :
        self.result=False
        self.current=math.log2(float(ecran.get()))
        self.display(self.current)

#---------------------------fonction cos et cosh -----------
    def cos(self) :
        self.result=False
        self.current=math.cos(math.radians(float(ecran.get())))
        self.display(self.current)

    def cosh(self) :
        self.result=False
        self.current=math.cosh(math.radians(float(ecran.get())))
        self.display(self.current)

#--------------------fonction sin et sinh-----------------------------
    
    def sin(self) :
        self.result=False
        self.current=math.sin(math.radians(float(ecran.get())))
        self.display(self.current)

    def sinh(self) :
        self.result=False
        self.current=math.sinh(math.radians(float(ecran.get())))
        self.display(self.current)
#------------------------------fontion tan et tanh --------------------------

    def tan(self) :
        self.result=False
        self.current=math.tan(math.radians(float(ecran.get())))
        self.display(self.current)

    def tanh(self) :
        self.result=False
        self.current=math.tanh(math.radians(float(ecran.get())))
        self.display(self.current)

#------------------------------fonction acosh et asinh ---------------------------
    def acosh(self) :
        self.result=False
        self.current=math.acosh(math.radians(float(ecran.get())))
        self.display(self.current)

    def asinh(self) :
        self.result=False
        self.current=math.asinh(math.radians(float(ecran.get())))
        self.display(self.current)


#-----------------------fonction degré et exp ---------------------

    def deg(self) :
        self.result=False
        self.current=math.degrees(float(ecran.get()))
        self.display(self.current)

    def exp(self) :
        self.result=False
        self.current=math.exp(float(ecran.get()))
        self.display(self.current)

#-----------------------------fonction carre,cude et inverse -----------------------------
    def carre(self):
        self.result=False
        self.current=math.pow(float(ecran.get()),2)
        self.display(self.current)
       
    
    def cube(self):
        self.result=False
        self.current=math.pow(float(ecran.get()),3)
        self.display(self.current)
           

    def inverse(self):
        self.result=False
        a =float(ecran.get())
        if a==0 :
            self.display("∞")
        else :
            self.current=1/a
            self.display(self.current) 


#---------------variable qui gere la classe calculator----------------------------------
added_value=Calculator()

#------------------------------------------ajout des nombres de la calculatrice----------------------------------------------
numberlist="789456123"
btn=[]
k=0
for i in range(2,5) :
    for j in range(3) :
        btn.append(Button(calculator,text=numberlist[k],width=4,height=1,font=("arial",20,"bold"),bg="black",fg="orange",bd=4))
        btn[k].grid(row=i, column=j, sticky="nsew")
        btn[k]["command"]=lambda x=numberlist[k]: added_value.input_number(x)
        k+=1

#--------------------------------------Ajout des bouttons de la partie standard-----------------------------------

btnEff=Button(calculator,text=chr(67), width=4,height=1,font=("arial",20,"bold"),bg="orange",fg="black",bd=4,command=added_value.clear).grid(row=1, column=0, sticky="nsew")
btnEffAll=Button(calculator,text=chr(67)+chr(69), width=4,height=1,font=("arial",20,"bold"),bg="orange",fg="black",bd=4,command=added_value.clear_all).grid(row=1, column=1, sticky="nsew")
btnracine=Button(calculator,text=chr(8730), width=4,height=1,font=("arial",20,"bold"),bg="orange",fg="black",bd=4,command=added_value.square).grid(row=1, column=2, sticky="nsew")

btnAdd=Button(calculator,text="+", width=4,height=1,font=("arial",20,"bold"),bg="orange",fg="black",bd=4,command=lambda : added_value.operator("add")).grid(row=1, column=3, sticky="nsew")
btnSub=Button(calculator,text="-", width=4,height=1,font=("arial",20,"bold"),bg="orange",fg="black",bd=4,command=lambda : added_value.operator("subb")).grid(row=2, column=3, sticky="nsew")
btnMul=Button(calculator,text="x", width=4,height=1,font=("arial",20,"bold"),bg="orange",fg="black",bd=4,command=lambda : added_value.operator("mul")).grid(row=3, column=3, sticky="nsew")
btnDiv=Button(calculator,text=chr(247), width=4,height=1,font=("arial",20,"bold"),bg="orange",fg="black",bd=4,command=lambda : added_value.operator("div")).grid(row=4, column=3, sticky="nsew")

btnZero=Button(calculator,text="0", width=4,height=1,font=("arial",20,"bold"),bg="black",fg="orange",bd=4,command= lambda :added_value.input_number(0)).grid(row=5, column=0, columnspan=1,sticky="nsew")
btnPoint=Button(calculator,text=".", width=4,height=1,font=("arial",20,"bold"),bg="orange",fg="black",bd=4,command= lambda :added_value.input_number(".")).grid(row=5, column=1,sticky="nsew" )
btnPM=Button(calculator,text=chr(177), width=4,height=1,font=("arial",20,"bold"),bg="orange",fg="black",bd=4,command=added_value.pm).grid(row=5, column=2, sticky="nsew")
btnEgual=Button(calculator,text="=", width=4,height=1,font=("arial",20,"bold"),bg="orange",fg="black",bd=4,command=added_value.sum_of_total).grid(row=5, column=3, sticky="nsew")

#-----------------------------------------------------------partie scientifique------------------------------------------------

btnpi=Button(calculator,text="π",width=4,height=1,font=("arial",20,"bold"),bg="orange",fg="black",bd=4,command=added_value.pi).grid(row=1,column=4,pady=1)
btnCos=Button(calculator,text="Cos",width=4,height=1,font=("arial",20,"bold"),bg="orange",fg="black",bd=4,command=added_value.cos).grid(row=1,column=5,pady=1)
btnTan=Button(calculator,text="Tan",width=4,height=1,font=("arial",20,"bold"),bg="orange",fg="black",bd=4,command=added_value.tan).grid(row=1,column=6,pady=1)
btnSin=Button(calculator,text="Sin",width=4,height=1,font=("arial",20,"bold"),bg="orange",fg="black",bd=4,command=added_value.sin).grid(row=1,column=7,pady=1)

btn2pi=Button(calculator,text="2π",width=4,height=1,font=("arial",20,"bold"),bg="orange",fg="black",bd=4,command=added_value.deux_pi).grid(row=2,column=4,pady=1)
btnCoh=Button(calculator,text="Cosh",width=4,height=1,font=("arial",20,"bold"),bg="orange",fg="black",bd=4,command=added_value.cosh).grid(row=2,column=5,pady=1)
btnTanh=Button(calculator,text="Tanh",width=4,height=1,font=("arial",20,"bold"),bg="orange",fg="black",bd=4,command=added_value.tanh).grid(row=2,column=6,pady=1)
btSinh=Button(calculator,text="sinh",width=4,height=1,font=("arial",20,"bold"),bg="orange",fg="black",bd=4,command=added_value.sinh).grid(row=2,column=7,pady=1)

btnlog=Button(calculator,text="log",width=4,height=1,font=("arial",20,"bold"),bg="orange",fg="black",bd=4,command=added_value.log).grid(row=3,column=4,pady=1)
btnepx=Button(calculator,text="exp",width=4,height=1,font=("arial",20,"bold"),bg="orange",fg="black",bd=4,command=added_value.exp).grid(row=3,column=5,pady=1)
btnMod=Button(calculator,text="%",width=4,height=1,font=("arial",20,"bold"),bg="orange",fg="black",bd=4,command=lambda : added_value.operator("mod")).grid(row=3,column=6,pady=1)
btnE=Button(calculator,text="e",width=4,height=1,font=("arial",20,"bold"),bg="orange",fg="black",bd=4,command=added_value.e).grid(row=3,column=7,pady=1)

btnlog2=Button(calculator,text="log2",width=4,height=1,font=("arial",20,"bold"),bg="orange",fg="black",bd=4,command=added_value.log2).grid(row=4,column=4,pady=1)
btndeg=Button(calculator,text="°",width=4,height=1,font=("arial",20,"bold"),bg="orange",fg="black",bd=4,command=added_value.deg).grid(row=4,column=5,pady=1)
btnacosh=Button(calculator,text="acosh",width=4,height=1,font=("arial",20,"bold"),bg="orange",fg="black",bd=4,command=added_value.acosh).grid(row=4,column=6,pady=1)
btnasinh=Button(calculator,text="asinh",width=4,height=1,font=("arial",20,"bold"),bg="orange",fg="black",bd=4,command=added_value.asinh).grid(row=4,column=7,pady=1)

btncaree=Button(calculator,text="x²",width=4,height=1,font=("arial",20,"bold"),bg="orange",fg="black",bd=4,command=added_value.carre).grid(row=5,column=4,pady=1)
btninverse=Button(calculator,text="1/x",width=4,height=1,font=("arial",20,"bold"),bg="orange",fg="black",bd=4,command=added_value.inverse).grid(row=5,column=5,pady=1)
btnCube=Button(calculator,text="x³",width=4,height=1,font=("arial",20,"bold"),bg="orange",fg="black",bd=4,command=added_value.cube).grid(row=5,column=6,pady=1)
btnpuissance=Button(calculator,text="xʸ",width=4,height=1,font=("arial",20,"bold"),bg="orange",fg="black",bd=4,command=lambda : added_value.operator("pui")).grid(row=5,column=7,pady=1)


Text=Label(calculator,text="Scientific Calculator",font=("arial",25,"bold"),justify=CENTER,bg="black",fg="white")
Text.grid(row=0,column=4,columnspan=4)




#-------------------------------------------creation de la barre de menu-------------------------------------------
menubar=Menu(windows)

#------------------------------------------------menu fichier------------------------------------------------------
menu_fichier=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Fichier",menu=menu_fichier)
menu_fichier.add_command(label="standard",command=standard)
menu_fichier.add_command(label="scientific",command=scientifique)
menu_fichier.add_separator()
menu_fichier.add_command(label="Exit",command=quitter)

#------------------------------------------------menu edition-----------------------------------------------------
menu_edit=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Editer",menu=menu_edit)
menu_edit.add_command(label="Couper")
menu_edit.add_command(label="Copier")
menu_edit.add_separator()
menu_edit.add_command(label="Coller")

#-------------------------------------------------menu d'aide-----------------------------------------------------
menu_aide=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Editer",menu=menu_aide)
menu_aide.add_command(label="Optenir de l'aide")
windows.config(menu=menubar)



windows.mainloop()