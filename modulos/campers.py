import os
from .variables import save, campers, camper

def create():
    save({
        "CC": int(input("Ingrese cedula: ")),
        "Nombre": input("Ingrese nombre: "),
        "Apellido": input("Ingrese apellidos: "),
        "Direccion": input("Ingrese direccion: "),
        "Acudiente": input("Ingrese acudiente: "),
        "Telefonos": {
            "Fijo": int(input("ingrese telefono fijo: ")),
            "Celular": int(input("Ingrese numero celular: "))
        },
        "Estado": input("Ingrese estado: ")
    })  
    os.system("Pause")

def prueba():
    pass

def Campers(codigo= None):
    os.system("cls")
    print("""
            **********************
            *       Campers      *
            **********************
    """)

    if(codigo == None):
        for i,val in enumerate(campers()):
            print(f"""
            _______________________
            Codigo: {i+1}
            CC: {val.get("CC")}
            Nombre: {val.get("Nombre")}
            Apellido: {val.get("Apellido")}
            Direccion: {val.get("Direccion")}
            Acudiente: {val.get("Acudiente")}
            Telefonos: Fijo {val['Telefonos']['Fijo']} Celular {val['Telefonos']['Celular']}
            Estado: {val.get("Estado")}
            _________________________
            """)
    else:
        val = campers()[codigo-1]
        print(f"""
            _______________________
            Codigo: {codigo}
            CC: {val.get("CC")}
            Nombre: {val.get("Nombre")}
            Apellido: {val.get("Apellido")}
            Direccion: {val.get("Direccion")}
            Acudiente: {val.get("Acudiente")}
            Telefonos: Fijo {val['Telefonos']['Fijo']} Celular {val['Telefonos']['Celular']}
            Estado: {val.get("Estado")}
            _________________________
        """)
    
    os.system("pause")

def ModificarCampers():
    os.system("cls")
    print("""
            **********************
            * Actualizar Camper  *
            **********************
    """)
    Campers()
    codigo = int(input("Ingrese codigo del camper a modificar: "))
    Campers(codigo)
    while(True):
        print("""
        Estas seguro que desea actualizar el camper?
        1 - Si
        2 - No
        """)
        opc = int(input(": "))
        match(opc):
            case 1:
                val = {
                    "CC": int(input("Ingrese cedula: ")),
                    "Nombre": input("Ingrese nombre: "),
                    "Apellido": input("Ingrese apellidos: "),
                    "Direccion": input("Ingrese direccion: "),
                    "Acudiente": input("Ingrese acudiente: "),
                    "Telefonos": {
                        "Fijo": int(input("ingrese telefono fijo: ")),
                        "Celular": int(input("Ingrese numero celular: "))
                    },
                    "Estado": input("Ingrese estado: ")
                }
                camper[codigo-1] = val
                print(f"""
                    El camper fue actualizado
                    _______________________
                    Codigo: {codigo}
                    CC: {val.get("CC")}
                    Nombre: {val.get("Nombre")}
                    Apellido: {val.get("Apellido")}
                    Direccion: {val.get("Direccion")}
                    Acudiente: {val.get("Acudiente")}
                    Telefonos: Fijo {val['Telefonos']['Fijo']} Celular {val['Telefonos']['Celular']}
                    Estado: {val.get("Estado")}
                    _________________________
                    """)
                os.system("pause")
                break
            case 2:
                os.system("cls")
                break
        
def delete():
    pass

def MenuCampers():
    menu = ["Registrar camper","Registro de Prueba","Ver Campers","Modificar Campers","Salir"]
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
                    case 3: Campers()
                    case 4: ModificarCampers()
                    case 5: menuPrincipal()
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

