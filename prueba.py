numero1 = int(input("Escribe un numero "))
operador = input("Deseas sumar, restar, multiplicar o dividir?")
numero2 = int(input("Escribe otro numero "))


if operador == "restar":
    resultado = numero1 - numero2
    print(resultado)
    
elif operador == "sumar":
    resultado = numero1 + numero2
    print(resultado)
    
elif operador == "multiplicar":
    resultado = numero1 * numero2
    print(resultado)
    
elif operador == "dividir":
    resultado = numero1 / numero2
    print(resultado)