#función para clasificar los paquetes por ID
def clasificar_paquetes():
    # método de ordenación simple
    for i in range(len(almacen)):
        for j in range(i + 1, len(almacen)):
            if almacen[i]["id"] > almacen[j]["id"]:
                temp = almacen[i]  
                almacen[i] = almacen[j] 
                almacen[j] = temp  
    
    print("Paquetes clasificados por ID.")