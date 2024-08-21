# Menú interactivo
def menu():
    while True:
        print("\nMenú de Gestión de Paquetes")
        print("1. Agregar paquete")
        print("2. Eliminar paquete")
        print("3. Clasificar paquetes")
        print("4. Buscar paquete")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            agregar_paquete()
        elif opcion == '2':
            eliminar_paquete()
        elif opcion == '3':
            clasificar_paquetes()
        elif opcion == '4':
            buscar_paquete()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
menu()