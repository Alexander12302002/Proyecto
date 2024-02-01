import os
from .variables import save, getAll, camper

def create():
    save({
        "CC": int(input("Ingrese cedula: ")),
        "Nombre": input("Ingrese nombre: "),
        "Apellido": input("Ingrese apellidos: "),
        "direccion": input("Ingrese direccion: "),
        "Acudiente": input("Ingrese acudiente: "),
        "Celular": int(input("Ingrese numero de celular: ")),
        "Fijo": int(input("Ingrese numero fijo: ")),
        "Estado": input("Ingrese estado")
    })  
    os.system("Pause")

def read():
    pass
def update():
    pass
def delete():
    pass
def menu():
    menu = ["Guardar", "Buscar","Actualizar","Eliminar","Salir"]
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
            if(opc<=len(menu) and opc>0):
                match (opc):
                    case 1: create()
                    case 2: read()
                    case 3: update()
                    case 4: delete()
                    case 5: break
        except ValueError:
            print(f"La opcion no es valida")