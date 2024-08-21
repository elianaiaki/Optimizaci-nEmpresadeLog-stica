# lista vacía para almacenar los paquetes
almacen = []

# función para agregar un nuevo paquete al almacén
def agregar_paquete():
    # Solicitar que se ingrese el ID del paquete
    print("Ingrese el ID del paquete: ")
    id_paquete = input()  

    # Solicitar que se ingrese el ID del paquete
    print("Ingrese el nombre del paquete: ")
    nombre = input() 

    # Creamos un diccionario que representa el paquete, con su ID y nombre
    paquete = {"id": id_paquete, "nombre": nombre}
    
    # Obtenemos la longitud actual de la lista almacen
    almacen_len = len(almacen)
    
     # Asignamos el nuevo paquete a la lista
    almacen[almacen_len] = paquete