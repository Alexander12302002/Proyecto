import os
from .variables import save, getAll, camper

def create():
    save({
        "CC": int(input("Ingrese cedula: ")),
        "Nombre": input("Ingrese nombre: "),
        "Apellido": input("Ingrese apellidos: "),
        "direccion": input("Ingrese direccion: "),
        "Acudiente": input("Ingrese acudiente: "),
        "Telefonos": {
            "Fijo": int(input("ingrese telefono fijo: ")),
            "Celular": int(input("Ingrese numero celular: "))
        },
        "Estado": input("Ingrese estado")
    })  
    os.system("Pause")

def read():
    pass
def update():
    pass
def delete():
    pass

def MenuCampers():
    menu = ["Registrar camper","Registro de Prueba","Salir"]
    while(True):
        os.system("cls")
        print("""
            **********************
            *  Menu del camper   *
            **********************
        """)
        print("".join([f"{i+1}. {val}\n" for i,val in enumerate(menu)]))
        try:
            opc = int(input())
            if(opc <= len(menu) and opc >0):
                match(opc):
                    case 1: create()
                    case 2: ()
                    case 3: menuPrincipal()
        except ValueError:
            print(f"La opcion {opc} no es valida")

def menuPrincipal():
    menu = ["Camper", "Rutas","Clases","Administracion","Salir"]
    while(True):
        os.system("cls")
        print("""
            *****************
            *  CAMPUSLAND   *
            *****************
        """)
        print("".join([f"{i+1}. {val}\n" for i,val in enumerate(menu)]))
        try:
            opc = int(input())
            if(opc<=len(menu) and opc>0):
                match (opc):
                    case 1: MenuCampers()
                    case 2: ()
                    case 3: ()
                    case 4: ()
                    case 5: break
        except ValueError:
            print(f"La opcion no es valida")

