# función para buscar un paquete por su ID
def buscar_paquete():
    print("Ingrese el ID del paquete a buscar: ")
    id_paquete = input()

    for paquete in almacen:
        if paquete["id"] == id_paquete:
            print(f"Paquete encontrado: {paquete}")
            return  

    print("Paquete no encontrado.")