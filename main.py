from random import randint as rd
from datetime import datetime as dt

def generarClave(long,cantChar,CantInt,CantSimbols):
    pass

def generarUsuarioPc():
    usersSalida=[]   
    name=f"usuariosYClaves_{dt.today().strftime("%Y-%m-%d")}.txt"
    #crear archivo
    fileSalida=open(name,'w')
    fileBase= open("usuariosPc.txt","r")
    usersBase=fileBase.readlines()
    # fileSalida.close()
    fileBase.close()
    for i in range(len(usersBase)):
        usersBase[i]=usersBase[i].replace("\n","")
        usersBase[i]=usersBase[i].replace(" ","")
    print(usersBase)
generarUsuarioPc()