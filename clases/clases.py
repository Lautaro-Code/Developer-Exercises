def main():
    """
        Aquí se instanciaran las diferentes posibilidades que se pueden presentar.
        Haremos uso de DocTests para las pruebas
        
        >>> c1 = Circulo(2)
        
        >>> c3 = Circulo(20)
        
        >>> c2 = Circulo(-1)
        No se puede ingresar radios menores o iguales a cero. Por favor, ingresa un radio mayor a 0. :D
        
        >>> c4 = Circulo(10)
        
        >>> c5 = Circulo(25)
        
        >>> print(c3)
        El circulo tiene radio 20
        
        >>> print(c1)
        El circulo tiene radio 2
        
        >>> print(c4)
        El circulo tiene radio 10
        
        >>> c3.multiplicacionCirculo(2)
        ¡Se a creado un nuevo Circulo!
        
        >>> c3.multiplicacionCirculo(-2)
        Error! Por favor ingresa un numero mayor a 0.
        
        >>> c4.set_radio(-4)
        No se puede modificar debido a que ingresaste un radio negativo o igual a cero. Por favor intenta de nuevo ingresando un radio mayor a 0. :D
        
        >>> c5.area()
        El area del circulo es: 1963.5
        
        >>> c5.perimetro()
        El perimetro del circulo es: 157.08
        
    """
    
from cmath import pi

class Circulo(object):
    """Clase Circulo y sus metodos"""
    #Constructor
    def __init__(self, radio):
        try:
            if(radio > 0):
                self.radio = radio
            else:
                raise ValueError("No se puede ingresar radios menores o iguales a cero. Por favor, ingresa un radio mayor a 0. :D")
        except ValueError as ve:
            print(ve)
    
    def __str__(self):
        return f"El circulo tiene radio {self.radio}"
    
    def get_Radio(self):
        return self.radio
        
    def set_radio(self, radio):
        try:
            if(radio > 0):
                self.radio = radio
            else:
                raise ValueError("No se puede modificar debido a que ingresaste un radio negativo o igual a cero. Por favor intenta de nuevo ingresando un radio mayor a 0. :D")
        except ValueError as ve:
            print(ve)
        
    def area(self):
        
        area = round((pi * self.radio * self.radio), 2)
        
        return print("El area del circulo es: {}".format(area))
    
    def perimetro(self):
        
        perimetro = round((2 * pi * self.radio), 2)
        
        return print("El perimetro del circulo es: {}".format(perimetro))
    
    def multiplicacionCirculo(self, n):
        try:
            if(n >= 1):
                
                radio = self.get_Radio()
                
                newCircle = Circulo(radio * n)
                
                print("¡Se a creado un nuevo Circulo!")
                
            else:
                raise ValueError("Error! Por favor ingresa un numero mayor a 0.")     
        except ValueError as ve:
            print(ve)
            
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    