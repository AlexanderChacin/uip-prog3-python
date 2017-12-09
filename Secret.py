print("     Secret Word")

print("Adivine la palabra secreta !")
print("Que tiene manos pero no puede aplaudir?")
palabra_secreta = "reloj"

intentos = 3
while intentos > 0:
    respuesta = input("La palabra secreta es: el..... ").lower()

    if respuesta not in palabra_secreta:
        print("Porfavor: Intenta de nuevo.")
        intentos -= 1

    else:
        print("FELICIDADES ESTAS CORRECTO")
        exit();

if respuesta not in palabra_secreta:
    print("Felicidades! Eres tonto !.")
    intentos += 1