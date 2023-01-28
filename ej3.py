class Armaduras():
        def __init__(self, name, rango):
            self.name = name
            self.rango = rango
            self.calificacion()
            print('Se ha creado una armadura con éxito!')
        
        def __str__(self):
            return 'La armadura: {} con rango {} y calificacion: {}'.format(self.name, self.rango, self.calificacion)

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

Armadura1 = Armaduras('TK-421', 10)
Armadura2 = Armaduras('8-8-8', 10)
Armadura3 = Armaduras('6-6-6', 10)
Lista = [Armadura1, Armadura2, Armadura3]

#mostramos por pantalla la armadura 1
print(Armadura1)

#ahora mostramos todas las armaduras
for i in Lista:
    print(i)