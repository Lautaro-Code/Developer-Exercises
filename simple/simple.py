import random

from pkg_resources import resource_string

def list_generator():
    
    """
        Aqui generamos nuestra lista oredenada por ID pero con edades aleatorias.
    
        Y es devuelta como salida.
    """
    
    lista = [
        {
            'id': 1,
            'edad': random.randint(1, 100)
        },
        {
            'id': 2,
            'edad': random.randint(1, 100)
        },
        {
            'id': 3,
            'edad': random.randint(1, 100)
        },
        {
            'id': 4,
            'edad': random.randint(1, 100)
        },
        {
            'id': 5,
            'edad': random.randint(1, 100)
        },
        {
            'id': 6,
            'edad': random.randint(1, 100)
        },
        {
            'id': 7,
            'edad': random.randint(1, 100)
        },
        {
            'id': 8,
            'edad': random.randint(1, 100)
        },
        {
            'id': 9,
            'edad': random.randint(1, 100)
        },
        {
            'id': 10,
            'edad': random.randint(1, 100)
        },       
    ]
    
    return lista

def order_list(lista: list):
    
    """
        Ésta función devuelve el ID que tiene la menor edad, la mayor, ordena la lista ingresada como parámetro y la muestra por pantalla.     
    """
    
    maximo = 0
    minimo = 100
    
    """
        Aquí se encuentran el id de la persona más vieja y más joven.
    """
    
    for i in lista:
        if(i['edad'] < minimo):
            minimo = i['edad']
            id_min = i['id']
        
        if(i['edad'] > maximo):
            maximo = i['edad']
            id_max = i['id']
                
    new_list = []
    copy_list = lista 
    
    """
        En éste bucle ordenamos la lista de acuerdo a lo solicitado.
        
        Se ordena la lista de diccionarios de menor edad a mayor.
    """
    
    while copy_list:
        
        is_min = 100
        save_dictionary = {}
        
        for diccionario in copy_list:
            if (diccionario['edad'] < is_min):
                is_min = diccionario['edad']
                save_dictionary = diccionario
        
        for i in copy_list:
            if (i == save_dictionary):
                new_list.append(save_dictionary)
                copy_list.remove(i)
                continue
               
    return print(f"""

            El ID con la menor edad es: {id_min}
            
            El ID con la mayor edad es: {id_max}
            
            Lista ordenada: {new_list}
    """)


if __name__ == "__main__":
    
    """
        No usé DocTests ya que considero que no son necesarios dado que genero automaticamente ya la lista de diccionarios.
    """
    
    control = 'y'
    
    while (control == 'y'):
        order_list(list_generator())
        
        control = input("¿Desea realizar otra prueba? (y/n) ")