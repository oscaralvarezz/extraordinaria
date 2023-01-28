def main():
    
    #creamos la clase armadura
    class Armadura():
        def __init__(self, name, rango):
            self.name = name
            self.rango = rango
            self.calificacion()
            print('¡Se ha creado una armadura con exito!')

        #creamos una función para calificar las armaduras
        def calificacion(self):
            for i in self.name:
                if self.name == 'TK':
                    print('{}código de legión {}'.format(self.name, self.rango))
                if self.name == '8':
                    print('{}identificador coherente{}'.format(self.name, self.rango))
                if self.name == '6':
                    print('{}identificador de siglo {}'.format(self.name, self.rango))
                if self.name == '5':
                    print('{} tiene un número de trooper {}'.format(self.name, self.rango))
                if self.name == '4':
                    print('{}identificador de escuadra{}'.format(self.name, self.rango))

    #a continuación asignamos valores a distintas armaduras
    Armadura1 = Armadura('TK-421', 10)
    Armadura2 = Armadura('8-8-8', 10)
    Armadura3 = Armadura('6-6-6', 10)
    Lista = [Armadura1, Armadura2, Armadura3]

    #calificamos las armaduras
    for i in Lista:
        i.calificacion()

if __name__=='__main__':
    main()