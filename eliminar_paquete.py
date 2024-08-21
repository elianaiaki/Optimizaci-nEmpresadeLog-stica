almacen = []
# Función para eliminar un paquete usando un bucle for
def eliminar_paquete():
    id_paquete = int(input("Ingrese el ID del paquete a eliminar: "))
    
    # Recorremos cada elemento en la lista almacen
    for i in range(len(almacen)):
        # Comparamos el ID del paquete en la posición i con el ID ingresado por el usuario
        if almacen[i]["id"] == id_paquete:
            # Si encontramos el paquete, lo eliminamos usando del
            del almacen[i]
            print("Paquete eliminado exitosamente.")
            return  
    
    print("Paquete no encontrado.")
