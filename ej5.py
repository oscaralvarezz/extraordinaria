#usamos repositorio de repaso para examen para hacer este ejercicio.

def main():
  
#Creamos una función que nos de falso si la mochila esta vacía.
  def hijo_sin_amor(mochila, numero_objetos=0):
    if not mochila:
      return False, numero_objetos

    #Sacamos de la mochila el primer objeto que haya
    objeto = mochila[0]
    mochila = mochila[1:]

    #Usamos una función recursiva para ver si encuentra el sable de luz o no, si no lo encuentra
    #seguirá sacando objetos hasta encontrarlo.
    if objeto == "anillo de poder":
      return True, numero_objetos
    return hijo_sin_amor(mochila, numero_objetos + 1)

  #Ahora comprobamos si está el sable de luz
  #también se muestra el número de elementos extraídos hasta encontrarlo.
  lista = ["espada láser","anillo de poder","sable de luz", "bocadillo"]
  print(hijo_sin_amor(lista))

if __name__=='__main__':
    main()