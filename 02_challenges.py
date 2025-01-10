### challenges ###

'''
EL FAMOSO "FIZZ BUZZ"
escribe un programa que muestre por consola (con un print) los 
números del 1 al 100 (ambos incluidos y con un salto de linea entre 
cada impresion), sutituyendo los siguientes:
- Multiplos de 3 por la palabra "Fizz".
- Multiplos de 5 por la palabra "Buzz".
- Multiplos de 3 y 5 por la palabra "FizzBuzz".
'''

def fizzbuzz():
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            print("fizzBuzz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5 == 0:
            print("buzz")
        else:
            print(index)
        
fizzbuzz()