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

'''
ES UN ANAGRAMA?
Escribe una funcion que reciba dos palabras (String) y retorne
verdadero o falso (bool) segun sean o no anagramas.
- Un anagrama constiste en formar una palabra reordenado
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- DOS palabras exctamente iguales no son anagrama.
'''

def is_anagram(word_one, word_two): 
    if word_one == word_two:
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())

print(is_anagram('Amor', 'Roma'))

'''
LA SUCESION DE FIBONACCI
Escribe un programa que imprima los 50 primeros numeros de la sucesion de Fibonacci.
empieza en.
 - La serie Fibonacci se compone por una sucesion de numeros en la que el siguiente
   siempre es la suma de los dos anteriores.
    0, 1, 1, 2, 3, 5, 8, 13...
'''

def fibonacci():

    prev = 0
    next = 1

    for index in range(0, 50):
        print(prev)
        fib = prev + next
        prev = next
        next = fib

fibonacci()

'''
Es un numero primo?
Escriba un programa que  se encargue de comprobar si un numero es o no primo.
Hecho esto, imprime los numeros primos entre 1 y 100.
'''

def is_prime(number):

    if number < 2:
        return False

    for index in range(2, number):
        if number % index == 0:
            return False
    return True

for number in range(1, 101):
    if is_prime(number):
        print(number)

'''
Crea un programa que invierta el orden de una cadea de texto
sin usar funciones propias del lenguaje que lo hagan de forma automatica.
- Si le pasamos "Hola Mundo" nos retornaria "odnuM aloH"
'''

def reverse(text):
    text_len = len(text)
    reversed_text = ""
    for index in range(0, text_len):
        reversed_text += text[text_len - index -1 ]
    return reversed_text


print(reverse("Hola Mundo"))