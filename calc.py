langoptions = "EN - DE - FR - ES - PT"

print("Avaliable languages: {}".format(langoptions))
lang = input("Choose your language: ")

#Idioma
if lang == "EN":
    print("The calculator is in English!")

if lang == "PT":
    print("A calculadora está em Português!")

if lang == "ES":
    print("¡La calculadora está en Español!")

if lang == "DE":
    print("Der Rechner ist auf Deutsch!")

if lang == "FR":
    print("La calculatrice est en Français!")

#Digita o cálculo
if lang == "EN":
    problem = input("Enter the calculation:")

if lang == "PT":
    problem = input("Digita o cálculo:")

if lang == "ES":
    problem = input("Introduzca el cálculo:")

if lang == "DE":
    problem = input("Geben Sie die Berechnung ein:")

if lang == "FR":
    problem = input("Saisissez le calcul:")

#Calculadora
result = eval(problem)

#Resultado
if lang == "EN":
    print(f"The result is {result}")

if lang == "PT":
    print(f"O resultado é {result}")

if lang == "ES":
    print(f"El resultado es {result}")

if lang == "DE":
    print(f"Das Ergebnis ist {result}")

if lang == "FR":
    print(f"Le résultat est {result}")

#Enter para fechar
if lang == "EN":
    input("Press Enter to close!")

if lang == "PT":
    input("Prime Enter para fechar!")

if lang == "ES":
    input("¡Presiona Enter para cerrar!")

if lang == "DE":
    input("Zum Schließen Enter drücken!")

if lang == "FR":
    input("Appuyez sur Enter pour fermer!")