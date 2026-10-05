# Função: Celsius para Fahrenheit
def celsius_para_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# Função: Celsius para Kelvin
def celsius_para_kelvin(celsius):
    return celsius + 273.15


# Função: Fahrenheit para Celsius
def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


# Função: Fahrenheit para Kelvin
def fahrenheit_para_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15


# Função: Kelvin para Celsius
def kelvin_para_celsius(kelvin):
    return kelvin - 273.15


# Função: Kelvin para Fahrenheit
def kelvin_para_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9 / 5 + 32


# Menu principal
while True:
    print("\n===== CONVERSOR DE TEMPERATURA =====")
    print("1: Celsius para Fahrenheit")
    print("2: Celsius para Kelvin")
    print("3: Fahrenheit para Celsius")
    print("4: Fahrenheit para Kelvin")
    print("5: Kelvin para Celsius")
    print("6: Kelvin para Fahrenheit")
    print("0: Sair")

    opcao = input("\nDigite uma opção: ")

    # Validação da opção
    if opcao not in ["0", "1", "2", "3", "4", "5", "6"]:
        print("Opção inválida! Digite uma opção de 0 a 6.")
        continue

    # Encerramento
    if opcao == "0":
        print("Programa encerrado!")
        break

    # Solicita a temperatura
    try:
        temperatura = float(input("Digite a temperatura: "))
    except ValueError:
        print("Erro! Digite uma temperatura válida.")
        continue

    # Realiza a conversão
    if opcao == "1":
        resultado = celsius_para_fahrenheit(temperatura)
        print(f"{temperatura:.2f} °C = {resultado:.2f} °F")

    elif opcao == "2":
        resultado = celsius_para_kelvin(temperatura)
        print(f"{temperatura:.2f} °C = {resultado:.2f} K")

    elif opcao == "3":
        resultado = fahrenheit_para_celsius(temperatura)
        print(f"{temperatura:.2f} °F = {resultado:.2f} °C")

    elif opcao == "4":
        resultado = fahrenheit_para_kelvin(temperatura)
        print(f"{temperatura:.2f} °F = {resultado:.2f} K")

    elif opcao == "5":
        resultado = kelvin_para_celsius(temperatura)
        print(f"{temperatura:.2f} K = {resultado:.2f} °C")

    elif opcao == "6":
        resultado = kelvin_para_fahrenheit(temperatura)
        print(f"{temperatura:.2f} K = {resultado:.2f} °F")