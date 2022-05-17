def run():

    while True:
        
        option = int(input("Ingrese '1' para añadir matrices 5x5 por cuenta propia, '0' para verificar con ejemplos propios o cualquier otra tecla para salir."))
        
        if(option == 1):
            # Ingresá tu ejemplo (matriz 5x5) y verifique el funcionamiento del programa.
                control_matriz(input("Ingrese la matriz 5x5 "))

        elif(option == 0):
            # Ejemplos concretos de matrices
            
            print("Esta es la Matriz 1.")
        
            matriz = [
                [1, 1, 1, 1, 3],
                [1, 5, 1, 1, 6],
                [1, 6, 6, 6, 6],
                [1, 2, 1, 1, 6],
                [1, 1, 1, 1, 6]
                ]
            
            control_matriz(matriz)

            print("Esta es la Matriz 2.")

            matriz2 = [
                [2, 1, 1, 13, 3],
                [5, 5, 5, 5, 6],
                [1, 6, 6, 6, 6],
                [1, 1, 1, 1, 6],
                [1, 13, 1, 1, 6]
                ]
        
            control_matriz(matriz2)
        
            print("Esta es la Matriz 3.")
        
            matriz3 = [
                [22, 22, 22, 22, 67],
                [22, 52, 52, 51, 67],
                [22, 6, 6, 6, 67],
                [22, 1, 1, 1, 67],
                [1, 13, 13, 13, 13]
                ]
            
            control_matriz(matriz3)
            
        else:
            break
    
def traverseArray_columns(matriz, column):
    
    # Ésta función nos devuelve las columnas que cumplen una secuencia de 4 números enteros seguidos.
    
    control_sec = 0
    position_initial = 0
    add = 0
    init_num = matriz[0][column]
    
    for i in range(5):     
        control_num = matriz[i][column]     
        control_sec += 1
        if(control_num == init_num):         
            if(control_sec == 4):               
                print(f"La matriz tiene una secuencia de 4 numeros enteros consecutivos que empieza en fila [{position_initial+1}], columna [{column+1}] y termina en fila [{control_sec+add}], columna [{column+1}]")
                break
        else:
            if(control_sec <= 2):
                add = 1
                init_num = matriz[i][column]
                position_initial = 1
            else:
                break
            
def traverseArray_rows(matriz, row):
    
    # Ésta función nos devuelve las filas que cumplen una secuencia de 4 números enteros seguidos.
    
    control_sec = 0
    position_initial = 0
    add = 0
    init_num = matriz[row][0]
    
    for j in range(5):     
        control_num = matriz[row][j]     
        control_sec += 1
        if(control_num == init_num):         
            if(control_sec == 4):               
                print(f"La matriz tiene una secuencia de 4 numeros enteros consecutivos que empieza en fila [{row+1}], columna [{position_initial+1}] y termina en fila [{row+1}], columna [{control_sec+add}]")
                break
        else:
            if(control_sec <= 2):
                add = 1
                init_num = matriz[row][j]
                position_initial = 1
            else:
                break                               
    
def control_matriz(matriz):    
     
    # Aquí se llaman a las dos funciones anteriormente definidas.
     
        for column in range(5):
            traverseArray_columns(matriz, column)
        
        for row in range(5):
            traverseArray_rows(matriz, row)                
    
if __name__ == '__main__':
    run()
    