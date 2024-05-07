import json

with open("servicios.json", "r") as openfile:
    servicitos = json.load(openfile)

with open("categoriasUsuarios.json", "r") as openfile:
    categoritas = json.load(openfile)

with open("registro.json", "r") as openfile:
    registro = json.load(openfile)




newUser = {}

print("------------------------------------------------------")
print("              BIENVENIDO A MI MOVISTAR                ")
print("------------------------------------------------------")

print("///////////////////////////////////////////////////////")
print("                        MENÚ                           ")
print("///////////////////////////////////////////////////////")
print("1.               Registro de clientes                  \n2.               Actualizacion de Datos\n3.               Eliminación de Perfiles\n4.               Informes de adquisición de Servicios\n5.               Informe sobre nuestros productos")
print("///////////////////////////////////////////////////////")
print("")

# Captura de información detallada de cada usuario, incluyendo nombre, dirección, información de contacto, entre otros.

selec = int(input("¿Qué opción desea ejecutar?\n\n"))
print("")

if selec == 1:
    print("///////////////////////////////////////////////////////")
    print("               Registro de clientes                    ")
    print("///////////////////////////////////////////////////////")
    print("")

    print("        Por favor, ingrese los siguientes datos        \n")

    id = int(input("C.C: "))
    print("")
    name = str(input("Nombre Completo: "))
    print("")
    adress = input("Dirección: ")
    print("")
    contact = input("Correo Electrónico: ")
    print("")
    service = int(input("Servicio que desea:\n1.Fibra Optica\n2.Prepago\n3.Pospago\n\n"))
    
    if service == 1:
        service = "Fibra Optica"   
        newUser = {
            "identificacion": id,
            "nombre": name,
            "direccion": adress,
            "contacto": contact,
            "servicio": service
        }
        registro += [newUser]

    
    if service == 2:
        service = "Prepago"
        newUser = {
            "identificacion": id,
            "nombre": name,
            "direccion": adress,
            "contacto": contact,
            "servicio": service
        }
        registro += [newUser]

    if service == 3:
        service = "Pospago"
        newUser = {
            "identificacion": id,
            "nombre": name,
            "direccion": adress,
            "contacto": contact,
            "servicio": service
        }
        registro += [newUser]

        
    with open("registro.json", "w") as f:
        json.dump(registro, f, indent=4)

   

if selec == 2:
    n = int(input("        Por favor, ingrese su numero de identificación        \n"))

    for i in registro:
        if n == i["identificacion"]:

            

            i["identificacion"] = i["identificacion"]
            print("")
            i["nombre"] = str(input("Nombre Completo: "))
            print("")
            i["direccion"] = input("Dirección: ")
            print("")
            i["contacto"] = input("Correo Electrónico: ")
            print("")
            i["servicio"] = int(input("Servicio que desea:\n1.Fibra Optica\n2.Prepago\n3.Pospago\n\n"))

            if i["servicio"] == 1:
                i["servicio"] = "Fibra Optica",   

        
            if i["servicio"] == 2:
                i["servicio"] = "Prepago"
                

            if i["servicio"] == 3:
                i["servicio"] = "Pospago"
                
                
            with open("registro.json", "w") as f:
                json.dump(registro, f, indent=4)

        


    

            
                
        
            
        

