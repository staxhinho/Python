langoptions = "EN - PT - ES"

print("Avaliable languages: {}".format(langoptions))
lang = input("Choose your language: ")

#Idioma
if lang == "EN":
    print("The calculator is in English!")

if lang == "PT":
    print("A calculadora está em Português!")

if lang == "ES":
    print("¡La calculadora está en portugués!")

#Digita o cálculo
if lang == "EN":
    problema = input("Enter the calculation:")

if lang == "PT":
    problema = input("Digita o cálculo:")

if lang == "ES":
    problema = input("Introduzca el cálculo:")

#Calculadora
resultado = eval(problema)

#Resultado
if lang == "EN":
    print(f"The result is {resultado}")

if lang == "PT":
    print(f"O resultado é {resultado}")

if lang == "ES":
    print(f"El resultado es {resultado}")

#Enter para fechar
if lang == "EN":
    input("Press Enter to close!")

if lang == "PT":
    input("Prime Enter para fechar!")

if lang == "ES":
    input("¡Presiona Enter para cerrar!")